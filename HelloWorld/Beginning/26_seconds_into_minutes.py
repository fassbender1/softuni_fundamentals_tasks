seconds_first = int(input())
seconds_second = int(input())
seconds_third = int(input())

total_time = seconds_first + seconds_second + seconds_third

minutes = total_time // 60
seconds = total_time % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")

else:
    print(f"{minutes}:{seconds}")
