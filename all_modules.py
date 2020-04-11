# help("modules")
# a = 12
# if a == 122:
#     raise Exception('抛出异常！')
# else:
#     print('没有异常！')
#
# def shengChengqi():
#     list1 = [3, 5, 2]
#     for i in list1:
#         yield i
#
# # 使用变量来表示一个实际的生成器对象
# scq = shengChengqi()
# print(next(scq))
# print(next(scq))
# print(next(scq))
# print(next(scq))
#
# laoliuAge = 31/10
# a = 1
# if a == 11:
#     raise Exception('这是老刘抛出的异常')
# else:
#     print('没有异常')
#
#
# b = '2'
# c = int(b) + 2
# try:
#     c = b + 2
#     print(c)
# except:
#     print('程序有点小问题，请联系管理员')

# print(list(i for i in range(0, 101, 2)))
#
# print(list(i for i in range(0, 101) if i%2 != 0))


# for i in range(1,10):
#     for j in range(1, i+1):
#         print("%d*%d=%2d"%(j, i, j*i), end=' ')
#     print('')

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}*{}={}'.format(j, i, i*j), end=' ')
#     print('')

def StringSort(data):
    startIndex=0
    endIndex=0
    count=len(data)
    while startIndex+endIndex<count:
        if data[startIndex]=='-':
            data[startIndex],data[count-endIndex-1]=data[count-endIndex-1],data[startIndex]
            endIndex+=1
        else:
            startIndex+=1
    return data
data=['-','-','+','-','+','+','-','+','+','-','-','+','-']
print(StringSort(data))
