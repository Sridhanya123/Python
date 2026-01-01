header= """Estimate Bill
Check the bill before leaving the shop"""

book_title1="Python Basics"
book_title2="Data Science Intro"

book_price1=450
book_price2=600
print(header)
item_1="{}-{}"
print(item_1.format(book_title1,book_price1))
print(item_1.format(book_title2,book_price2))
Total_price=book_price1+book_price2
print("Total price:",Total_price)
thankyou= "\n\tThankyou for Shopping with us\t"
