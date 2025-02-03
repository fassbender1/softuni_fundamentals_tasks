num_lines = int(input())

is_Balanced = True
open_bracket = False

for i in range(num_lines):
    new_line = input()
    if new_line == "(":
        if open_bracket:
            is_Balanced = False
            break
        open_bracket = True
    elif new_line == ")":
        if not open_bracket:
            is_Balanced = False
            break
        open_bracket = False

if open_bracket:
    is_Balanced = False

if not is_Balanced:
    print(f"UNBALANCED")
else:
    print(f"BALANCED")
