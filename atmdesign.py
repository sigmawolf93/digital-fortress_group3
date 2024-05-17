# pin = 1234
# card_number = 333322224444
# balance = 1000
# cmd = ""
# print('Welcome to Digital Fortress MFB')
# card_pin = int(input('Enter pin > '))
# if card_pin == pin:
#     card_no_ver = int(input("Confirm account number > "))
#     if card_no_ver == 333322224444:
#         name = input('Enter name > ')
#         print(f'Hello {name}!\n Choose your option: '
#               f'\n C-Check Balance\n D-Deposit\n W-Withdraw\n B-Back\n Q-Quit')
#     else:
#         print('Invalid')
#         exit()
#
# while True:
#     cmd = input('> ').upper()
#     if cmd == "D":
#         new_deposit = float(input('Enter the amount: '))
#         balance += new_deposit
#         print("Successful!\nYour new balance is: N{:,.2f}".format(new_deposit))
#         print("B.Back\nQ.Quit")
#
#     elif cmd == "W":
#         withdrawal = float(input('Enter amount: '))
#         if withdrawal <= balance:
#             balance -= withdrawal
#             print("Withdrawal Successful")
#             print("B.Back\nQ.Quit")
#
#         else:
#             print('Insufficient funds')
#             print("B.Back\nQ.Quit")
#
#     elif cmd == "C":
#         print("Your current balance is: {:,.2f}".format(balance))
#         print("D.Deposit\nW.Withdraw\nB.Back\nQ.Quit")
#
#     elif cmd == "B":
#         print(f'Choose your option: '
#               f'\n C-Check Balance\n D-Deposit\n W-Withdraw\n B-Back\n Q-Quit')
#
#     elif cmd == "Q":
#         print('Thank you for banking with us')
#         break

