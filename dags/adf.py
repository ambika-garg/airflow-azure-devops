from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="demo_one", start_date=datetime(2023, 8, 15), schedule="0 0 * * *") as dag:

    # Tasks are represented as operators
    task1 = BashOperator(task_id="hello", bash_command="echo hello")

    version = BashOperator(task_id="Check_python_version", bash_command="python --version")

    task2 = BashOperator(task_id="task2", bash_command="echo task2")

    task3 = BashOperator(task_id="task3", bash_command="echo task3")

    task4 = BashOperator(task_id="task4", bash_command="echo task4")

    task5 = BashOperator(task_id="task5", bash_command="echo task5")

    # Set dependencies between tasks
    task1 >> version >> task2 >> task3 >> task4
