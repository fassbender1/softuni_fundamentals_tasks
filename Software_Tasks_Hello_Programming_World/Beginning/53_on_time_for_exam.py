# Студент трябва да отиде на изпит в определен час (например в 9:30 часа). Той идва в изпитната зала в даден час
# на пристигане (например 9:40). Счита се, че студентът е дошъл навреме, ако е пристигнал в часа на изпита
# или до половин час преди това. Ако е пристигнал по-рано повече от 30 минути, той е подранил.
# Ако е дошъл след часа на изпита, той е закъснял. Напишете програма, която прочита време на изпит и време на
# пристигане и отпечатва дали студентът е дошъл навреме, дали е подранил или е закъснял и с колко часа или минути е подранил или закъснял.

hour_of_exam = int(input())
minute_of_exam = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = hour_of_exam * 60 + minute_of_exam
arrival_time = arrival_hour * 60 + arrival_minute

time_difference = arrival_time - exam_time

hours_late = 0
minutes_late = 0


if time_difference > 0:
    print("Late")
    if time_difference < 60:
        print(f"{time_difference} minutes after the start")
    else:
        hours_late = time_difference // 60
        minutes_late = time_difference % 60
        print(f"{hours_late}:{minutes_late:02d} hours after the start")

elif time_difference == 0 or time_difference >= -30:
    print("On time")
    if time_difference != 0:
        print(f"{abs(time_difference)} minutes before the start")

else:
    print("Early")
    time_difference = abs(time_difference)
    if time_difference < 60:
        print(f"{time_difference} minutes before the start")
    else:
        hours_early = time_difference // 60
        minutes_early = time_difference % 60
        print(f"{hours_early}:{minutes_early:02d} hours before the start")

# Ако студентът пристига с поне минута разлика от часа на изпита, отпечатайте на следващия ред:
# · "mm minutes before the start" за идване по-рано с по-малко от час;
# · "hh:mm hours before the start" за подраняване с 1 час или повече. Минутите винаги печатайте с 2 цифри, например "1:05”;
# · "mm minutes after the start" за закъснение под час;
# · "hh:mm hours after the start" за закъснение от 1 час или повече. Минутите винаги печатайте с 2 цифри, например "1:03”.