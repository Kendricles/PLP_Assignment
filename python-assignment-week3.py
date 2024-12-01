def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount is 20% or higher, apply the discount; otherwise, return the original price.
    """
    if discount_percent >= 20:  # Compare as a percentage, not decimal
        discount = price * (discount_percent / 100)  # Convert percentage to decimal
        final_price = price - discount
        return final_price
    else:
        return price

# Prompt the user for input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the function
final_price = calculate_discount(price, discount_percent)

# Display the result
print(f"The final price after applying the discount is: {final_price:.2f}")
