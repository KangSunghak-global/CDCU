import datetime

def variable(size, signalName, value, length):
    if size == "unsigned char":
        size = "uint8"
    elif size == "char":
        size = "sint8"
    elif size == "unsigned short":
        size = "uint16"
    elif size == "unsigned int":
        if length >16:
            size = "uint32"
        else:
            size = "uint16"
    elif size == "int":
        if length >16:
            size = "sint32"
        else:
            size = "sint16"
    elif size == "float":
        size = "float32"
    else:
        pass

    variable_dec = "extern {type} {Name};\n".format(type=size, Name=signalName)
    variable_def = "{type} {Name}={init};\n".format(type=size, Name=signalName, init=value)

    return variable_dec, variable_def

def EEp_variable(size, signalName, length):
    if size == "unsigned char":
        size = "uint8"
    elif size == "char":
        size = "sint8"
    elif size == "unsinged short":
        size = "uint16"
    elif size == "unsigned int":
        if length == 4:
            size = "uint32"
        else:
            size = "uint16"
    elif size == "int":
        if length == 4:
            size = "sint32"
        else:
            size = "sint16"
    elif size == "float":
        size = "float32"
    else:
        pass

    variable_dec = "extern {type} {Name};\n".format(type=size, Name=signalName)
    variable_def = "{type} {Name};\n".format(type=size, Name=signalName)

    return variable_dec, variable_def

def Start_State(CANName):
    defineState = """/** ================================**/
/** Company : Kyungshin              **/
/** Project Name : CDCU             **/
/** Create Date :  {0}-{1}-{2}      **/
/** Author      : KangSH            **/
/** ================================**/
/****************E2E Error Value *********************** 
 E2E_P_OK : 0  - there is no problem when checking E2E 
 E2E_P_REPEATED : 1 - duplicate about alive counter
 E2E_P_WRONGSEQUENCE : 2 - Ailve counter error (over count)
 E2E_P_ERROR : 3 - CRC not matching
 E2E_P_NOTAVAILABLE : 4 -  Can not access in the data
 E2E_P_NONEWDATA : 5 -  Can not access in the data
***************************************************/

#include "interface.h"
#include "APP_Variable_KSC.h"
#include "Rte_{channel}_Swc.h"
#include "E2E_Types.h"

/*******************************************************************************
**                      MACRO			                                  **
*******************************************************************************/
#define {channel}_200MS		20U
#define {channel}_100MS		10U
#define {channel}_20MS		2U
#define {channel}_ERR_TIME  50U
/*******************************************************************************
**                      Veriable Definitions                                  **
*******************************************************************************/
static uint8 ubS_C_{channel}_200msCnt = 0U;
static uint8 ubS_C_{channel}_100msCnt = 0U;
static uint8 ubS_C_{channel}_20msCnt = 0U;

/*******************************************************************************
**                      Function Definitions                                  **
*******************************************************************************/\n\n""".format(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day,channel=CANName)

    return defineState

# { or } must be twice for charactor
def Indicate_Function(filename, MessageName, cycle):
    if cycle > 0:
        text = """FUNC (void, {file}_Swc_CODE)Rt_{Message}_Ind(void)
{{
     ubS_F_{Message}_Ind = STD_ON;
     Rxmissing_{Message} = STD_OFF;
}}
 
FUNC (void, {file}_Swc_CODE)RTout_{Message}_Ind(void)
{{
     Rxmissing_{Message} = STD_ON;
}}\n\n""".format(file = filename, Message = MessageName)

    else:
        text = """FUNC (void, {file}_Swc_CODE)Rt_{Message}_Ind(void)
{{
    ubS_F_{Message}_Ind = STD_ON;
}}\n\n""".format(file = filename, Message = MessageName)

    return text

