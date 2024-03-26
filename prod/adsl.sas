/******************************************************************************
* This scripts mocks the following use case:
*  1. Loading in the original SDTM tv.sas7bdat data 
*  2. Using that data to create the ADAM ADSL dataset
* 
*****************************************************************************/
%include "/mnt/code/domino.sas";

options dlcreatedir;
libname inputs "/workflow/inputs"; /* All inputs live in this directory at workflow/inputs/<NAME OF INPUT> */ 
libname outputs "/workflow/outputs"; /* All outputs must go to this directory at workflow/inputs/<NAME OF OUTPUT>y */ 

libname dataset "/mnt/data/snapshots/sdtm-blind/1";

/* TODO: Read the inputs and write the outputs properly. For now, we will just create an empty output file */
libname outputs "/workflow/outputs";
data outputs.adam;
    set dataset.tv;
run;


/* Testing */

/* data _null_; */
/*     call sleep(200000,1); */
/* run; */

/* %include "/mnt/code/domino.sas"; */
/* options dlcreatedir; */
/* libname dataset "/mnt/data/sdtm-blind"; */
/* libname adam "/workflow/outputs/adam"; */
/* data adam; */
/*     set dataset.tv; */
/* run; */