
# import my_package as mp

# from my_package import fibo

import my_package
import my_package.math
import my_package.math.fibo as fibo

print(dir(my_package))
print(dir(my_package.math))

fibo.fib(10)
my_package.math.fibo.fib(10)