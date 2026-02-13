import pandas
import numpy
import matplotlib.pyplot as plt
import math

if (__name__ == "__main__"):
    array1 = numpy.array([x for x in range(0, 1001)])
    array2 = numpy.array([math.cos(x) for x in range(0, 1001)])
    x = pandas.Series(array1)
    y = pandas.Series(array2)

    plt.plot(x, y)
    plt.savefig("analysis.png")
