# TIP CALCULATOR


def count_people(p):
    return 1 if p <= 0 else p


def calc_tip(t):
    return 0 if t <= 0 else t


def calc_pay_per_person(total_bill, total_people, percent_tip):
    tip = 1 + (percent_tip/100)
    person_pay = (total_bill/total_people) * tip
    return person_pay


def calculate_bill():
    print("WELCOME TO TIP CALCULATOR!!!")
    bill = float(input("What is the amount of bill? $"))

    people = count_people(int(input("How many people will split the bill? ")))

    tip_percent = calc_tip(float(input("What percentage tip would you like to give? ")))

    Pay_per_person = calc_pay_per_person(bill,people, tip_percent)

    if people <=1:
        print(f"You have to pay ${round(Pay_per_person, 2)}.")
    else:
        print(f"Each person should pay ${round(Pay_per_person, 2)}.")


calculate_bill()