/******************************************************************************
* This scripts mocks the following use case:
*  1. Loading in the original SDTM ts.sas7bdat data & a processed ADSL data
*  2. Using that data to create the ADAE dataset
* 
*  For simplcity, we will simply merging the datasets together
*****************************************************************************/
%include "/mnt/code/domino.sas";

options dlcreatedir;
libname inputs "/workflow/inputs"; /* All inputs live in this directory */ 
libname outputs "/workflow/outputs"; /* All outputs must go to this directory */ 

/* Hardcoding the dataset root for now. 
/* TODO: Take in the actual input from instead /workflow/inputs/<NAME OF INPUT> instead */
libname dataset "/mnt/data/sdtm-blind";

data outputs.adam;
    merge dataset.ts inputs.adsl;
run;

/* (Required) This line signals to Domino Flows that outputs were successfully created */
libname success "/workflow/outputs/_SUCCESS";

