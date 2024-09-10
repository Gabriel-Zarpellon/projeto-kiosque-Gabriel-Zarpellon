from menu import products
from operator import itemgetter


def get_product_by_id(id: int) -> dict:
    if type(id) is not int:
        raise TypeError('product id must be an int')

    for product in products:
        if product['_id'] == id:
            return product

    return {}


def get_products_by_type(search_type: str) -> list:
    if type(search_type) is not str:
        raise TypeError('product type must be a str')

    found_products = []

    for product in products:
        if product['type'] == search_type:
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


def menu_report() -> str:
    product_count = len(products)
    total_price = 0

    for product in products:
        total_price = total_price + product['price']
    average_price = round(total_price / product_count, 2)
    types = {'bakery': 0, 'dairy': 0, 'drink': 0, 'fruit': 0, 'vegetable': 0}

    for product in products:
        for key in types:
            if key == product['type']:
                types[key] = types[key] + 1

    most_common_type = {'most_common': 0, 'type': ''}

    for key, value in types.items():
        if value > most_common_type['most_common']:
            most_common_type['most_common'] = value
            most_common_type['type'] = key

    return (f'Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common_type['type']}')


def add_product_extra(menu: list,  *args: tuple, **kwargs: dict) -> dict:
    id = 0

    if len(menu) == 0:
        id = 1
    else:
        sorted_list = sorted(menu, key=itemgetter('_id'))
        last_product = sorted_list[-1]
        id = last_product['_id'] + 1

    for arg in args:
        if kwargs.get(arg, False) is False:
            raise KeyError(f'field {arg} is required')

    for key in kwargs.copy():
        if args.count(key) == 0:
            kwargs.pop(key)

    kwargs['_id'] = id
    menu.append(kwargs)

    return kwargs
