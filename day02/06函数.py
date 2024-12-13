

def add(x,y=1,*args,**kwargs)->int:
    print(args)
    print(kwargs)
    return x+y

aargs = (1,2,3)
user_dic ={"name":"Hank","age":18}

# 位置参数 必须在 关键字参数 之前
add(1,1,*aargs, **user_dic)

lambda_add = lambda a,b:a+b

print(lambda_add(1,2))

def subtract(a,b)->(int,int):
    return a,b

x,y = subtract(1,2)
print(x,y)

ret = subtract(213,32)

# 是元组类型
print(type(ret))
print(ret[0])
print(ret[1])

