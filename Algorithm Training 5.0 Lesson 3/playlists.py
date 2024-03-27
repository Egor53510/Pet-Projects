n = int(input())
playlists = {}
for i in range(n):
    l = int(input())
    playlists[i] = list(map(str, input().split()))

common_values = set(playlists[next(iter(playlists))])
for key in playlists:
    common_values = common_values.intersection(playlists[key])


print(len(common_values))
print(" ".join(list(sorted(common_values))))