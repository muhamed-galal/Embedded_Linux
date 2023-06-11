
while True:
    print("Hello in My Python School")
    Choose=input('Choose the Function to Display:\n1-capitalize()\n2-casefold()\n')
    if Choose == '1':
        a='''
    Definition and Usage
        The capitalize() method returns a string where the first character is upper case, and the rest is lower case.

    Syntax
        string.capitalize()

    Example:
        Upper case the first letter in this sentence:

        txt = "hello, and welcome to my world."

        x = txt.capitalize()

        print (x)") 
        '''
        print(a)
        choosecontinue=input('Do you want to continue (yes/no): ')
        if choosecontinue == 'yes':
            continue
        else:
            break

    elif Choose == '2':
        b='''
        The casefold() method returns a string where all the characters are lower case.
        This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, 
        and will find more matches when comparing two strings and both are converted using the casefold() method.
            
        Syntax
            string.casefold()

        Example:
            Make the string lower case:

            txt = "Hello, And Welcome To My World!"

            x = txt.casefold()

            print(x)
            '''
        print(b)
        choosecontinue=input('Do you want to continue (yes/no): ')
        if choosecontinue == 'yes':
            continue
        else:
            break

