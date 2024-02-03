from buying_a_product import add_products_to_dict
from price import calculate_total_price
from payment import form_of_payment
from discount import there_is_a_discount
from save_csv_file import write_to_csv_file 

def main():
    my_products = {}
    
    while True:
        my_products = add_products_to_dict(my_products)
        chosen_payment_method = form_of_payment()
        
        total_price_before_discount = calculate_total_price(my_products)
        print("Products Bought:")
        for product, price in my_products.items():
            print(f"{product}: ${price}")

        discount_price, discount_amount = there_is_a_discount(chosen_payment_method, total_price_before_discount)
        
        print("Chosen Payment Method:", chosen_payment_method)
        print("Total Price Before Discount:", total_price_before_discount)

        if discount_amount != 0:
            print(f"You have a discount of ${discount_amount}!")
            print("Discounted Price:", discount_price)
            print("Total Discount Amount:", discount_amount)
            print("Total Price After Discount:", discount_price)
        else:
            print("No discount applied.")
            print("Total Price After Discount:", total_price_before_discount)

        write_to_csv_file(my_products, total_price_before_discount, discount_amount, discount_price, chosen_payment_method)

        while True:
            finish_response = input("Finished buying? Type: Yes or No\n").lower()

            if finish_response == 'yes':
                print("Thank you for shopping here in our supermarket! Goodbye!")
                return
            elif finish_response == 'no':
                break
            else:
                print("Invalid input. Please type 'Yes' or 'No'.")

if __name__ == "__main__":
    main()