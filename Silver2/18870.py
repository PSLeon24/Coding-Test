import sys

input = sys.stdin.readline
n = int(input())
coordinates = list(map(int, input().split()))
sorted_coordinates = list(set(coordinates))
sorted_coordinates.sort()
hash_coordinates = {sorted_coordinates[i]: 0 for i in range(len(sorted_coordinates))}

for i in range(len(sorted_coordinates)):
    if sorted_coordinates[i] in hash_coordinates:
        hash_coordinates[sorted_coordinates[i]] = i

for i in range(len(coordinates)):
    coordinates[i] = hash_coordinates[coordinates[i]]

print(*coordinates)

# for i in range(len(coordinates)):
#     for j in range(len(sorted_coordinates)):
#         if coordinates[i] > sorted_coordinates[j]:
#             child[i] += 1

# print(*child)
