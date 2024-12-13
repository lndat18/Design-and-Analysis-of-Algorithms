from sympy import *
from sympy.plotting import plot

def example1():
    x = symbols('x')
    f = 2**(2**x)
    g = 2**(x**2)
    df = limit(diff(f,x)/diff(g,x),x, oo)
    return df

def example2():
    x = symbols('x')
    f = 2**(x**2)
    g = 2**(x)
    df = limit(diff(f,x)/diff(g,x),x, oo)
    return df

def example3():
    x = symbols('x')
    f = 2**(x)
    g = x**(log(x,2))
    df = limit(diff(f,x)/diff(g,x),x, oo)
    return df

def example4():
    x = symbols('x')
    f = x**(log(x,2))
    g = x**(4/3)
    df = limit(diff(f,x)/diff(g,x),x, oo)
    return df

def example5():
    x = symbols('x')
    f = x**(4/3)
    g = x*(log(x,2))**3
    df = limit(diff(f,x)/diff(g,x),x, oo)
    return df

def example6():
    x = symbols('x')
    f = x*(log(x,2))**3
    g = 2**(sqrt(log(x,2)))
    df = limit(diff(f,x)/diff(g,x),x, oo)
    return df

def main():
    print(example1())
    print(example2())
    print(example3())
    print(example4())
    print(example5())    
    print(example6())

if __name__ == '__main__':
    main()