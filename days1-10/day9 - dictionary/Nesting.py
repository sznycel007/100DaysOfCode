# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a List in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

print(travel_log["France"])
print(travel_log["Germany"])


# Nesting Dictionary in a Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}
print(travel_log)


SpotifyWrap = {
    "Band": {"Pink Floyd": ["Animals", "High Hopes", "Wish you where here"],"total_hours": 23}
}
print(SpotifyWrap)

# Nesting dictionary in a list
print()

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]
print(travel_log[0])
print(travel_log[1])




