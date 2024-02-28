import os
from .job import define_job
from typing import List
from domino.flyte.task import DominoJobConfig, DominoJobTask
from flytekit import workflow, task
from flytekit.types.file import FlyteFile
from flytekit.types.directory import FlyteDirectory

api_key=os.environ.get('DOMINO_USER_API_KEY')
owner_name=os.environ.get('DOMINO_USER_NAME')
project_name=os.environ.get('DOMINO_PROJECT_NAME')
CommitId="43d7dd73a00f7ab5f2c114f1dae635d6bf48a80e" # DFS artifacts git commit

class ADAM:
    def __init__(self, filename: str, data: FlyteFile):
        self.filename = filename
        self.data = data

def create_adam_data(
    name: str, 
    command: str, 
    environmentId: str, 
    sdtm_data_path: str = None, 
    adam_dataset: ADAM = None
) -> ADAM:

    inputs={"sdtm_data_path": str}

    if adam_dataset:
        inputs[adam_dataset.filename] = FlyteFile

    job = define_job(
        name=f"Create {name} dataset",
        command=command, 
        environmentId=environmentId,
        inputs=inputs,
        outputs={"adam": FlyteFile}
    )

    if adam_dataset:
        output = job(**{f"{adam_dataset.filename}": adam_dataset.data, "sdtm_data_path": sdtm_data_path})
    else:
        output = job(sdtm_data_path=sdtm_data_path)

    return ADAM(filename=f"{name}.7bdat", data=output)



 