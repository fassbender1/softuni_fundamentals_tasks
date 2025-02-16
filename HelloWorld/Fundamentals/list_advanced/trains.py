def wagons_peeps(string):

    command = input().split()

    while command[0] != "End":

        if command[0] == "add":
            number_of_people = int(command[1])
            string[-1] += number_of_people
        elif command[0] == "insert":
            index = int(command[1])
            people = int(command[2])
            string[index] += people
        elif command[0] == "leave":
            index = int(command[1])
            people = int(command[2])
            string[index] -= people

        command = input().split()
    return string


wagons = [0] * int(input())
print(wagons_peeps(wagons))
