#             0      1      2       3       4 = 5 - 1
#            -5      -4     -3      -2        -1

friends = ["hoang", "an", "minh", "tien", "trinh"]
print(friends[2])
print(len(friends))
print(friends[len(friends) - 1])
print(friends[-3])
print(friends[-len(friends)])
friends.append("tuan")    #add to final list
print(friends)
friends.remove("an")  #delete an
print(friends)
del friends[2]   #xoa vi tri thu 2
print(friends)
friends.extend(["ngoc", "thu", "trung", "lam", "phat", "hao", "trang", "long", "khai", "tuyet"]) #them danh sach
print(friends)
friends.insert(-1000, "vu") #chen them danh sach
print(friends)

friends.reverse() #dao thu tu danh sach
print(friends)
friends.sort()   #sap xep theo thu tu abc
print(friends)
print(friends.pop())   #lay cai danh sach o cuoi ra va xoa no
print(friends)

print(friends.count("ngoctrinh"))  # dem xem co bao nhieu ngoctrinh
print(friends.index("phat"))     #tim vi tri cua danh sach
print(friends.copy() is friends)   #fasle
# array[start:stop:step]
print(friends[:3])     #in list theo thu tu mong muon
print(friends[-5:])
print(friends[1:-1])


# t = 1, 2, 3
# t[0] = 1
# print(t)
