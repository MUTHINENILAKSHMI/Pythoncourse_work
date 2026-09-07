data={
    'salt':20,
    'sugar':100,
    'cooking oil': 90,
    'rice flour' : 120,
    'wheat flour ': 500,
    'chilli powder': 98,
    'eggs' : 93,
    'turmeric ': 45,
    'masala poweder': 100,
    'coconut powder': 130
}

for i in data:
    print(i.ljust(20),data[i])
print("---------------#--------------")
prod=input("enter your data").split()
bil=0
for i in prod:
    print(i.ljust(20),data[i])
    bil+=data[i]
print("total bill",bil)




