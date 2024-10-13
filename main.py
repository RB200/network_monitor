import os
import time
import plotly_express as px
import pandas as pd
import statistics
import random


curTime = time.time()

#stream = os.popen("ping google.com -n 20 -4 -w 10000")
#output = stream.read()
results = []
for i in range(10):
    results.append(random.randint(1,10))
#for s in output.split(" "):
    #if "ms" in s and "time=" in s:
        #results.append(s.split("=")[1].split("ms")[0])

print(results)
d = {}
d.update({'col1':[1,2,3,4,5,6,7,8,9,10],'Average':results})
df = pd.DataFrame(data=d,index=[1,2,3,4,5,6,7,8,9,10])

fig = px.line(df,x="col1",y="Average")
fig.show()
print(df)
    