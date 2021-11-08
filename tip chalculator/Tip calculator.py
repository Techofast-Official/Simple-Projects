def design(fun):
    def another():
        print("*****************------------")
        fun()
        print("*****************------------")

    return another


@design
def fun():
    print("Welcome to the tip calculator")


fun()


def fun2():
    total_bil = float(input("What was the total bill? $ "))
    percentage1 = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
    people = int(input("How many people to split the bill?"))
    final_percentage = total_bil * (percentage1 / 100)
    bill_with_percentage = total_bil + final_percentage
    result= bill_with_percentage/people
    return f'each person should pay: ${round(result,2)}'




print(fun2())
