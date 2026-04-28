while True:

    print("__________________MENU____________________________")
    print("1.check_balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.new_account")
    print("5.update pin")
    print("6.delete account")
    print("7.exit")
    o=int(input("Select your choice:   "))
    if o==1:
        from check_balance import check_balance
        check_balance(int(input("Enter your pin: ")))
    elif o==2:
        from deposit import money_deposit
        money_deposit(int(input("enter your pin to proceed transaction: ")),int(input("enter your amount to deposit: ")))
    elif o==3:
        from withdraw import withdraw
        withdraw(int(input("enter your pin to proceed transaction: ")),int(input("enter your amount to withdraw: ")))
    elif o==4:
        from new_account import new_account
        new_account(input("enter your name: "),input("enter your phone number: "))
    elif o==5:
        from update_pin import update_pin
        update_pin(int(input("enter your old pin:  ")),int(input("create  your new pin: ")))
    elif o==6:
        from delete_account import delete_account
        delete_account(int(input("enter your pin to proceed:  ")))
    elif o==7:
        break
    else:
        print("you selected wrong option.....")