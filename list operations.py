list1 = []
for i in range(int(input())):
    input_string = input().split(" ")
    if input_string[0] == "insert":
        list1.insert(int(input_string[1]), int(input_string[2]))
    elif input_string[0] == "remove":
        list1.remove(int(input_string[1]))
    elif input_string[0] == "append":
        list1.append(int(input_string[1]))
    elif input_string[0] == "sort":
        list1.sort()
    elif input_string[0] == "pop":
        list1.pop()
    elif input_string[0] == "print":
        print(list1)
    elif input_string[0] == "reverse":
        list1.reverse()
        
