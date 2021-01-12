#!/usr/bin/env python
# coding: utf-8

# In[13]:


import telepot

# 봇 토큰
token= "1545683010:AAE5yCIkbuGh4z9Am0rPENKlNF1KAc06ucw"

# 보낼사람 ID
mc = "1186881443"

bot = telepot.Bot(token)
bot.sendMessage(mc, "테스트")

