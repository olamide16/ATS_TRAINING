from ast import Not


has_crimal_record = True
has_good_credit = False
if has_crimal_record and not has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")