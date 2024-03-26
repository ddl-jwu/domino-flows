import os
from .job import define_job
from .adam import ADAM
from typing import List
from flytekitplugins.domino.task import DominoJobConfig, DominoJobTask
from flytekit import workflow, task
from flytekit.types.file import FlyteFile
from flytekit.types.directory import FlyteDirectory

def create_tfl_report(
    name: str, 
    command: str, 
    environment: str = "65cd54180df82f018c4fb7cf", # HARDCODING DEFAULT FOR NOW. NEED TO UPDATE THIS TO TAKE IN PROJECT DEFAULT 
    hardware_tier: str = "small-k8s", # HARDCODING DEFAULT FOR NOW. NEED TO UPDATE THIS TO TAKE IN PROJECT DEFAULT
    adam_dataset: ADAM = None
) -> FlyteFile:
    """
    This method provides a standard interface for creating a TFL report 

    :param name: The name in which to give the report. This is used to generate the step name.
    :param command: The command to execute for generating the report
    :param environmentId: The ID of the environment you want to you. 
    :param adam_dataset: The processed ADAM dataset to use for generating the report
    :return: A PDF files containing the final TFL report
    """
    inputs = {}
    inputs[adam_dataset.filename] = FlyteFile

    job = define_job(
        name=f" Generate {name} report",
        command=command, 
        environment=environment,
        hardware_tier=hardware_tier,
        inputs=inputs,
        outputs={"report": FlyteFile}
    )

    output = job(**{f"{adam_dataset.filename}": adam_dataset.data})

    return output



 