# Financial Data Extraction

The Financial News Data Extraction Tool is a web application built using Streamlit, a Python library for creating interactive web applications for data science and machine learning tasks. The purpose of this project is to help users extract relevant financial data from news articles quickly and efficiently.

The application has a simple and user-friendly interface that consists of two main components:

Data Extraction Section:
In this section, users can paste a financial news article into a text area. The application leverages the OpenAI GPT-3.5-based language model and a custom-built helper module called "openai_helper" to analyze the input text and extract specific financial data. Users can click the "Extract" button to trigger the data extraction process.

Financial Data Display Section:
After extracting the financial data from the news article, the results are displayed in a structured tabular format. The data includes essential financial measures such as the Company Name, Stock Symbol, Revenue, Net Income, and EPS (Earnings Per Share). The data is presented neatly in a DataFrame, making it easy for users to analyze and interpret the information.

Additionally, to enhance the data presentation, the application features a simple bar chart displaying sample financial data. The graph is situated below the data extraction and display components, allowing users to visualize some example data points related to the financial measures extracted from the article.

Potential Use Cases:

Financial Analysts: Financial analysts can use this tool to quickly gather key financial metrics from news articles related to specific companies or industries. The extracted data can aid in performing analyses, creating reports, and making informed investment decisions.
Investors: Investors can utilize the application to stay up-to-date with financial news and extract relevant financial data of companies they are interested in, helping them assess potential investment opportunities.
Traders: Traders can use the tool to monitor the impact of financial news on different companies' performance and quickly identify trends or anomalies.
Note: The actual functionality and effectiveness of the tool will heavily rely on the underlying natural language processing capabilities of the OpenAI GPT-3.5 model and the accuracy of the custom-built "openai_helper" module. Additionally, the sample graph included in the project is for illustrative purposes and should be replaced with real financial data and more sophisticated visualizations in a production-ready application.
![image](https://github.com/Monish-07/Financial-Data-Extraction/assets/95215581/067f27db-f8dd-456e-a557-3453509163b5)
![image](https://github.com/Monish-07/Financial-Data-Extraction/assets/95215581/7c7ae2da-cb8c-4a7e-956f-1c25c3d997ad)

