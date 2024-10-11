print ("Welcome to the simple Vending Machine") #start message

#simple data arrays
itemName = ["Cola", "Dr.Kelp", "Ice Tea", "Coffee"]
itemCode = ["10","11", "12","13"]
itemPrice = ["£0.99","£1.25","£1.10","£1.20"]

while True:
    itemSelected = input ("Enter Code for an Item to View Price or Purchase Item:") #Item selected by the the user
    if itemSelected in itemCode:
        break
    else:
        print ("Please Enter a Valid Item Code!")
index = itemCode.index(itemSelected)
print ("You have selected", itemName[index], "which costs", itemPrice[index])
print ("Please insert ", itemPrice[index])
print ("Thank you for using the Simple Vending Machine, Enjoyy your drink!")
