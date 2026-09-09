# Restautant Bill Calculator


# Food items
item1 = "Steak"
item2 = "Juice"
item3 = "Pudding"

# Food Prices
steak_price = 119.99
drink_price = 69.99
desert_price = 89.99

# Calculate Total
total = steak_price + drink_price + desert_price

# VAT percentage
vat_percentage = 15

# VAT amount
vat_amount = (vat_percentage / 100) * total


# Final Total amount
final_total = total + vat_amount

# Display amount
print("=======Restraurant bill=========")
print(item1,"-R", steak_price)
print(item2,"-R",drink_price)
print(item3,"-R",desert_price)
print("*********************************")
print("Subtotal: R", total)
print("VAT:", vat_percentage, "%")
print("Final Total: R", final_total)