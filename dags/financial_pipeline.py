from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Importa suas funções
import sys
import os

# Adiciona o path da pasta scripts
BASE_DIR = '/opt/airflow'
SCRIPTS_PATH = os.path.join(BASE_DIR, "scripts")

sys.path.append('/opt/airflow')


from scripts.extract import getData
from scripts.transform import transform_actions
from scripts.load import load_data

# Configuração padrão
default_args = {
    "owner": "luis",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Definição da DAG
with DAG(
    dag_id="financial_data_pipeline",
    default_args=default_args,
    description="Pipeline de dados financeiros com Airflow",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["finance", "etl"],
) as dag:

    # 🔹 Task 1 - Extract
    def extract_task():
        data = getData()

        import json
        with open(os.path.join(BASE_DIR, "database", "actions.json"), "w") as f:
            json.dump(data, f, indent=4)

    extract = PythonOperator(
        task_id="extract_data",
        python_callable=extract_task
    )

    # 🔹 Task 2 - Transform
    def transform_task():
        df = transform_actions()
        df.to_csv(os.path.join(BASE_DIR, "database", "actions.csv"), index=False)

    transform = PythonOperator(
        task_id="transform_data",
        python_callable=transform_task
    )

    # 🔹 Task 3 - Load
    load = PythonOperator(
        task_id="load_data",
        python_callable=load_data
    )

    # 🔗 Ordem das tasks
    extract >> transform >> load