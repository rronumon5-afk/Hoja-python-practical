1# Print all elements of an array

arr = [10, 20, 30, 40, 50]

for x in arr:
    print(x)
#⃣ Iterate over an array using a for looppython
arr = [10, 20, 30, 40, 50]

for i in range(len(arr)):
    print(arr[i])
#3️⃣ Iterate over an array using a while looppython
arr = [10, 20, 30, 40, 50]

i = 0
while i < len(arr):
    print(arr[i])
    i += 1
#4 Change all elements of an array to their squarepytho
arr = [2, 3, 4, 5]

for i in range(len(arr)):
    arr[i] = arr[i] ** 2

print(arr)   # [4, 9, 16, 25]
#5️⃣ Count how many elements are greater than a given numberpython
arr = [10, 25, 30, 5, 40]
num = 20

count = 0
for x in arr:
    if x > num:
        count += 1

print("Count:", count)   # 3
#6️⃣ Find the last element of an array without using [-1]python
arr = [10, 20, 30, 40, 50]

last = arr[len(arr) - 1]
print("Last element:", last)   # 50
#7️⃣ Print elements in reverse orderpython
arr = [10, 20, 30, 40, 50]

for i in range(len(arr) - 1, -1, -1):
    print(arr[i])
#8️⃣ Swap the first and last element of an arraypython
arr = [10, 20, 30, 40, 50]

arr[0], arr[-1] = arr[-1], arr[0]
print(arr)   # [50, 20, 30, 40, 10]
#9️⃣ Replace all occurrences of a given element with another value

arr = [1, 2, 3, 2, 4, 2]
old = 2
new = 99

for i in range(len(arr)):
    if arr[i] == old:
        arr[i] = new

print(arr)   # [1, 99, 3, 99, 4, 99]
#🔟 Create a new array containing only the first half

arr = [10, 20, 30, 40, 50, 60]

half = arr[:len(arr)//2]
print(half)   # [10, 20, 30]

