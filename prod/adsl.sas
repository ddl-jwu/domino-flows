/******************************************************************************
* This scripts mocks the following use case:
*  1. Loading in the original SDTM tv.sas7bdat data 
*  2. Using that data to create the ADSL dataset
* 
*  For simplcity, we will simply carry forward the input to the output directory
*****************************************************************************/
%include "/mnt/code/domino.sas";

options dlcreatedir;
libname outputs "/workflow/outputs"; /* All outputs must go to this directory */ 

/* data outputs.adsl;
    infile "/workflow/inputs/data_path";
    input file_contents $char250.;
    call symputx('file_contents', file_contents,'G');
    set "&file_contents./tv.sas7bdat";
run; */

/* Above code for reading input not working right now, hardcoding the dataset root for now */

libname dataset "/mnt/data/sdtm-blind";

data outputs.adam;
    set dataset.tv;
run;

/* (Required) This line signals to Domino Flows that outputs were successfully created */
libname success "/workflow/outputs/_SUCCESS";
