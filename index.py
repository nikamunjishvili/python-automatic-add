fruits = {}

while True:
    if len(fruits) == 0:
        name = input("enter fruit name: ")
        kg = int(input("input fruits weight: "))
        fruits[name] = int(kg)
    else:
        print("this is your cart: ", fruits)
        ques = input("Add More? yes/no: ")
        if ques == "yes":
            name = input("enter fruit name: ")
            kg = int(input("input fruits weight: "))
            fruits[name] = int(kg)
        else:
            break

print("this is your cart: ", fruits)
