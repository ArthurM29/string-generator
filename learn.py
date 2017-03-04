
dirty_salary = int(input("Please enter dirty salary: "))

tax_rate = 25.7

income_tax = dirty_salary / 100 * tax_rate

clean_salary = dirty_salary - income_tax

print("Clean salary = " + str(clean_salary))
