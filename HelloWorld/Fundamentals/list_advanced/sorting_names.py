def sorting_names(names):

    sorted_names = sorted(names, key=lambda name: (-len(name), name))
    return sorted_names


string = input().split(", ")
result = sorting_names(string)
print(result)

