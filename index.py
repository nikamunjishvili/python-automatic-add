fruits = {}


def end_questions():
    ques = input("Add More? yes/no: ")
    ques = ques.lower()
    if ques == "yes":
        return True
    else:
        return False


def main_question():
    helper = {}
    name = input("enter fruit name: ")
    kg = int(input("input fruits weight: "))
    price = input("Enter fruit price: ")
    basket = {}
    helper["kg"] = kg
    helper["price"] = helper
    fruits[name] = helper

    return fruits


while True:
    if len(fruits) == 0:
        main_question()
    else:
        print("this is your cart: ", fruits)

        if end_questions == True:
            main_question()
        else:
            break
result = 0

for key, value in fruits.items():
    kg = int(value['kg'])
    price = int(value['price'])
    result += kg*price
    print(key, "your amount", kg*price, "GEL")


print("you have to pay: ", result, "GEL")
