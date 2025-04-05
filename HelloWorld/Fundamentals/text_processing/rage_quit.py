def rage_quit(string):
    symbol_counter = 0
    final_string = ""
    string_found = ""
    multiplier = ""

    for index in range(len(string)):
        if not string[index].isnumeric():
            if string[index].upper() in final_string:
                string_found += string[index].upper()
                continue
            symbol_counter += 1
            string_found += string[index].upper()
        else:
            for next_symbols_index in range(index, len(string)):
                if not string[next_symbols_index].isnumeric():
                    break
                multiplier += string[next_symbols_index]

            final_string += string_found * int(multiplier)
            string_found = ""
            multiplier = ""

    return f"Unique symbols used: {symbol_counter}\n" \
           f"{final_string}"


text = input()
result = rage_quit(text)
print(result)


















