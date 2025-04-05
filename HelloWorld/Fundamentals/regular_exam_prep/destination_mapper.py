def dest_mapper(string):

    import re

    pattern = r"(=|\/)([A-Z][a-zA-Z]{2,})\1"
    matches = re.findall(pattern, string)
    destinations = [match[1] for match in matches]
    travel_counter = sum(len(destination) for destination in destinations)

    print(f"Destinations: {', '.join(destinations)}")
    print(f"Travel Points: {travel_counter}")


map_string = input()
dest_mapper(map_string)











