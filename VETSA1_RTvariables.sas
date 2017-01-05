/** SAS Syntax for the creation of Reaction Time variables **/
libname vetsa 'C:\Documents and Settings\vetsatwinstudy\Desktop\VETSA 1237';
  data temp1 ;
  set work.vetsa1_reactiontime; 
options nofmterr;

/** Correcting ID Errors **/

/* This element of the syntax can be deleted once the raw data files have been corrected */

if vetsaid='20779A' then vetsaid='20799A';
if vetsaid='10975B' then vetsaid='19075B';
if vetsaid='11003A' then delete;
if vetsaid='19755A' then vetsaid='19775A';
if vetsaid='19755B' then vetsaid='19775B';
if vetsaid='19897B' then vetsaid='19797B'; 
if vetsaid='20477B' then vetsaid='20744B';
if vetsaid='21043A' then vetsaid='21034A';
if vetsaid='21043B' then vetsaid='21034B';

/** Creating a Dummy Variable to indicate who has RT data **/
if rtbrk12 ge 0 then VETSART=1 ;

/** Imposing Limitations on Individual Reaction Times **/

/* A minimum threshold of 150ms is imposed for all trials */
/* The maximum thresholds are the 3SD cut-points for each individual trial (calculated after the minimum threshold is imposed) */

if RT101RT lt 150 or RT101RT gt 819.634 then RT101RT=. ;
if RT102RT lt 150 or RT102RT gt 504.175 then RT102RT=. ; 
if RT103RT lt 150 or RT103RT gt 756.059 then RT103RT=. ; 
if RT104RT lt 150 or RT104RT gt 470.130 then RT104RT=. ; 
if RT105RT lt 150 or RT105RT gt 463.594 then RT105RT=. ;  
if RT106RT lt 150 or RT106RT gt 639.417 then RT106RT=. ; 
if RT107RT lt 150 or RT107RT gt 502.413 then RT107RT=. ;  
if RT108RT lt 150 or RT108RT gt 701.148 then RT108RT=. ; 
if RT109RT lt 150 or RT109RT gt 551.774 then RT109RT=. ;  
if RT110RT lt 150 or RT110RT gt 489.975 then RT110RT=. ; 

if RT201RT lt 150 or RT201RT gt 553.341 then RT201RT=. ;  
if RT202RT lt 150 or RT202RT gt 544.785 then RT202RT=. ; 
if RT203RT lt 150 or RT203RT gt 541.091 then RT203RT=. ;  
if RT204RT lt 150 or RT204RT gt 441.339 then RT204RT=. ; 
if RT205RT lt 150 or RT205RT gt 553.545 then RT205RT=. ; 
if RT206RT lt 150 or RT206RT gt 770.302 then RT206RT=. ; 
if RT207RT lt 150 or RT207RT gt 466.464 then RT207RT=. ;  
if RT208RT lt 150 or RT208RT gt 575.177 then RT208RT=. ; 
if RT209RT lt 150 or RT209RT gt 441.458 then RT209RT=. ;  
if RT210RT lt 150 or RT210RT gt 502.338 then RT210RT=. ; 

if RT301RT lt 150 or RT301RT gt 558.588 then RT301RT=. ;  
if RT302RT lt 150 or RT302RT gt 647.398 then RT302RT=. ; 
if RT303RT lt 150 or RT303RT gt 716.774 then RT303RT=. ; 
if RT304RT lt 150 or RT304RT gt 694.918 then RT304RT=. ; 
if RT305RT lt 150 or RT305RT gt 644.418 then RT305RT=. ;  
if RT306RT lt 150 or RT306RT gt 609.275 then RT306RT=. ; 
if RT307RT lt 150 or RT307RT gt 879.904 then RT307RT=. ; 
if RT308RT lt 150 or RT308RT gt 855.414 then RT308RT=. ; 
if RT309RT lt 150 or RT309RT gt 825.096 then RT309RT=. ;  
if RT310RT lt 150 or RT310RT gt 721.924 then RT310RT=. ; 
if RT311RT lt 150 or RT311RT gt 810.673 then RT311RT=. ;  
if RT312RT lt 150 or RT312RT gt 770.500 then RT312RT=. ; 
if RT313RT lt 150 or RT313RT gt 1167.517 then RT313RT=. ;  
if RT314RT lt 150 or RT314RT gt 767.613 then RT314RT=. ; 
if RT315RT lt 150 or RT315RT gt 767.745 then RT315RT=. ;   
if RT316RT lt 150 or RT316RT gt 604.306 then RT316RT=. ;
if RT317RT lt 150 or RT317RT gt 629.969 then RT317RT=. ;  
if RT318RT lt 150 or RT318RT gt 630.855 then RT318RT=. ; 
if RT319RT lt 150 or RT319RT gt 790.190 then RT319RT=. ; 
if RT320RT lt 150 or RT320RT gt 1006.925 then RT320RT=. ; 
if RT321RT lt 150 or RT321RT gt 825.491 then RT321RT=. ; 

