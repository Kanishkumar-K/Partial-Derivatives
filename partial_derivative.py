#computing the partial derivative for the given function

from sympy import Symbol, Derivative
function=input("Enter a function: ")
x=Symbol('x')
y=Symbol('y')

p=partialderiv=Derivative(function,x)
p=partialderiv.doit()

q=partialderiv=Derivative(function,y)
q=partialderiv.doit()

r=partialderiv=Derivative(p,y)
r=partialderiv.doit()

s=partialderiv=Derivative(p,x)
s=partialderiv.doit()

t=partialderiv=Derivative(q,y)
t=partialderiv.doit()

print("∂f/∂x     :",p)
print("∂f/∂y     :",q)
print("∂²f/∂x²   :",r)
print("∂²f/∂x∂y  :",s)
print("∂²f/∂y²   :",t)
