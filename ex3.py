new_list = [1, 2, 3, [4, 5, [6, 7]], [8,9]]
new_list = str(new_list)
# for i in new_list:
#     print(i)

def recursion(x):
    flag = 0
    for i in x:
        # print("the {} level".format(flag))
        try:
            if len(i) > 1:
                print("if condition")
                recursion(i)
            else:
                print(i)
        except:
            print(i)



#p = recursion(new_list)
# p = list(p)
#print(p)
class FileWriter:
    def __init__(self, data):
        self.data = data

    def write(data):
        with open('out.csv', 'w', encoding="UTF-8") as f:
            f.write(data)

FileWriter.write(new_list)


