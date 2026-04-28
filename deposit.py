class money_deposit:
    print("____________Money Deposit______________")
    def __init__(self,p,amt):
        from db_connection import cur_obj,db_connection
        query="select balance from bank_details where pin=%s"
        data=(p,)
        cur_obj.execute(query,data)
        res=cur_obj.fetchone()
        if res:
            balance=res[0]
            if amt>0:
                balance+=amt
                query_d="update bank_details set balance=%s where pin=%s"
                data_d=(balance,p)
                cur_obj.execute(query_d,data_d)
                db_connection.commit()
                print("your money has deposited.....")
            else:
                print("enter correct amount....")
        else:
            print("you entered wrong pin....")
    
