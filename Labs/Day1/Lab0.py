'''
print("Name: Mohamed Galal")                #printing basic informations
print("Age: 26 years")
print("Alexandria, Egypt")
print("Faculty of Engineering, 2020")

'''

'''
a,b,c,d=1,2,3,"galal"      
print("{}: first num is {} and second num is {}".format(d,a,b))                                        #getting multiple data with format {}
print("{first}: first num is {second} and second num is {third}".format(first=d,second=a,third=b))     #getting multiple data with format {}
print(d,'first num is',a,'and second num is',b)                                                        #printing data next to each other without %
print((d) + ':first number ' + str(a) + ' second number is ' + str(b))                                 #concatenation

'''

'''
Myname=input("Hello enter your name:\n")                                 #entering multiple data
Age=int(input("Please enter your age:\n"))
Faculty=input("Please enter your Univercity:\n")
print("Output:")
print('my name is',Myname,'\nMy age is ',Age,'\nMy university is ',Faculty)
#print("%s %d %s="%(Myname,Age,Faculty))
#print ("Name: " + (Myname))
#print ("Age: %d" %(Age))
#print ("Univercity: " + (Faculty))

'''

'''
x = int("100")
print (x)
x = str (100)
print (x)
x = float (100)
print (x)
# printing asci value 
x=ord('A') 
print (x)
'''

'''

a,b,c = input("enter your name\n").split(" ",3)
print(a,b,c)

'''




'''
num1 = int(input(" please enter the first num: "))
num2 = int(input("please enter the second number: "))

print("a & b",num1 & num2)
print("a | b",num1 | num2)
print("a ^ b",num1 ^ num2)
print("a > b",num1>num2)
print("a < b",num1<num2)
print("a = b",num1==num2)
print("a >> b", num1>>num2)
'''



my_list = ['Alaa', 1, 5.4, 'Elnaggar', 0.7]
x = "ITI"
Y = "67572" 

#my_list.insert(0, x) # insert x at index 0
#print(my_list)

#my_list.remove(x) # remove first occurance of x from list
#print(my_list)

#my_list.append(x) # append x to end of list 
#print(my_list)
#['Alaa', 1, 5.4, 'Elnaggar', 0.7, 'ITI']

#my_list.extend(Y) # append all elements of Y to list
#print(my_list)
#['Alaa', 1, 5.4, 'Elnaggar', 0.7, 'ITI', '6', '7', '5', '7', '2']

#my_list.pop(2) # pop element at index i (defaults to end of list)
#print(my_list)