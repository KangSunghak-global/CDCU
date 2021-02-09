import SourceGen
import os
import glob
import datetime
import time
import Arxml_gen

Curruntpath = os.getcwd()

filepath = os.path.join(Curruntpath, 'excel')
Sourcepath = os.path.join(Curruntpath, 'Source')
Arxmlpath = os.path.join(Curruntpath, 'Arxml')

declareFile = "interface.h"
defineFile = "interface.c"

InforVar_H = """\n/****** ECU Information variable****/
extern uint8 cdcu_Core1_Defect;
extern uint8 cdcu_Core2_Defect;
extern uint16 cdcu_Bat_Volt;
extern uint8 cdcu_Bat_Volt_IVD;
extern uint8 cdcu_CCAN_BusOff;
extern uint8 cdcu_PCAN_BusOff;
extern uint8 cdcu_GCAN_BusOff;
extern uint8 cdcu_CycleTimeErrFlg_Core1;
extern uint8 cdcu_CycleTimeErrFlg_Core2;
extern uint8 cdcu_FnCallErrFlg_Core1;
extern uint8 cdcu_FnCallErrFlg_Core2;
extern uint8 cduc_Region_Val;
extern uint8 cduc_PT_info;
extern uint8 cduc_PE_info;
extern uint8 cdcu_SCC_Enable;
extern uint8 cdcu_AEB_Enable;
extern uint8 cdcu_LKA_Enable;
extern uint8 cdcu_ECS_Exist;
extern uint8 cdcu_AWD_Exist;
extern uint8 cdcu_eLSD_Exist;
extern uint8 cdcu_SW_ID;
extern uint8 cdcu_m_val_TxOn;
extern uint8 cdcu_EEPROM_IVD;"""

InforVar_C = """\n/****** ECU Information variable****/
uint8 cdcu_Core1_Defect;
uint8 cdcu_Core2_Defect;
uint16 cdcu_Bat_Volt;
uint8 cdcu_Bat_Volt_IVD;
uint8 cdcu_CCAN_BusOff;
uint8 cdcu_PCAN_BusOff;
uint8 cdcu_GCAN_BusOff;
uint8 cdcu_CycleTimeErrFlg_Core1;
uint8 cdcu_CycleTimeErrFlg_Core2;
uint8 cdcu_FnCallErrFlg_Core1;
uint8 cdcu_FnCallErrFlg_Core2;
uint8 cduc_Region_Val;
uint8 cduc_PT_info;
uint8 cduc_PE_info;
uint8 cdcu_SCC_Enable;
uint8 cdcu_AEB_Enable;
uint8 cdcu_LKA_Enable;
uint8 cdcu_ECS_Exist;
uint8 cdcu_AWD_Exist;
uint8 cdcu_eLSD_Exist;
uint8 cdcu_SW_ID;
uint8 cdcu_m_val_TxOn;
uint8 cdcu_EEPROM_IVD;"""

EEPROM_H = """\n/****** EEPROM variable****/
extern uint8 Ivss_Offset_StrAng[2];
extern uint8 Ivss_Offset_Yawrate[2];
extern uint8 Ivss_Offset_Ay[2];
extern uint8 CpOffset1[2];
extern uint8 CpOffset2[2];
extern uint8 CountCPE1;
extern uint8 CountCPE2;
extern uint8 NewIEB_detect;
extern uint8 CountLongCPE1[2];
extern uint8 CountLongCPE2[2];
extern uint8 DMIC_eeprom0[2];
extern uint8 DMIC_eeprom1[2];
extern uint8 DMIC_eeprom2[2];
extern uint8 DMIC_eeprom3[2];
extern uint8 DMIC_eeprom4[2];
extern uint8 DMIC_eeprom5[2];
extern uint8 DMIC_eeprom6[2];
extern uint8 DMIC_eeprom7[2];
extern uint8 Ivss_Offset_Ax[2];
extern uint8 cdcu_eDTVC_errflg[2];
extern uint8 cdcu_DTCH_errflg[2];
extern uint8 cdcu_BFE_errflg[2];
extern uint8 cdcu_CWSC_errflg[2];
extern uint8 cdcu_DMIC_errflg[2];
extern uint8 cdcu_ATM_errflg[2];
extern uint8 cdcu_RGR_errflg[2];
extern uint8 cdcu_BJD_errflg[2];
extern uint8 cdcu_DLR_errflg[2];
extern uint8 cdcu_LWR_errflg[2];
extern uint8 cdcu_DRR_errflg[2];
extern uint8 cdcu_SRR_errflg[2];
extern uint8 cdcu_RSR_errflg[2];

enum{
 	enum_Ivss_Offset_StrAng = 0U,
	enum_Ivss_Offset_Yawrate,
	enum_Ivss_Offset_Ay,
	enum_CpOffset1,
	enum_CpOffset2,
	enum_CountCPE1,
	enum_CountCPE2,
	enum_NewIEB_detect,
	enum_CountLongCPE1,
	enum_CountLongCPE2,
	enum_DMIC_eeprom0,
	enum_DMIC_eeprom1,
	enum_DMIC_eeprom2,
	enum_DMIC_eeprom3,
	enum_DMIC_eeprom4,
	enum_DMIC_eeprom5,
	enum_DMIC_eeprom6,
	enum_DMIC_eeprom7,
	enum_Ivss_Offset_Ax,
	enum_cdcu_eDTVC_errflg,
	enum_cdcu_DTCH_errflg,
	enum_cdcu_BFE_errflg,
	enum_cdcu_CWSC_errflg,
	enum_cdcu_DMIC_errflg,
	enum_cdcu_ATM_errflg,
	enum_cdcu_RGR_errflg,
	enum_cdcu_BJD_errflg,
	enum_cdcu_DLR_errflg,
	enum_cdcu_LWR_errflg,
	enum_cdcu_DRR_errflg,
	enum_cdcu_SRR_errflg,
	enum_cdcu_RSR_errflg,
	EEPROM_NUM
};"""

