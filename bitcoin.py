#!/usr/bin/env python
# coding: utf-8

# In[1]:


from time import time
from IPython.display import clear_output
import os
import pandas as pd
from urllib.request import urlopen
import requests


# In[2]:


def URL(url):
 url=urlopen(url)
 Data=eval(url.read().decode('ascii'))
 url.close()
 return Data
def RAWURL(url):
 url=urlopen(url)
 Data=url.read()
 url.close()
 return Data


# In[3]:


prehashblock="https://blockchain.info/rawblock/"
prehashtransaction="https://blockchain.info/rawtx/"
true=True
false=False
null=0


# In[4]:


header=pd.read_csv('./raw blocks//header.csv')
try:
 CurrentBlock=pd.read_csv('./raw blocks/current.blk')
except:
 Hash=URL('https://blockchain.info/latestblock')['hash']   
 LatestBlock=URL(prehashblock+Hash)   
 CurrentBlock=header.append(LatestBlock,ignore_index=True)


# In[6]:


start=time()
_=0
while(time()-start < 300):
 _=_+1
 Hash=CurrentBlock['prev_block']
 Hash=Hash[len(Hash)-1]
 block=URL(prehashblock+Hash)
 Block=header.append(block,ignore_index=True)
 os.rename('./raw blocks/current.blk','./raw blocks/'+CurrentBlock['hash'][0]+'.blk')
 Block.to_csv('./raw blocks/current.blk',index=False)
 CurrentBlock=Block
 clear_output()
 print(f'{_} Block Done In {time()-start} Time')

