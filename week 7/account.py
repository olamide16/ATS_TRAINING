# '''Solution by: AlexanderSro'''

# account = 0
# while True:
#     action = input("Deposit/Whitdrow/Balance/Quit? D/W/B/Q: ").lower()
#     if action == "d":
#         deposit = input("How much would you like to deposit? ")
#         account = account + int(deposit)
#     elif action == "w":
#         withdrow = input("How much would you like to withdrow? ")
#         account = account - int(withdrow)
#     elif action == "b":
#         print(account)
#     else:
#         quit()

'''Solution by: popomaticbubble 
'''
transactions = []

while True:
    text = input("> ")
    if text:
    	text = text.strip('D ')
    	text = text.replace('W ', '-')
    	transactions.append(text)
    else: 
		break	
		
transactions = (int(i) for i in transactions)
balance = sum(transactions)
print(f"Balance is {balance}")