import os
from domino.flyte.task import DominoJobConfig, DominoJobTask, EnvironmentRevisionSpecification, EnvironmentRevisionType, GitRef

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
        CommitId=CommitId, # DFS commit
        MainRepoGitRef=GitRef("Head"),
        EnvironmentRevisionSpec=EnvironmentRevisionSpecification(
            EnvironmentRevisionType=EnvironmentRevisionType.SomeRevision,
            EnvironmentRevisionId="65cd542f0df82f018c4fb7d3",
        ),
        HardwareTierId="small-k8s",
        VolumeSizeGiB=10,
        ExternalVolumeMountIds=[]
    )

    job = DominoJobTask(
        name,
        job_config,
        inputs=inputs,
        outputs=outputs
    )

    return job



 