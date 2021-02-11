import pandas
import numpy
import seaborn
import collections
import matplotlib.pyplot as plt


rainfall = pandas.read_csv("Seattle2014.csv")['PRCP'].values
inches = rainfall/254
print(inches.shape)

seaborn.set()
plt.hist(inches, bins=40)
#plt.show()

print("Number of days without rain: ", numpy.sum(inches==0))
print("Number of days with rain: ", numpy.sum(inches !=0))
print("days  with more than 0.5 inches or rain: ", numpy.sum(inches > 0.5))
#print("days  with less than 0.1 inches or rain: ", numpy.sum((inches > 0 ) &amp; (inches < 0.2)))

print("Rainy days with &lt; 0.1 inches:", numpy.sum((inches > 0) & (inches < 0.2)))
