/******************************************************************************
* This scripts mocks the following use case:
*  1. Loading in the original SDTM tv.sas7bdat data 
*  2. Using that data to create the ADSL dataset
* 
*  For simplcity, we will simply carry forward the input to the output directory
*****************************************************************************/
%include "/mnt/code/domino.sas";

options dlcreatedir;
libname inputs "/workflow/inputs"; /* All inputs live in this directory */ 
libname outputs "/workflow/outputs"; /* All outputs must go to this directory */ 

data _null_;
    infile "/workflow/inputs/data_path";
    input file_contents $char250.;
    %put The value of file_contents is: &file_contents;
	call symputx('path', file_contents,'G');
    %put The value of path before is: &path;
run;

%put The value of path after is: &path;

libname data "&path";

data outputs.adsl;
    set data.tv;
run;

/* (Required) This line signals to Domino Flows that outputs were successfully created */
libname success "/workflow/outputs/_SUCCESS";
