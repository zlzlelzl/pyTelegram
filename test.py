#!/usr/bin/env python
# coding: utf-8

# In[13]:


import telepot

# 봇 토큰
token= ""

# 보낼사람 ID
mc = ""

bot = telepot.Bot(token)
bot.sendMessage(mc, "테스트")

