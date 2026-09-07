class flipkart:
    discount=30
    @classmethod
    def updateddiscount(cls):
        cls.discount=40
        print("updated discount",cls.discount)

    def info(self,name,phno,addr):
        self.name=name
        self.phno=phno
        self.addr=addr
        print(f"welcome to flipcart",self.name)
    @staticmethod
    def banner():
        print(f"{flipkart.discount}% discount is going , on grab the products")

lakshmi=flipkart()
lakshmi.info('lakshmi',9876543211,'hyd')
lakshmi.updateddiscount()
lakshmi.banner()
vishnu=flipkart()
vishnu.info('vishnu',9876543211,'hyd')
vishnu.updateddiscount()
vishnu.banner()
siva=flipkart()
siva.info('siva',9876543211,'hyd')
siva.updateddiscount()
siva.banner()
