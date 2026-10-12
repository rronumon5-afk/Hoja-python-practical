class MyATM:
    def withdraw(self):
        print("cash withdraw successfully")
        
    def verify_pin(self):
        print("pin verified")
    def check_balance(self):
        print("balnce checked")
    def update_server(self):
        print("server updated")

atm=MyATM()

atm.verify_pin()
atm.check_balance()
atm.update_server()
atm.withdraw()

                    