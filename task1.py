import numpy as np
import sympy as sy
#Your optional code here
#You can import some modules or create additional functions

# DO NOT CHANGE THE NAME OF gausslegendre() function
def gausslegendre(f, a, b, n=20):
    
    # wf is the weight multiply by the function f(y)
    wf=0 
    #X is sample point, W is weight
    X,W=np.polynomial.legendre.leggauss(n)       
    i=1
    for i in range(n):
    #Translate x values from the interval [0, 1] to [a, b]
       y= 0.5*(b-a)*X[i]+ 0.5*(a+b)
       wf = wf+ W[i]*f(y)
    return np.array(0.5*(b-a)*wf)

if __name__ == "__main__":
    def f(x):
        return (x**2 +7*x)/(1 +np.sqrt(x))**4
    
    def my_integral():
        x = sy.Symbol('x')
        ans = sy.integrate((x**2 +7*x)/(1 +sy.sqrt(x))**4, (x,0, 1))
        return ans
    
    print('Answer:                    I = ', my_integral())
    print('Your implementation gives: I = ', gausslegendre(f, 0,1))
