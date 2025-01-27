# Ани отива до родния си град след много дълъг период извън страната. Прибирайки се вкъщи, тя вижда старата библиотека
# на баба си и си спомня за любимата си книга. Помогнете на Ани, като напишете програма,
# в която тя въвежда търсената от нея книга (текст). Докато Ани не намери любимата си книга или не провери
# всички книги в библиотеката, програмата трябва да чете всеки път на нов ред името на всяка следваща книга (текст),
# която тя проверява. Книгите в библиотеката са свършили щом получите текст "No More Books".
# · Ако не открие търсената книгата да се отпечата на два реда:
# o "The book you search is not here!"
# o "You checked {брой} books."
# · Ако открие книгата си се отпечатва един ред:
# o "You checked {брой} books and found it."

favorite_book = input()

count = 0
is_favorite_book = False
next_book = input()

while next_book != "No More Books":
    if next_book == favorite_book:
        is_favorite_book = True
        print(f"You checked {count} books and found it.")
        break
    else:
        count += 1
        next_book = input()

if is_favorite_book == False:
    print(f"The book you search is not here!")
    print(f"You checked {count} books.")


