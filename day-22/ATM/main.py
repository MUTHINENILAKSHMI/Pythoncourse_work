import logic as lg
if lg.login():
    while True:
        lg.menu()
        ch=input("enter your choice:").upper()
        if ch=='C':
            lg.checkbalance()
        elif ch=='D':
            lg.deposit()
        elif ch=='W':
            lg.withdraw()
        elif ch=='V':
            lg.viewtranscation()
        elif ch=='E':
            print("---------------visit again thankyou-----------")
            break
        else:
            print("invaild login")