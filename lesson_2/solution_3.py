book_box_str: str # количество коробок с книгами в формате строки
stat_box_str: str # количество коробок с канцтоварами в формате строки
toy_box_str: str # количество коробок с игрушками в формате строки

book_box_float: float # количество коробок с книгами в формате числа
stat_box_float: float # количество коробок с канцтоварами в формате числа
toy_box_float: float # количество коробок с игрушками в формате числа

book_box_size_float: float = 2 # объём одной коробки с книгами в м^3
stat_box_size_float: float = 1.5 # объём одной коробки с канцтоварами в м^3
toy_box_size_float: float = 3 # объём одной коробки с игрушками в м^3


storage_size_int: float  # объём склада под все коробки в м^3

book_box_str = input('Количество коробок с книгами: ')
stat_box_str = input('Количество коробок с канцтоварами: ')
toy_box_str = input('Количество коробок с игрушками: ')

book_box_float = float(book_box_str)
stat_box_float = float(stat_box_str)
toy_box_float = float(toy_box_str)

storage_size_float = book_box_float*book_box_size_float + stat_box_float*stat_box_size_float + toy_box_float*toy_box_size_float

print('Общий объём:', storage_size_float, ' м^3')
