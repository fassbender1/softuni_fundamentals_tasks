passwd = input()

print(len(passwd))

if len(passwd) < 6 or len(passwd) > 10:
    print(f"more than 10 or less than 6 chars")
