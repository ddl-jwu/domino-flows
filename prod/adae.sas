/******************************************************************************
* This is a dummy script that mocks the following use case:
*  1. Loading in the original SDTM ts.sas7bdat data & a processed ADSL data
*  2. Using that data to create the ADAE dataset
* 
*****************************************************************************/
%include "/mnt/code/domino.sas";

options dlcreatedir;
libname inputs "/workflow/inputs"; /* All inputs live in this directory at workflow/inputs/<NAME OF INPUT> */ 
libname outputs "/workflow/outputs"; /* All outputs must go to this directory at workflow/inputs/<NAME OF OUTPUT>y */ 

libname dataset "/mnt/data/snapshots/sdtm-blind/1";

data outputs.adam;
    merge dataset.ts inputs.adsl;
run;


