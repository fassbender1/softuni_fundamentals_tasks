username = input()
password = input()

password_attempt = input()

while True:
    if password_attempt == password:
        print(f"Welcome {username}!")
        break
    password_attempt = input()

