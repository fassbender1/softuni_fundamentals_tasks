# Шеф на компания забелязва че все повече служители прекарват време в сайтове, които ги разсейват.
# За да предотврати това, той въвежда изненадващи проверки на отворените табове на браузъра на служителите си.
# Според отворения сайт в таба се налагат следните глоби:
# · "Facebook" -> 150 лв.
# · "Instagram" -> 100 лв.
# · "Reddit" -> 50 лв.

# От конзолата се четат два реда:
# · Брой отворени табове в браузъра n - цяло число в интервала [1...10]
# · Заплата - число в интервала [500...1500]

browser_tabs = int(input())
Salary = float(input())

for _ in range(1, browser_tabs + 1):
    website_name = input()
    if website_name == "Facebook":
        Salary -= 150
        if Salary <= 0:
            print("You have lost your salary.")
            break
    elif website_name == "Instagram":
        Salary -= 100
        if Salary <= 0:
            print("You have lost your salary.")
            break
    elif website_name == "Reddit":
        Salary -= 50
        if Salary <= 0:
            print("You have lost your salary.")
            break

if Salary > 0:
    print(f"{int(Salary)}")


# След това n – на брой пъти се чете име на уебсайт – текст
# Изход
# · Ако по време на проверката заплатата стане по-малка или равна на 0 лева, на конзолата се изписва
# "You have lost your salary." и програмата приключва.
# · В противен случай след проверката на конзолата се изписва остатъкът от заплатата (да се изпише като цяло число).