""" def input(withdraw):
    while True:
        if withdraw < 500:
            user_input = int(input("Amount of withdraw"))
            print("withdraw")
            balance = balance - withdraw
        if withdraw > 500:
            print("Insufficient funds")
        else:
            exit """

""" def input(withdraw):
    while balance == 500:
        input("How much money is withdraw")
        if withdraw < 500:
            print("withdraw")
            balance = 500 - withdraw
        if withdraw > 500:
            print("Insufficient funds")
        else:
            exit """

while True:
    withdraw = input("How much withdraw")
    if int(withdraw) < 500:
        balance = 500 - int(withdraw)
        print("withdraw completed")
    if int(withdraw) > 500:
        print("Insufficient funds")
    else:
        break