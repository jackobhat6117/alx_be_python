monthly_income = int(input("Enter your monthly income:"))
monthly_expense = int((input("Enter your montly expense:")))
monthly_saving = monthly_income - monthly_expense
projected_savings = monthly_saving * 12 + (monthly_saving * 12 * 0.05)

print(f"your montly savings are ${monthly_saving}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")