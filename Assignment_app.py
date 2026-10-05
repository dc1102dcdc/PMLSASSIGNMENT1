from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd

app = FastAPI(title="PMLS Campaign Analysis")

CSV_FILE = "skin clinic campaign.csv"

def response_rate(data, group_col):
    result = data.groupby(group_col)["Response_to_Campaign"].apply(
        lambda x: (x == "Yes").mean() * 100
    ).reset_index()
    result.columns = [group_col, "Response Rate (%)"]
    result["Response Rate (%)"] = result["Response Rate (%)"].round(2)
    return result

@app.get("/")
def home():
    return {"message": "PMLS Campaign Analysis API is running"}

@app.get("/campaign-analysis", response_class=HTMLResponse)
def campaign_analysis():
    df = pd.read_csv(CSV_FILE)

    df["Age Group"] = pd.cut(
        df["Age"],
        bins=[0, 29, 50, float("inf")],
        labels=["<30", "30-50", ">50"]
    )

    df["Product Usage"] = pd.cut(
        df["Unique_Products_Purchased"],
        bins=[0, 4, 8, float("inf")],
        labels=["1-4", "5-8", ">8"]
    )

    gender = response_rate(df, "Gender")
    age = response_rate(df, "Age Group")
    purchase = response_rate(df, "Purchase_Last_Quarter")
    products = response_rate(df, "Product Usage")

    html = f'''
    <html>
    <head>
        <title>Campaign Analysis</title>
        <style>
            body {{ font-family: Arial; margin: 30px; }}
            table {{ border-collapse: collapse; margin-bottom: 30px; }}
            th, td {{ border: 1px solid #999; padding: 8px 12px; }}
            th {{ background: #5b9bd5; color: white; }}
        </style>
    </head>
    <body>
        <h1>Skin Clinic Campaign Analysis</h1>
        <h2>Gender vs Campaign Response</h2>
        {gender.to_html(index=False)}
        <h2>Age Group vs Campaign Response</h2>
        {age.to_html(index=False)}
        <h2>Purchase in Last Quarter vs Campaign Response</h2>
        {purchase.to_html(index=False)}
        <h2>Product Usage vs Campaign Response</h2>
        {products.to_html(index=False)}
    </body>
    </html>
    '''
    return html

