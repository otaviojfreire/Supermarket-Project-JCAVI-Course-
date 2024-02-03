# I will write funtions in python for buying products 
# in my supermarket
# Let's start writing the functions with def in python

def add_products_to_dict(my_dict):
    while True:
        product_name = input("Enter the product name (or 'exit' to stop): ")

        if product_name.lower() == 'exit':
            break

        try:
            product_price = float(input("Enter the product price: "))
        except ValueError:
            print("Invalid input. Please enter a valid numeric price.")
            continue

        my_dict[product_name] = product_price

    return my_dict