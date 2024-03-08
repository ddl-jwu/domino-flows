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

    """
    This method provides a standard interface for creating a TFL report 

    :param name: The name in which to give the report. This is used to generate the step name.
    :param command: The command to execute for generating the report
    :param environmentId: The ID of the environment you want to you. 
    :param sdtm_data_path: The process ADAM dataset in which to generate the report with
    :return: A PDF files containing the final TFL report
    """

    inputs = {}
    inputs[adam_dataset.filename] = FlyteFile

    job = define_job(
        name=f" Generate {name} report ",
        command=command, 
        environmentId=environmentId,
        inputs=inputs,
        outputs={"report": FlyteFile}
    )

    output = job(**{f"{adam_dataset.filename}": adam_dataset.data})

    return output



 