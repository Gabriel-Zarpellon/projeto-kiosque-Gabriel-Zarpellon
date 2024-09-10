from menu import products


def calculate_tab(tab: list) -> dict:
    total = 0

    for item in tab:
        id = item['_id']
        amount = item['amount']
        product = list(product for product in products if product['_id'] == id)
        total = round(total + (product[0]['price'] * amount), 2)

    subtotal = {'subtotal': f'${total}'}

    return subtotal
