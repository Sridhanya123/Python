rice_price=45
sugar_price=40
oil_price=130

rice_qnty=3.0
sugar_qnty=2.5
oil_qnty=1.8

rice=rice_price*rice_qnty
sugar=sugar_price*sugar_qnty
oil=oil_price*oil_qnty
total_bill=rice+sugar+oil

print("Price for rice:",rice)
print("Price for sugar:",sugar)
print("Price for oil:",oil)
print("Total bill:",total_bill)

total_billInt=int(total_bill)
print("Total bill in Integer value:",total_billInt)

total_billStr=str(total_bill)
print("Total bill in string:",total_billStr)

import random
delivery_charge=random.randrange(5, 10)
print("Delivery Charge:",delivery_charge)

final_bill=total_bill+delivery_charge
print("Final bill including delivery charge=",final_bill)