import time
import numpy as np
import random
x=np.random.random(100000000)
start=time.time()
avg=sum(x)/len(x)
end=time.time()
print(end-start)
start=time.time()
avg=np.mean(x)
end=time.time()
print(end-start)