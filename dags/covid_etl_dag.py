from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import pandas as pd
import os

# 1️⃣ Extract data
def extract_data():
    url = "https://disease.sh/v3/covid-19/countries"
    response = requests.get(url)
    data = response.json()
    df = pd.json_normalize(data)
    os.makedirs("/tmp/data", exist_ok=True)
    df.to_csv("/tmp/data/raw_covid_data.csv", index=False)
    print("✅ Extracted data saved to /tmp/data/raw_covid_data.csv")

# 2️⃣ Transform data
def transform_data():
    df = pd.read_csv("/tmp/data/raw_covid_data.csv")
    df = df[['country', 'cases', 'deaths', 'updated']]
    df.rename(columns={
        'country': 'Country',
        'cases': 'TotalConfirmed',
        'deaths': 'TotalDeaths',
        'updated': 'Date'
    }, inplace=True)
    df.to_csv("/tmp/data/clean_covid_data.csv", index=False)
    print("✅ Transformed data saved to /tmp/data/clean_covid_data.csv")

# 3️⃣ Load data
# def load_data():
#     df = pd.read_csv("/tmp/data/clean_covid_data.csv")
#     df.to_csv("/tmp/data/final_covid_data.csv", index=False)
#     print("✅ Final data saved to /tmp/data/final_covid_data.csv")

from airflow.providers.postgres.hooks.postgres import PostgresHook

def load_data():
    import pandas as pd

    # Read transformed data
    df = pd.read_csv('/tmp/data/clean_covid_data.csv')

    # Connect to Postgres
    hook = PostgresHook(postgres_conn_id='postgres_default')
    engine = hook.get_sqlalchemy_engine()

    # Write data to Postgres
    with engine.connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS covid_data (
                Country TEXT,
                TotalConfirmed INT,
                TotalDeaths INT,
                Date TIMESTAMP
            );
        """)
        df.to_sql('covid_data', con=engine, if_exists='replace', index=False)


# Define DAG
with DAG(
    dag_id="covid_etl_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    description="ETL pipeline for COVID-19 data using disease.sh API"
) as dag:

    extract = PythonOperator(
        task_id="extract",
        python_callable=extract_data
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=transform_data
    )

    load = PythonOperator(
        task_id="load",
        python_callable=load_data
    )

    extract >> transform >> load
