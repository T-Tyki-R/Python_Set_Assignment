# Python Set Adventure

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def display_travel(airport1, airport2):
    res1 = ""
    res2 = ""
    for i in airport1:
        res1 += f"{i}\n"
    for i in airport2:
        res2 +=  f"{i}\n"
    return f"The locations we're flying to are:\n{res1}\nThe locations our competitor are flying to are:\n{res2}"

unique_location = our_routes.difference(competitor_routes)
location_exception = our_routes.symmetric_difference(competitor_routes)

print(display_travel(our_routes, competitor_routes))
print(unique_location)
print(location_exception)