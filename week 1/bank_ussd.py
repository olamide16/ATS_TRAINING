bank_ussd = "*634#"
bank_list = """
1.  Acess bank 
2. Fidelity Bank
3. Guarantee Trust Bank
4. Stanbic IBTC
5. Wema bank
6. Kuda
"""
banking_option = """
1. Open new account
2. Account balance
3. Buy airtime
4. tansfer 
5. change pin
"""
transfer_option = """
1. tansfer to self bank
2. Tansfer  to other bank"""
ussd = []
input_ussd = input("Enter ussd: ")
if ussd == bank_ussd:
    print(banking_option)
else:
    print("Unsupported ussd")