/** Recoding Response Data based on Reaction Time **/

/* If a trial has no RT it should not have a BU, otherwise our mean and std values will be wrong */

if RT101RT=. then RT101BU=. ;
if RT102RT=. then RT102BU=. ; 
if RT103RT=. then RT103BU=. ; 
if RT104RT=. then RT104BU=. ; 
if RT105RT=. then RT105BU=. ;  
if RT106RT=. then RT106BU=. ; 
if RT107RT=. then RT107BU=. ;  
if RT108RT=. then RT108BU=. ; 
if RT109RT=. then RT109BU=. ;  
if RT110RT=. then RT110BU=. ; 

if RT201RT=. then RT201BU=. ;  
if RT202RT=. then RT202BU=. ; 
if RT203RT=. then RT203BU=. ;  
if RT204RT=. then RT204BU=. ; 
if RT205RT=. then RT205BU=. ; 
if RT206RT=. then RT206BU=. ; 
if RT207RT=. then RT207BU=. ;  
if RT208RT=. then RT208BU=. ; 
if RT209RT=. then RT209BU=. ;  
if RT210RT=. then RT210BU=. ; 

if RT301RT=. then RT301BU=. ;  
if RT302RT=. then RT302BU=. ; 
if RT303RT=. then RT303BU=. ; 
if RT304RT=. then RT304BU=. ; 
if RT305RT=. then RT305BU=. ;  
if RT306RT=. then RT306BU=. ; 
if RT307RT=. then RT307BU=. ; 
if RT308RT=. then RT308BU=. ; 
if RT309RT=. then RT309BU=. ;  
if RT310RT=. then RT310BU=. ; 
if RT311RT=. then RT311BU=. ;  
if RT312RT=. then RT312BU=. ; 
if RT313RT=. then RT313BU=. ;  
if RT314RT=. then RT314BU=. ; 
if RT315RT=. then RT315BU=. ;   
if RT316RT=. then RT316BU=. ;
if RT317RT=. then RT317BU=. ;  
if RT318RT=. then RT318BU=. ; 
if RT319RT=. then RT319BU=. ; 
if RT320RT=. then RT320BU=. ; 
if RT321RT=. then RT321BU=. ; 

/** From this point on the syntax is the same as what Hong and Hui developed **/
array lbutton[10] RT101BU RT102BU RT103BU RT104BU RT105BU 
	RT106BU RT107BU RT108BU RT109BU RT110BU; 
array lrt[10] RT101RT RT102RT RT103RT RT104RT RT105RT 
	RT106RT RT107RT RT108RT RT109RT RT110RT; 
array ltt[10] $ RT101TT RT102TT RT103TT RT104TT RT105TT 
	RT106TT RT107TT RT108TT RT109TT RT110TT; 

	srtlcount=0; sumsrtl=0; srtrcount=0; sumsrtr=0; varsrtl=0; varsrtr=0;
do i=1 to 10; 
	if ltt[i]= 'left' and lbutton[i] = 1 then do;
		srtlcount=srtlcount+1; sumsrtl= sumsrtl+lrt[i];
	end;
end;

	if srtlcount > 0 then srtlmean = sumsrtl/srtlcount; 
do i=1 to 10; 
	if ltt[i]= 'left' and lbutton[i] = 1 then do;
		varsrtl= (lrt[i]-srtlmean)*(lrt[i]-srtlmean)+ varsrtl; 
	end;
