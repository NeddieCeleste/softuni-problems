countries = input().split(", ")
capitals = input().split(", ")

country_dictionary = dict(zip(countries, capitals))
for country, capital in country_dictionary.items():
    print(f"{country} -> {capital}")