
def SetBit(reg,bit):
    reg|=(1<<bit)
    return reg
def ClrBit(reg,bit):
    reg &=~(1<<bit)
    return reg
def TogBit(reg,bit):
    reg ^=(1<<bit)
    return reg
