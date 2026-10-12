s = "Hellooo"
duplicates = []

for hi in s:
    if s.count(hi) > 1 and hi not in duplicates:
        duplicates.append(hi)

print(duplicates) 