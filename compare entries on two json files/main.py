import json

file_a = json.load(open("input/file1.json", "r"))
file_b = json.load(open("input/file2.json", "r"))
non_matches = []
output = []


for a in file_b:
    x = int(a)
    match = False
    for b in file_a["response"]["badges"]:
        if x == int(b["appid"]):
            match = True
    if match == False:
        non_matches.append(x)

print(non_matches)
print(len(non_matches))

with open("output.json", "w") as f:
    json.dump(non_matches, f)