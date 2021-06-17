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

InforVar_H = """\n/****** ECU Information variable, Refer CDCU_BSW_Requirements_v2.5.xlsx ****/
extern uint8 cdcu_Core1_Defect;
extern uint8 cdcu_Core2_Defect;
extern uint16 cdcu_Bat_Volt;
extern uint8 cdcu_Bat_Volt_IVD;
extern uint8 cdcu_CCAN_BusOff;
extern uint8 cdcu_PCAN_BusOff;
extern uint8 cdcu_GCAN_BusOff;
extern uint8 cdcu_m_val_TxOn;
extern uint32 BSW_ID;

/*** Function Called monitoring ***/
extern uint8 cdcu_CallErr_core1_10ms_1;
extern uint8 cdcu_CallErr_core1_10ms_2;
extern uint8 cdcu_CallErr_core1_10ms_3;
extern uint8 cdcu_CallErr_core1_10ms_4;
extern uint8 cdcu_CallErr_core1_10ms_5;
extern uint8 cdcu_CallErr_core1_10ms_6;
extern uint8 cdcu_CallErr_core1_10ms_7;
extern uint8 cdcu_CallErr_core1_10ms_8;
extern uint8 cdcu_CallErr_core1_10ms_9;
extern uint8 cdcu_CallErr_core1_10ms_10;
extern uint8 cdcu_CallErr_core1_10ms_11;
extern uint8 cdcu_CallErr_core1_10ms_12;
extern uint8 cdcu_CallErr_core1_10ms_13;
extern uint8 cdcu_CallErr_core2_10ms_1;
extern uint8 cdcu_CallErr_core2_10ms_2;
extern uint8 cdcu_CallErr_core2_10ms_3;
extern uint8 cdcu_CallErr_core2_10ms_4;
extern uint8 cdcu_CallErr_core2_10ms_5;
extern uint8 cdcu_CallErr_core2_10ms_6;
extern uint8 cdcu_CallErr_core2_10ms_7;
extern uint8 cdcu_CallErr_core2_10ms_8;
extern uint8 cdcu_CallErr_core2_10ms_9;
extern uint8 cdcu_CallErr_core2_10ms_10;
extern uint8 cdcu_CallErr_core2_10ms_11;
extern uint8 cdcu_CallErr_core2_10ms_12;
extern uint8 cdcu_CallErr_core2_10ms_13;

/*** Function Operation Time monitoring ***/
extern uint8 cdcu_ExeTimeErr_core1_10ms_1;
extern uint8 cdcu_ExeTimeErr_core1_10ms_2;
extern uint8 cdcu_ExeTimeErr_core1_10ms_3;
extern uint8 cdcu_ExeTimeErr_core1_10ms_4;
extern uint8 cdcu_ExeTimeErr_core1_10ms_5;
extern uint8 cdcu_ExeTimeErr_core1_10ms_6;
extern uint8 cdcu_ExeTimeErr_core1_10ms_7;
extern uint8 cdcu_ExeTimeErr_core1_10ms_8;
extern uint8 cdcu_ExeTimeErr_core1_10ms_9;
extern uint8 cdcu_ExeTimeErr_core1_10ms_10;
extern uint8 cdcu_ExeTimeErr_core1_10ms_11;
extern uint8 cdcu_ExeTimeErr_core1_10ms_12;
extern uint8 cdcu_ExeTimeErr_core1_10ms_13;
extern uint8 cdcu_ExeTimeErr_core2_10ms_1;
extern uint8 cdcu_ExeTimeErr_core2_10ms_2;
extern uint8 cdcu_ExeTimeErr_core2_10ms_3;
extern uint8 cdcu_ExeTimeErr_core2_10ms_4;
extern uint8 cdcu_ExeTimeErr_core2_10ms_5;
extern uint8 cdcu_ExeTimeErr_core2_10ms_6;
extern uint8 cdcu_ExeTimeErr_core2_10ms_7;
extern uint8 cdcu_ExeTimeErr_core2_10ms_8;
extern uint8 cdcu_ExeTimeErr_core2_10ms_9;
extern uint8 cdcu_ExeTimeErr_core2_10ms_10;
extern uint8 cdcu_ExeTimeErr_core2_10ms_11;
extern uint8 cdcu_ExeTimeErr_core2_10ms_12;
extern uint8 cdcu_ExeTimeErr_core2_10ms_13;

/*** EOL Variable ***/
extern uint8 var_cdcu_EOL_Byte_0_Region;
extern uint8 var_cdcu_EOL_Byte_0_DrvType;
extern uint8 var_cdcu_EOL_Byte_1_PTType;
extern uint8 var_cdcu_EOL_Byte_1_EngVol;
extern uint8 var_cdcu_EOL_Byte_2_EngType;
extern uint8 var_cdcu_EOL_Byte_2_MTRType;
extern uint8 var_cdcu_EOL_Byte_3_TMType;
extern uint8 var_cdcu_EOL_Byte_3_ECSExist;
extern uint8 var_cdcu_EOL_Byte_3_ELSDExist;
extern uint8 var_cdcu_EOL_Byte_0_Region_IVD;
extern uint8 var_cdcu_EOL_Byte_0_DrvType_IVD;
extern uint8 var_cdcu_EOL_Byte_1_PTType_IVD;
extern uint8 var_cdcu_EOL_Byte_1_EngVol_IVD;
extern uint8 var_cdcu_EOL_Byte_2_EngType_IVD;
extern uint8 var_cdcu_EOL_Byte_2_MTRType_IVD;
extern uint8 var_cdcu_EOL_Byte_3_TMType_IVD;
extern uint8 var_cdcu_EOL_Byte_3_ECSExist_IVD;
extern uint8 var_cdcu_EOL_Byte_3_ELSDExist_IVD;

//Extern Definition for ASW ID
extern uint8 SWID_eDTVC[29];
extern uint8 SWID_DTCH[29];
extern uint8 SWID_DMIC[29];
extern uint8 SWID_ATM[29]
extern uint8 SWID_RSE[29];
extern uint8 SWID_BJD[29];
extern uint8 SWID_BFE[29];
extern uint8 SWID_CCS[29];
extern uint8 SWID_TPA[29];
extern uint8 SWID_TTCS[29];
extern uint8 SWID_eVMC[29];"""