end;
	if srtlcount=1 then srtlstd=0;
	else if srtlcount > 1 then srtlstd = sqrt(varsrtl/(srtlcount-1));

******* Right side only *******;
array rbutton[10] RT201BU RT202BU RT203BU RT204BU RT205BU 
	RT206BU RT207BU RT208BU RT209BU RT210BU; 
array rrt[10] RT201RT RT202RT RT203RT RT204RT RT205RT 
	RT206RT RT207RT RT208RT RT209RT RT210RT; 
array rtt[10] $ RT201TT RT202TT RT203TT RT204TT RT205TT 
	RT206TT RT207TT RT208TT RT209TT RT210TT; 
do i=1 to 10; 
	if rtt[i]= 'right' and rbutton[i] = 2 then do; 
		srtrcount=srtrcount+1; sumsrtr= sumsrtr+rrt[i];
	end;
end;
	if srtlcount > 0 then srtrmean = sumsrtr/srtrcount; 
do i=1 to 10; 
	if rtt[i]= 'right' and rbutton[i] = 2 then do;
		varsrtr= (rrt[i]-srtrmean)*(rrt[i]-srtrmean)+ varsrtr; 
	end;
end;
	if srtrcount = 1 then srtrstd =0;
	else if srtrcount > 1 then srtrstd = sqrt(varsrtr/(srtrcount-1));

** Grand mean for left side only and right side only **;

	srtcount=srtlcount+srtrcount; 	*Total count;

	if srtcount > 0 then srtgmean=(sumsrtl+sumsrtr)/(srtcount);	 * Grand mean;

	if srtcount = 1 then srtstd = 0;
	else if srtcount > 1 then srtgstd = sqrt((varsrtl+varsrtr)/(srtcount-1));  * Grand STD;

******** Left and right *******;
array buttons(21) RT301BU RT302BU RT303BU RT304BU RT305BU RT306BU RT307BU RT308BU RT309BU RT310BU
	RT311BU RT312BU RT313BU RT314BU RT315BU RT316BU	RT317BU RT318BU RT319BU RT320BU RT321BU;
array rts(21) RT301RT RT302RT RT303RT RT304RT RT305RT RT306RT RT307RT RT308RT RT309RT RT310RT
	RT311RT RT312RT RT313RT RT314RT RT315RT RT316RT	RT317RT RT318RT RT319RT RT320RT RT321RT;
array tts(21) $ RT301TT RT302TT RT303TT RT304TT RT305TT RT306TT RT307TT RT308TT RT309TT RT310TT
	RT311TT RT312TT RT313TT RT314TT RT315TT RT316TT	RT317TT RT318TT RT319TT RT320TT RT321TT;

* choice RT Left and right side means;
	chrtlcount=0; sumchrtl=0; varchrtl=0; 
	chrtrcount=0; sumchrtr=0; varchrtr=0; varchrt=0;
	
do i=1 to 21; 
	if tts[i] = 'left' and buttons[i] = 1 then do;
	chrtlcount = chrtlcount	+ 1;	sumchrtl=sumchrtl + rts[i];
	end;
	else if tts[i]= 'right' and buttons[i] = 2 then do;
		chrtrcount=chrtrcount+1; sumchrtr= sumchrtr+rts[i];
	end;
end;
	if chrtlcount > 0 then chrtlmean=sumchrtl/chrtlcount; 
	if chrtrcount > 0 then chrtrmean=sumchrtr/chrtrcount;

do i=1 to 21; 
	if tts[i]= 'left' and buttons[i] = 1 and chrtlcount > 0 then 
		varchrtl= (rts[i]-chrtlmean)*(rts[i]-chrtlmean)+ varchrtl;
	else if tts[i]= 'right' and buttons[i] = 2 and chrtrcount > 0 then
		varchrtr= (rts[i]-chrtrmean)*(rts[i]-chrtrmean)+ varchrtr;
end;
	if chrtlcount = 1 then chrtlstd=0;
	else if chrtlcount > 1 then chrtlstd = sqrt(varchrtl/(chrtlcount-1));
	if chrtrcount =1 then chrtrstd = 0;
	else if chrtrcount > 1 then chrtrstd = sqrt(varchrtr/(chrtrcount-1));

