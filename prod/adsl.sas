/******************************************************************************
* This scripts mocks the following use case:
*  1. Loading in the original SDTM tv.sas7bdat data 
*  2. Using that data to create the ADSL dataset
* 
*  For simplcity, we will simply carry forward the input to the output directory
*****************************************************************************/
%include "/mnt/code/domino.sas";
options dlcreatedir;

/* NOTE: Inputs are stored at /workflow/inputs/<NAME OF INPUT>. 
/* TODO: Take in the actual input from /workflow/inputs/<NAME OF INPUT>. For now, just hardcoding the input */
libname dataset "/mnt/data/sdtm-blind";

/* Outputs are written to /workflow/outputs/adam*/
libname adam "/workflow/outputs/adam"; /* All outputs must be written to this directory */ 

data adam;
    set dataset.tv;
run;