def Rx_Signal(size, Var,filename,Cluster, MessageName,SignalName, Offset, Factor):
    if size == "unsigned char":
        size = "uint8"
    elif size == "char":
        size = "sint8"
    elif size == "unsigned int":
        size = "uint16"
    elif size == "int":
        size = "sint16"
    elif size == "float":
        size = "float32"
    else:
        pass

    if Offset < 0:
        Offset_t = str(Offset).split('.')
        if Offset_t[1] == "0": ## remove '.0'
            text = "{Variable} = ({type})(((Rte_DRead_{File}_Swc_{ClusterName}_{Msg}_{Sig}())*{Fac}){Off});\n\t\t".format(type=size, Variable=Var, File=filename, ClusterName=Cluster, Msg=MessageName, Sig=SignalName,Off=Offset_t[0], Fac=Factor)
        else:
            text = "{Variable} = ({type})(((Rte_DRead_{File}_Swc_{ClusterName}_{Msg}_{Sig}())*{Fac}){Off});\n\t\t".format(type=size,Variable=Var,File=filename,ClusterName=Cluster,Msg=MessageName,Sig=SignalName,Off=Offset,Fac=Factor)
    else:
        Offset_t = str(Offset).split('.')
        if Offset_t[1] == "0": ## remove '.0'
            text = "{Variable} = ({type})(((Rte_DRead_{File}_Swc_{ClusterName}_{Msg}_{Sig}())*{Fac})+{Off});\n\t\t".format(type=size, Variable=Var, File=filename, ClusterName=Cluster, Msg=MessageName, Sig=SignalName,Off=Offset_t[0], Fac=Factor)
        else:
            text = "{Variable} = ({type})(((Rte_DRead_{File}_Swc_{ClusterName}_{Msg}_{Sig}())*{Fac})+{Off});\n\t\t".format(type=size,Variable=Var,File = filename,ClusterName = Cluster, Msg=MessageName, Sig=SignalName, Off=Offset, Fac=Factor)
    return text

def Rx_E2E_Signal(size, Var,MessageName, SignalName, Offset, Factor):
    if size == "unsigned char":
        size = "uint8"
    elif size == "char":
        size = "sint8"
    elif size == "unsigned int":
        size = "uint16"
    elif size == "int":
        size = "sint16"
    elif size == "float":
        size = "float32"
    else:
        pass

    if Offset < 0:
        Offset_t = str(Offset).split('.')
        if Offset_t[1] == "0" :
            text = "{Variable} = ({type})(((stS_D_RC_E2E_{Msg}.{Sig})*{Fac}){Off});\n\t\t".format(type=size,Variable=Var, Msg=MessageName,Sig=SignalName, Off=Offset_t[0], Fac=Factor)
        else:
            text = "{Variable} = ({type})(((stS_D_RC_E2E_{Msg}.{Sig})*{Fac}){Off});\n\t\t".format(type=size,Variable=Var,Msg=MessageName,Sig=SignalName,Off=Offset,Fac=Factor)
    else:
        Offset_t = str(Offset).split('.')
        if Offset_t[1] == "0" :
            text = "{Variable} = ({type})(((stS_D_RC_E2E_{Msg}.{Sig})*{Fac})+{Off});\n\t\t".format(type=size,Variable=Var, Msg=MessageName, Sig=SignalName, Off=Offset_t[0],Fac=Factor)
        else:
            text = "{Variable} = ({type})(((stS_D_RC_E2E_{Msg}.{Sig})*{Fac})+{Off});\n\t\t".format(type=size,Variable=Var, Msg=MessageName, Sig=SignalName, Off=Offset, Fac=Factor)

    return text

