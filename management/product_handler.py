from menu import products


def get_product_by_id(id: int):
    for product in products:
        if product['_id'] == id:
            return product
    return {}


def get_products_by_type(type: str):
    found_products = []
    for product in products:
        if product['type'] == type:
            found_products.append(product)
    return found_products
