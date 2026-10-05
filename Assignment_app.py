from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="Skin Clinic Campaign Analysis")

# Load the campaign data
data = pd.read_csv("skin clinic campaign.csv")

# Create product usage groups
data["Product_Usage_Category"] = pd.cut(
    data["Unique_Products_Purchased"],
    bins=[0, 4, 8, float("inf")],
    labels=["1-4", "5-8", ">8"]
)

def make_table(column):
    result = data.groupby(column, observed=False).agg(
        Customers=("Response_to_Campaign", "size"),
        Responded=("Response_to_Campaign", lambda x: (x == "Yes").sum())
    ).reset_index()

    result["Response_Rate_%"] = (
        result["Responded"] / result["Customers"] * 100
    ).round(2)

    return result

@app.get("/")
def home():
    return {"message": "Skin Clinic Campaign Analysis API"}

@app.get("/campaign-analysis")
def campaign_analysis():
    return {
        "Gender_vs_Campaign_Response": make_table("Gender").to_dict(orient="records"),
        "Age_Group_vs_Campaign_Response": make_table("AgeGroup").to_dict(orient="records"),
        "Purchase_Last_Quarter_vs_Campaign_Response": make_table(
            "Purchase_Last_Quarter"
        ).to_dict(orient="records"),
        "Product_Usage_vs_Campaign_Response": make_table(
            "Product_Usage_Category"
        ).to_dict(orient="records")
    }
