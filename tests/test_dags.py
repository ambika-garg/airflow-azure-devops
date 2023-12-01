# from datetime import datetime
# from airflow.operators.bash import BashOperator
# from airflow.models import DAG
import os
import sys
import pytest
from airflow.models import DagBag
import logging


sys.path.append(os.path.join(os.path.dirname(__file__), "./dags"))


@pytest.fixture()
def dagbag():
    return DagBag(dag_folder="dags", include_examples=False)


def test_dag(dagbag):
    """Validate a complete DAG"""
    dagIds = dagbag.dag_ids
    logging.info("dagIds %s", dagIds)
    # print(dagIds)

    for id in dagIds:
        dag = dagbag.get_dag(id)
        dag.test()

def test_expected_dags(dagbag):
    """
    Test whether expected dag Ids are present.
    """
    expected_dag_ids = ["ci-cd-demo"]
    for dag_id in expected_dag_ids:
        dag = dagbag.get_dag(dag_id)

    assert dag is not None
    assert dag_id == dag.dag_id

def test_import_dags(dagbag):
    assert not dagbag.import_errors