InforVar_C = """\n/****** ECU Information variable, Refer CDCU_BSW_Requirements_v2.5.xlsx ****/
uint8 cdcu_Core1_Defect;
uint8 cdcu_Core2_Defect;
uint16 cdcu_Bat_Volt;
uint8 cdcu_Bat_Volt_IVD;
uint8 cdcu_CCAN_BusOff;
uint8 cdcu_PCAN_BusOff;
uint8 cdcu_GCAN_BusOff;
uint8 cdcu_m_val_TxOn;
uint32 BSW_ID;

/*** Function Called monitoring ***/
uint8 cdcu_CallErr_core1_10ms_1;
uint8 cdcu_CallErr_core1_10ms_2;
uint8 cdcu_CallErr_core1_10ms_3;
uint8 cdcu_CallErr_core1_10ms_4;
uint8 cdcu_CallErr_core1_10ms_5;
uint8 cdcu_CallErr_core1_10ms_6;
uint8 cdcu_CallErr_core1_10ms_7;
uint8 cdcu_CallErr_core1_10ms_8;
uint8 cdcu_CallErr_core1_10ms_9;
uint8 cdcu_CallErr_core1_10ms_10;
uint8 cdcu_CallErr_core1_10ms_11;
uint8 cdcu_CallErr_core1_10ms_12;
uint8 cdcu_CallErr_core1_10ms_13;
uint8 cdcu_CallErr_core2_10ms_1;
uint8 cdcu_CallErr_core2_10ms_2;
uint8 cdcu_CallErr_core2_10ms_3;
uint8 cdcu_CallErr_core2_10ms_4;
uint8 cdcu_CallErr_core2_10ms_5;
uint8 cdcu_CallErr_core2_10ms_6;
uint8 cdcu_CallErr_core2_10ms_7;
uint8 cdcu_CallErr_core2_10ms_8;
uint8 cdcu_CallErr_core2_10ms_9;
uint8 cdcu_CallErr_core2_10ms_10;
uint8 cdcu_CallErr_core2_10ms_11;
uint8 cdcu_CallErr_core2_10ms_12;
uint8 cdcu_CallErr_core2_10ms_13;

/*** Function Operation Time monitoring ***/
uint8 cdcu_ExeTimeErr_core1_10ms_1;
uint8 cdcu_ExeTimeErr_core1_10ms_2;
uint8 cdcu_ExeTimeErr_core1_10ms_3;
uint8 cdcu_ExeTimeErr_core1_10ms_4;
uint8 cdcu_ExeTimeErr_core1_10ms_5;
uint8 cdcu_ExeTimeErr_core1_10ms_6;
uint8 cdcu_ExeTimeErr_core1_10ms_7;
uint8 cdcu_ExeTimeErr_core1_10ms_8;
uint8 cdcu_ExeTimeErr_core1_10ms_9;
uint8 cdcu_ExeTimeErr_core1_10ms_10;
uint8 cdcu_ExeTimeErr_core1_10ms_11;
uint8 cdcu_ExeTimeErr_core1_10ms_12;
uint8 cdcu_ExeTimeErr_core1_10ms_13;
uint8 cdcu_ExeTimeErr_core2_10ms_1;
uint8 cdcu_ExeTimeErr_core2_10ms_2;
uint8 cdcu_ExeTimeErr_core2_10ms_3;
uint8 cdcu_ExeTimeErr_core2_10ms_4;
uint8 cdcu_ExeTimeErr_core2_10ms_5;
uint8 cdcu_ExeTimeErr_core2_10ms_6;
uint8 cdcu_ExeTimeErr_core2_10ms_7;
uint8 cdcu_ExeTimeErr_core2_10ms_8;
uint8 cdcu_ExeTimeErr_core2_10ms_9;
uint8 cdcu_ExeTimeErr_core2_10ms_10;
uint8 cdcu_ExeTimeErr_core2_10ms_11;
uint8 cdcu_ExeTimeErr_core2_10ms_12;
uint8 cdcu_ExeTimeErr_core2_10ms_13;

/*** EOL Variable ***/
uint8 var_cdcu_EOL_Byte_0_Region;
uint8 var_cdcu_EOL_Byte_0_DrvType;
uint8 var_cdcu_EOL_Byte_1_PTType;
uint8 var_cdcu_EOL_Byte_1_EngVol;
uint8 var_cdcu_EOL_Byte_2_EngType;
uint8 var_cdcu_EOL_Byte_2_MTRType;
uint8 var_cdcu_EOL_Byte_3_TMType;
uint8 var_cdcu_EOL_Byte_3_ECSExist;
uint8 var_cdcu_EOL_Byte_3_ELSDExist;
uint8 var_cdcu_EOL_Byte_0_Region_IVD;
uint8 var_cdcu_EOL_Byte_0_DrvType_IVD;
uint8 var_cdcu_EOL_Byte_1_PTType_IVD;
uint8 var_cdcu_EOL_Byte_1_EngVol_IVD;
uint8 var_cdcu_EOL_Byte_2_EngType_IVD;
uint8 var_cdcu_EOL_Byte_2_MTRType_IVD;
uint8 var_cdcu_EOL_Byte_3_TMType_IVD;
uint8 var_cdcu_EOL_Byte_3_ECSExist_IVD;
uint8 var_cdcu_EOL_Byte_3_ELSDExist_IVD;
"""

