income = int(input("请输入税前工资:"))
final_income = 0
if income <= 5000:
	final_income = income
elif 5000 < income <= 8000:
	final_income = (income - 5000) * 0.97 + 5000
elif 8000 < income <= 17000:
	final_income = 5000 + 3000 * 0.97 + (income - 8000) * 0.9
elif 17000 < income <= 30000:
	final_income = 5000 + 3000 * 0.97 + 9000 * 0.9 + (income - 17000) * 0.8
else:
	final_income = 5000 + 3000 * 0.97 + 9000 * 0.9 + 13000 * 0.8 + (income - 30000) * 0.75
print(f"税后工资为:{final_income}")