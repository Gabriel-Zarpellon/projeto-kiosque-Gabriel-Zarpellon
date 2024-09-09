from menu import products


def calculate_tab(tab: list) -> dict:
    total = 0
    for item in tab:
        id = item['_id']
        amount = item['amount']
        for product in products:
            if product['_id'] == id:
                price = product['price']
                total = round(total + (price * amount), 2)
    subtotal = {'subtotal': f'${total}'}
    return subtotal
