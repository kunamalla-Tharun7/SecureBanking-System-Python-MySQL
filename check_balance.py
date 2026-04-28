class check_balance:

    def __init__(self,p):
        print("___________view account_____________________")
        from db_connection import cur_obj, db_connection
        query = "select balance from bank_details where pin=%s"
        cur_obj.execute(query,(p,))
        res = cur_obj.fetchone()
        if res:
            print("Your balance is:", res[0])
        else:
            print("invalid pin.....")
