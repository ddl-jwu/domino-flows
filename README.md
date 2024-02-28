# sas-workflow

This repo mocks a sample clinical trial, by taking in the directory to your SDTM data and eventually generating output TFL reports.

To run the workflow using the sample data execute the following command: 

```
pyflyte run --remote workflow.py study_workflow --sdtm_data_path "/mnt/code/blind"
```

If you want to change the input data, replace the sdtm_data_path parameters with the location to your input data.