Quarter_1_grade=float(input("Please Enter Your Tentative Grade for Quarter 1: "))
Quarter_2_grade=float(input("Please Enter Your Tentative Grade for Quarter 2: "))
Quarter_3_grade=float(input("Please Enter Your Tentative Grade for Quarter 3: "))
Quarter_4_grade=float(input("Please Enter Your Tentative Grade for Quarter 4: "))
q2=(Quarter_1_grade + 2*Quarter_2_grade) / 3
q3=(Quarter_2_grade + 2*Quarter_3_grade) / 3
Final_grade= (q3 + 2*Quarter_4_grade) / 3
print("Your Final Grade is: ", Final_grade)
