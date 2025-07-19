def online_store(customer_name, item, quantity, price_per_item):
    print(f"Hello {customer_name}!")
    print("Welcome to Rabi Warsi Online Store")
    print(f"You bought: {item}")
    print(f"Quantity: {quantity}")
    print(f"Price per item: {price_per_item}")
    total_cost = price_per_item * quantity
    print(f"The total cost of your item is: {total_cost}")
    print("Thank you for shopping with us! Your order will be delivered soon.")
