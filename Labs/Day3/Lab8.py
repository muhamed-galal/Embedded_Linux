import os
os.remove("LCD_Interface.c")
os.remove("LCD_Private.h")
os.remove("LCD_Program.c")
os.remove("LCD_Reg.h")


ChooseComponents=input("Enter The SW Components:    ")
f1 = open((ChooseComponents) + "_Private.h" , 'x')
f2 = open((ChooseComponents) + "_Reg.h" , 'x')
f3 = open((ChooseComponents) + "_Program.c" , 'x')
f4 = open((ChooseComponents) + "_Interface.h" , 'x')

f1 = open((ChooseComponents) + "_Private.h", 'w')
f1.write("#ifndef\n#define "+ChooseComponents+"_Private.h""\n\n\n\n\n#endif")
f1 = open((ChooseComponents) + "_Private.h", 'r')
print(f1.read())
f1.close()

f2 = open((ChooseComponents) + "_Reg.h", 'w')
f2.write("#ifndef\n#define "+ChooseComponents+"_Reg.h""\n\n\n\n\n#endif")
f2 = open((ChooseComponents) + "_Reg.h", 'r')
print(f2.read())
f2.close()


f3 = open((ChooseComponents) + "_Program.c", 'w')
f3.write("#ifndef\n#define "+ChooseComponents+"_Program.c""\n\n\n\n\n#endif")
f3 = open((ChooseComponents) + "_Program.c", 'r')
print(f3.read())
f3.close()

f4 = open((ChooseComponents) + "_Interface.h", 'w')
f4.write("#ifndef\n#define "+ChooseComponents+"_Interface.c""\n\n\n\n\n#endif")
f4 = open((ChooseComponents) + "_Interface.h", 'r')
print(f4.read())
f4.close()