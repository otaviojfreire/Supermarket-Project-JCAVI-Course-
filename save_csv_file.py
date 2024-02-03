# I'll develop a function to save into a csv file the entire products
# if the informantion of the shopping
import csv

def write_to_csv_file(products, total_price, discount_amount, discounted_price, payment_method):
    try:
        with open('shopping_products.csv', 'w', newline='') as csvfile:
            fieldnames = ['Product', 'Price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for product, price in products.items():
                writer.writerow({'Product': product, 'Price': price})

            # Add an empty row
            writer.writerow({'Product': '', 'Price': ''})

            writer.writerow({'Product': 'Total Price Before Discount', 'Price': total_price})
            writer.writerow({'Product': 'Discount Amount', 'Price': discount_amount})
            writer.writerow({'Product': 'Discounted Price', 'Price': discounted_price})
            writer.writerow({'Product': 'Payment Method', 'Price': payment_method})
    except Exception as e:
        print(f"An error occurred: {e}")
