import fuzzification, inference
import numpy as np
import math

def print_result(res):
        result = ''
        if res < 1.78 :
            result = 'healthy'
        if 1 <= res <= 2.51:
            result = 'sick1'
        if 1.78 <= res < 3.25:
            result = 'sick2'
        if 1.5 <= res <= 4.5:
            result = 'sick3'
        if 3.25 <= res:
            result = 'sick4'
        return result

def calculate(input):
    points = np.linspace(0, 4, 200)
    force = fuzzification.output(input)
    sum1 = 0
    sum2 = 0
    
    for p in points:
        sum1 += p * force.output(p)
        sum2 += force.output(p)
    if math.isnan((sum1 / sum2)):
        return 0
    else:
        return print_result(sum1 / sum2)