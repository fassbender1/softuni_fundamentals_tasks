results_per_user = {}
submissions_per_language = {}

while True:
    command = input().split("-")
    if len(command) == 1:
        break
    elif len(command) == 2:
        user = command[0]
        del results_per_user[user]
    else:
        name, language, result = command[0], command[1], int(command[2])
        if name not in results_per_user.keys():
            results_per_user[name] = 0
        if result > results_per_user[name]:
            results_per_user[name] = result
        if language not in submissions_per_language.keys():
            submissions_per_language[language] = 0
        submissions_per_language[language] += 1

print(f"Results:")
for username, points in results_per_user.items():
    print(f"{username} | {points}")
print(f"Submissions:")
for language, subs in submissions_per_language.items():
    print(f"{language} - {subs}")

















