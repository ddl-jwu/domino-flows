# sas-workflow

This repo mocks a sample clinical trial, by taking in multiple SDTM data files and eventually generating output PDF reports.

To run the workflow using the sample data execute the following command: 

```
pyflyte run --remote workflow.py sas_workflow --sdtm_tv_file "/mnt/code/data/tv.sas7bdat" --sdtm_ts_file "/mnt/code/data/ts.sas7bdat" --sdtm_ta_file "/mnt/code/data/ta.sas7bdat"
```

If you want to change the input data, replace the sdtm_tv_file, sdtm_ts_file, sdtm_ta_file parameters with locations to your input data.