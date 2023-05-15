
print('Car System')
CarDict={'Year': '2020',
        'Model': 'F30',
        'Motor': "230HP",
        'Torque': '450NM',
        'Wheelbase': '3.2'
         }

while True:
    print('The System Options is: ')
    SysOptions=int(input('1-Display Dictionary\n2-Display Keys\n3-Display Values\n4-Add Key\n5-Update Value\n6-Remove Key\n7-Clear the Dictionary:\nEnter the Option Number: '))
    Options_Range=range(1,8,1)
    if SysOptions in Options_Range:
        if SysOptions == 1:
                print(CarDict)
                CheckContinue=input('you want to choose another option (yes/no): ')
                if CheckContinue == 'yes':
                    continue
                else:
                    print("Thanks For using Our Car System")
                    break
        elif SysOptions == 2:
                print(CarDict.keys())
                CheckContinue=input('you want to choose another option (yes/no): ')
                if CheckContinue == 'yes':
                    continue
                else:
                    print("Thanks For using Our Car System")
                    break
        elif SysOptions == 3:
                print(CarDict.values())
                CheckContinue=input('you want to choose another option (yes/no): ')
                if CheckContinue == 'yes':
                    continue
                else:
                    print("Thanks For using Our Car System")
                    break
        elif SysOptions == 4:
                UpdatedKey=input("Enter The Key to be Added: ")
                UpdatedValue=input('Enter the new value of the key: ')
                CarDict[UpdatedKey]= UpdatedValue
                CheckContinue=input('you want to choose another option (yes/no): ')
                if CheckContinue == 'yes':
                    continue
                else:
                    print("Thanks For using Our Car System")
                    break
        elif SysOptions == 5:
            UpdatedKey=input("Enter The Key to be Updated: ")
            UpdatedValue=input('Enter the new value of the key: ')
            CarDict[UpdatedKey]= UpdatedValue
            CheckContinue=input('you want to choose another option (yes/no): ')
            if CheckContinue == 'yes':
                continue
            else:
                print("Thanks For using Our Car System")
                break
        elif SysOptions == 6:
            UpdatedKey=input("Enter The Key to be Deleted: ")
            CarDict.pop(UpdatedKey)
            CheckContinue=input('you want to choose another option (yes/no): ')
            if CheckContinue == 'yes':
                continue
            else:
                print("Thanks For using Our Car System")
                break
        elif SysOptions == 7:
            CheckClear=input('The Dictionary will be remover are you sure (yes/no): ')
            if CheckClear == 'yes':
                CarDict.clear()
            CheckContinue=input('you want to choose another option (yes/no): ')
            if CheckContinue == 'yes':
                continue
            else:
                print("Thanks For using Our Car System")
                break
    else :
         print('The option you choose is not valid')
         CheckContinue=input('you want to choose another option (yes/no): ')
         if CheckContinue == 'yes':
            continue
         else:
            print("Thanks For using Our Car System")
            break
