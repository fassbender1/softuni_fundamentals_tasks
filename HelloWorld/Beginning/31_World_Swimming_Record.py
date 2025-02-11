# Иван решава да подобри Световния рекорд по плуване на дълги разстояния. На конзолата се въвежда рекордът
# в секунди, който Иван трябва да подобри,  разстоянието в метри, което трябва да преплува и времето в секунди,
# за което плува разстояние от 1 м. Да се напише програма, която изчислява дали се е справил със задачата,
# като се има предвид, че: съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди. Когато се изчислява
# колко пъти Иван ще се забави, в резултат на съпротивлението на водата, резултатът трябва да се закръгли
# надолу до най-близкото цяло число.
# Да се изчисли времето в секунди, за което Иван ще преплува разстоянието и разликата спрямо Световния рекорд.
# Вход
# От конзолата се четат 3 реда:
# ⦁	Рекордът в секунди – реално число;
# ⦁	Разстоянието в метри – реално число;
# ⦁	Времето в секунди, за което плува разстояние от 1 м. - реално число.

current_world_record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_per_meter = float(input())

import math

total_time_for_the_distance = distance_in_meters * time_in_seconds_per_meter
water_resistance_delay = math.floor((distance_in_meters / 15)) * 12.5
total_time_with_delay = total_time_for_the_distance + water_resistance_delay

if total_time_with_delay < current_world_record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {total_time_with_delay :.2f} seconds.')

else:
    total_time_with_delay -= current_world_record_in_seconds
    print(f'No, he failed! He was {total_time_with_delay :.2f} seconds slower.')


