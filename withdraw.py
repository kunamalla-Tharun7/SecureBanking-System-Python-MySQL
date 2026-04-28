class withdraw:
    print("__________withdraw______________")
    def __init__(self,p,amt):
        from db_connection import cur_obj,db_connection
        query="select balance from bank_details where pin=%s"
        data=(p,)
        cur_obj.execute(query,data)
        res=cur_obj.fetchone()
        if res:
            balance=res[0]
            if amt>0:
                balance-=amt
                query_w="update bank_details set balance=%s where pin=%s"
                data_w=(balance,p)
                cur_obj.execute(query_w,data_w)
                db_connection.commit()
                print("your amount has withdrawn....")
            else:
                print("enter correct amount....")
        else:
            print("invalid pin....")