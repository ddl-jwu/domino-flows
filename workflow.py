import os
from flytekit import workflow
from flytekit.types.file import FlyteFile
from utils.adam import create_adam_data
from utils.tfl import create_tfl_report

@workflow
def sce_workflow_test_2(sdtm_data_path: str) -> (FlyteFile, FlyteFile):
    """
    This script mocks a sample clinical trial using Domino Flows. 

    The input to this flow is the path to your SDTM data. You can point this to either your SDTM-BLIND dataset or your SDTM-UNBLIND dataset. The output to this flow are a series of TFL reports.

    To the run the workflow remotely, execute the following code in your terminal:
    
    pyflyte run --remote workflow.py sce_workflow_test_2 --sdtm_data_path "/mnt/data/snapshots/sdtm-blind/1"

    :param sdtm_data_path: The root directory of your SDTM dataset
    :return: A list of PDF files containing the TFL reports
    """
    # Create task that generates ADSL dataset. This will run a unique Domino job and return its outputs.
    adsl = create_adam_data(
        name="ADSL", 
        command="prod/adsl.sas", 
        environment="SAS Analytics Pro", # Optional parameter. If not set, then the default for the project will be used.
        hardware_tier= "small-k8s", # Optional parameter. If not set, then the default for the project will be used.
        sdtm_data_path=sdtm_data_path # Note this this is simply the input value taken in from the command line argument
    )
    # Create step that generates ADAE dataset. This takes the output from the previous task as an input.
    adae = create_adam_data(
        name="ADAE", 
        command="prod/adae.sas", 
        sdtm_data_path=sdtm_data_path, 
        adam_dataset=adsl # Note how this is the output from the previous task
    )
    # Create step that generates ADVS dataset. 
    advs = create_adam_data(
        name="ADVS", 
        command="prod/advs.sas", 
        sdtm_data_path=sdtm_data_path, 
        adam_dataset=adsl
    )
    # Create step that generates TFL report from ADAE dataset.
    t_ae_rel = create_tfl_report(
        name="T_AE_REL", 
        command="prod/t_ae_rel.sas", 
        adam_dataset=adae
    )
    # Create step that generates TFL report from ADVS dataset
    t_vscat = create_tfl_report(
        name="T_VSCAT", 
        command="prod/t_ae_rel.sas", 
        adam_dataset=advs
    )
    return t_ae_rel, t_vscat