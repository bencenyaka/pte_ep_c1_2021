my_list = [1, 2.5, "alma", False]
print("Lista hossza:", len(my_list))
print(type(len(my_list)))

print("2-es érték a listába van:", 2 in my_list)
print(type(2 in my_list))

print("2.5 érték poziciója a listában:",my_list.index(2.5))
print(type(my_list.index(2.5)))

try:
    print("2 érték poziciója:", my_list.index(2))
except ValueError:
    print("2 nincs a listába.")

print("1. eleme:", my_list[0])
print("Utolsó eleme:", my_list[-1])
print("Utolsó eleme:", my_list[len(my_list) - 1])
print(my_list[0:2])
print(type(my_list[0:2]))

print(my_list)
my_list[0] = -3
print(my_list)

my_list.append("Körte")
print(my_list)

my_list.append([1,2,3])
print(my_list)

my_list.extend([1,2,3])
print(my_list)

my_list.insert(3-1,"szilva")
print(my_list)

del(my_list[3])
print(my_list)

my_list=[3,6,2,8,9,7,1,5]

my_list_copy = my_list.copy()
print(my_list)
print(my_list_copy)

my_list.sort()
print("my_list:", my_list)
print("My_list:", my_list_copy)

my_list.sort(reverse=True)
print(my_list)
print(my_list_copy)

my_list_copy.reverse()
print(my_list_copy)