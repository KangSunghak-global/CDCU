import datetime

def variable(size, signalName, value):
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

    variable_dec = "extern {type} {Name};\n".format(type=size, Name=signalName)
    variable_def = "{type} {Name}={init};\n".format(type=size, Name=signalName, init=value)

    return variable_dec, variable_def

def Start_State(CANName):
    defineState = """/** ================================**/
/** Company : Kyungshin              **/
/** Project Name : CDCU             **/
/** Create Date :  {0}-{1}-{2}      **/
/** Author      : KangSH            **/
/** ================================**/
#include "App_Variable.h"
#include "Rte_{channel}Swc.h"\n\n""".format(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day,channel=CANName)

    return defineState

# { or } must be twice for charactor
def Indicate_Function(filename, MessageName, cycle):
    if cycle > 0:
        text = """FUNC (void, {file}Swc_CODE)Rt_{Message}_Ind(void)
{{
     ubS_F_{Message}_Ind = STD_ON;
     Rxmissing_{Message} = STD_OFF;
}}
 
FUNC (void, {file}Swc_CODE)RTout_{Message}_Ind(void)
{{
     Rxmissing_{Message} = STD_ON;
}}\n\n""".format(file = filename, Message = MessageName)

    else:
        text = """FUNC (void, {file}Swc_CODE)Rt_{Message}_Ind(void)
{{
    ubS_F_{Message}_Ind = STD_ON;
}}\n\n""".format(file = filename, Message = MessageName)

    return text

def Rx_Signal(Var,filename,MessageName,SignalName, ECU):
    text = "{Variable} = Rte_DRead_{File}Swc_{File}_{Sender}_{Msg}_{Sig}();\n\t\t".format(Variable=Var,File = filename, Msg=MessageName, Sig=SignalName, Sender = ECU)
    return text

def Rx_Function(filename, MessageName, set):
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

def Tx_Signal(Var,filename,MessageName,SignalName):
    text = """if({Variable}_Old != {Variable})
	{{
		Rte_Write_{file}wc_{file}_CDCU_{Msg}_{Sig}({Variable});
		{Variable}_Old = {Variable};
	}}\n\n\t""".format(file = filename, Msg=MessageName, Variable=Var, Sig=SignalName)
    return text


def Tx_Function(filename, MessageName, Old_VarableSet, Txset):
    text = """{Old_Var}
static void s_{file}_{Msg}_Tx(void)
{{
    {TxVar}
}}\n\n""".format(file = filename, Msg=MessageName, Old_Var=Old_VarableSet, TxVar=Txset)

    return text

def Rx_FunctionSet(filename, MessageName):
    text = "s_{file}_{Msg}_Rx();\n\t".format(file = filename, Msg=MessageName)
    return text

def RTE_Rx_Function(filename, RxFunctionSet):
    text = """FUNC (void, {file}Swc_CODE) RTE_{file}Rx(void)
{{
    {RxFunction}
}}\n""".format(file=filename, RxFunction=RxFunctionSet)
    return text

def Tx_FunctionSet(filename, MessageName):
    text = "s_{file}_{Msg}_Tx();\n\t".format(file = filename, Msg=MessageName)
    return text

def RTE_Tx_Function(filename, TxFunctionSet):
    text = """FUNC (void, {file}Swc_CODE) RTE_{file}Tx(void)
{{
    {TxFunction}
}}\n""".format(file=filename, TxFunction=TxFunctionSet)
    return text