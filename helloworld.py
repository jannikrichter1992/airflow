from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
import subprocess

def install_modules():
    subprocess.call(['cd ', '/opt/airflow/envs'])
    subprocess.call(['python', '-m', 'venv' ,'helloworld_venv'])
    subprocess.call(['cd', '/helloworld_venv/bin'])
    subprocess.call(['./activate'])
    subprocess.call(['pip', 'install', '-r', 'helloworld_modules.txt'])

dag = DAG('hello_world_prep', description='Hello World DAG',
          schedule_interval='@once',
          start_date=datetime(2017, 3, 20), catchup=False)

hello_operator = PythonOperator(task_id='hello_prep_task', python_callable=install_modules, dag=dag)

hello_operator