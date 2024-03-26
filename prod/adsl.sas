/******************************************************************************
* This scripts mocks the following use case:
*  1. Loading in the original SDTM tv.sas7bdat data 
*  2. Using that data to create the ADAM ADSL dataset
* 
*****************************************************************************/
%include "/mnt/code/domino.sas";

/* NOTE: Inputs are stored at /workflow/inputs/<NAME OF INPUT>. 
/* TODO: Take in the actual input from /workflow/inputs/<NAME OF INPUT>. For now, just hardcoding the input */
libname dataset "/mnt/data/sdtm-blind";

/* Outputs are written to /workflow/outputs/<OUTPUT NAME> */
/* TODO: Write actual data to the output. For now, just creating an empty file */
options dlcreatedir;
libname outputs "/workflow/outputs"; 

data outputs.adam;
    set dataset.tv;
run;
