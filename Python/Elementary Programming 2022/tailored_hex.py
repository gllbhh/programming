def format_hex(int_value, bits):
    """MAGIC_HEX"""
    str_1 = hex(int_value).removeprefix('0x')
    result = "0" * (bits // 4 - len(str_1)) + str_1
    return result


try:
    number = int(input("Give an integer: "))
    number_of_bits = int(input("Give hexadecimal length (number of bits): "))
except ValueError:
    print("Integer please")
else:
    print(format_hex(number, number_of_bits))
