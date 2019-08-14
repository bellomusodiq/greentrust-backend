from pypaystack import Transaction

class Paystack:
    
    transaction = Transaction(authorization_key="sk_test_40842031d9cd521f662260d98a0248ed8c569d73")

    def __init__(self, ref_code):
        self.ref_code = ref_code
        self.email = ""
        self.transaction_date = ""
        self.amount = 0
        self.status = None

    def convert_amount(self, amount):
        return amount/100
    
    def verify_payment(self):
        try:
            response = self.transaction.verify(self.ref_code)[3]
            print(response["customer"]["email"], 
            response["customer"]["customer_code"], 
            response["status"], 
            self.convert_amount(response["amount"]),
            response["reference"]
            )
            return 'verified'
        except:
            return 'not verified'

    
Paystack("n873cRSs.awptNG").verify_payment()