EEPROM_H = """\n/****** EEPROM variable , Refer CDCU_BSW_Requirements_v2.1.xlsx****/
extern float32 Ivss_Offset_StrAng;
extern float32 Ivss_Offset_Yawrate;
extern float32 Ivss_Offset_Ay;
extern float32 Ivss_TTC_TolWhlFL_E2P; //v2.1 add
extern float32 Ivss_TTC_TolWhlFR_E2P; //v2.1 add
extern float32 Ivss_TTC_TolWhlRL_E2P; //v2.1 add
extern float32 Ivss_TTC_TolWhlRR_E2P; //v2.1 add
extern float32 eAWD_Offset_StrAng; //v2.1 add
extern float32 eAWD_Offset_Yawrate; //v2.1 add
extern float32 eAWD_Offset_Ay; //v2.1 add
extern float32 eAWD_TTC_TolWhlFL_E2P; //v2.1 add
extern float32 eAWD_TTC_TolWhlFR_E2P; //v2.1 add
extern float32 eAWD_TTC_TolWhlRL_E2P; //v2.1 add
extern float32 eAWD_TTC_TolWhlRR_E2P; //v2.1 add
extern sint32 CpOffset1;
extern sint32 CpOffset2;
extern uint8 CountCPE1;
extern uint8 CountCPE2;
extern sint8 NewIEB_detect;
extern uint32 CountLongCPE1;
extern uint32 CountLongCPE2;
extern uint16 DMIC_eeprom_InitChk; //v2.1 add
extern uint32 DMIC_eeprom0;
extern uint32 DMIC_eeprom1;
extern uint32 DMIC_eeprom2;
extern uint32 DMIC_eeprom3;
extern uint32 DMIC_eeprom4;
extern uint32 DMIC_eeprom5;
extern uint32 DMIC_eeprom6;
extern uint32 DMIC_eeprom7;
extern sint32 Ivss_Offset_Ax;
extern uint32 IO_BJD_EepBuff_PUB[21]; //v2.1 add
extern uint8 IO_BJD_EepSts_U8; //v2.1 add
extern uint32 ATM_LastRoad; //v2.1 add
extern uint32 ATM_NormProb; //v2.1 add
extern uint32 ATM_SnowProb; //v2.1 add
extern uint32 ATM_SandProb; //v2.1 add
extern uint32 ATM_MudProb; //v2.1 add
extern float32 TTCS_Offset_StrAng; //v2.1 add
extern float32 TTCS_Offset_Yawrate; //v2.1 add
extern float32 TTCS_Offset_Ay; //v2.1 add
extern float32 TTCS_TTC_TolWhlFL_E2P; //v2.1 add
extern float32 TTCS_TTC_TolWhlFR_E2P; //v2.1 add
extern float32 TTCS_TTC_TolWhlRL_E2P; //v2.1 add
extern float32 TTCS_TTC_TolWhlRR_E2P; //v2.1 add
extern uint8 Ivss_Offset_StrAng_IVD; //v2.1 add
extern uint8 Ivss_Offset_Yawrate_IVD; //v2.1 add
extern uint8 Ivss_Offset_Ay_IVD; //v2.1 add
extern uint8 Ivss_TTC_TolWhlFL_E2P_IVD; //v2.1 add
extern uint8 Ivss_TTC_TolWhlFR_E2P_IVD; //v2.1 add
extern uint8 Ivss_TTC_TolWhlRL_E2P_IVD; //v2.1 add
extern uint8 Ivss_TTC_TolWhlRR_E2P_IVD; //v2.1 add
extern uint8 eAWD_Offset_StrAng_IVD; //v2.1 add
extern uint8 eAWD_Offset_Yawrate_IVD; //v2.1 add
extern uint8 eAWD_Offset_Ay_IVD; //v2.1 add
extern uint8 eAWD_TTC_TolWhlFL_E2P_IVD; //v2.1 add
extern uint8 eAWD_TTC_TolWhlFR_E2P_IVD; //v2.1 add
extern uint8 eAWD_TTC_TolWhlRL_E2P_IVD; //v2.1 add
extern uint8 eAWD_TTC_TolWhlRR_E2P_IVD; //v2.1 add
extern uint8 CpOffset1_IVD; //v2.1 add
extern uint8 CpOffset2_IVD; //v2.1 add
extern uint8 CountCPE1_IVD; //v2.1 add
extern uint8 CountCPE2_IVD; //v2.1 add
extern uint8 NewIEB_detect_IVD; //v2.1 add
extern uint8 CountLongCPE1_IVD; //v2.1 add
extern uint8 CountLongCPE2_IVD; //v2.1 add
extern uint8 DMIC_eeprom_InitChk_IVD; //v2.1 add
extern uint8 DMIC_eeprom0_IVD; //v2.1 add
extern uint8 DMIC_eeprom1_IVD; //v2.1 add
extern uint8 DMIC_eeprom2_IVD; //v2.1 add
extern uint8 DMIC_eeprom3_IVD; //v2.1 add
extern uint8 DMIC_eeprom4_IVD; //v2.1 add
extern uint8 DMIC_eeprom5_IVD; //v2.1 add
extern uint8 DMIC_eeprom6_IVD; //v2.1 add
extern uint8 DMIC_eeprom7_IVD; //v2.1 add
extern uint8 Ivss_Offset_Ax_IVD; //v2.1 add
extern uint8 IO_BJD_EepBuff_PUB_IVD; //v2.1 add
extern uint8 ATM_LastRoad_IVD; //v2.1 add
extern uint8 ATM_NormProb_IVD; //v2.1 add
extern uint8 ATM_SnowProb_IVD; //v2.1 add
extern uint8 ATM_SandProb_IVD; //v2.1 add
extern uint8 ATM_MudProb_IVD; //v2.1 add
extern uint8 TTCS_Offset_StrAng_IVD; //v2.1 add
extern uint8 TTCS_Offset_Yawrate_IVD; //v2.1 add
extern uint8 TTCS_Offset_Ay_IVD; //v2.1 add
extern uint8 TTCS_TTC_TolWhlFL_E2P_IVD; //v2.1 add
extern uint8 TTCS_TTC_TolWhlFR_E2P_IVD; //v2.1 add
extern uint8 TTCS_TTC_TolWhlRL_E2P_IVD; //v2.1 add
extern uint8 TTCS_TTC_TolWhlRR_E2P_IVD; //v2.1 add

enum{
 	enum_Ivss_Offset_StrAng = 0U,
	enum_Ivss_Offset_Yawrate,
	enum_Ivss_Offset_Ay,
	enum_Ivss_TTC_TolWhlFL_E2P,  //v2.1 add
    enum_Ivss_TTC_TolWhlFR_E2P,  //v2.1 add
    enum_Ivss_TTC_TolWhlRL_E2P,  //v2.1 add
    enum_Ivss_TTC_TolWhlRR_E2P,  //v2.1 add
    enum_eAWD_Offset_StrAng,  //v2.1 add
    enum_eAWD_Offset_Yawrate,  //v2.1 add
    enum_eAWD_Offset_Ay,  //v2.1 add
    enum_eAWD_TTC_TolWhlFL_E2P,  //v2.1 add
    enum_eAWD_TTC_TolWhlFR_E2P,  //v2.1 add
    enum_eAWD_TTC_TolWhlRL_E2P,  //v2.1 add
    enum_eAWD_TTC_TolWhlRR_E2P,  //v2.1 add
    enum_DMIC_eeprom_InitChk, //v2.1 add
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
	enum_IO_BJD_EepBuff_PUB, //v2.1 add
	enum_IO_BJD_EepSts_U8, //v2.1 add
    enum_ATM_LastRoad, //v2.1 add
    enum_ATM_NormProb, //v2.1 add
    enum_ATM_SnowProb, //v2.1 add
    enum_ATM_SandProb, //v2.1 add
    enum_ATM_MudProb, //v2.1 add
    enum_TTCS_Offset_StrAng, //v2.1 add
    enum_TTCS_Offset_Yawrate, //v2.1 add
    enum_TTCS_Offset_Ay, //v2.1 add
    enum_TTCS_TTC_TolWhlFL_E2P, //v2.1 add
    enum_TTCS_TTC_TolWhlFR_E2P, //v2.1 add
    enum_TTCS_TTC_TolWhlRL_E2P, //v2.1 add
    enum_TTCS_TTC_TolWhlRR_E2P, //v2.1 add
    /**** EOL Variable*****/
    enum_EOL_Byte_0_Region,
    enum_EOL_Byte_0_DrvType,
    enum_EOL_Byte_1_PTType,
    enum_EOL_Byte_1_EngVol,
    enum_EOL_Byte_2_EngType,
    enum_EOL_Byte_2_MTRType,
    enum_EOL_Byte_3_TMType,
    enum_EOL_Byte_3_ECSExist,
    enum_EOL_Byte_3_ELSDExist,
 	enum_Ivss_Offset_StrAng_MIRR,
	enum_Ivss_Offset_Yawrate_MIRR,
	enum_Ivss_Offset_Ay_MIRR,
	enum_Ivss_TTC_TolWhlFL_E2P_MIRR,  //v2.1 add
    enum_Ivss_TTC_TolWhlFR_E2P_MIRR, //v2.1 add
    enum_Ivss_TTC_TolWhlRL_E2P_MIRR,  //v2.1 add
    enum_Ivss_TTC_TolWhlRR_E2P_MIRR,  //v2.1 add
    enum_eAWD_Offset_StrAng_MIRR,  //v2.1 add
    enum_eAWD_Offset_Yawrate_MIRR,  //v2.1 add
    enum_eAWD_Offset_Ay_MIRR,  //v2.1 add
    enum_eAWD_TTC_TolWhlFL_E2P_MIRR,  //v2.1 add
    enum_eAWD_TTC_TolWhlFR_E2P_MIRR,  //v2.1 add
    enum_eAWD_TTC_TolWhlRL_E2P_MIRR,  //v2.1 add
    enum_eAWD_TTC_TolWhlRR_E2P_MIRR,  //v2.1 add
    enum_DMIC_eeprom_InitChk_MIRR, //v2.1 add
	enum_CpOffset1_MIRR,
	enum_CpOffset2_MIRR,
	enum_CountCPE1_MIRR,
	enum_CountCPE2_MIRR,
	enum_NewIEB_detect_MIRR,
	enum_CountLongCPE1_MIRR,
	enum_CountLongCPE2_MIRR,
	enum_DMIC_eeprom0_MIRR,
	enum_DMIC_eeprom1_MIRR,
	enum_DMIC_eeprom2_MIRR,
	enum_DMIC_eeprom3_MIRR,
	enum_DMIC_eeprom4_MIRR,
	enum_DMIC_eeprom5_MIRR,
	enum_DMIC_eeprom6_MIRR,
	enum_DMIC_eeprom7_MIRR,
	enum_Ivss_Offset_Ax_MIRR,
	enum_IO_BJD_EepBuff_PUB_MIRR, //v2.1 add
	enum_IO_BJD_EepSts_U8_MIRR, //v2.1 add
    enum_ATM_LastRoad_MIRR, //v2.1 add
    enum_ATM_NormProb_MIRR, //v2.1 add
    enum_ATM_SnowProb_MIRR, //v2.1 add
    enum_ATM_SandProb_MIRR, //v2.1 add
    enum_ATM_MudProb_MIRR, //v2.1 add
    enum_TTCS_Offset_StrAng_MIRR, //v2.1 add
    enum_TTCS_Offset_Yawrate_MIRR, //v2.1 add
    enum_TTCS_Offset_Ay_MIRR, //v2.1 add
    enum_TTCS_TTC_TolWhlFL_E2P_MIRR, //v2.1 add
    enum_TTCS_TTC_TolWhlFR_E2P_MIRR, //v2.1 add
    enum_TTCS_TTC_TolWhlRL_E2P_MIRR, //v2.1 add
    enum_TTCS_TTC_TolWhlRR_E2P_MIRR, //v2.1 add   
    /**** EOL Variable*****/
    enum_EOL_Byte_0_Region_MIRR,
    enum_EOL_Byte_0_DrvType_MIRR,
    enum_EOL_Byte_1_PTType_MIRR,
    enum_EOL_Byte_1_EngVol_MIRR,
    enum_EOL_Byte_2_EngType_MIRR,
    enum_EOL_Byte_2_MTRType_MIRR,
    enum_EOL_Byte_3_TMType_MIRR,
    enum_EOL_Byte_3_ECSExist_MIRR,
    enum_EOL_Byte_3_ELSDExist_MIRR,
	enum_WriteCheck,
	EEPROM_NUM
};"""


