def calculate_discount(price,discount_percent):
    if discount_percent<20:
        return price
    else:
        return price-(discount_percent/100*price)
    
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent) 