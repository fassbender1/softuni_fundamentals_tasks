# # tail = input()
# # body = input()
# # head = input()
# #
# # template = [head, body, tail]
# #
# # print(template)
#
# tail = input()
# body = input()
# head = input()
#
# template = [tail, body, head]
#
# template[0], template[2] = template[2], template[0]
#
# print(template)

my_list = []

for i in range(3):
    data = input()
    my_list.append(data)

my_list[0], my_list[1], my_list[2] = my_list[2], my_list[1], my_list[0]
print(my_list)