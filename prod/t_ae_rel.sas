/******************************************************************************
*  This script mocks the scenario for generating a final t_ae_rel PDF report
*
* For simplicity, we will simply print the input data onto a PDF file 
*****************************************************************************/
%include "/mnt/code/domino.sas";
options dlcreatedir;
libname inputs "/workflow/inputs";
libname outputs "/workflow/outputs";

ods pdf file=outputs.report;

proc report data=inputs.adae; 
    title 'T_AE_REL Report' tsparmcs=100;
run; 

ods pdf close;

libname success "/workflow/outputs/_SUCCESS";