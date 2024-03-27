/******************************************************************************
* This scripts mocks the following use case:
*  1. Loading in the original SDTM tv.sas7bdat data 
*  2. Using that data to create the ADAM ADSL dataset
* 
*  For simplicity, we are going to just return the same dataset back
*  and assume some data processing happened.
*****************************************************************************/
/* %include "/mnt/code/domino.sas"; */

options dlcreatedir;
libname inputs "/workflow/inputs"; /* All inputs live in this directory at workflow/inputs/<NAME OF INPUT> */ 
libname outputs "/workflow/outputs"; /* All outputs must go to this directory at workflow/inputs/<NAME OF OUTPUT>y */ 

/* HITTING A BUG WITH READING IN THE INPUT STRING PROPERLY. HARDCODING THE DATASET PATH FOR NOW */
libname dataset "/mnt/data/snapshots/sdtm-blind/1";

libname outputs "/workflow/outputs";
data outputs.adam;
    set dataset.tv;
run;