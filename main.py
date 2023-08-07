import streamlit as st
import pandas as pd
import openai_helper
import matplotlib.pyplot as plt

col1, col2 = st.columns([3,2])

financial_data_df = pd.DataFrame({
        "Measure": ["Company Name", "Stock Symbol", "Revenue", "Net Income", "EPS"],
        "Value": ["", "", "", "", ""]
    })

with col1:
    st.title("Data Extraction Tool")
    news_article = st.text_area("Paste your financial news article here","paste paste paste" ,height=300)
    if st.button("Extract"):
        financial_data_df = openai_helper.extract_financial_data(news_article)

with col2:
    st.markdown("<br/>" * 5, unsafe_allow_html=True)  # Creates 5 lines of vertical space
    st.dataframe(
        financial_data_df,
        column_config={
            "Measure": st.column_config.Column(width=150),
            "Value": st.column_config.Column(width=150)
        },
        hide_index=True
    )

sample_data = [10, 20, 30, 40, 50]
sample_labels = ["Label 1", "Label 2", "Label 3", "Label 4", "Label 5"]

# Create a new row for the graph
st.markdown("<br/>" * 5, unsafe_allow_html=True)
st.subheader("Sample Graph")
plt.bar(sample_labels, sample_data)  # Create a simple bar chart
st.pyplot(plt)  # Display the graph in Streamlit