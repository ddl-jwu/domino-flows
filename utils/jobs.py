import os
from domino.flyte.task import DominoJobConfig, DominoJobTask
from flytekit import workflow, task
from flytekit.types.file import FlyteFile
from flytekit.types.directory import FlyteDirectory

api_key=os.environ.get('DOMINO_USER_API_KEY')
owner_name=os.environ.get('DOMINO_USER_NAME')
project_name=os.environ.get('DOMINO_PROJECT_NAME')
CommitId="43d7dd73a00f7ab5f2c114f1dae635d6bf48a80e" # DFS artifacts git commit

def create_adam_data(name: str, command: str, environmentId: str, sdtm_dataset: str) -> FlyteFile:

    job_config = DominoJobConfig(
        OwnerName=owner_name,
        ProjectName=project_name,
        ApiKey=api_key,
        Command=command,
        EnvironmentId=environmentId,
        CommitId=CommitId, # DFS commit
        mainRepoGitRef=GitRef("head")  # Only relevant for git-based projects
    )

    job = DominoJobTask(
        f"Create {name} dataset",
        job_config,
        inputs={"sdtm_dataset": str},
        outputs={"adam": FlyteFile}
    )

    return job(sdtm_dataset=sdtm_dataset)



 