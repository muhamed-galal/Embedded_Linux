import Arrow_Module
import os
import time

ChooseOp=input("Manual Rotation or Automatic Rotation (M/A):   ")
if ChooseOp == 'M':
   print("1 For Left   3 For Right    \n5 For Top    2 For Down") 
     
while True:
 if ChooseOp == 'M':  
   Choose=int(input())
   if Choose == 1:
      os.system("cls")
      Arrow_Module.PrintLeftArrow()
   elif Choose == 5:
      os.system("cls")
      Arrow_Module.PrintTopArrow()  
   elif Choose == 3:
      os.system("cls")
      Arrow_Module.PrintRightArrow()
   elif Choose == 2:
      os.system("cls")
      Arrow_Module.PrintDownArrow()

 elif ChooseOp == 'A':
      os.system("cls")
      Arrow_Module.PrintLeftArrow()
      time.sleep(0.5)
      os.system("cls")
      Arrow_Module.PrintTopArrow()
      time.sleep(0.5)
      os.system("cls")
      Arrow_Module.PrintRightArrow()
      time.sleep(0.5)
      os.system("cls")
      Arrow_Module.PrintDownArrow()
      time.sleep(0.5)

