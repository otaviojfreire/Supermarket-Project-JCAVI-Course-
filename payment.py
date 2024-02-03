# Let's develop a funtion for the payment


def form_of_payment():
    while True:
        response = input("Would you like to pay with your credit or debit card, in cash, or with Pix?\n").lower()

        if response in ['credit card', 'debit card', 'cash', 'pix']:
            return response
        else:
            print("Invalid input. Please enter 'credit card', 'debit card', 'cash', or 'pix'.")
