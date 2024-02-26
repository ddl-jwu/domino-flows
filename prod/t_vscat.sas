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

proc print data=inputs.advs;
run;

ods pdf close;

libname success "/workflow/outputs/_SUCCESS";

/* %include "/mnt/code/domino.sas"; */
/*  */
/* options dlcreatedir; */
/* libname inputs "/workflow/inputs"; */
/* libname outputs "/workflow/outputs"; */
/*  */
/* proc print data=inputs.advs(obs=5); */
/* run; */
/*  */
/* libname success "/workflow/outputs/_SUCCESS"; */
