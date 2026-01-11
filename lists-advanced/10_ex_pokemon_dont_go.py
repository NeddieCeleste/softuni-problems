pokemon_distances = [int(x) for x in input().split()]
removed_sum = 0

while pokemon_distances:
    index = int(input())

    if index < 0:
        removed = pokemon_distances[0]
        removed_sum += removed
        pokemon_distances[0] = pokemon_distances[-1]
    elif index >= len(pokemon_distances):
        removed = pokemon_distances[-1]
        removed_sum += removed
        pokemon_distances[-1] = pokemon_distances[0]
    else:
        removed = pokemon_distances.pop(index)
        removed_sum += removed


    for i in range(len(pokemon_distances)):
        if pokemon_distances[i] <= removed:
            pokemon_distances[i] += removed
        else:
            pokemon_distances[i] -= removed

print(removed_sum)