ENUM = """enum{
 	enum_Ivss_Offset_StrAng = 0U,
	enum_Ivss_Offset_Yawrate,
	enum_Ivss_Offset_Ay,
	enum_Ivss_TTC_TolWhlFL_E2P,  //v2.1 add
    enum_Ivss_TTC_TolWhlFR_E2P,  //v2.1 add
    enum_Ivss_TTC_TolWhlRL_E2P,  //v2.1 add
    enum_Ivss_TTC_TolWhlRR_E2P,  //v2.1 add
    enum_eAWD_Offset_StrAng,  //v2.1 add
    enum_eAWD_Offset_Yawrate,  //v2.1 add
    enum_eAWD_Offset_Ay,  //v2.1 add
    enum_eAWD_TTC_TolWhlFL_E2P,  //v2.1 add
    enum_eAWD_TTC_TolWhlFR_E2P,  //v2.1 add
    enum_eAWD_TTC_TolWhlRL_E2P,  //v2.1 add
    enum_eAWD_TTC_TolWhlRR_E2P,  //v2.1 add
    enum_DMIC_eeprom_InitChk, //v2.1 add
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
	enum_IO_BJD_EepBuff_PUB, //v2.1 add
	enum_IO_BJD_EepSts_U8, //v2.1 add
    enum_ATM_LastRoad, //v2.1 add
    enum_ATM_NormProb, //v2.1 add
    enum_ATM_SnowProb, //v2.1 add
    enum_ATM_SandProb, //v2.1 add
    enum_ATM_MudProb, //v2.1 add
    enum_TTCS_Offset_StrAng, //v2.1 add
    enum_TTCS_Offset_Yawrate, //v2.1 add
    enum_TTCS_Offset_Ay, //v2.1 add
    enum_TTCS_TTC_TolWhlFL_E2P, //v2.1 add
    enum_TTCS_TTC_TolWhlFR_E2P, //v2.1 add
    enum_TTCS_TTC_TolWhlRL_E2P, //v2.1 add
    enum_TTCS_TTC_TolWhlRR_E2P, //v2.1 add
    /**** EOL Variable*****/
    enum_EOL_Byte_0_Region,
    enum_EOL_Byte_0_DrvType,
    enum_EOL_Byte_1_PTType,
    enum_EOL_Byte_1_EngVol,
    enum_EOL_Byte_2_EngType,
    enum_EOL_Byte_2_MTRType,
    enum_EOL_Byte_3_TMType,
    enum_EOL_Byte_3_ECSExist,
    enum_EOL_Byte_3_ELSDExist,
 	enum_Ivss_Offset_StrAng_MIRR,
	enum_Ivss_Offset_Yawrate_MIRR,
	enum_Ivss_Offset_Ay_MIRR,
	enum_Ivss_TTC_TolWhlFL_E2P_MIRR,  //v2.1 add
    enum_Ivss_TTC_TolWhlFR_E2P_MIRR, //v2.1 add
    enum_Ivss_TTC_TolWhlRL_E2P_MIRR,  //v2.1 add
    enum_Ivss_TTC_TolWhlRR_E2P_MIRR,  //v2.1 add
    enum_eAWD_Offset_StrAng_MIRR,  //v2.1 add
    enum_eAWD_Offset_Yawrate_MIRR,  //v2.1 add
    enum_eAWD_Offset_Ay_MIRR,  //v2.1 add
    enum_eAWD_TTC_TolWhlFL_E2P_MIRR,  //v2.1 add
    enum_eAWD_TTC_TolWhlFR_E2P_MIRR,  //v2.1 add
    enum_eAWD_TTC_TolWhlRL_E2P_MIRR,  //v2.1 add
    enum_eAWD_TTC_TolWhlRR_E2P_MIRR,  //v2.1 add
    enum_DMIC_eeprom_InitChk_MIRR, //v2.1 add
	enum_CpOffset1_MIRR,
	enum_CpOffset2_MIRR,
	enum_CountCPE1_MIRR,
	enum_CountCPE2_MIRR,
	enum_NewIEB_detect_MIRR,
	enum_CountLongCPE1_MIRR,
	enum_CountLongCPE2_MIRR,
	enum_DMIC_eeprom0_MIRR,
	enum_DMIC_eeprom1_MIRR,
	enum_DMIC_eeprom2_MIRR,
	enum_DMIC_eeprom3_MIRR,
	enum_DMIC_eeprom4_MIRR,
	enum_DMIC_eeprom5_MIRR,
	enum_DMIC_eeprom6_MIRR,
	enum_DMIC_eeprom7_MIRR,
	enum_Ivss_Offset_Ax_MIRR,
	enum_IO_BJD_EepBuff_PUB_MIRR, //v2.1 add
	enum_IO_BJD_EepSts_U8_MIRR, //v2.1 add
    enum_ATM_LastRoad_MIRR, //v2.1 add
    enum_ATM_NormProb_MIRR, //v2.1 add
    enum_ATM_SnowProb_MIRR, //v2.1 add
    enum_ATM_SandProb_MIRR, //v2.1 add
    enum_ATM_MudProb_MIRR, //v2.1 add
    enum_TTCS_Offset_StrAng_MIRR, //v2.1 add
    enum_TTCS_Offset_Yawrate_MIRR, //v2.1 add
    enum_TTCS_Offset_Ay_MIRR, //v2.1 add
    enum_TTCS_TTC_TolWhlFL_E2P_MIRR, //v2.1 add
    enum_TTCS_TTC_TolWhlFR_E2P_MIRR, //v2.1 add
    enum_TTCS_TTC_TolWhlRL_E2P_MIRR, //v2.1 add
    enum_TTCS_TTC_TolWhlRR_E2P_MIRR, //v2.1 add   
    /**** EOL Variable*****/
    enum_EOL_Byte_0_Region_MIRR,
    enum_EOL_Byte_0_DrvType_MIRR,
    enum_EOL_Byte_1_PTType_MIRR,
    enum_EOL_Byte_1_EngVol_MIRR,
    enum_EOL_Byte_2_EngType_MIRR,
    enum_EOL_Byte_2_MTRType_MIRR,
    enum_EOL_Byte_3_TMType_MIRR,
    enum_EOL_Byte_3_ECSExist_MIRR,
    enum_EOL_Byte_3_ELSDExist_MIRR,
	enum_WriteCheck,
	EEPROM_NUM
};"""