EEPROM_C = """\n/****** EEPROM variable****/
uint8 Ivss_Offset_StrAng[2];
uint8 Ivss_Offset_Yawrate[2];
uint8 Ivss_Offset_Ay[2];
uint8 CpOffset1[2];
uint8 CpOffset2[2];
uint8 CountCPE1;
uint8 CountCPE2;
uint8 NewIEB_detect;
uint8 CountLongCPE1[2];
uint8 CountLongCPE2[2];
uint8 DMIC_eeprom0[2];
uint8 DMIC_eeprom1[2];
uint8 DMIC_eeprom2[2];
uint8 DMIC_eeprom3[2];
uint8 DMIC_eeprom4[2];
uint8 DMIC_eeprom5[2];
uint8 DMIC_eeprom6[2];
uint8 DMIC_eeprom7[2];
uint8 Ivss_Offset_Ax[2];
uint8 cdcu_eDTVC_errflg[2];
uint8 cdcu_DTCH_errflg[2];
uint8 cdcu_BFE_errflg[2];
uint8 cdcu_CWSC_errflg[2];
uint8 cdcu_DMIC_errflg[2];
uint8 cdcu_ATM_errflg[2];
uint8 cdcu_RGR_errflg[2];
uint8 cdcu_BJD_errflg[2];
uint8 cdcu_DLR_errflg[2];
uint8 cdcu_LWR_errflg[2];
uint8 cdcu_DRR_errflg[2];
uint8 cdcu_SRR_errflg[2];
uint8 cdcu_RSR_errflg[2];"""

declarState_Start = """/** ================================**/
/** Company : Kyungshin              **/
/** Project Name : CDCU             **/
/** Create Date :  {0}-{1}-{2}      **/
/** Author      : KangSH            **/
/** ================================**/
#ifndef INTERFACE_H_
#define INTERFACE_H_

#include "APP_Variable_KSC.h"
#include "Rte_Type.h"\n""".format(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)

declarState_End = "{Infor}\n{eeprom}\n#endif /* APP_VARIABLE_H_ */".format(Infor = InforVar_H, eeprom = EEPROM_H)

defineState ="""/** ================================**/
/** Company : Kyungshin              **/
/** Project Name : CDCU             **/
/** Create Date :  {0}-{1}-{2}      **/
/** Author      : KangSH            **/
/** ================================**/
#include "interface.h"\n\n""".format(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)

defineState_End = "{Infor}\n{eeprom}".format(Infor = InforVar_C, eeprom = EEPROM_C)
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

            ##### Interface.c/interface.h create ########
            ## header file create
            headerfilepath = os.path.join(Sourcepath, declareFile)
            if not os.path.isdir(headerfilepath):
                with open(headerfilepath, 'w') as f:
                    f.write(declarState_Start)

            Cfilepath = os.path.join(Sourcepath, defineFile)
            ## Source file create
            if not os.path.isdir(Cfilepath):
                with open(Cfilepath, 'w') as f:
                    f.write(defineState)

            ##### add to message Ind, timeout Ind ########
            source.Ind_variable(Cfilepath, headerfilepath)
            source.TimeOutInd_variable(Cfilepath, headerfilepath)
            source.Invalid_variable(Cfilepath, headerfilepath)
            source.Signal_variable(Cfilepath, headerfilepath)

            with open(headerfilepath, 'a') as f:
                f.write(declarState_End)

            with open(Cfilepath, 'a') as f:
                f.write(defineState_End)
            #######################################################

            ##### C-CAN File Create ######
            #CCANfilepath = os.path.join(Sourcepath, "CCANFD_Swc.c")
            #source.CCANFD_File(CCANfilepath)

            ##### P-CAN File Create ######
            PCANfilepath = os.path.join(Sourcepath, "PCANFD_Swc.c")
            source.PCANFD_File(PCANfilepath)

            ##### G-CAN File Create ######
            #GCANfilepath = os.path.join(Sourcepath, "GCANFD_Swc.c")
            #source.GCANFD_File(GCANfilepath)

            #### Create ARXML #####
            if not os.path.isdir(Arxmlpath): #creat folder if not folder
                os.makedirs(Arxmlpath)

            arxmlfile_list = glob.glob(Arxmlpath + "\\" + "*.arxml")
            arxmlNum = len(arxmlfile_list)

            print("find Arxmlfile :", arxmlfile_list)

            if arxmlNum == 0:
                print("put Arxml file into Arxml folder")
            else:
                outputpath = os.path.join(Arxmlpath, arxmlfile_list[0])
                arxmlpath = os.path.join(Arxmlpath, arxmlfile_list[0])

            #Arxml = Arxml_gen.ArxmlParser(arxmlpath, excelfile_list[0]) # arxml class instance
            #ccan_ind = Arxml.CCAN_extract_data() # runnable name extract
            #Arxml.xml_gen(ccan_ind)
            #Arxml.make_xml(outputpath)
            #print(list)

            Arxml = Arxml_gen.ArxmlParser(arxmlpath, excelfile_list[0]) # arxml class instance
            pcan_ind = Arxml.PCAN_extract_data() # runnable name extract
            Arxml.xml_gen(pcan_ind)
            Arxml.make_xml(outputpath)

    else:
        print("put into file after excel folder is created")
        os.makedirs(filepath)

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time() - start
    print ('Operating Time : {0}s' .format(end))