* Choice RT grand means;
	chrtcount = chrtlcount + chrtrcount;

if chrtcount > 0 then chrtgmean = (sumchrtl+sumchrtr)/(chrtcount);

if chrtcount = 1 then chrtstd = 0;
else if chrtcount > 1 then chrtgstd = sqrt((varchrtl+ varchrtr)/(chrtcount-1));

* Choice RT left incorrect and misses;
		chrtlincr =0; chrtrincr=0; chrtincr=0; chrtlmiss=0; chrtrmiss=0; chrtmiss=0;
do i=1 to 21;
	if tts[i]='left' and buttons[i] = 2 then chrtlincr = chrtlincr + 1;
	if tts[i]='right' and buttons[i] = 1 then chrtrincr = chrtrincr + 1;
	if tts[i]='left' and buttons[i] < 1 then chrtlmiss = chrtlmiss + 1;
	if tts[i]='right' and buttons[i] < 1 then chrtrmiss = chrtrmiss + 1;
end;

chrtincr = chrtlincr + chrtrincr;
chrtmiss = chrtlmiss + chrtrmiss;

keep vetsaid VETSART RTBRK11 RTBRK12 RTBRK13 RTBRK14  
RT101BU RT101RT RT101TT RT101DT 
RT102BU RT102RT RT102TT RT102DT
RT103BU RT103RT RT103TT RT103DT 
RT104BU RT104RT RT104TT RT104DT
RT105BU RT105RT RT105TT RT105DT 
RT106BU RT106RT RT106TT RT106DT
RT107BU RT107RT RT107TT RT107DT 
RT108BU RT108RT RT108TT RT108DT
RT109BU RT109RT RT109TT RT109DT 
RT110BU RT110RT RT110TT RT110DT

RTBRK21 RTBRK22 RTBRK23 RTBRK24
RT201BU RT201RT RT201TT RT201DT 
RT202BU RT202RT RT202TT RT202DT
RT203BU RT203RT RT203TT RT203DT 
RT204BU RT204RT RT204TT RT204DT
RT205BU RT205RT RT205TT RT205DT 
RT206BU RT206RT RT206TT RT206DT
RT207BU RT207RT RT207TT RT207DT 
RT208BU RT208RT RT208TT RT208DT
RT209BU RT209RT RT209TT RT209DT 
RT210BU RT210RT RT210TT RT210DT

RTBRK31 RTBRK32 RTBRK33 RTBRK34
RT301BU RT301RT RT301TT RT301DT 
RT302BU RT302RT RT302TT RT302DT
RT303BU RT303RT RT303TT RT303DT 
RT304BU RT304RT RT304TT RT304DT
RT305BU RT305RT RT305TT RT305DT 
RT306BU RT306RT RT306TT RT306DT
RT307BU RT307RT RT307TT RT307DT 
RT308BU RT308RT RT308TT RT308DT
RT309BU RT309RT RT309TT RT309DT 
RT310BU RT310RT RT310TT RT310DT
RT311BU RT311RT RT311TT RT311DT 
RT312BU RT312RT RT312TT RT312DT
RT313BU RT313RT RT313TT RT313DT 
RT314BU RT314RT RT314TT RT314DT
RT315BU RT315RT RT315TT RT315DT 
RT316BU RT316RT RT316TT RT316DT
RT317BU RT317RT RT317TT RT317DT 
RT318BU RT318RT RT318TT RT318DT
RT319BU RT319RT RT319TT RT319DT
RT320BU RT320RT RT320TT RT320DT
RT321BU RT321RT RT321TT RT321DT

srtlmean srtlstd
srtrmean srtrstd 
srtgmean srtgstd 
srtlcount srtrcount srtcount
CHRTLmean CHRTLstd 
CHRTRmean CHRTRstd 
CHRTgmean CHRTgstd 
CHRTLcount CHRTRcount CHRTcount 
CHRTLincr CHRTRincr CHRTincr 
CHRTLmiss CHRTRmiss CHRTmiss; 

label SRTLmean = 'Simple Reaction Time Left Mean'
SRTLstd = 'Simple Reaction Time Left Standard Deviation'
 
SRTRmean = 'Simple Reaction Time Right Mean'
SRTRstd = 'Simple Reaction Time Right Standard Deviation'
 
