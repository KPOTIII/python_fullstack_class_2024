USD_RR_ER_str: str
USD_cost_str: str

shop_length_float : float
shop_width_float : float

USD_RR_ER_str = input('Введите курс доллара: ')
USD_cost_str = input('Введите цену товара в долларах: ')

shop_length_float = float(shop_length_str)
shop_width_float = float(shop_width_str)

shop_area = shop_length_float * shop_width_float

print(shop_area)