rooms = {"A": "Dirty", "B": "Dirty"}
loc = "A"

while "Dirty" in rooms.values():
    if rooms[loc] == "Dirty":
        print("Cleaning Room", loc)
        rooms[loc] = "Clean"
    loc = "B" if loc == "A" else "A"

print("All Rooms Clean")