def Rx_Function(Cluster, filename, MessageName, set, E2EFlag, Sender, Cycle):
    if E2EFlag == 1:
        if Cycle == 10:
            text = """static MsgGr_E2E_{ClusterName}_{Msg} stS_D_RC_E2E_{Msg};
static Rte_TransformerError stS_D_RC_E2E_ErrCode_{Msg};
static uint16 ubS_C_RC_{Msg}_Crc_Cnt;
static uint16 ubS_C_RC_{Msg}_Ac_Cnt;
static void s_{file}_{Msg}_Rx(void)
{{
    Rte_Read_{file}_Swc_Gr_MsgGr_E2E_{ClusterName}_{Msg}_MsgGr_E2E_{ClusterName}_{Msg}(&stS_D_RC_E2E_{Msg}, &stS_D_RC_E2E_ErrCode_{Msg});

    {RxSignalSet}

    if((stS_D_RC_E2E_ErrCode_{Msg}.errorCode & 0x0FU) == E2E_P_OK)
    {{
        /** Not error **/
        IVD_{ECU}_CrcVal = STD_OFF;
        IVD_{ECU}_AlvCntVal = STD_OFF;
        ubS_C_RC_{Msg}_Crc_Cnt = 0U;
        ubS_C_RC_{Msg}_Ac_Cnt = 0U;
    }}
    else if(((stS_D_RC_E2E_ErrCode_{Msg}.errorCode & 0x0FU) == E2E_P_REPEATED)||((stS_D_RC_E2E_ErrCode_{Msg}.errorCode & 0x0FU) == E2E_P_WRONGSEQUENCE))
    {{
        /** Alive counter error **/
        if(ubS_C_RC_{Msg}_Ac_Cnt < {ClusterName}FD_ERR_TIME)
        {{
            ubS_C_RC_{Msg}_Ac_Cnt ++;
        }}
        else
        {{
             IVD_{ECU}_AlvCntVal = STD_ON;
        }}
    }}	
    else if((stS_D_RC_E2E_ErrCode_{Msg}.errorCode & 0x0FU) == E2E_P_ERROR)
    {{
        /** CRC error **/
        if(ubS_C_RC_{Msg}_Crc_Cnt < {ClusterName}FD_ERR_TIME)
        {{
            ubS_C_RC_{Msg}_Crc_Cnt ++;
        }}
        else
        {{
            IVD_{ECU}_CrcVal = STD_ON;
        }}
    }}
    else{{
        /**nop**/
    }}

}}\n\n""".format(file=filename, Msg=MessageName, RxSignalSet=set, ClusterName=Cluster, ECU=Sender)
        else:
            text = """static MsgGr_E2E_{ClusterName}_{Msg} stS_D_RC_E2E_{Msg};
static Rte_TransformerError stS_D_RC_E2E_ErrCode_{Msg};
static uint16 ubS_C_RC_{Msg}_Crc_Cnt;
static uint16 ubS_C_RC_{Msg}_Ac_Cnt;
static void s_{file}_{Msg}_Rx(void)
{{
    if(ubS_F_{Msg}_Ind == STD_ON)
    {{
        Rte_Read_{file}_Swc_Gr_MsgGr_E2E_{ClusterName}_{Msg}_MsgGr_E2E_{ClusterName}_{Msg}(&stS_D_RC_E2E_{Msg}, &stS_D_RC_E2E_ErrCode_{Msg});
        
        {RxSignalSet}
        
        if((stS_D_RC_E2E_ErrCode_{Msg}.errorCode & 0x0FU) == E2E_P_OK)
        {{
            /** Not error **/
            IVD_{ECU}_CrcVal = STD_OFF;
            IVD_{ECU}_AlvCntVal = STD_OFF;
            ubS_C_RC_{Msg}_Crc_Cnt = 0U;
            ubS_C_RC_{Msg}_Ac_Cnt = 0U;
        }}
        else if(((stS_D_RC_E2E_ErrCode_{Msg}.errorCode & 0x0FU) == E2E_P_REPEATED)||((stS_D_RC_E2E_ErrCode_{Msg}.errorCode & 0x0FU) == E2E_P_WRONGSEQUENCE))
        {{
            /** Alive counter error **/
            if(ubS_C_RC_{Msg}_Ac_Cnt < {ClusterName}FD_ERR_TIME)
            {{
                ubS_C_RC_{Msg}_Ac_Cnt ++;
            }}
            else
            {{
                 IVD_{ECU}_AlvCntVal = STD_ON;
            }}
        }}	
        else if((stS_D_RC_E2E_ErrCode_{Msg}.errorCode & 0x0FU) == E2E_P_ERROR)
        {{
            /** CRC error **/
            if(ubS_C_RC_{Msg}_Crc_Cnt < {ClusterName}FD_ERR_TIME)
            {{
                ubS_C_RC_{Msg}_Crc_Cnt ++;
            }}
            else
            {{
                IVD_{ECU}_CrcVal = STD_ON;
            }}
        }}
        else{{
            /**nop**/
        }}
         	
        ubS_F_{Msg}_Ind = STD_OFF;
    }}
}}\n\n""".format(file=filename, Msg=MessageName, RxSignalSet=set, ClusterName = Cluster, ECU=Sender)
    else:
        text = """static void s_{file}_{Msg}_Rx(void)
{{
    if(ubS_F_{Msg}_Ind == STD_ON)
    {{
        {RxSignalSet}		
        ubS_F_{Msg}_Ind = STD_OFF;
    }}
}}\n\n""".format(file = filename, Msg=MessageName, RxSignalSet=set)

    return text

def variable_Old(size, VarName):
    if size == "unsigned char":
        size = "uint8"
    elif size == "char":
        size = "sint8"
    elif size == "unsigned int":
        size = "uint16"
    elif size == "int":
        size = "sint16"
    elif size == "float":
        size = "float32"
    else:
        pass

    text = "static {type} {Name}_Old=0;\n".format(type=size, Name=VarName)

    return text

