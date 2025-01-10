shop_length_str: str
shop_width_str: str

shop_length_float : float
shop_width_float : float

shop_length_str = input('Введите длину магазина: ')
shop_width_str = input('Введите ширину магазина: ')

shop_length_float = float(shop_length_str)
shop_width_float = float(shop_width_str)

shop_area = shop_length_float * shop_width_float

print(shop_area, 'м.кв')