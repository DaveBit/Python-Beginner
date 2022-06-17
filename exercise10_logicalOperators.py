#operators covered and or and not

has_high_income = True
has_good_credit = False
if has_high_income and has_good_credit:
    print("Eligible for Loan")
else:
    print("Not eligible for a loan")

has_high_income = True
has_good_credit = False
if has_high_income or has_good_credit:
    print("Eligible for Loan")
else:
    print("Not eligible for a loan")

has_high_income = True
has_good_credit = False
has_criminal_record = True
if (has_high_income or has_good_credit) and not has_criminal_record:
    print("Eligible for Loan")
else:
    print("Not eligible for a loan")