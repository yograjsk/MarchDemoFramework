list = ["a", "b", "c", "d"]

for i in range(len(list)):
    print(list[i])
    if list.index(list[i]) == len(list)-1:
    # if i.index() == len(list):
        print("click")
    else:
        print("hover")

def myFunc(*args):
    for i in range(len(args)):
        print(args[i])
        if args.index(args[i]) == len(args)-1:
        # if i.index() == len(list):
            print("click")
        else:
            print("hover")

myFunc("a", "b", "c", "d")
myFunc(list)