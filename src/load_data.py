import os
from google.cloud import bigquery
from dotenv import load_dotenv


def load_data_to_bigquery_clear_table(dataset_id, table_id, data):

    load_dotenv()

    # Initialize a BigQuery client
    client = bigquery.Client()

    # Specify the dataset and table
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    # Load data into the table
    job_config = bigquery.LoadJobConfig(autodetect=True,write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE) 
    job = client.load_table_from_json(data, table_ref, job_config=job_config)
    
    # Wait for the job to complete
    job.result()

    print(f"Loaded {len(data)} rows into {table_id}")