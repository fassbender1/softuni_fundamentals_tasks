def to_do_list():

    to_do_notes = []

    while True:
        notes = input()
        if notes == "End":
            break

        to_do_notes.append(notes)

    sorted_notes = sorted(to_do_notes, key=lambda x: int(x.split('-')[0]))
    string_sorted = [note.split('-')[1] for note in sorted_notes]
    return string_sorted


result = to_do_list()
print(result)


