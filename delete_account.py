class delete_account:
    print("__________delete account_______________")
    def __init__(self,p):
        from db_connection import cur_obj,db_connection
        query="delete from bank_details where pin=%s"
        data=(p,)
        cur_obj.execute(query,data)
        db_connection.commit()
        if cur_obj.rowcount>0:
            print("your account has deleted......")
        else:
            print("your account not found.....")

