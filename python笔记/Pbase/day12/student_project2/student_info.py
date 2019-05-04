# student_info.py


def input_student():
    lst = []  # 创建一个空列表用于存储学生的信息(字典)
    while True:
        n = input("请输入学生姓名: ")
        if not n:
            break
        a = int(input("请输入学生年龄: "))
        s = int(input("请输入学生成绩: "))
        # 创建一个新的字典
        d = {'name': n,
             'age': a,
             'score': s
            }
        lst.append(d)  # 把字典放入列表中
    return lst  


def output_studnet(lst):
    print("+-----------+--------+---------+")
    print("|   name    |  age   |  score  |")
    print("+-----------+--------+---------+")
    
    for d in lst:  # d绑定学生信息的字典
        info = "| %9s | %6d | %7d |" % (
            d['name'], d['age'], d['score']
            )
        print(info)

    print("+-----------+--------+---------+")


# L = input_student()  # 输入学生信息形成字典列表
# print(L)
# output_studnet(L)  # 打印学生信息表格

def show_menu():
    print("1) 添加学生")
    print("2) 显示")
    print("q) 退出")

def main():
    docs = []  # 此列表用于存储所有学生的信息
    while True:
        # 显示菜单
        show_menu()
        # 让用户做出选择
        s = input("请选择: ")
        # 根据用户做出的选择处理相应的事情
        if s == 'q':
            return
        if s == '1':
            docs += input_student()
        elif s == '2':
            output_studnet(docs)
        # elif .....:
        #     以下同学们自己完成


main()
