import os
from domino.flyte.task import DominoJobConfig, DominoJobTask

api_key=os.environ.get('DOMINO_USER_API_KEY')
owner_name=os.environ.get('DOMINO_USER_NAME')
project_name=os.environ.get('DOMINO_PROJECT_NAME')
CommitId="43d7dd73a00f7ab5f2c114f1dae635d6bf48a80e" # DFS artifacts git commit

def define_job(
    name: str, 
    command: str, 
    environmentId: str, 
    inputs: dict = None,
    outputs: dict = None
) -> DominoJobTask:

    job_config = DominoJobConfig(
        OwnerName=owner_name,
        ProjectName=project_name,
        ApiKey=api_key,
        Command=command,
        EnvironmentId=environmentId,
        CommitId=CommitId # DFS commit
    )

    job = DominoJobTask(
        name,
        job_config,
        inputs=inputs,
        outputs=outputs
    )

    return job



 