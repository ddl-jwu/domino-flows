import os
from flytekit import workflow
from flytekit.types.file import FlyteFile
from utils.adam import create_adam_data
from utils.tfl import create_tfl_report

@workflow
def sce_workflow_test_1(sdtm_data_path: str) -> (FlyteFile, FlyteFile):
    """
    This workflow mocks a sample clinical trial, by taking in the directory 
    to a SDTM dataset and eventually generating output TFL reports.

    To the run the workflow remotely, execute the following code in your terminal:
    
    pyflyte run --remote workflow.py sce_workflow_test --sdtm_data_path "/mnt/data/stdm-blind"

    :param sdtm_data_path: The root directory of your SDTM dataset
    :return: A list of PDF files containing the TFL reports
    """
    # Create step that generates ADSL dataset
    adsl = create_adam_data(
        name="ADSL", 
        command="prod/adsl.sas", 
        environment="SAS Analytics Pro", 
        hardware_tier= "small-k8s", # Optional parameter. If not set, then the default for the project will be used
        sdtm_data_path=sdtm_data_path
    )
    # Create step that generates ADAE dataset
    adae = create_adam_data(
        name="ADAE", 
        command="prod/adae.sas", 
        environment="SAS Analytics Pro",
        hardware_tier="small-k8s",
        sdtm_data_path=sdtm_data_path, 
        adam_dataset=adsl
    )
    # Create step that generates ADVS dataset
    advs = create_adam_data(
        name="ADVS", 
        command="prod/advs.sas", 
        environment="SAS Analytics Pro", 
        hardware_tier="small-k8s",
        sdtm_data_path=sdtm_data_path, 
        adam_dataset=adsl
    )
    # Create step that generates TFL report from ADAE dataset
    t_ae_rel = create_tfl_report(
        name="T_AE_REL", 
        command="prod/t_ae_rel.sas", 
        environment="SAS Analytics Pro",  
        hardware_tier="small-k8s",
        adam_dataset=adae
    )
    # Create step that generates TFL report from ADVS dataset
    t_vscat = create_tfl_report(
        name="T_VSCAT", 
        command="prod/t_ae_rel.sas", 
        environment="SAS Analytics Pro",  
        hardware_tier="small-k8s",
        adam_dataset=advs
    )
    return t_ae_rel, t_vscat