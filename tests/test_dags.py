# from datetime import datetime
# from airflow.operators.bash import BashOperator
# from airflow.models import DAG
import pytest
from airflow.models import DagBag
import logging


@pytest.fixture()
def dagbag():
    return DagBag(dag_folder="dags")


def test_dag(dagbag):
    """Validate a complete DAG"""
    dagIds = dagbag.dag_ids
    logging.info("dagIds", dagIds)
    print(dagIds)

    for id in dagIds:
        dag = dagbag.get_dag(id)
        dag.test()


def test_import_dags(dagbag):
    assert not dagbag.import_errors
