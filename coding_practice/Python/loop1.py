# What does the following code print?
# for i in "hello":
# if i == "l":
# continue
# print(i)
# A) heo
# B) hello
# C) helo
#  D) he
# for i in "hello":
#   if i =="l":
#     continue
#   print(i)


# What does the following code print?
# for i in "hello":
# continue at index 1
# print(i)

for index,i in enumerate("hello"):
  if index == 1:
    continue
  print(i, end="")