def Tx_Signal(Var,filename,Cluster,MessageName,SignalName, E2EFlag):
    if E2EFlag == 1:
        text = """if(stS_D_RC_E2E_{ClusterName}_{Msg}.{Sig} != {Variable})
    {{
        stS_D_RC_E2E_{ClusterName}_{Msg}.{Sig} = {Variable};
        ubS_F_RC_E2E_{ClusterName}_{Msg}_SigChanged_Ind = STD_ON;
        
    }}\n\n\t""".format(file=filename, ClusterName=Cluster, Msg=MessageName, Variable=Var, Sig=SignalName)
    elif E2EFlag == 2:
        text = """if({Variable}_Old != {Variable})
	{{
		Rte_Write_{file}_Swc_{ClusterName}_{Msg}_{Sig}({Variable});
		{Variable}_Old = {Variable};
	}}\n\n\t""".format(file = filename, ClusterName=Cluster, Msg=MessageName, Variable=Var, Sig=SignalName)
    else:
        text = """Rte_Write_{file}_Swc_{ClusterName}_{Msg}_{Sig}({Variable});\n\n\t""".format(file=filename, ClusterName=Cluster, Msg=MessageName, Variable=Var, Sig=SignalName)

    return text


def Tx_Function(filename, Cluster, MessageName, Old_VarableSet, Txset, E2EFlag):
    if E2EFlag == 1:
        text = """static uint8 ubS_F_RC_E2E_{ClusterName}_{Msg}_SigChanged_Ind = STD_OFF;
static MsgGr_E2E_{ClusterName}_{Msg}  stS_D_RC_E2E_{ClusterName}_{Msg};        
static void s_{file}_{Msg}_Tx(void)
{{
    {TxVar}
    
    /**** E2E Message Tx *****/
    if(ubS_F_RC_E2E_{ClusterName}_{Msg}_SigChanged_Ind == STD_ON)
    {{
        ubS_F_RC_E2E_{ClusterName}_{Msg}_SigChanged_Ind = STD_OFF;
        Rte_Write_{file}_Swc_Gr_MsgGr_E2E_{ClusterName}_{Msg}_MsgGr_E2E_{ClusterName}_{Msg}(&stS_D_RC_E2E_{ClusterName}_{Msg});
    }}
}}\n\n""".format(file=filename, ClusterName=Cluster, Msg=MessageName, Old_Var=Old_VarableSet, TxVar=Txset)
    elif E2EFlag == 2:
        text = """{Old_Var}
static void s_{file}_{Msg}_Tx(void)
{{
    {TxVar}   
}}\n\n""".format(file = filename, Msg=MessageName, Old_Var=Old_VarableSet, TxVar=Txset)
    else:
        text = """static void s_{file}_{Msg}_Tx(void)
{{
   {TxVar}   
}}\n\n""".format(file=filename, Msg=MessageName, Old_Var=Old_VarableSet, TxVar=Txset)
    return text

def Rx_FunctionSet(filename, MessageName):
    text = "s_{file}_{Msg}_Rx();\n\t".format(file = filename, Msg=MessageName)
    return text

def RTE_Rx_Function(filename, RxFunctionSet):
    text = """/*******************************************************************************
**						   initial function 								 **
*******************************************************************************/
void {file}_Init(void)
{{
	/** it have to RTE write for 'E2E Periodic(without Event)' Type message to avoid alive Counter error when MCU intial **/

}}

FUNC (void, {file}_Swc_CODE) RE_{file}Rx(void)
{{
    {RxFunction}
}}\n""".format(file=filename, RxFunction=RxFunctionSet)
    return text

def Tx_FunctionSet(filename, MessageName):
    text = "s_{file}_{Msg}_Tx();\n\t".format(file = filename, Msg=MessageName)
    return text

def RTE_Tx_Function(filename, TxFunctionSet):
    text = """FUNC (void, {file}_Swc_CODE) RE_{file}Tx(void)
{{
    /*** 'P'(without event) type message have to transmite every cycle to avoid alive count error **/
	if(ubS_C_{file}_200msCnt < {file}_200MS)
	{{
		ubS_C_{file}_200msCnt ++;
	}}
	else
	{{
		ubS_C_{file}_200msCnt = 0U;

	}}
	
	if(ubS_C_{file}_100msCnt < {file}_100MS)
	{{
        ubS_C_{file}_100msCnt ++;
	}}
	else
	{{
        ubS_C_{file}_100msCnt = 0U;
	}}	
	
	if(ubS_C_{file}_20msCnt < {file}_20MS)
	{{
        ubS_C_{file}_20msCnt ++;
	}}
	else
	{{
        ubS_C_{file}_20msCnt = 0U;
	}}	
	
    {TxFunction}
}}\n""".format(file=filename, TxFunction=TxFunctionSet)
    return text

