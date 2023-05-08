#Dict for Cards_Numbers
Cards_Numbers={"Card_1":"1111",
               "Card_2":"2222",
               "Card_3":"3333",
               "Card_4":"3333",
			   }

#Dict for Cards_Pins
Cards_Pins={"Pin_1":"1234",
            "Pin_2":"2222",
            "Pin_3":"3333",
            "Pin_4":"3333",
			}

#Dict for Available_Processes
Available_Processes={"Deposite":"1",
                     "Withdraw":"2",
                     "Balance":"3",
                     "Exit":"4",
					}

#List for User_1 with Name and Balance 
User_1=["Mohamed",4000]

#List for User_2 with Name and Balance
User_2=["Galal",1000]

print("Gelo ATM")
Input_Card_Num=input("Enter your card number: ")

CashRange=range(0,10000,50)
	#Checking Card_Number_Case of User_1
if Input_Card_Num == Cards_Numbers["Card_1"] :
	Input_Pin=input("Enter your pin: ")

#Three tries if Input_Pin is not correct using range
	if Input_Pin!=Cards_Pins["Pin_1"] :
		x=range(0,2)
		for n in x:
			print("Wrong pin try again")
			Input_Pin=input("Enter your pin")
			if Input_Pin==Cards_Pins["Pin_1"] :
				break
					
		#In case of correct Input_Pin	
	while True:		
		if Input_Pin==Cards_Pins["Pin_1"] :
			print("Welcome: " + User_1[0])
			#Print the available processes and let the user chose
			print(Available_Processes)
			Chosen_Process=input("Chose your process: ")
			#In case of Deposite
			if Chosen_Process==Available_Processes["Deposite"]:
				Deposite_Value=input("Enter your deposite value : ")
				print("Process done succssesfully")
				if input('you want to another option (yes/no): ') == 'yes':
					continue
				else:
					print('Thanks for using Gelo Bank')
					break
			#In case of Withdraw	
			elif Chosen_Process==Available_Processes["Withdraw"]:
				Withdraw_Value=int(input("Enter your Withdraw value in muiltiples of 50: "))
				if Withdraw_Value<User_1[1] :
					if Withdraw_Value in CashRange:
						User_1[1]-= Withdraw_Value
						print("Processes done succssesfully")
						print("Your new balance %d "%(User_1[1]))
					else :
						print("you entered an invalid value")
					if input('you want to another option (yes/no): ') == 'yes':
						continue
					else:
						print('Thansk for using Gelo Bank')
						break
				else:
					print("No enough balance")
					if input('you want to another option (yes/no): ') == 'yes':
						continue
					else:
						print('Thanks for using Gelo Bank')
						break
			#Incase of Balance		
			elif Chosen_Process==Available_Processes["Balance"]:
				print("Your balance = %d"%(User_1[1]))
				if input('you want to another option (yes/no): ') == 'yes':
					continue
				else:
					print('Thanks for using Gelo Bank')
					break
			#Incase of Exit	
			elif Chosen_Process==Available_Processes["Exit"]:
				print("Thank you")
				break
			#Incase of wrong entry 	
			else:
				print("Wrong Entry")
				if input('you want to another option (yes/no): ') == 'yes':
					continue
				else:
					print('Thanks for using Gelo Bank')
					break
				
				
		else:
			print("Wrong pin try again")
				
				
	#Checking Card_Number_Case of User_1
elif Input_Card_Num== Cards_Numbers["Card_2"] :
		Input_Pin=input("Enter your pin: ")
		
		#Three tries if Input_Pin is not correct using range
		if Input_Pin!=Cards_Pins["Pin_2"] :
			x=range(0,2,1)
			for n in x:
				print("Wrong pin try again")
				Input_Pin=input("Enter your pin")
				if Input_Pin==Cards_Pins["Pin_2"] :
					break
					
		#In case of correct Input_Pin			
		if Input_Pin==Cards_Pins["Pin_2"] :
			print("Welcome: "+User_2[0])
			#Print the available processes and let the user chose
			print(Available_Processes)
			Chosen_Process=input("Chose your process: ")
			#Incase of Deposite
			if Chosen_Process==Available_Processes["Deposite"]:
				Deposite_Value=input("Enter your deposite value: ")
				print("Processes done succssesfully")
			#Incase of Withdraw	
			elif Chosen_Process==Available_Processes["Withdraw"]:
				Withdraw_Value=int(input("Enter your Withdraw value: "))
				if Withdraw_Value<User_2[1] :
					User_2[1]-=Withdraw_Value
					print("Processes done succssesfully")
					print("Your new balance %d"%(User_1[2]))
				else:
					print("No enough balance")
			#Incase of Balance		
			elif Chosen_Process==Available_Processes["Balance"]:
				print("Your balance=%d"%(User_2[1]))
			#Incase of Exit	
			elif Chosen_Process==Available_Processes["Exit"]:
				print("Thank you")
			#Incase of wrong entry 	
			else:
				print("Wrong Entry")
				
		else:
			print("Wrong pin try again")
				
	#Incase of Wrong Card_Number		
else :
		print("No such card number!")	
		
	#print(type(Cards_Numbers))
	#print(Cards_Numbers["Card_1"])