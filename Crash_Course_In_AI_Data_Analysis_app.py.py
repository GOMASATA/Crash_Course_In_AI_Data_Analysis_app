# streamlit_app.py
import streamlit as st

# Set page config
st.set_page_config(page_title="Crash Course in AI Data Analysis", layout="wide")

# Title
st.title("📘 Crash Course in AI Data Analysis: From Basics to Real World Projects")
st.markdown("---")

# Helper function to display chapters
def show_chapter(title, content, code_blocks=None):
    st.header(title)
    st.write(content)
    if code_blocks:
        for code in code_blocks:
            st.code(code, language="python")
    st.markdown("---")

# Introduction
show_chapter("Introduction", """
Why AI + Data Analysis matters today
Real world applications (business, trading, customer service, healthcare, finance)
What readers will gain from this crash course:
- Practical Python skills
- AI techniques for analysis
- Hands-on projects
- Deployment strategies
- Ethical awareness
""")

# Chapter 1
show_chapter("Chapter 1: Foundations of Data Analysis", """
Data analysis is the process of examining raw information to uncover patterns, trends, and insights.

Types of Data:
- Structured: Organized in rows/columns (spreadsheets, databases)
- Unstructured: Free form (emails, social posts, audio)
- Semi-structured: JSON, XML

Key Concepts:
- Datasets, Features, Labels, Metrics

Tools Overview:
- Python, Pandas, NumPy, Excel, SQL
""")

# Chapter 2
show_chapter("Chapter 2: AI Meets Data Analysis", """
Traditional vs AI Driven Analysis:
Traditional = manual effort. AI automates and uncovers deeper insights.

Core AI Concepts:
- Supervised, Unsupervised, Reinforcement Learning

Generative vs Discriminative AI:
- Generative: Creates new content
- Discriminative: Classifies categories

Popular Frameworks:
- Scikit-Learn, TensorFlow, PyTorch, NLP libraries
""")

# Chapter 3 with code examples
show_chapter("Chapter 3: Essential Python Skills", """
Setting up your environment (Python, Anaconda, Jupyter, VS Code)
Data cleaning, preprocessing, visualization, automation
""", code_blocks=[
    'import pandas as pd\ndf = pd.read_csv("jobs.csv")\ndf = df.dropna()\ndf = df.rename(columns={"JobTitle":"Title"})',
    'import numpy as np\narr = np.array([10,20,30,40])\nprint(np.mean(arr))',
    'import matplotlib.pyplot as plt\nimport seaborn as sns\nsns.histplot(df["Salary"], bins=10, kde=True)\nplt.show()'
])

# Chapter 4 with code examples
show_chapter("Chapter 4: Practical AI Techniques", """
Regression, Classification, Clustering, NLP, Time-Series Analysis
""", code_blocks=[
    'from sklearn.linear_model import LinearRegression\nimport pandas as pd\n\n# Regression Example\ndata = {"Experience":[1,2,3,4,5], "Salary":[8500,9500,11000,12500,14000]}\ndf = pd.DataFrame(data)\nX = df[["Experience"]]\ny = df["Salary"]\nmodel = LinearRegression()\nmodel.fit(X, y)\nprint(model.predict([[6]]))',
    'from sklearn.tree import DecisionTreeClassifier\nX = [[1],[2],[3],[4],[5]]\ny = ["No","No","Yes","Yes","Yes"]\nmodel = DecisionTreeClassifier()\nmodel.fit(X, y)\nprint(model.predict([[2]]))',
    'from sklearn.cluster import KMeans\nimport numpy as np\nX = np.array([[100],[200],[300],[400],[500]])\nkmeans = KMeans(n_clusters=2)\nkmeans.fit(X)\nprint(kmeans.labels_)',
    'from textblob import TextBlob\nreview = "The service was excellent!"\nprint(TextBlob(review).sentiment)'
])

# Chapter 5 with projects
show_chapter("Chapter 5: Hands-On Projects", """
Project 1: Knowledge Retrieval Bot
Project 2: Forex Trading Signal Analyzer
Project 3: Call Centre Job Market Dashboard
Project 4: Sentiment Analysis on Social Media
""", code_blocks=[
    'from whoosh.index import create_in\nfrom whoosh.fields import Schema, TEXT\nfrom whoosh.qparser import QueryParser\n\nschema = Schema(content=TEXT(stored=True))\nix = create_in("indexdir", schema)\nwriter = ix.writer()\nwriter.add_document(content="Policy: Verify ID before service.")\nwriter.commit()\n\nwith ix.searcher() as searcher:\n    query = QueryParser("content", ix.schema).parse("ID")\n    results = searcher.search(query)\n    for r in results:\n        print(r["content"])',
    'import pandas as pd\ndata = {"Close":[1800,1810,1820,1815,1805,1795,1800]}\ndf = pd.DataFrame(data)\ndf["Change"] = df["Close"].diff()\ndf["Gain"] = df["Change"].clip(lower=0)\ndf["Loss"] = -df["Change"].clip(upper=0)\navg_gain = df["Gain"].rolling(14).mean()\navg_loss = df["Loss"].rolling(14).mean()\nrs = avg_gain / avg_loss\ndf["RSI"] = 100 - (100 / (1 + rs))\nprint(df)',
    'import streamlit as st\nimport pandas as pd\nimport seaborn as sns\n\ndf = pd.read_csv("callcentre_jobs.csv")\nst.title("Job Market Dashboard")\nsns.countplot(x="Location", data=df)\nst.pyplot()',
    'from textblob import TextBlob\ncomments = ["Great service!", "Terrible wait time.", "Average experience."]\nfor c in comments:\n    print(c, "→", TextBlob(c).sentiment.polarity)'
])

# Chapter 6
show_chapter("Chapter 6: Deploying and Sharing Your Work", """
Dashboards: Streamlit, Dash, Voila
Publishing Apps: Streamlit Cloud, Heroku, GitHub Pages
Digital Portfolios: GitHub, LinkedIn, Personal websites
Sharing Reports: Export notebooks as PDF/HTML
""")

# Chapter 7
show_chapter("Chapter 7: Ethics and Future of AI Data Analysis", """
Bias in AI, Responsible Data Handling, Transparency, Human Element
Future Trends: Automation, Edge AI, AI + Creativity, Global collaboration
""")

# Conclusion
show_chapter("Conclusion", """
Recap: Python skills, AI techniques, projects, deployment, ethics
Next Steps: Continue learning, apply AI analysis, build portfolio
""")
