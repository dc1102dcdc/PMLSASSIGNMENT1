# PMLS Assignment 1 - Model Deployment Using FastAPI

## Student Assignment

This project analyses the response to a skin clinic marketing campaign.

The analysis looks at:

1. Gender vs campaign response
2. Age group vs campaign response
3. Purchase in the last quarter vs campaign response
4. Number of unique products purchased vs campaign response

## Files

- `app.py` - FastAPI application
- `skin clinic campaign.csv` - campaign dataset
- `requirements.txt` - Python packages required
- `analysis_results.csv` - calculated results
- `README.md` - project information

## Running the API

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn app:app --reload
```

The API can then be opened at:

http://127.0.0.1:8000

The campaign analysis endpoint is:

http://127.0.0.1:8000/campaign-analysis

FastAPI also provides documentation at:

http://127.0.0.1:8000/docs

## Render Deployment

The project can be deployed to Render as a Web Service.

Build command:

```bash
pip install -r requirements.txt
```

Start command:

```bash
uvicorn app:app --host 0.0.0.0 --port $PORT
```

After deployment, Render provides a public URL. Add `/campaign-analysis` to the end of that URL to access the analysis.

## Main findings

Female customers had a higher response rate than male customers.

Customers aged 30-50 had the highest response rate of the three age groups.

Customers who purchased something in the last quarter had a much higher response rate than customers who did not.

Customers who purchased more than 8 unique products in the last year had the highest response rate in the product usage analysis.

