amountPaid = int(input("Enter the amount paid: "))
amountToSave = int(input("Enter the amount you would like to save: "))
#This program is assuming you get paid on a bi-weekly basis
payFrequency = 2

def main():
    global amountPaid, amountToSave, payFrequency
    canUse = amountPaid - amountToSave
    weekly = canUse/2
    daily = weekly/7
    print("You can use $" + str(round(canUse, 2)) + " in total")
    print("You can use $" + str(round(weekly, 2)) + " every week")
    print("Every day you can spend up to $" + str(round(daily, 2)) + " in order to save $" + str(round(amountToSave, 2)))

main()