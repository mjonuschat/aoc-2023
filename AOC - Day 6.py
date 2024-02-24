#!/usr/bin/env python
# coding: utf-8

# In[6]:


INPUT = """
Time:        48     98     90     83
Distance:   390   1103   1112   1360
"""


# In[23]:


def calc(time,dist):
    for ct in range(time):
        if (time-ct)*ct > dist:
            return time - 2 * ct + 1

    return 0
def day6_puzzle1():
    inp = INPUT.strip().splitlines()
    times = list(map(int, re.findall(r"\d+", inp[0])))
    dists = list(map(int, re.findall(r"\d+", inp[1])))
    res=1
    for time,dist in zip(times,dists):
        x = calc(time, dist)
        print(x)
        res *= x

    print (f"Margin of error: {res}")

def day6_puzzle2():
    inp = INPUT.strip().splitlines()
    time = int("".join(re.findall(r"\d+", inp[0])))
    dist = int("".join(re.findall(r"\d+", inp[1])))

    res = calc(time,dist)

    print (f"Margin of error: {res}")


day6_puzzle1()
day6_puzzle2()


# In[ ]:
