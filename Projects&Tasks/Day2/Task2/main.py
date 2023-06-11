import Calc
import os
print("****************************************************************\n","            Scientific & Logical Calculator")
Options='''
             | Arithmatic |    Logical   |
             |Add:  +     |and: &        |
             |Sub:  -     |or:  |        |
             |Mul:  *     |xor: ^        |
             |Div:  /     |ShiftRight:>> |
             |Power:**    |ShiftLeft:<<  |
            '''
print(Options)
while True:
   In1,Op,In2=input("Please enter the Numbers and The Operator\n").split(" ",3)
   float(In1)
   float(In2)
   result =float(Calc.Calc(In1,In2,Op))
   print('{} {} {} = {}'.format(In1,Op,In2,result))
   CheckEnd=input("Do you Want Another Operation (yes/No):  ")
   if CheckEnd == 'yes':
      os.system('cls')
      continue
   elif CheckEnd == 'no':
      os.system('cls')
      print("               Calculator Power OFF\n*****************************************************************") 
      break
   