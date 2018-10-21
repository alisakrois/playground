"""
Given a list of countries and cities of each country.
Then given the names of the cities. For each city specify the country in which it is located.
"""

capitals = {}
for _ in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        capitals[city] = country

for _ in range(int(input())):
    print(capitals[input()])
