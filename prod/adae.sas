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

/* TODO: Read the inputs and write the outputs properly. For now, we will just create an empty output file */
libname adam "/workflow/outputs/adam";

