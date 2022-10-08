#code1 func

name="A"
wt=68
ht= 1.62
def bmi_calc(name, ht, wt):
    bmi= wt/(ht**2)
    print("bmi:")
    print(bmi)
    if bmi<25:
        print("not overwt")
    elif 25<bmi<30:
        return name + "normal wt"
    else:
        print("overweight")

res=bmi_calc(name,ht,wt)
print(res)

#newfunc

def function1():
    print("aeiou")
    print("bcdfg")
print("outside")
function1()

def function2(x):
    return x**2

a= function2(3)
print(a)

def func3(x):
    print(x)
    print("haha")
    return 3*x
m= func3(2)
print(m)

