def palindrome(numbers: list):
    is_palindrome = bool
    check_list = []
    for num in numbers:
        if num == num[::-1]:
            is_palindrome = True
            check_list.append(is_palindrome)
        else:
            is_palindrome = False
            check_list.append(is_palindrome)
    return check_list


list_as_str = input().split(", ")
result = palindrome(list_as_str)
print(*result, sep="\n")