EEPROM_C = """\n/****** EEPROM variable , Refer CDCU_BSW_Requirements_v2.1.xlsx****/
float32 Ivss_Offset_StrAng;
float32 Ivss_Offset_Yawrate;
float32 Ivss_Offset_Ay;
float32 Ivss_TTC_TolWhlFL_E2P; //v2.1 add
float32 Ivss_TTC_TolWhlFR_E2P; //v2.1 add
float32 Ivss_TTC_TolWhlRL_E2P; //v2.1 add
float32 Ivss_TTC_TolWhlRR_E2P; //v2.1 add
float32 eAWD_Offset_StrAng; //v2.1 add
float32 eAWD_Offset_Yawrate; //v2.1 add
float32 eAWD_Offset_Ay; //v2.1 add
float32 eAWD_TTC_TolWhlFL_E2P; //v2.1 add
float32 eAWD_TTC_TolWhlFR_E2P; //v2.1 add
float32 eAWD_TTC_TolWhlRL_E2P; //v2.1 add
float32 eAWD_TTC_TolWhlRR_E2P; //v2.1 add
sint32 CpOffset1;
sint32 CpOffset2;
uint8 CountCPE1;
uint8 CountCPE2;
sint8 NewIEB_detect;
uint32 CountLongCPE1;
uint32 CountLongCPE2;
uint16 DMIC_eeprom_InitChk; //v2.1 add
uint32 DMIC_eeprom0;
uint32 DMIC_eeprom1;
uint32 DMIC_eeprom2;
uint32 DMIC_eeprom3;
uint32 DMIC_eeprom4;
uint32 DMIC_eeprom5;
uint32 DMIC_eeprom6;
uint32 DMIC_eeprom7;
sint32 Ivss_Offset_Ax;
uint32 IO_BJD_EepBuff_PUB[21]; //v2.1 add
uint8 IO_BJD_EepSts_U8; //v2.1 add
uint32 ATM_LastRoad; //v2.1 add
uint32 ATM_NormProb; //v2.1 add
uint32 ATM_SnowProb; //v2.1 add
uint32 ATM_SandProb; //v2.1 add
uint32 ATM_MudProb; //v2.1 add
float32 TTCS_Offset_StrAng; //v2.1 add
float32 TTCS_Offset_Yawrate; //v2.1 add
float32 TTCS_Offset_Ay; //v2.1 add
float32 TTCS_TTC_TolWhlFL_E2P; //v2.1 add
float32 TTCS_TTC_TolWhlFR_E2P; //v2.1 add
float32 TTCS_TTC_TolWhlRL_E2P; //v2.1 add
float32 TTCS_TTC_TolWhlRR_E2P; //v2.1 add
uint8 Ivss_Offset_StrAng_IVD; //v2.1 add
uint8 Ivss_Offset_Yawrate_IVD; //v2.1 add
uint8 Ivss_Offset_Ay_IVD; //v2.1 add
uint8 Ivss_TTC_TolWhlFL_E2P_IVD; //v2.1 add
uint8 Ivss_TTC_TolWhlFR_E2P_IVD; //v2.1 add
uint8 Ivss_TTC_TolWhlRL_E2P_IVD; //v2.1 add
uint8 Ivss_TTC_TolWhlRR_E2P_IVD; //v2.1 add
uint8 eAWD_Offset_StrAng_IVD; //v2.1 add
uint8 eAWD_Offset_Yawrate_IVD; //v2.1 add
uint8 eAWD_Offset_Ay_IVD; //v2.1 add
uint8 eAWD_TTC_TolWhlFL_E2P_IVD; //v2.1 add
uint8 eAWD_TTC_TolWhlFR_E2P_IVD; //v2.1 add
uint8 eAWD_TTC_TolWhlRL_E2P_IVD; //v2.1 add
uint8 eAWD_TTC_TolWhlRR_E2P_IVD; //v2.1 add
uint8 CpOffset1_IVD; //v2.1 add
uint8 CpOffset2_IVD; //v2.1 add
uint8 CountCPE1_IVD; //v2.1 add
uint8 CountCPE2_IVD; //v2.1 add
uint8 NewIEB_detect_IVD; //v2.1 add
uint8 CountLongCPE1_IVD; //v2.1 add
uint8 CountLongCPE2_IVD; //v2.1 add
uint8 DMIC_eeprom_InitChk_IVD; //v2.1 add
uint8 DMIC_eeprom0_IVD; //v2.1 add
uint8 DMIC_eeprom1_IVD; //v2.1 add
uint8 DMIC_eeprom2_IVD; //v2.1 add
uint8 DMIC_eeprom3_IVD; //v2.1 add
uint8 DMIC_eeprom4_IVD; //v2.1 add
uint8 DMIC_eeprom5_IVD; //v2.1 add
uint8 DMIC_eeprom6_IVD; //v2.1 add
uint8 DMIC_eeprom7_IVD; //v2.1 add
uint8 Ivss_Offset_Ax_IVD; //v2.1 add
uint8 IO_BJD_EepBuff_PUB_IVD; //v2.1 add
uint8 ATM_LastRoad_IVD; //v2.1 add
uint8 ATM_NormProb_IVD; //v2.1 add
uint8 ATM_SnowProb_IVD; //v2.1 add
uint8 ATM_SandProb_IVD; //v2.1 add
uint8 ATM_MudProb_IVD; //v2.1 add
uint8 TTCS_Offset_StrAng_IVD; //v2.1 add
uint8 TTCS_Offset_Yawrate_IVD; //v2.1 add
uint8 TTCS_Offset_Ay_IVD; //v2.1 add
uint8 TTCS_TTC_TolWhlFL_E2P_IVD; //v2.1 add
uint8 TTCS_TTC_TolWhlFR_E2P_IVD; //v2.1 add
uint8 TTCS_TTC_TolWhlRL_E2P_IVD; //v2.1 add
uint8 TTCS_TTC_TolWhlRR_E2P_IVD; //v2.1 add"""

