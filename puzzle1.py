total = 0
counter = 0
list = []

# Sum every elf calories and store inside a list
with open("puzzle1.list") as f:
  for line in f:
    if line == "\n":
      total = 0
    else: 
      list.append(None)
      total += int(line.strip())
      list[counter] = total
      counter += 1

# Find the largest value in the list and return the index
max_calories = max(list)
index = list.index(max_calories)
print("Elf", index+1, "has the most calories! It has", max_calories, "calories!")