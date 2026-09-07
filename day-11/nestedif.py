# nested if: we have if  inside the if 
#Instagram  story visibilty 

"""follow_account=eval(input("follow account"))
if follow_account:
    close_friendacc= eval(input("close friend account is following or not"))
    if close_friendacc:
        print("Story visible")
    else:
        print("not in a closefriend acount")
else:
    print("first follow the acount")
"""
# registration status for game tournement
"""reg=eval(input("regidtered:"))
if reg:
    fee=eval(input("fee paid"))
    if fee:
        print("Tournament entery confirmed")
    else:
        print("fee pending")
else:
    print("registartion required")"""

#Google Drive file access
"""link=eval(input("enter the link"))
if link:
    premission=eval(input("enter your permission"))
    if premission:
        print("link opened sucessfully")
    else:
        print("access Deined")
else:
    print("link is invaild")"""

#student marks:
"""data={
    'lakshmi': {'status': True, 'python': 96, 'Mysql': 92 , 'flask': 98},
    'shiva': {'status': False, 'python': None, 'Mysql': None , 'flask': None},
    'vishnu': {'status': True, 'python': 97, 'Mysql': 93 , 'flask': 88},
    'baji': {'status': True, 'python': 86, 'Mysql': 92 , 'flask': 78},
    'sunitha': {'status': True, 'python': 69, 'Mysql': 82 , 'flask': 68},
    'deepthi': {'status': True, 'python': 70, 'Mysql': 82 , 'flask': 88}
    }
name=input("Enter Your Name")
if name in data:
    if data[name]['status']:
        sum=data[name]['python']+data[name]['Mysql']+data[name]['flask']
        avg=sum/3
        print(f"hello{name}!!!")
        print(f"your average is {avg}")
        if avg>=90:
            print("Outstanding Performance")
        elif avg>=80:
            print("Very good")
        elif avg>=70:
            print("Good work hard")
        elif avg>=35:
            print("better luck next time")
        else:
            print("your failed exam please try hard ")
    else:
        print(f"{name} did not attempt the exam  bring your parents")
else:
    print(f"{name} not found in data")"""
