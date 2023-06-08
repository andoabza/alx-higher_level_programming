#!/usr/bin/python3
import calculator_1
a = 10
b = 5
add = calculator_1.add(a, b)
sub = calculator_1.sub(a, b)
mul = calculator_1.mul(a, b)
div = calculator_1.div(a, b)
print("{:d} + {:d} = {:d}".format(a, b, add))
print("{:d} + {:d} = {:d}".format(a, b, sub))
print("{:d} + {:d} = {:d}".format(a, b, mul))
print("{:d} + {:d} = {:d}".format(a, b, div))
