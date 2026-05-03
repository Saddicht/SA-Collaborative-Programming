Quarter_1_grade=float(input("Please Enter Your Tentative Grade for Quarter 1: "))
Quarter_2_grade=float(input("Please Enter Your Tentative Grade for Quarter 2: "))
Quarter_3_grade=float(input("Please Enter Your Tentative Grade for Quarter 3: "))
Quarter_4_grade=float(input("Please Enter Your Tentative Grade for Quarter 4: "))
q2=(Quarter_1_grade + 2*Quarter_2_grade) / 3
q3=(Quarter_2_grade + 2*Quarter_3_grade) / 3
Final_grade= (q3 + 2*Quarter_4_grade) / 3

Q1 = round(Quarter_1_grade, 2)
Q2 = round(q2, 2)
Q3 = round(q3, 2)
Q4 = round(Final_grade, 2)

print("Your Final Grade is:", Q4)

if Q1 == 1.00:
    print("First Quarter Grade:", Q1, "- Excellent")
elif Q1 <= 1.50:
    print("First Quarter Grade:", Q1, "- Very Good")
elif Q1 <= 2.00:
    print("First Quarter Grade:", Q1, "- Good")
elif Q1 <= 2.50:
    print("First Quarter Grade:", Q1, "- Satisfactory")
elif Q1 <= 3.00:
    print("First Quarter Grade:", Q1, "- Fair")
elif Q1 <= 4.00:
    print("First Quarter Grade:", Q1, "- Failed on condition")
else:
    print("First Quarter Grade:", Q1, "- Failed")

if Q2 == 1.00:
    print("Second Quarter Grade:", Q2, "- Excellent")
elif Q2 <= 1.50:
    print("Second Quarter Grade:", Q2, "- Very Good")
elif Q2 <= 2.00:
    print("Second Quarter Grade:", Q2, "- Good")
elif Q2 <= 2.50:
    print("Second Quarter Grade:", Q2, "- Satisfactory")
elif Q2 <= 3.00:
    print("Second Quarter Grade:", Q2, "- Fair")
elif Q2 <= 4.00:
    print("Second Quarter Grade:", Q2, "- Failed on condition")
else:
    print("Second Quarter Grade:", Q2, "- Failed")

Quarter_1_grade=float(input("Please Enter Your Tentative Grade for Quarter 1: "))
Quarter_2_grade=float(input("Please Enter Your Tentative Grade for Quarter 2: "))
Quarter_3_grade=float(input("Please Enter Your Tentative Grade for Quarter 3: "))
Quarter_4_grade=float(input("Please Enter Your Tentative Grade for Quarter 4: "))
q2=(Quarter_1_grade + 2*Quarter_2_grade) / 3
q3=(Quarter_2_grade + 2*Quarter_3_grade) / 3
Final_grade= (q3 + 2*Quarter_4_grade) / 3

Q1 = round(Q1, 2)
Q2 = round(Q2, 2)
Q3 = round(Q3, 2)
Q4 = round(Final_grade, 2)

print("Your Final Grade is: ", Final_grade)

if Q1 == 1.00:
    print("First Quarter Grade:", Q1, "- Excellent")
elif Q1 <= 1.50:
    print("First Quarter Grade:", Q1, "- Very Good")
elif Q1 <= 2.00:
    print("First Quarter Grade:", Q1, "- Good")
elif Q1 <= 2.50:
    print("First Quarter Grade:", Q1, "- Satisfactory")
elif Q1 <= 3.00:
    print("First Quarter Grade:", Q1, "- Fair")
elif Q1 <= 4.00:
    print("First Quarter Grade:", Q1, "- Failed on condition")
else:
    print("First Quarter Grade:", Q1, "- Failed")

if Q2 == 1.00:
    print("Second Quarter Grade:", Q2, "- Excellent")
elif Q2 <= 1.50:
    print("Second Quarter Grade:", Q2, "- Very Good")
elif Q2 <= 2.00:
    print("Second Quarter Grade:", Q2, "- Good")
elif Q2 <= 2.50:
    print("Second Quarter Grade:", Q2, "- Satisfactory")
elif Q2 <= 3.00:
    print("Second Quarter Grade:", Q2, "- Fair")
elif Q2 <= 4.00:
    print("Second Quarter Grade:", Q2, "- Failed on condition")
else:
    print("Second Quarter Grade:", Q2, "- Failed")

if Q3 == 1.00:
    print("Third Quarter Grade:", Q3, "- Excellent")
elif Q3 <= 1.50:
    print("Third Quarter Grade:", Q3, "- Very Good")
elif Q3 <= 2.00:
    print("Third Quarter Grade:", Q3, "- Good")
elif Q3 <= 2.50:
    print("Third Quarter Grade:", Q3, "- Satisfactory")
elif Q3 <= 3.00:
    print("Third Quarter Grade:", Q3, "- Fair")
elif Q3 <= 4.00:
    print("Third Quarter Grade:", Q3, "- Failed on Condition")
else:
    print("Third Quarter Grade:", Q3, "- Failed")

if Q4 == 1.00:
    print("Fourth Quarter Grade:", Q4, "- Excellent")
elif Q4 <= 1.50:
    print("Fourth Quarter Grade:", Q4, "- Very Good")
elif Q4 <= 2.00:
    print("Fourth Quarter Grade:", Q4, "- Good")
elif Q4 <= 2.50:
    print("Fourth Quarter Grade:", Q4, "- Satisfactory")
elif Q4 <= 3.00:
    print("Fourth Quarter Grade:", Q4, "- Fair")
elif Q4 <= 4.00:
    print("Fourth Quarter Grade:", Q4, "- Failed on Condition")
else:
    print("Fourth Quarter Grade:", Q4, "- Failed")