SRTgmean = 'Simple Reaction Time Grand Mean'
SRTgstd = 'Simple Reaction Time Grand Standard Deviation'
 
SRTLcount = 'Simple Reaction Time Left Total Responses'
SRTRcount = 'Simple Reaction Time Right Total Responses'
SRTcount = 'Simple Reaction Time Total Responses'
 
CHRTLmean = 'Choice Reaction Time Left Mean'
CHRTLstd = 'Choice Reaction Time Left Standard Deviation'
CHRTRmean = 'Choice Reaction Time Right Mean'
CHRTRstd = 'Choice Reaction Time Right Standard Deviation'
CHRTgmean = 'Choice Reaction Time Grand Mean'
CHRTgstd = 'Choice Reaction Time Grand Standard Deviation'
CHRTLcount = 'Choice Reaction Time Left Total Correct Responses'
CHRTRcount = 'Choice Reaction Time Right Total Correct Responses'
CHRTcount = 'Choice Reaction Time Total Correct Responses'
CHRTLincr = 'Choice Reaction Time Left Total Incorrect Responses'
CHRTRincr = 'Choice Reaction Time Right Total Incorrect Responses'
CHRTincr = 'Choice Reaction Time Total Incorrect Responses'
CHRTLmiss = 'Choice Reaction Time Left Total Misses'
CHRTRmiss = 'Choice Reaction Time Right Total Misses'
CHRTmiss = 'Choice Reaction Time Total Misses';
run;

/*data rt.rtstats; set rtstats; run; 

proc print data=temp1 (obs=5);   run;*/

proc means data=temp1 n mean std min max;
	var rt101rt rt102rt rt103rt rt104rt rt105rt rt106rt rt107rt rt108rt rt109rt rt110rt	
	rt201rt rt202rt rt203rt rt204rt rt205rt rt206rt rt207rt rt208rt rt209rt rt210rt	
	rt301rt rt302rt rt303rt rt304rt rt305rt rt306rt rt307rt rt308rt rt309rt rt310rt	
	rt311rt rt312rt rt313rt rt314rt rt315rt rt316rt rt317rt rt318rt rt319rt rt320rt	rt321rt;
run;

/** Preliminary looks at the means and std **/
proc means data=temp1 n mean std min max ;
	var srtlmean srtlstd srtrmean srtrstd srtgmean srtgstd ;
proc means data=temp1 n mean std min max ;
	var CHRTLmean CHRTLstd CHRTRmean CHRTRstd CHRTgmean CHRTgstd ;
run;

proc freq data=temp1;
	table srtlcount srtrcount srtcount CHRTLcount CHRTRcount CHRTcount ;
run;
proc freq data=temp1;
	table srtlcount*srtrcount;
run;

proc freq data=temp1;
	table CHRTLincr CHRTRincr CHRTincr CHRTLmiss CHRTRmiss CHRTmiss;
run; 

proc univariate data=temp1 normal plot;
	var srtlmean srtlstd srtrmean srtrstd srtgmean srtgstd CHRTLmean CHRTLstd CHRTRmean CHRTRstd CHRTgmean CHRTgstd ;
run;

proc sort data=temp1; by vetsaid;
run;

/******************************************************************************/
/** Below is the syntax that I used for calculating the transformed measures **/
/******************************************************************************/
libname vetsa 'C:\Documents and Settings\vetsatwinstudy\Desktop\VETSA 1237';
  data temp2 ;
  set work.temp1 (keep = vetsaid VETSART srtlmean srtlstd srtrmean srtrstd srtgmean srtgstd CHRTLmean CHRTLstd CHRTRmean CHRTRstd CHRTgmean CHRTgstd
srtlcount srtrcount srtcount CHRTLcount CHRTRcount CHRTcount CHRTLincr CHRTRincr CHRTincr CHRTLmiss CHRTRmiss CHRTmiss) ; 
options nofmterr;

/*Simple Reaction Time Cleaning */
if srtlcount lt 8 then srtlmean=. ;
if srtlcount lt 8 then srtlstd=. ;

if srtrcount lt 8 then srtrmean=. ;
if srtrcount lt 8 then srtrstd=. ;

if srtcount lt 16 then srtgmean=. ;
if srtcount lt 16 then srtgstd=. ;

