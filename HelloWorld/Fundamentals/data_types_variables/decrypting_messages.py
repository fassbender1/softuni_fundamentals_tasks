key = int(input())
num_lines = int(input())

for i in range(num_lines):
    new_line = input()
    hex_to_dec = ord(new_line) + key
    new_dec_to_hex = chr(hex_to_dec)
    print(new_dec_to_hex, end = '')

