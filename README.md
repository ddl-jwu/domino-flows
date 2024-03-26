# Clincial Trial Workflow

This repo mocks a sample SCE clinical trial using Domino Flows. 

The input to this flow is the path to your SDTM data. You can point this to either a snapshot of your SDTM-BLIND dataset or your SDTM-UNBLIND dataset. The output to this flow are a series of TFL reports.

To run the flow, execute the following command in a workspace: 

```
pyflyte run --remote workflow.py sce_workflow --sdtm_data_path "/mnt/data/snapshots/sdtm-blind/1"
```

If you want to change the input data, replace the `sdtm_data_path` parameter with the location to your input data.

## Flow Breakdown

The flow definition is located in the file named `workflow.py` under a method called `sce_workflow`. Notice how the SDTM dataset path that was specified in the command line argument gets taken in as parameter to this method.

Within the flow definition, there are two helper methods that are used for defining common tasks that are used in clinical trial studies. These methods will utltimately trigger a Domino Job with the specified parameters and return the outputs that get produced by the job.  

**create_adam_data()**

This method provides a standardized interface for triggering a SAS script that produces an ADAM dataset. 

Here is a sample code snippet of how the method can be used:

```
# Create task that generates ADSL dataset. This will run a unique Domino job and return its outputs.
adsl = create_adam_data(
    name="ADSL", 
    command="prod/adsl.sas", 
    environment="SAS Analytics Pro", 
    hardware_tier= "small-k8s", 
    sdtm_data_path="/mnt/data/stdm-blind"
)
# Create task that generates ADAE dataset. This takes the output from the previous task as an input.
adae = create_adam_data(
    name="ADAE", 
    command="prod/adae.sas", 
    sdtm_data_path="/mnt/data/stdm-blind", 
    adam_dataset=adsl # Note that this is the output from the previous step
)
```
Explaining the parameters in more detail:

- `name`: The name for the dataset that will be produced.
- `command`: The command that will be used when triggering the Domino job. This should point to the SAS file you want to execute.
- `environment`: The name of the environment to use in the job. If not specified, this will point to the default environment.
- `hardware_tier`: The name of the hardware tier to use in the job. If not specified, this will point to the default hardware tier.
- `sdtm_data_path`: This is the path pointing to the location of the SDTM data. This parameter will be taken into the task as an input, which can be parsed and used as a parameter within the SAS script during the Domino job.
- `adam_dataset`: The is the output from another create_adam_data() task, which is effectively a pointer to a blob storage location where that previous output was written to. This is passed as an input, which can be used within the SAS script during the Domino job.

Within the SAS script that gets executed by this method:

- You can get the `sdtm_data_path` variable by reading the contents of the file located at `/workflow/inputs/sdtm_data_path`
- You can get the `adam_dataset` by loading the contents of the file located at `/workflow/inputs/<NAME OF DATASET>`
- The output ADAM dataset must be written to `workflow/outputs/adam` in order for it to be returned, tracked properly, and passed into another task.

**create_tfl_report**

This method provides a standardized interface for triggering a SAS script that to produces aa TFL report. 

Here is a sample code snippet of how the method can be used:

```
t_ae_rel = create_tfl_report(
    name="T_AE_REL", 
    command="prod/t_ae_rel.sas", 
    environment="SAS Analytics Pro",  
    hardware_tier="small-k8s",
    adam_dataset=adae
)
```
Explaining the parameters in more detail:

- `name`: A name for the task
- `command`: The command that will be use when triggering the Domino job. This should point to the SAS file you want to execute.
- `environment`: The name of the environment to use in the job. If not specified, this will point to the default environment.
- `hardware_tier`: The name of the hardware tier to use in the job. If not specified, this will point to the default hardware tier.
- `adam_dataset`: The is the output from a create_adam_data() task, which is effectively a pointer to a blob storage location where an ADAM dataset exists. This is passed as an input, which can be used within the SAS script to create the final report.

Within the SAS script that gets executed by this method:

- You can get the `adam_dataset` by loading the contents of the file located at `/workflow/inputs/<NAME OF DATASET>`
- The output report must be written to `workflow/outputs/report` in order for it to be returned and tracked properly.

