"""#username and password
username=input("enter a username")
password=input("enter a  password")
if username=="Lakshmi" and password=="Lakshmi123":
    print("Login sucessfully")
else:
    print("Invaild Credentials")"""

# products are found or not found
"""list=input().split()
search=input()
if search in list:
    print(f"{search} list found")
else:
    print(f"{search}  list not found")"""

bil=int(input("enter a bil:"))
if bil>99:
    print("actual bil", bil)
else:
    print("Actual bil+ dilevry charge" ,bil+30)