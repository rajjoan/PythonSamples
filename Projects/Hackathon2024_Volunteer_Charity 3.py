import time

print("__        __   _                          _ ")
print("\ \      / /__| | ___ ___  _ __ ___   ___| |")
print(" \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |")
print("  \ V  V /  __/ | (_| (_) | | | | | |  __/_|")
print("   \_/\_/ \___|_|\___\___/|_| |_| |_|\___(_)")
time.sleep(0.5)
print("-----------------------------")
goal = 1000
time.sleep(0.5)
print("Goal to reach: $" + str(goal) + "!")
time.sleep(0.5)
donors = {}
while True:
    print("-----------------------------")
    time.sleep(0.5)
    print("----Donation Tracker Menu----")
    print("1. Add a new donor")
    print("2. Add a donation")
    print("3. Display donations")
    print("4. Exit")
    time.sleep(0.5)
    print("-----------------------------")
    time.sleep(0.5)

    user_choice = input("Please enter what you would like to do (1-4): ")
    print("-----------------------------")

    if user_choice == '1':
        name = input("Enter the donor's name: ")
        if name in donors:
            print(name, "is already in the system")
            time.sleep(1)
        else:
            donors[name] = []
            print(name, "has been added as a donor")
            time.sleep(1)

    elif user_choice == '2':
        donation_name = input("Enter donor's name: ")
        if donation_name in donors:
            donation_amount_input = input("Enter the donation amount: ")
            if donation_amount_input == '0':
                print("Invalid amount. Please enter a valid number")
            elif donation_amount_input.replace(".", "", 1).isdigit():
                donation_amount = float(donation_amount_input)
                donors[donation_name].append(donation_amount)
                print("Added donation of $"+ str(donation_amount), "from", donation_name)
                time.sleep(0.5)
                

                total_donations = 0
                for donor in donors:
                    total_donations = total_donations + sum(donors[donor])

                if total_donations < goal:
                    print("Thank you for your genorosity!")
                time.sleep(1)

                if total_donations >= goal:
                    print(" _____ _                 _     __   __          _ ")
                    print("|_   _| |__   __ _ _ __ | | __ \ \ / /__  _   _| |")
                    print("  | | | '_ \ / _` | '_ \| |/ /  \ V / _ \| | | | |")
                    print("  | | | | | | (_| | | | |   <    | | (_) | |_| |_|")
                    print("  |_| |_| |_|\__,_|_| |_|_|\_\   |_|\___/ \__,_(_)")
                    print("Our goal of $1000 has been reached!")
                    break
            else:
                print("Invalid amount. Please enter a valid number")
                time.sleep(1)
        else:
            print(donation_name, "is not in the system. Please add them as a donor first.")
            time.sleep(1)

    elif user_choice == '3':
        print("Donations Summary:")
        total_donations = 0
        for donor in donors:
            donor_total = sum(donors[donor])
            total_donations = total_donations + donor_total
            print(donor + ": $" + str(round(donor_total, 2))+ ' from' , str(len(donors[donor]))+ " donation(s)")
            time.sleep(1)
        
        print("-----------------------------")
        print("Total Donations: $" + str(round(total_donations,2)))
        time.sleep(0.5)
        print("We need $" +str(goal-round(total_donations,2)) + " to reach our goal!")
        print("-----------------------------")
        print()

    elif user_choice == '4':
        print("Exiting the Donoation Tracker. Bye!")
        break
    else: 
        print("Invalid entry")
        print("Please enter a number 1-4 based on the Donation Tracker Menu")
        time.sleep(0.5)
    

