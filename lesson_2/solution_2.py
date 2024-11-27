number_1_str: str
number_2_str: str
number_3_str: str

number_1_float: float
number_2_float: float
number_3_float: float

sred_arifm_str: str
sred_arifm_float: float

number_1_str = input()
number_2_str = input()
number_3_str = input()

number_1_float = float(number_1_str)
number_2_float = float(number_2_str)
number_3_float = float(number_3_str)

sred_arifm_float = (number_1_float+number_2_float+number_3_float)/3
sred_arifm_str = str(sred_arifm_float)

print(sred_arifm_str)
