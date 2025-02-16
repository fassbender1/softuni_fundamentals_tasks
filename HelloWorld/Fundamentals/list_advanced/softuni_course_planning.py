def softuni_course_planning(lessons):

    commands = input()

    while commands != "course start":
        command = commands.split(":")
        action, lesson = command[0], command[1]
        if action == "Add":
            if lesson not in lessons:
                lessons.append(lesson)
        elif action == "Insert":
            index = int(command[2])
            if lesson not in lessons:
                lessons.insert(index, lesson)
        elif action == "Remove":
            if lesson in lessons:
                lessons.remove(lesson)
                check_exercise = lesson + "-Exercise"
                if check_exercise in lessons:
                    lessons.remove(check_exercise)
        elif action == "Swap":
            lesson_2 = command[2]
            if lesson in lessons and lesson_2 in lessons:
                lesson_index, lesson_2_index = lessons.index(str(lesson)), lessons.index(lesson_2)
                lessons[lesson_index], lessons[lesson_2_index] = lessons[lesson_2_index], lessons[lesson_index]
                check_exercise_first = lesson + "-Exercise"
                check_exercise_second = lesson_2 + "-Exercise"
                if check_exercise_first in lessons:
                    lessons.remove(check_exercise_first)
                    lessons.insert(lesson_2_index + 1, check_exercise_first)
                elif check_exercise_second in lessons:
                    lessons.remove(check_exercise_second)
                    lessons.insert(lesson_index + 1, check_exercise_second)

        elif action == "Exercise":
            if lesson in lessons and lesson + "-Exercise" not in lessons:
                lesson_index = lessons.index(str(lesson))
                lessons.insert(lesson_index + 1, lesson + "-Exercise")
            elif lesson not in lessons:
                lessons.append(lesson)
                lessons.append(lesson + "-Exercise")

        commands = input()
    for i, lesson in enumerate(lessons, start=1):
        print(f"{i}.{lesson}")


string = input().split(", ")
result = softuni_course_planning(string)


