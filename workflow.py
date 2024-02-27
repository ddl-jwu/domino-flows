
import os
from flytekit import workflow
from flytekit.types.file import FlyteFile
from utils.adam import create_adam_data

# pyflyte run --remote workflow.py study_workflow --sdtm_data_path "/mnt/code/blind"
@workflow
def study_workflow(sdtm_data_path: str) -> FlyteFile:
    adsl = create_adam_data(name="ADSL", command="prod/adsl.sas", environmentId="65cd54180df82f018c4fb7cf", sdtm_data_path=sdtm_data_path)
    return adsl.data