declarState_Start = """/** ================================**/
/** Company : Kyungshin              **/
/** Project Name : CDCU             **/
/** Create Date :  {0}-{1}-{2}      **/
/** Author      : KangSH            **/
/** ================================**/
#ifndef INTERFACE_H_
#define INTERFACE_H_

#include "APP_Variable_KSC.h"
#include "Rte_Type.h"\n

#define HMC_FUNC_CALL 		STD_ON""".format(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)

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
        excelfile_list = glob.glob(filepath + "\\" + "*.xlsx") ## File searching within filepath
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
            EepSource = SourceGen.EEpCodeGenerate(excelfile_list[0])

            if not os.path.isdir(Sourcepath): #creat folder if not folder
                os.makedirs(Sourcepath)

            refer = "/************{referfile}***************/\n".format(referfile = fileName)
            ##### Interface.c/interface.h create ########
            ## header file create
            headerfilepath = os.path.join(Sourcepath, declareFile)
            if not os.path.isdir(headerfilepath):
                with open(headerfilepath, 'w') as f:
                    f.write(refer + declarState_Start)

            Cfilepath = os.path.join(Sourcepath, defineFile)
            ## Source file create
            if not os.path.isdir(Cfilepath):
                with open(Cfilepath, 'w') as f:
                    f.write(refer + defineState)

            ##### add to message Ind, timeout Ind ########
            source.Ind_variable(Cfilepath, headerfilepath)
            source.TimeOutInd_variable(Cfilepath, headerfilepath)
            source.Invalid_variable(Cfilepath, headerfilepath)
            source.Signal_variable(Cfilepath, headerfilepath)
            EepH, EepC = EepSource.Eep_variable()
            declarState_End2 = "{Infor}\n{eeprom}\n{extra}\n#endif /* APP_VARIABLE_H_ */".format(Infor=InforVar_H,eeprom=EepH, extra = ENUM)
            defineState_End2 = "{Infor}\n{eeprom}".format(Infor=InforVar_C, eeprom=EepC)

            with open(headerfilepath, 'a') as f:
                f.write(declarState_End2)

            with open(Cfilepath, 'a') as f:
                f.write(defineState_End2)
            #######################################################

            ##### C-CAN File Create ######
            CCANfilepath = os.path.join(Sourcepath, "CCANFD_Swc.c")
            source.CCANFD_File(CCANfilepath)

            ##### P-CAN File Create ######
            #PCANfilepath = os.path.join(Sourcepath, "PCANFD_Swc.c")
            #source.PCANFD_File(PCANfilepath)

            ##### G-CAN File Create ######
            #GCANfilepath = os.path.join(Sourcepath, "GCANFD_Swc.c")
            #source.GCANFD_File(GCANfilepath)

            ##### TxMon Generate #####
            #TxMonfilepath = os.path.join(Sourcepath, "TxMon.c")
            #source.TxMon_Gen(TxMonfilepath)

            ####### NvM File Generate #########
            #NvMfilepath = os.path.join(Sourcepath, "NvMSwc.c")
            #EepSource.NvM_File(NvMfilepath)

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

            #### CCANFDSwc Arxml Generate about indicate function and timeout function ####
            #Arxml = Arxml_gen.ArxmlParser(arxmlpath, excelfile_list[0]) # arxml class instance
            #ccan_ind = Arxml.CCAN_extract_data() # runnable name extract
            #Arxml.xml_gen(ccan_ind)
            #Arxml.make_xml(outputpath)
            #print(list)

            #### PCANFDSwc Arxml Generate about indicate function and timeout function ####
            #Arxml = Arxml_gen.ArxmlParser(arxmlpath, excelfile_list[0]) # arxml class instance
            #pcan_ind = Arxml.PCAN_extract_data() # runnable name extract
            #Arxml.xml_gen(pcan_ind)
            #Arxml.make_xml(outputpath)

            #### GCANFDSwc Arxml Generate about indicate function and timeout function ####
            #Arxml = Arxml_gen.ArxmlParser(arxmlpath, excelfile_list[0]) # arxml class instance
            #gcan_ind = Arxml.GCAN_extract_data() # runnable name extract
            #Arxml.xml_gen(gcan_ind)
            #Arxml.make_xml(outputpath)
    else:
        print("put into file after excel folder is created")
        os.makedirs(filepath)

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time() - start
    print ('Operating Time : {0}s' .format(end))


