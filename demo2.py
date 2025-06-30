import math
import random
import datetime
'''
m=(4,5,6)
n=min(m)
print(n)
m1=max(m)
print(m1)

a=abs(-4.5)
print(a)
p=pow(3,2)
print(p)
p=math.sqrt(64)
print(p)
c=math.ceil(4.5)
print(c)
f=math.floor(4.5)
print(f)
p=math.pi
print(p)
f=math.factorial(5)
print(f)
s=math.fsum((4,5,56))
print(s)
l=math.log1p(13)
print(l)
l=math.log(10)
print(l)
l=math.log2(1)
print(l)
r=math.radians(10)
print(r)
s=math.sin(10)
print(s)
s=math.sinh(10)
print(s)
print(random.random())
print(random.randint(1,2))
print(random.randrange(1,10,3))
print(random.choice([3,4,5,7]))
print(random.choices((1,2,3)))
print(random.shuffle((1,2,3,4)))

r=datetime.datetime.now()
print(r)
print(r.strftime("%B"))
print(r.strftime("%b"))
print(r.strftime("%a"))
print(r.strftime("%A"))
print(r.strftime("%y"))
print(r.strftime("%Y"))
print(r.strftime("%h"))
print(r.strftime("%H"))
print(r.strftime("%I"))
print(r.strftime("%M"))
print(r.strftime("%S"))
print(r.strftime("%m"))
print(r.strftime("%D"))
print(r.strftime("%a"))
print(r.strftime("%A"))
print(r.strftime("%y"))
print(r.strftime("%Y"))
print(r.strftime("%b"))
print(r.strftime("%B"))



r=datetime.datetime.now()
print(r.strftime("%a"))
print(r.strftime("%A"))
print(r.strftime("%b"))
print(r.strftime("%B"))
print(r.strftime("%y"))
print(r.strftime("%Y"))
print(r.strftime("%H"))
print(r.strftime("%I"))
print(r.strftime("%M"))
print(r.strftime("%S"))
print(r.strftime("%m"))
print(r.strftime("%D"))
print(r.strftime("%d"))


#json
# it convert json file to python fine
import json
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)
print(type(y))

d={
    1:11,2:22
}
l=json.dumps(d)
print(l)
print(type(l))

lis=[3,4,45]
d=json.dumps(lis)
print(d)
print(type(d))




# try and except
try: 
    x=4
    print(x)
except:
    print("varialbe is not found")
else:
    print("when there will no error in try block then it will execute")
finally:
    print("finally block will always execute wheather try block execute or not")

    
try:
        a=10/0
        print(a)
except NameError:
        print("variable is not find")
except:
         print("this is other type error")
  
              

price=232
quantity=4
st=f"this is a bage and its price {'expensive' if price>100 else 'non'} and quantity was {quantity}  rupes"
print(st)

price=434535
st=f"this is strig {price:,}"
print(st)
st=f"this is strig {price:<}"
print(st)

ft=" i am well"
str=f"hello teesa how are you {ft}"
print(str)

n=10
str=f"this is f string {n:.3f}"
print(str)

print(f"string {3+5}")
print(f"this is example of f string {43:.4f}")
price=4000
quantity=2
print(f"i purchase clothse which was {price:.3f} rupees and total {price+(price+quantity)}")
n=34
print(f"i will use if else statement in this serei{' positive no.' if n>0 else 'negati'}")
str="mango"
print(f"this is upper case in string {str.upper()}")
print(f"lower case {str.lower()}")
print(f"capatilize function {str.capitalize()}")
print(f"title {str.title()}")
'''



