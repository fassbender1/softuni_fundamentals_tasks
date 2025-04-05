def followers():
    followers_dict = {}

    while True:
        command = input()
        if command == "Log out":
            break

        parts = command.split(": ")
        action = parts[0]

        if action == "New follower":
            username = parts[1]
            if username not in followers_dict:
                followers_dict[username] = {'likes': 0, 'comments': 0}
            else:
                continue

        elif action == "Like":
            username, like_count = parts[1], int(parts[2])
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
            if username not in followers_dict:
                print(f"{username} doesn't exist.")
            else:
                del followers_dict[username]

    print(f"{len(followers_dict.items())} followers")
    for username, likes in followers_dict.items():
        print(f"{username}: {likes['likes'] + likes['comments']}")


followers()

