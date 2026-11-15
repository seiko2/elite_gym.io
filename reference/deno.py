#-----------------OPTICS FITNESS GYM KAMPALA----------------- 
daily_members = 0
monthly_members = 0
quartery_members = 0
annual_members = 0
weight = 0
height = 0
end = 0
revenue = 0
codes = ["CODE 0","CODE 1","CODE 1", "CODE 3", "CODE 4"]
import time

while True:    
    name = input("Enter your name: ").strip().upper()
    if name == "":
        print("Name cannot be empty. Please try again.")
        continue
    try:
        age = int(input("Enter your age: ").strip())
    except ValueError:
        print("Age is a number, age is required")
        continue

    print("===== OPTICS FITNESS GYM PLAN's =====")
    print("+--------+-------------+------------+")
    print(f"| {'CODE':<6} | {'MEMBERSHIP':<11} | {'FEE (UGX)':<10} |")
    print("+--------+-------------+------------+")
    print(f"| {'CODE 1':<6} | {'Daily':<11} | {'10000':<10} |")
    print(f"| {'CODE 2':<6} | {'Monthly':<11} | {'120000':<10} |")
    print(f"| {'CODE 3':<6} | {'Quarterly':<11} | {'300000':<10} |")
    print(f"| {'CODE 4':<6} | {'Annual':<11} | {'1000000':<10} |")
    print(f"| {'CODE 0':<6} | {'End day':<11}|")
    print("+--------+-------------+------------+")

    code = input("Enter membership code ie (code 1): ").strip().upper()
    if code == "CODE 1":
        membership = "Daily"
        fee = 10000
    elif code == "CODE 2":
        membership = "Monthly"
        fee = 120000
    elif code == "CODE 3":
        membership = "Quarterly"
        fee = 300000
    elif code == "CODE 4":
        membership = "Annual"
        fee = 1000000
    elif code == "CODE 0":
       # ----------------day ends------------
        print("+================= end of day report =================+")
        print(f"| {'Daily members' :<21} |", daily_members)
        print(f"| {'Monthly members' :<21} |", monthly_members)
        print(f"| {'Quartery members' :<21} |", quartery_members)
        print(f"| {'Annual members' :<21} |", annual_members)
        print(f"| {'Total revenue' :<21} |", revenue)
        print(f"| {'Date' :<21} |", time.strftime("%Y-%m-%d %H:%M:%S"))
        print("+================= end of day report =================+")
        break 
    else:
        print("Invalid membership code. Please try again.")
        continue
    if code == "CODE 1":
        daily_members += 1
    elif code == "CODE 2":
        monthly_members += 1
    elif code == "CODE 3":
        quartery_members += 1
    elif code == "CODE 4":
        annual_members += 1

    print("=========OPTIONAL===========")
    print("+-------------+------------+")
    print(f"| {'MEMBERSHIP':<11} | {'TRAINER FEE':<10}|")
    print("+-------------+------------+")
    print(f"| {'Daily':<11} | {'15000':<10} |")
    print(f"| {'Monthly':<11} | {'50000':<10} |")
    print(f"| {'Quartery':<11} | {'150000':<10} |")
    print(f"| {'Annually':<11} | {'600000':<10} |")
    print("+-------------+------------+")
    trainer = input("Would you like a trainer? (y/n): ").strip().lower()
    if trainer == "y":
        if code == "CODE 1":
            trainer_fee = 15000
        elif code == "CODE 2":
            trainer_fee = 50000
        elif code == "CODE 3":
            trainer_fee = 150000
        elif code == "CODE 4":
            trainer_fee = 600000
    if trainer == "n":
        trainer_fee = 0 
    membership_fee = fee + trainer_fee
    revenue += membership_fee

    # bmi part
    weight = float(input("Enter weight in 'kgs': "))
    height = float(input("Enter height in 'm': "))
    if weight <= 0 or height <= 0:
        print("Weight and height must be positive numbers. Please try again.")
        continue
    if weight > 0 and height > 0:
        bmi = (weight) / (height * height)
        if bmi < 18.5:
            status = "Underweight"
        elif 18.5 <= bmi <= 24.49:
            status = "Normal"
        elif 25.0 <= bmi <= 29.99:
            status = "Overweight" 
        else:
            status = "Obesse"
        if status == "Underweight":
            recommend = "Strenght and Nutrition"
        elif status == "Normal":
            recommend = "General fitness"
        elif status == "Overweight":
            recommend ="Cardio and toning"
        else:
            recommend ="Supervised weight loss"

# ----------------membership card----------------------
    print("+======== membership card =========+")
    print(f"| {'Name' :<21} |", name)
    print(f"| {'Membership type' :<21} |", membership)
    print(f"| {'Trainer fee' :<21} |", trainer_fee)
    print(f"| {'Total amount payable' :<21} |", membership_fee)
    print(f"| {'BMI' :<21} |", round(bmi, 1))
    print(f"| {'Recommended program' :<21} |", recommend)
    print("+====optics fitness gym kampala====+")
    continue

