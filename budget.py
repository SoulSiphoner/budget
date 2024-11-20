money = float(input("How much money do you have?\n"))
days = float(input("How many days until next pay?\n"))

print("You can spend " + str(round(money / days, 2)) + " a day.")

input()
