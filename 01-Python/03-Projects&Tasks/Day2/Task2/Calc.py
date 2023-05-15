def Calc(In1,In2,Op):
#In1,In2,Op=input("Please enter the Numbers and The Operator\n").split(" ",3)
#print(In1,In2,Op)
 Result =0
 if Op == '+':
    Result= int(In1)+int(In2)
    return Result
 elif Op == '-':
   Result=int(In1)-int(In2)
   return Result
 elif Op == '*':
   Result=int(In1)*int(In2)
   return Result
 elif Op == '/':
   Result=int(In1)/int(In2)
   return Result
 elif Op == '%':
   Result=int(In1)%int(In2)
   return Result
 elif Op == '**':
    Result=int(In1)**int(In2)
    return Result
 elif Op == '|':
   Result=int(In1)|int(In2)
   return Result
 elif Op== '&':
   Result=int(In1)&int(In2)
   return Result
 elif Op == '^':
   Result=int(In1)^int(In2)
   return Result
 elif Op =='<<':
   Result=int(In1)<<int(In2)
   return Result
 elif Op =='>>':
   Result=int(In1)>>int(In2)
   return Result
 elif Op == '//':
   Result=int(In1)//int(In2)
   return Result
 

   
 