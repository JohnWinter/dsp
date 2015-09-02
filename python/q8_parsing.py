


import pandas

def answer(data):
    x=pandas.read_csv(data,index_col="Team")
    x['dif']=x["Goals"]-x["Goals Allowed"]
    x['dif']=abs(x['dif'])
    s=x['dif'].idxmin()

    print s

answer(r"/Users/jennilee09/ds/metis/prework/dsp/python/football.csv")