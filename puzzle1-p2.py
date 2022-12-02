total = 0
counter = 0
list1 = []

# Part 1
# ******

# Sum every elf calories and store inside list1
with open("puzzle1.list") as f:
  for line in f:
    if line == "\n":
      total = 0
    else: 
      list1.append(None)
      total += int(line.strip())
      list1[counter] = total
      counter += 1

# Find the largest value in the list1 and return the index
max_calories = max(list1)
index = list1.index(max_calories)
print("Elf", index+1, "has the most calories! It has", max_calories, "calories!")

# Part 2
# ******

# Create another list and sort it to determine top 3 calory carrying elves
list2 = list(list1)
list2.sort(reverse=True)
print("Top three calory carrying elves are:", list2[0:3])
print("In total, they carry",sum(list2[0:3]),"calories")