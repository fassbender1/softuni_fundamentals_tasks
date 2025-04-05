import re

string = input()
pattern = r"(www\.[A-Za-z0-9\-]+(\.[a-z]+)+)"
while string:
    matches = re.search(pattern, string)
    if matches:
        url = matches.group(1)
        print(url)
    string = input()

