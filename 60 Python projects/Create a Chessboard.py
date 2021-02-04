import matplotlib.pyplot as plt
import numpy
from matplotlib.colors import LogNorm
from matplotlib.ticker import MultipleLocator
import matplotlib.ticker as plticker

dx, dy = 0.015, 0.05
x=numpy.arange(-4.0,4.0,dx)
y=numpy.arange(-4.0,4.0,dy)
X, Y = numpy.meshgrid(x, y)
extent = numpy.min(x),numpy.max(x),numpy.min(y), numpy.max(y)
z1=numpy.add.outer(range(8), range(8)) %2
plt.imshow(z1, cmap="binary_r", interpolation="nearest", extent=extent, alpha=1)
def chess(x, y):
    return(1-x / 2+x**5 + y**6)*numpy.exp(-(x**2+y**2))
z2=chess(X, Y)
plt.imshow(z2, alpha=0.6, interpolation="bilinear", extent=extent)
plt.title("CHESS BOARD")
#major_ticks=numpy.array(["A,B,C,D,E,F,G,H"])
loc = plticker.MultipleLocator(base=1.0)
#plt.xticks(major_ticks)
plt.yticks(loc)
plt.show()
