import os
from domino.flyte.task import DominoJobConfig, DominoJobTask
from flytekit import workflow, task
from flytekit.types.file import FlyteFile, CSVFile
from flytekit.types.directory import FlyteDirectory

api_key=os.environ.get('DOMINO_USER_API_KEY')
owner_name=os.environ.get('DOMINO_USER_NAME')
project_name=os.environ.get('DOMINO_PROJECT_NAME')
CommitId="418feff0c0226f2b74af6edf64cbb574833d7fd5" # DFS artifacts git commit

def define_job(name: str, command: str, environment_id: str, inputs: dict, outputs: dict):
    job_config = DominoJobConfig(
        OwnerName=owner_name,
        ProjectName=project_name,
        ApiKey=api_key,
        Command=command,
        EnvironmentId=environment_id,
        CommitId=CommitId
    )
    job = DominoJobTask(
        name,
        job_config,
        inputs=inputs,
        outputs=outputs
    )
    return job

def run_job(job: DominoJobTask, inputs: dict):
    outputs = job(inputs)
    return outputs



 