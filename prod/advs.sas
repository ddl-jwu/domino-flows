/******************************************************************************
* This scripts mocks the following use case:
*  1. Loading in the original SDTM ta.sas7bdat data & a processed ADSL data
*  2. Using that data to create the ADVS dataset
* 
*  For simplcity, we will simply merging the datasets together
*****************************************************************************/
%include "/mnt/code/domino.sas";

options dlcreatedir;
libname inputs "/workflow/inputs"; /* All inputs live in this directory */ 
libname outputs "/workflow/outputs"; /* All outputs must go to this directory */ 

/* Hardcoding the dataset root for now. 
/* TODO: Take in the input string instead */

libname dataset "/mnt/code/blind";

data outputs.advs;
    merge dataset.ta inputs.adsl;
run;

/* (Required) This line signals to Domino Flows that outputs were successfully created */
libname success "/workflow/outputs/_SUCCESS";

