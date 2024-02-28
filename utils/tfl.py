import os
from .job import define_job
from .adam import ADAM
from typing import List
from domino.flyte.task import DominoJobConfig, DominoJobTask
from flytekit import workflow, task
from flytekit.types.file import FlyteFile
from flytekit.types.directory import FlyteDirectory

def create_tfl_report(
    name: str, 
    command: str, 
    environmentId: str, 
    adam_dataset: ADAM = None
) -> ADAM:

    inputs = {}
    inputs[adam_dataset.filename] = FlyteFile

    job = define_job(
        name=f"Generate {name} report ",
        command=command, 
        environmentId=environmentId,
        inputs=inputs,
        outputs={"report": FlyteFile}
    )

    output = job(**{f"{adam_dataset.filename}": adam_dataset.data})

    return output



 