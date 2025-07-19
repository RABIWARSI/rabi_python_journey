def online_store(customer_name, item, quantity, price_per_item, discount_percent=0):
    print(f"Hello {customer_name}!")
    print("Welcome to Rabi Warsi Online Store 🛒")
    print(f"You bought: {item}")
    print(f"Quantity: {quantity}")
    print(f"Price per item: Rs.{price_per_item}")
    
    total_cost = price_per_item * quantity
    discount_amount = total_cost * (discount_percent / 100)
    final_cost = total_cost - discount_amount

    print(f"\nSubtotal: Rs.{total_cost}")
    print(f"Discount: {discount_percent}% (-Rs.{discount_amount})")
    print(f"Total Payable: Rs.{final_cost}")
    print("\nThank you for shopping with us! Your order will be delivered soon 🚚")

# Example call:
online_store("Shazmina", "Bag", 2, 3000, discount_percent=10)
