import SourceGen
import os
import glob
import datetime

Curruntpath = os.getcwd()

filepath = os.path.join(Curruntpath, 'excel')
Sourcepath = os.path.join(Curruntpath, 'Source')
Arxmlpath = os.path.join(Curruntpath, 'Arxml')

declareFile = "App_Variable.h"
defineFile = "App_Variable.c"

declarState_Start = """/** ================================**/
/** Company : Kyungshin              **/
/** Project Name : CDCU             **/
/** Create Date :  {0}-{1}-{2}      **/
/** Author      : KangSH            **/
/** ================================**/
#ifndef APP_VARIABLE_H_
#define APP_VARIABLE_H_

#include "Rte_Type.h"
////SW Version /////
extern const uint8 ubC_SoftwareVer1;
extern const uint8 ubC_SoftwareVer2;
extern const uint8 ubC_SoftwareVer3;
extern const uint8 ubC_SoftwareVer4;
/*** Draft #0  ****/
extern const uint8 ubC_DraftReleaseCnt1;

\n""".format(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)

declarState_End = "#endif /* APP_VARIABLE_H_ */"

defineState ="""/** ================================**/
/** Company : Kyungshin              **/
/** Project Name : CDCU             **/
/** Create Date :  {0}-{1}-{2}      **/
/** Author      : KangSH            **/
/** ================================**/
#include "App_Variable.h"

/* SW Version A.00.0 */
const uint8 ubC_SoftwareVer1 = (uint8)'A';
const uint8 ubC_SoftwareVer2 = (uint8)'0';
const uint8 ubC_SoftwareVer3 = (uint8)'0';
const uint8 ubC_SoftwareVer4 = (uint8)'0';
/* Draft #0*/
const uint8 ubC_DraftReleaseCnt1 = (uint8)0x00;\n\n""".format(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)

def main():
    if(os.path.isdir(filepath)):
        excelfile_list = glob.glob(filepath + "\\" + "*.xlsx")
        fileNum = len(excelfile_list)
        #print("file number :" , fileNum)
        if fileNum == 0:
            print("make sure that file exist in excel folder")
        elif fileNum > 1:
            print("it need Only 1 excel file, plz check folder")
        else:
            fileName = os.path.basename(excelfile_list[0])
            print("find execlfile :", fileName)
            source = SourceGen.CANCodeGenerate(excelfile_list[0])
            if not os.path.isdir(Sourcepath): #creat folder if not folder
                os.makedirs(Sourcepath)

            ## header file creat
            headerfilepath = os.path.join(Sourcepath, declareFile)
            if not os.path.isdir(headerfilepath):
                with open(headerfilepath, 'w') as f:
                    f.write(declarState_Start)

            Cfilepath = os.path.join(Sourcepath, defineFile)
            ## Source file creat
            if not os.path.isdir(Cfilepath):
                with open(Cfilepath, 'w') as f:
                    f.write(defineState)

            #source.Ind_variable(Cfilepath, headerfilepath)
            #source.TimeOutInd_variable(Cfilepath, headerfilepath)
            #source.Invalid_variable(Cfilepath, headerfilepath)
            #source.Signal_variable(Cfilepath, headerfilepath)

            with open(headerfilepath, 'a') as f:
                f.write(declarState_End)

            #CCANfilepath = os.path.join(Sourcepath, "CCAN.c")
            #source.CCANFD_File(CCANfilepath)

            #### Create ARXML #####
            if not os.path.isdir(Arxmlpath): #creat folder if not folder
                os.makedirs(Arxmlpath)

    else:
        print("put into file after excel folder is created")
        os.makedirs(filepath)

if __name__ == '__main__':
    main()



