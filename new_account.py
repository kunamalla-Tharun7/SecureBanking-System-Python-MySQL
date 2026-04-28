class new_account:
    print("__________new account creation______________")
    def __init__(self,n,phone,balance=1000):
        pin=int(input("create your pin: "))
        c_pin=int(input("confirm   your pin:"))
        if pin==c_pin:
            query="insert into bank_details(name,phone_number,balance,pin) values(%s,%s,%s,%s)"
            data=(n,phone,balance,c_pin)
            from db_connection import cur_obj,db_connection
            cur_obj.execute(query,data)
            db_connection.commit()
            print("your account has created successfully....")
        else:
            print("your pin must be only in 4 characters....")






