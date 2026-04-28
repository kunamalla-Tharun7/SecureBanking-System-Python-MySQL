class update_pin:
    print("________________________update Account_______________")
    def __init__(self,p,new_p):
        from db_connection import cur_obj,db_connection
        query="select pin from bank_details where pin=%s"
        data=(p,)
        cur_obj.execute(query,data)
        res=cur_obj.fetchone()
        if res:
            pin=new_p
            query_u="update bank_details set pin=%s where pin=%s"
            data_u=(pin,res[0])
            cur_obj.execute(query_u,data_u)
            db_connection.commit()
            print("your pin has updated....")
        else:
            print("enter correct pin....")





