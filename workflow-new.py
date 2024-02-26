
import os
from domino.flyte.task import DominoJobConfig, DominoJobTask
from utils.jobs import run_job, define_job
from flytekit import workflow, task
from flytekit.types.file import FlyteFile
from enum import Enum

class SDTMDataset(Enum):
    BLIND = "/mnt/code/blind"
    UNBLIND = "/mnt/code/unblind"

api_key=os.environ.get('DOMINO_USER_API_KEY')
owner_name=os.environ.get('DOMINO_USER_NAME')
project_name=os.environ.get('DOMINO_PROJECT_NAME')
CommitId="418feff0c0226f2b74af6edf64cbb574833d7fd5" # DFS artifacts git commit

# Define the job for creating ADSL dataset
job_config = DominoJobConfig(
    OwnerName=owner_name,
    ProjectName=project_name,
    ApiKey=api_key,
    Command="sleep 325",
    EnvironmentId="65cd54180df82f018c4fb7cf",
    CommitId=CommitId
)

job = DominoJobTask(
    "Dummy job",
    job_config,
    inputs={"data_path": str}
)

# Define the job for creating ADSL dataset
adsl_job_config = DominoJobConfig(
    OwnerName=owner_name,
    ProjectName=project_name,
    ApiKey=api_key,
    Command="prod/adsl.sas",
    EnvironmentId="65cd54180df82f018c4fb7cf",
    CommitId=CommitId
)

adsl_job = DominoJobTask(
    "Create ADSL dataset",
    adsl_job_config,
    inputs={"data_path": str},
    outputs={"adsl": FlyteFile}
)


# pyflyte run --remote workflow-new.py sas_workflow 
# @workflow
# def sas_workflow():
#     job = define_job(name="Create ADSL dataset", command="prod/adsl.sas", environment_id="65cd54180df82f018c4fb7cf", inputs={"tv.sas7bdat": FlyteFile}, outputs={"adsl": FlyteFile})
#     output = run_job(job, inputs={"tv.sas7bdat": "/mnt/code/data/tv.sas7bdat"})
#     return 



# pyflyte run --remote workflow-new.py sas_workflow --sdtm_data_folder "/mnt/code/blind"
@workflow
def sas_workflow(sdtm_data_folder: SDTMDataset):
    adsl = adsl_job(data_path="/mnt/code/blind")
    return 
