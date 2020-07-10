n = int(input())
my_dict = {}
for i in range(n):
    data = list(input().rstrip().split())
    my_dict[data[0]] = data[1]

my_dict_keys = my_dict.keys()

while(True):
    try:
        name = input()
        if name in my_dict_keys:
            print(name+"="+my_dict[name])
        else:
            print("Not found")
    except:
        break
