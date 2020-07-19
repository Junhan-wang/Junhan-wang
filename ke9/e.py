import requests

requests.get()


#*args,**kwargs,第一个是元祖形式 第二个是键值对 字典形式
def funx(k,j=0,*args,**kwargs):
    print("输出:%s"%str(args))
    print(args[0])
    print(args[1])
    print(kwargs)   #   {'a': 6, 'b': 2}
    print(kwargs["a"])
    print(k) # k没值 所以默认第一个给k
    print(j)

funx(1,2,3,4,5,a=6,b=2)


















