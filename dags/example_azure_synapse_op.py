from __future__ import annotations

import os
from datetime import datetime

from airflow.models import DAG
from airflow.providers.microsoft.azure.operators.synapse import AzureSynapseRunPipelineOperator

ENV_ID = os.environ.get("SYSTEM_TESTS_ENV_ID")

with DAG(
    dag_id="example_synapse_run_pipeline",
    start_date=datetime(2021, 8, 13),
    schedule="@daily",
    catchup=False,
    tags=["synapse", "example"],
) as dag:
    run_pipeline1 = AzureSynapseRunPipelineOperator(
        task_id="run_pipeline1",
        azure_synapse_conn_id="azure_synapse_connection",
        pipeline_name="Pipeline 1",
        azure_synapse_workspace_dev_endpoint="https://ambika-synapse-workspace.dev.azuresynapse.net",
        wait_for_termination=False
    )

    run_pipeline1
