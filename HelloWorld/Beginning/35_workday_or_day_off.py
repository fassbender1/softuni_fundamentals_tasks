# Напишете програма която, чете ден от седмицата (текст), на английски език - въведен от потребителя.
# Ако денят е работен отпечатва на конзолата - "Working day", ако е почивен - "Weekend".
# Ако се въведе текст различен от ден от седмицата да се отпечата - "Error".

day_of_the_week = str(input())

if day_of_the_week == 'Monday' \
        or day_of_the_week == 'Tuesday' \
        or day_of_the_week == 'Wednesday'\
        or day_of_the_week == 'Thursday'\
        or day_of_the_week == 'Friday':
    result = "Working day"
elif day_of_the_week == 'Saturday' \
        or day_of_the_week == 'Sunday':
    result = "Weekend"
else:
    result = "Error"

print(result)
