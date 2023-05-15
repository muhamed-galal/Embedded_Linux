print('Welcome to Gelo-Grocery')
price=0
VegTuple=('Potato','Carrot','Tomato','Onion','Garlic','Apple','Banana','Orange','Mango','Cherry')

print('Today\'s Vegetables List:')
#print(VegTuple)
for n in VegTuple:
    print(n)
ProceedShopping=input('Do you want to purchase some items (yes/no): ')
if ProceedShopping == 'yes' :
 while True:   
    Add_Item=input("Add an Item: ")
    if Add_Item in VegTuple:
        if Add_Item == 'Potato':
            PotatoPrice=1.5 
            print('Potato Price: ',PotatoPrice)
            Add_Quantity=int(input('Add Quantity: '))
            price += PotatoPrice*Add_Quantity

        elif Add_Item == 'Tomato':
            TomatoPrice=2.5
            print('Tomato Price: ',TomatoPrice)                
            Add_Quantity=int(input('Add Quantity: '))
            price += TomatoPrice*Add_Quantity

        elif Add_Item == 'Carrot':
            CarrotPrice=2.6
            print('Carrot Price: ',CarrotPrice)
            Add_Quantity=int(input('Add Quantity: '))
            price += CarrotPrice*Add_Quantity

        elif Add_Item == 'Garlic':
            GarlicPrice=3.2
            print('Garlic Price: ',GarlicPrice)
            Add_Quantity=int(input('Add Quantity: '))
            price += GarlicPrice*Add_Quantity
        elif Add_Item == 'Onion':
            OnionPrice= 5.6
            print('Onion Price: ',OnionPrice)
            Add_Quantity=int(input('Add Quantity: '))
            price += OnionPrice*Add_Quantity

        CheckContinue=input("Do you want add another items (yes/no): ")
        if CheckContinue == 'no':
           print('you total value :%d $\nThanks for Visting us' %(price))
           break
    else :
       item_wrong=input("This item is not found Do you want to purchase another item (yes/no): ")
       if item_wrong == 'yes':
            continue
       else :
            print('Thanks for Visting us') 
            break   
else :
    print("Thanks for Visting us Hope to see you soon")

    

