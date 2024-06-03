# Music Festival Playlist Organization

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set()
unique_artists.update(artist_names)


if len(artist_names) != len(unique_artists):
    for i, x in enumerate(artist_names):
        print(x)
    print(f"Duplicate found: {True}")

# duplicate_checker = {f"Duplicate Found: {True}" if len(i) != len(unique_artists) else "Duplicate Found: {False}" for i in enumerate(artist_names)}

# print(duplicate_checker)