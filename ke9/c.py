
# 函数不会主动去执行，被动调用才会执行，非test开头
# a = 0 缺省值  默认值


def add(a,b):
    '''
    函数功能
    :param a: 参数a传哪些内容，实现什么功能
    :param b: 参数b传哪些内容，实现什么功能
    :return:  返回什么值
    '''
    c = a+b

    return c

f = add(a=1, b=2)
f = add(1,1)
print(f)


def add(i = 0,j = 0):
    d = i+j

    return d


g = add(i=2)
print(g)






