#             0      1      2       3       4 = 5 - 1
#            -5      -4     -3      -2        -1
from Day_4.demo import last_in_line

friends = ["hoang", "an", "minh", "tien", "trinh"]

print(friends[2])
print(len(friends))
print(friends[len(friends) - 1])
print(friends[-3])
print(friends[-len(friends)])
friends.append("tuan")
print(friends)
friends.remove("an")
print(friends)
del friends[2]
print(friends)
friends.extend(["ngoc", "thu", "trung", "lam", "phat", "hao", "trang", "long", "khai", "tuyet"])
print(friends)
friends.insert(-1000, "vu")
print(friends)

friends.reverse()
print(friends)
friends.sort()
print(friends)
print(friends.pop())
print(friends)

print(friends.count("ngoctrinh"))
print(friends.index("phat"))
print(friends.copy() is friends)
# array[start:stop:step]
print(friends[:3])
print(friends[-5:])
print(friends[1:-1])