def Tx_MonSig(Message, Signal, flag, cnt):
    if flag == 1:
     text = """\t}}
    else if(RxTestCase == {num})
    {{
        /*** {msg} **/
        {sig}\n""".format(msg=Message, sig=Signal, num=cnt)
    else:
        text = """\t\t/*** {msg} **/
        {sig}\n""".format(msg=Message, sig=Signal)
    return text

def JobFinished(NvM_list):
    text ="""FUNC (void , NvMSwc_CODE) NvM_{NvM}_Jobfinished(
	VAR(uint8, AUTOMATIC) ServiceId,
	VAR(NvM_RequestResultType, AUTOMATIC) JobResult)
{{
	stS_D_NvMchnage[enum_{NvM}] = STD_OFF;
	stS_D_JobFinished[enum_{NvM}] = JobResult;
}}\n""".format(NvM = NvM_list)
    return text

def JobFinished_Mirr(NvM_list):
    text ="""FUNC (void , NvMSwc_CODE) NvM_{NvM}_Jobfinished_Mirr(
	VAR(uint8, AUTOMATIC) ServiceId,
	VAR(NvM_RequestResultType, AUTOMATIC) JobResult)
{{
	stS_D_NvMchnage[enum_{NvM}_MIRR] = STD_OFF;
	stS_D_JobFinished[enum_{NvM}_MIRR] = JobResult;
}}\n""".format(NvM = NvM_list)
    return text

def Init_Header():
    text ="""\n/*******************************************************************************
**                      Function Definitions                                  **
*******************************************************************************/
/*******************************************************************************
**                         initial function                                  **
*******************************************************************************/
/********************************************************************************************************/
/** Description 		NvM Parameter initalize							                               **/
/** Input parameter   : size        - variable for calculation of size                                 **/ 
/**                     *OldValue	- NvM Parameter value after Writiing  				               **/
/** 					*CurValue   - NvM real parameter												**/
/** 					*NvMValue   - Parameter which was stored in the past                           **/
/** Output parameter : 																					**/
/********************************************************************************************************/
static void Init_NvM_Variable(uint8 size, uint8 *OldValue, uint8 *CurValue, uint8 *NvMValue)
{
	uint8 i;

	if(size > 1U)
	{
		for(i = 0; i < size; i++)
	    {
			CurValue[i] = NvMValue[i];
			OldValue[i] = NvMValue[i];
		}
	}
	else
	{
		*CurValue = *NvMValue;
		*OldValue = *NvMValue;
	}
}

void Init_Nvm(void)
{
	uint8 Loop;
	
	Init_NvM_Variable(sizeof(NvMWriteCheck), &NvMWriteCheck_old[0], &NvMWriteCheck[0], &Dem_WriteCheck[0]); // It must be initial at fisrt in order to choose initial value of other MvM
\n"""
    return text

def Init_Nvm(NvM_list, InitV, MaxV, MinV):
    text ="""	if(NvMWriteCheck[enum_{NvM}] == 0xa5)
	{{
		if(Dem_{NvM} == Dem_{NvM}_Mirr)
		{{
			Init_NvM_Variable(sizeof({NvM}), &{NvM}_old, &{NvM}, &Dem_{NvM});

			if({NvM} < {Min}) // under Min value
			{{
				{NvM} = {Min};
				{NvM}_IVD = TRUE;
			}}
			else if({NvM} > {Max}) // Over Max value
			{{
				{NvM} = {Max};
				{NvM}_IVD = TRUE;
			}}
			else{{
				{NvM}_IVD = FALSE;
			}}
		}}
		else
		{{
			{NvM} = {Init};
			{NvM}_old = {Init};
			{NvM}_IVD = TRUE;
		}}
	}}
	else
	{{
		{NvM} = {Init};
		{NvM}_old = {Init};
	}}\n""".format(NvM = NvM_list , Init = InitV, Max=MaxV, Min=MinV)

    return text