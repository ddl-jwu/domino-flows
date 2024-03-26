import os
from .job import define_job
from typing import List
from flytekitplugins.domino.task import DominoJobConfig, DominoJobTask
from flytekit import workflow, task
from flytekit.types.file import FlyteFile
from flytekit.types.directory import FlyteDirectory

class ADAM:
    def __init__(self, filename: str, data: FlyteFile):
        self.filename = filename
        self.data = data

# TODO: Options to add: HWT
def create_adam_data(
    name: str, 
    command: str, 
    environment: str = "65cd54180df82f018c4fb7cf", # HARDCODING DEFAULT FOR NOW. NEED TO UPDATE THIS TO TAKE IN PROJECT DEFAULT 
    hardware_tier: str = "small-k8s", # HARDCODING DEFAULT FOR NOW. NEED TO UPDATE THIS TO TAKE IN PROJECT DEFAULT
    sdtm_data_path: str = None, 
    adam_dataset: ADAM = None
) -> ADAM:
    """
    This method provides a standard interface for creating an ADAM dataset 

    :param name: The name in which to give the dataset. This is used to generate the step name.
    :param command: The command to execute for generating the dataset
    :param environmentId: The ID of the environment you want to you. 
    :param sdtm_data_path: The root directory to the SDTM data
    :param adam_dataset: Any processed ADAM dataset to use in the generation.
    :return: An ADAM dataset
    """
    inputs={"sdtm_data_path": str}

    if adam_dataset:
        inputs[adam_dataset.filename] = FlyteFile

    job = define_job(
        name=f" Create {name}  dataset   ",
        command=command, 
        environment=environment,
        hardware_tier=hardware_tier,
        inputs=inputs,
        outputs={"adam": FlyteFile}
    )

    if adam_dataset:
        output = job(**{f"{adam_dataset.filename}": adam_dataset.data, "sdtm_data_path": sdtm_data_path})
    else:
        output = job(sdtm_data_path=sdtm_data_path)

    return ADAM(filename=f"{name}.sas7bdat".lower(), data=output)


 