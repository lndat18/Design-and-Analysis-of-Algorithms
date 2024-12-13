from sympy import *
from sympy.plotting import plot

def example1():
    x = symbols('x')
    f = 100**x
    g = 10**x
    df = limit(diff(f,x)/diff(g,x),x, oo)
    return df

def example2():
    x = symbols('x')
    f = 10**x
    g = x**(2.5)
    df = limit(diff(f,x)/diff(g,x),x, oo)
    return df

def example3():
    x = symbols('x')
    f = x**(2.5)
    g = (x**2)*log(x,2)
    df = limit(diff(f,x)/diff(g,x),x, oo)
    return df

def example4():
    x = symbols('x')
    f = (x**2)*log(x,2)
    g = x + 10
    df = limit(diff(f,x)/diff(g,x),x, oo)
    return df

def example5():
    x = symbols('x')
    f = x + 10
    g = sqrt(2*x)
    df = limit(diff(f,x)/diff(g,x),x, oo)
    return df

def main():
    print(example1())
    print(example2())
    print(example3())
    print(example4())
    print(example5())
    

if __name__ == '__main__':
    main()