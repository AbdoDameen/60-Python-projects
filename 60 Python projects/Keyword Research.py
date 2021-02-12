import pandas

from pytrends.request import TrendReq
import matplotlib.pyplot as plt

trends =TrendReq()
trends.build_payload(kw_list=["Data Science"])
data = trends.interest_by_region()
print(data.sample(10))



df = data.sample(15)
df.reset_index().plot(x="geoName", y="Data Science", figsize=(12, 8), kind="bar")
plt.show()
