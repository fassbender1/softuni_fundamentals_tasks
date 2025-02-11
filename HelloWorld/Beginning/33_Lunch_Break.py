# По време на обедната почивка искате да изгледате епизод от своя любим сериал. Вашата задача е да напишете програма,
# с която ще разберете дали имате достатъчно време да изгледате епизода. По време на почивката отделяте време
# за обяд и време за отдих. Времето за обяд ще бъде 1/8 от времето за почивка, а времето за отдих ще бъде 1/4 от
# времето за почивка.

TV_series = str(input())
runtime_per_episode = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
leisure_time = break_duration / 4

break_time_left = break_duration - (lunch_time + leisure_time)

from math import ceil

if break_time_left >= runtime_per_episode:
    free_time_left = break_time_left - runtime_per_episode
    print(f"You have enough time to watch {TV_series} and left with {ceil(free_time_left)} minutes free time.")
else:
    time_needed = runtime_per_episode - break_time_left
    print(f"You don't have enough time to watch {TV_series}, you need {ceil(time_needed)} more minutes.")

# Изход
# На конзолата да се изпише един ред:
# ⦁	Ако времето е достатъчно да изгледате епизода:
# "You have enough time to watch {име на сериал} and left with {останало време} minutes free time."
# ⦁	Ако времето не Ви е достатъчно:
# "You don't have enough time to watch {име на сериал}, you need {нужно време} more minutes."
# Времето в двете изходни съобщения да се закръгли до най-близкото цяло число нагоре.
