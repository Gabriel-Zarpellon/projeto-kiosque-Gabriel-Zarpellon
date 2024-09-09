from menu import products
from operator import itemgetter


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


def add_product(menu: list, **kwargs: dict) -> dict:
    id = 0
    if len(menu) == 0:
        id = 1
    else:
        sorted_list = sorted(menu, key=itemgetter('_id'))
        last_product = sorted_list[-1]
        id = last_product['_id'] + 1
    kwargs['_id'] = id
    menu.append(kwargs)
    return kwargs