/*Simple Reaction Data Transformation */
transrtlmean=log(srtlmean) ;
label transrtlmean = 'Log-Transformed SRTLMEAN';
transrtrmean=log(srtrmean) ;
label transrtrmean = 'Log-Transformed SRTRMEAN';
transrtgmean=log(srtgmean) ;
label transrtgmean = 'Log-Transformed SRTGMEAN';

transrtlstd=sqrt(srtlstd) ;
Label transrtlstd = 'SquareRoot-Transformed SRTLSTD';
transrtrstd=sqrt(srtrstd) ;
Label transrtrstd = 'SquareRoot-Transformed SRTRSTD';
transrtgstd=sqrt(srtgstd) ;
Label transrtgstd = 'SquareRoot-Transformed SRTGSTD';

/*Choice Reaction Time Cleaning */
if CHRTlcount lt 8 then CHRTlmean=. ;
if CHRTlcount lt 8 then CHRTlstd=. ;

if CHRTrcount lt 8 then CHRTrmean=. ;
if CHRTrcount lt 8 then CHRTrstd=. ;

if CHRTcount lt 16 then CHRTgmean=. ;
if CHRTcount lt 16 then CHRTgstd=. ;

/*Choice Reaction Data Transformation */
tranCHRTlmean=log(CHRTlmean) ;
label tranCHRTlmean = 'Log-Transformed CHRTLMEAN';
tranCHRTrmean=log(CHRTrmean) ;
label tranCHRTrmean = 'Log-Transformed CHRTRMEAN';
tranCHRTgmean=log(CHRTgmean) ;
label tranCHRTgmean = 'Log-Transformed CHRTGMEAN';

tranCHRTlstd=sqrt(CHRTlstd) ;
Label tranCHRTlstd = 'SquareRoot-Transformed CHRTLSTD';
tranCHRTrstd=sqrt(CHRTrstd) ;
Label tranCHRTrstd = 'SquareRoot-Transformed CHRTRSTD';
tranCHRTgstd=sqrt(CHRTgstd) ;
Label tranCHRTgstd = 'SquareRoot-Transformed CHRTGSTD';

proc means data=temp2 n mean std min max ;
	var srtlmean srtlstd srtrmean srtrstd srtgmean srtgstd CHRTLmean CHRTLstd CHRTRmean CHRTRstd CHRTgmean CHRTgstd ;
	title 'Clean Data - Descriptive Statistics';
run;
proc means data=temp2 n mean std min max ;
	var transrtlmean transrtlstd transrtrmean transrtrstd transrtgmean transrtgstd tranCHRTLmean tranCHRTLstd tranCHRTRmean tranCHRTRstd tranCHRTgmean tranCHRTgstd ;
	title 'Clean/Transformed Data - Descriptive Statistics';
run;

proc freq data=temp2;
	table vetsaid;
run;

/*****************************/
libname vetsa 'C:\Documents and Settings\vetsatwinstudy\Desktop\VETSA 1237';
  data tempcore ;
  set work.vetsacore; 
options nofmterr;

proc freq data=tempcore;
	table site;
run;

/******************************************************************************/
libname vetsa 'C:\Documents and Settings\mspanizzon\Desktop\VETSA 1237';
  data tempmerge;
  merge work.tempcore work.temp2 ;
  by vetsaid;

if vetsart=. then vetsart=0;
if site=5 then site=1;

proc mixed data=tempmerge;
	class case site ;
   	model srtgmean = age site / solution ;
   	lsmeans site / diff;
	random case ;
	title '';
run;quit;
proc mixed data=tempmerge;
	class case site ;
   	model srtgstd = age site / solution ;
   	lsmeans site / diff;
	random case ;
	title '';
run;quit;
proc mixed data=tempmerge;
	class case site ;
   	model CHRTgmean = age site / solution ;
   	lsmeans site / diff;
	random case ;
	title '';
run;quit;
proc mixed data=tempmerge;
	class case site ;
   	model CHRTgstd = age site / solution ;
   	lsmeans site / diff;
	random case ;
	title '';
run;quit;

proc corr data=tempmerge;
	var trl2t trl3t strwraw strcraw srtgmean chrtgmean;
run;
