import os
from flytekit import workflow
from flytekit.types.file import FlyteFile
from utils.adam import create_adam_data
from utils.tfl import create_tfl_report

@workflow
def sce_workflow_1(sdtm_data_path: str) -> (FlyteFile, FlyteFile):
    """
    This workflow mocks a sample clinical trial, by taking in the directory to your SDTM data and eventually generating output TFL reports.

    To the run the workflow remotely, execute the following code in your terminal:
    
    pyflyte run --remote workflow.py sce_workflow_test --sdtm_data_path "/mnt/data/stdm-blind"

    :param sdtm_data_path: The root directory of your SDTM dataset
    :return: A list of PDF files containing the TFL reports
    """
    adsl = create_adam_data(name="ADSL", command="prod/adsl.sas", environmentId="65cd54180df82f018c4fb7cf", sdtm_data_path=sdtm_data_path)
    adae = create_adam_data(name="ADAE", command="prod/adae.sas", environmentId="65cd54180df82f018c4fb7cf", sdtm_data_path=sdtm_data_path, adam_dataset=adsl)
    advs = create_adam_data(name="ADVS", command="prod/advs.sas", environmentId="65cd54180df82f018c4fb7cf", sdtm_data_path=sdtm_data_path, adam_dataset=adsl)
    t_ae_rel = create_tfl_report(name="T_AE_REL", command="prod/t_ae_rel.sas", environmentId="65cd54180df82f018c4fb7cf", adam_dataset=adae)
    t_vscat = create_tfl_report(name="T_VSCAT", command="prod/t_ae_rel.sas", environmentId="65cd54180df82f018c4fb7cf", adam_dataset=advs)
    return t_ae_rel, t_vscat