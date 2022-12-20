from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonVirtualenvOperator

def print_hello():
    return 'Hello world from first Airflow DAG!'

def get_modules():
    requirments = open("/opt/airflow/dags/helloworld_modules.txt", "r")
    lines = requirments.readlines()
    requirments.close()
    return lines

dag = DAG('hello_world_prep', description='Hello World DAG',
          schedule_interval='@once',
          start_date=datetime(2017, 3, 20), catchup=False)

python_task = PythonVirtualenvOperator(
        task_id='task1',
        python_callable=print_hello,
        requirements=get_modules(),
        #python_version='3.8',
        provide_context=True,
        dag=dag
    )

dummy_task = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

python_task >> dummy_task