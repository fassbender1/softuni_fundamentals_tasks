def followers():
    followers_dict = {}

    while True:
        command = input()
        if command == "Log out":
            break

        parts = command.split(": ", maxsplit=1)
        action = parts[0]

        if action == "New follower":
            username = parts[1]
            if username not in followers_dict:
                followers_dict[username] = {'likes': 0, 'comments': 0}

        elif action == "Like":
            username, like_count = parts[1].rsplit(": ", maxsplit=1)
            like_count = int(like_count)
            if username not in followers_dict:
                followers_dict[username] = {'likes': like_count, 'comments': 0}
            else:
                followers_dict[username]['likes'] += like_count

        elif action == "Comment":
            username = parts[1]
            if username not in followers_dict:
                followers_dict[username] = {'likes': 0, 'comments': 1}
            else:
                followers_dict[username]['comments'] += 1

        elif action == "Blocked":
            username = parts[1]
            if username in followers_dict:
                del followers_dict[username]
            else:
                print(f"{username} doesn't exist.")

    print(f"{len(followers_dict)} followers")
    for username, data in followers_dict.items():
        print(f"{username}: {data['likes'] + data['comments']}")


followers()