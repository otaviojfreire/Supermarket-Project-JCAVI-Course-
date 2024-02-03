# Let's verify if there is a discount according the form of payment

def there_is_a_discount(form_of_payment, total_price):
    discount_amount = 0

    if form_of_payment.lower() in ['debit card', 'pix']:
        discount_amount = total_price * 0.05
        discounted_price = total_price - discount_amount
        return discounted_price, discount_amount
    else:
        return None, discount_amount