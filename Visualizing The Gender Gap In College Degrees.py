#!/usr/bin/env python
# coding: utf-8

# ## Introduction

# In[1]:


get_ipython().magic('matplotlib inline')
import pandas as pd
from matplotlib import pyplot

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
cb_dark_blue = (0/255,107/255,164/255)
cb_orange = (255/255, 128/255, 14/255)
stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']

fig = pyplot.figure(figsize=(18, 3))

for sp in range(0,6):
    ax = fig.add_subplot(1,6,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    
    if sp == 0:
        ax.text(2005, 87, 'Men')
        ax.text(2002, 8, 'Women')
    elif sp == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2001, 35, 'Women')
pyplot.show()


# ## Comparing across all degree categories

# In[2]:


stem_cats = ['Psychology', 'Biology', 'Math and Statistics', 'Physical Sciences', 'Computer Science', 'Engineering', 'Computer Science']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']


# In[3]:


fig = pyplot.figure(figsize = (16, 16))

#0, 3, 6, 9, 12, 15
for sp in range(0, 18, 3):
    index = int(sp/3)
    ax = fig.add_subplot(6, 3, sp+1)
    ax.plot(women_degrees["Year"], women_degrees[stem_cats[index]], c = cb_dark_blue, linewidth = 3)
    ax.plot(women_degrees["Year"], 100 - women_degrees[stem_cats[index]], c = cb_orange, linewidth = 3)
    for key, spine in ax.spines.items():
        spine.set_visible(False)
    ax.tick_params(bottom = "off", top = "off", left = "off", right = "off")
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    ax.set_title(stem_cats[index])
    
    if index == 0:
        ax.text(2003, 85, 'Women')
        ax.text(2005, 10, 'Men')
    elif index == 5:
        ax.text(2005, 87, 'Men')
        ax.text(2003, 7, 'Women')
        
        
#1, 4, 7, 10, 13, 16
for sp in range(1, 16, 3):
    index = int((sp-1)/3)
    ax = fig.add_subplot(6, 3, sp+1)
    ax.plot(women_degrees["Year"], women_degrees[lib_arts_cats[index]], c = cb_dark_blue, linewidth = 3)
    ax.plot(women_degrees["Year"], 100 - women_degrees[lib_arts_cats[index]], c = cb_orange, linewidth = 3)
    for key, spine in ax.spines.items():
        spine.set_visible(False)
    ax.tick_params(bottom = "off", top = "off", left = "off", right = "off")
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    ax.set_title(lib_arts_cats[index])
    
    if index == 0:
        ax.text(2003, 78, 'Women')
        ax.text(2005, 18, 'Men')
    

#2, 5, 8, 11, 14, 17 
for sp in range(2, 18, 3):
    index = int((sp-2)/3)
    ax = fig.add_subplot(6, 3, sp+1)
    ax.plot(women_degrees["Year"], women_degrees[other_cats[index]], c = cb_dark_blue, linewidth = 3)
    ax.plot(women_degrees["Year"], 100 - women_degrees[other_cats[index]], c = cb_orange, linewidth = 3)
    for key, spine in ax.spines.items():
        spine.set_visible(False)
    ax.tick_params(bottom = "off", top = "off", left = "off", right = "off")
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    ax.set_title(other_cats[index])
    
    if index == 0:
        ax.text(2003, 90, 'Women')
        ax.text(2005, 5, 'Men')
    elif index == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2003, 31, 'Women')

pyplot.show()


# ## Hiding x-axis labels

# In[4]:


fig = pyplot.figure(figsize = (16, 16))

#0, 3, 6, 9, 12, 15
for sp in range(0, 18, 3):
    index = int(sp/3)
    ax = fig.add_subplot(6, 3, sp+1)
    ax.plot(women_degrees["Year"], women_degrees[stem_cats[index]], c = cb_dark_blue, linewidth = 3)
    ax.plot(women_degrees["Year"], 100 - women_degrees[stem_cats[index]], c = cb_orange, linewidth = 3)
    for key, spine in ax.spines.items():
        spine.set_visible(False)
    ax.tick_params(bottom = "off", top = "off", left = "off", right = "off", labelbottom = "off")
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    ax.set_title(stem_cats[index])
    
    if index == 0:
        ax.text(2003, 85, 'Women')
        ax.text(2005, 10, 'Men')
    elif index == 5:
        ax.text(2005, 87, 'Men')
        ax.text(2003, 7, 'Women')
        ax.tick_params(labelbottom = "on")
        
#1, 4, 7, 10, 13, 16
for sp in range(1, 16, 3):
    index = int((sp-1)/3)
    ax = fig.add_subplot(6, 3, sp+1)
    ax.plot(women_degrees["Year"], women_degrees[lib_arts_cats[index]], c = cb_dark_blue, linewidth = 3)
    ax.plot(women_degrees["Year"], 100 - women_degrees[lib_arts_cats[index]], c = cb_orange, linewidth = 3)
    for key, spine in ax.spines.items():
        spine.set_visible(False)
    ax.tick_params(bottom = "off", top = "off", left = "off", right = "off", labelbottom = "off")
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    ax.set_title(lib_arts_cats[index])
    
    if index == 0:
        ax.text(2003, 78, 'Women')
        ax.text(2005, 18, 'Men')
    elif index == 4:
        ax.tick_params(labelbottom = "on")


#2, 5, 8, 11, 14, 17 
for sp in range(2, 18, 3):
    index = int((sp-2)/3)
    ax = fig.add_subplot(6, 3, sp+1)
    ax.plot(women_degrees["Year"], women_degrees[other_cats[index]], c = cb_dark_blue, linewidth = 3)
    ax.plot(women_degrees["Year"], 100 - women_degrees[other_cats[index]], c = cb_orange, linewidth = 3)
    for key, spine in ax.spines.items():
        spine.set_visible(False)
    ax.tick_params(bottom = "off", top = "off", left = "off", right = "off", labelbottom = "off")
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    ax.set_title(other_cats[index])
    
    if index == 0:
        ax.text(2003, 90, 'Women')
        ax.text(2005, 5, 'Men')
    elif index == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2003, 31, 'Women')
        ax.tick_params(labelbottom = "on")

pyplot.show()


# ## Setting y-axis labels

# In[5]:


fig = pyplot.figure(figsize = (16, 16))

#0, 3, 6, 9, 12, 15
for sp in range(0, 18, 3):
    index = int(sp/3)
    ax = fig.add_subplot(6, 3, sp+1)
    ax.plot(women_degrees["Year"], women_degrees[stem_cats[index]], c = cb_dark_blue, linewidth = 3)
    ax.plot(women_degrees["Year"], 100 - women_degrees[stem_cats[index]], c = cb_orange, linewidth = 3)
    for key, spine in ax.spines.items():
        spine.set_visible(False)
    ax.tick_params(bottom = "off", top = "off", left = "off", right = "off", labelbottom = "off")
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    ax.set_yticks([0, 100])
    ax.set_title(stem_cats[index])
    
    if index == 0:
        ax.text(2003, 85, 'Women')
        ax.text(2005, 10, 'Men')
    elif index == 5:
        ax.text(2005, 87, 'Men')
        ax.text(2003, 7, 'Women')
        ax.tick_params(labelbottom = "on")
        
#1, 4, 7, 10, 13, 16
for sp in range(1, 16, 3):
    index = int((sp-1)/3)
    ax = fig.add_subplot(6, 3, sp+1)
    ax.plot(women_degrees["Year"], women_degrees[lib_arts_cats[index]], c = cb_dark_blue, linewidth = 3)
    ax.plot(women_degrees["Year"], 100 - women_degrees[lib_arts_cats[index]], c = cb_orange, linewidth = 3)
    for key, spine in ax.spines.items():
        spine.set_visible(False)
    ax.tick_params(bottom = "off", top = "off", left = "off", right = "off", labelbottom = "off")
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    ax.set_yticks([0, 100])
    ax.set_title(lib_arts_cats[index])
    
    if index == 0:
        ax.text(2003, 78, 'Women')
        ax.text(2005, 18, 'Men')
    elif index == 4:
        ax.tick_params(labelbottom = "on")


#2, 5, 8, 11, 14, 17 
for sp in range(2, 18, 3):
    index = int((sp-2)/3)
    ax = fig.add_subplot(6, 3, sp+1)
    ax.plot(women_degrees["Year"], women_degrees[other_cats[index]], c = cb_dark_blue, linewidth = 3)
    ax.plot(women_degrees["Year"], 100 - women_degrees[other_cats[index]], c = cb_orange, linewidth = 3)
    for key, spine in ax.spines.items():
        spine.set_visible(False)
    ax.tick_params(bottom = "off", top = "off", left = "off", right = "off", labelbottom = "off")
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    ax.set_yticks([0, 100])
    ax.set_title(other_cats[index])
    
    if index == 0:
        ax.text(2003, 90, 'Women')
        ax.text(2005, 5, 'Men')
    elif index == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2003, 31, 'Women')
        ax.tick_params(labelbottom = "on")
pyplot.show()


# ## Adding a horizontal line

# In[6]:


fig = pyplot.figure(figsize = (16, 16))
#0, 3, 6, 9, 12, 15
for sp in range(0, 18, 3):
    index = int(sp/3)
    ax = fig.add_subplot(6, 3, sp+1)
    ax.plot(women_degrees["Year"], women_degrees[stem_cats[index]], c = cb_dark_blue, linewidth = 3)
    ax.plot(women_degrees["Year"], 100 - women_degrees[stem_cats[index]], c = cb_orange, linewidth = 3)
    for key, spine in ax.spines.items():
        spine.set_visible(False)
    ax.tick_params(bottom = "off", top = "off", left = "off", right = "off", labelbottom = "off")
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    ax.set_yticks([0, 100])
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha = 0.3)
    ax.set_title(stem_cats[index])
    
    if index == 0:
        ax.text(2003, 85, 'Women')
        ax.text(2005, 10, 'Men')
    elif index == 5:
        ax.text(2005, 87, 'Men')
        ax.text(2003, 7, 'Women')
        ax.tick_params(labelbottom = "on")
        
#1, 4, 7, 10, 13, 16
for sp in range(1, 16, 3):
    index = int((sp-1)/3)
    ax = fig.add_subplot(6, 3, sp+1)
    ax.plot(women_degrees["Year"], women_degrees[lib_arts_cats[index]], c = cb_dark_blue, linewidth = 3)
    ax.plot(women_degrees["Year"], 100 - women_degrees[lib_arts_cats[index]], c = cb_orange, linewidth = 3)
    for key, spine in ax.spines.items():
        spine.set_visible(False)
    ax.tick_params(bottom = "off", top = "off", left = "off", right = "off", labelbottom = "off")
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    ax.set_yticks([0, 100])
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha = 0.3)
    ax.set_title(lib_arts_cats[index])
    
    if index == 0:
        ax.text(2003, 78, 'Women')
        ax.text(2005, 18, 'Men')
    elif index == 4:
        ax.tick_params(labelbottom = "on")


#2, 5, 8, 11, 14, 17 
for sp in range(2, 18, 3):
    index = int((sp-2)/3)
    ax = fig.add_subplot(6, 3, sp+1)
    ax.plot(women_degrees["Year"], women_degrees[other_cats[index]], c = cb_dark_blue, linewidth = 3)
    ax.plot(women_degrees["Year"], 100 - women_degrees[other_cats[index]], c = cb_orange, linewidth = 3)
    for key, spine in ax.spines.items():
        spine.set_visible(False)
    ax.tick_params(bottom = "off", top = "off", left = "off", right = "off", labelbottom = "off")
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    ax.set_yticks([0, 100])
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha = 0.3)
    ax.set_title(other_cats[index])
    
    if index == 0:
        ax.text(2003, 90, 'Women')
        ax.text(2005, 5, 'Men')
    elif index == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2003, 31, 'Women')
        ax.tick_params(labelbottom = "on")
pyplot.show()


# ## Exporting to a file

# In[7]:


fig = pyplot.figure(figsize = (16, 16))

#0, 3, 6, 9, 12, 15
for sp in range(0, 18, 3):
    index = int(sp/3)
    ax = fig.add_subplot(6, 3, sp+1)
    ax.plot(women_degrees["Year"], women_degrees[stem_cats[index]], c = cb_dark_blue, linewidth = 3)
    ax.plot(women_degrees["Year"], 100 - women_degrees[stem_cats[index]], c = cb_orange, linewidth = 3)
    for key, spine in ax.spines.items():
        spine.set_visible(False)
    ax.tick_params(bottom = "off", top = "off", left = "off", right = "off", labelbottom = "off")
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    ax.set_yticks([0, 100])
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha = 0.3)
    ax.set_title(stem_cats[index])
    
    if index == 0:
        ax.text(2003, 85, 'Women')
        ax.text(2005, 10, 'Men')
    elif index == 5:
        ax.text(2005, 87, 'Men')
        ax.text(2003, 7, 'Women')
        ax.tick_params(labelbottom = "on")
        
#1, 4, 7, 10, 13, 16
for sp in range(1, 16, 3):
    index = int((sp-1)/3)
    ax = fig.add_subplot(6, 3, sp+1)
    ax.plot(women_degrees["Year"], women_degrees[lib_arts_cats[index]], c = cb_dark_blue, linewidth = 3)
    ax.plot(women_degrees["Year"], 100 - women_degrees[lib_arts_cats[index]], c = cb_orange, linewidth = 3)
    for key, spine in ax.spines.items():
        spine.set_visible(False)
    ax.tick_params(bottom = "off", top = "off", left = "off", right = "off", labelbottom = "off")
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    ax.set_yticks([0, 100])
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha = 0.3)
    ax.set_title(lib_arts_cats[index])
    
    if index == 0:
        ax.text(2003, 78, 'Women')
        ax.text(2005, 18, 'Men')
    elif index == 4:
        ax.tick_params(labelbottom = "on")


#2, 5, 8, 11, 14, 17 
for sp in range(2, 18, 3):
    index = int((sp-2)/3)
    ax = fig.add_subplot(6, 3, sp+1)
    ax.plot(women_degrees["Year"], women_degrees[other_cats[index]], c = cb_dark_blue, linewidth = 3)
    ax.plot(women_degrees["Year"], 100 - women_degrees[other_cats[index]], c = cb_orange, linewidth = 3)
    for key, spine in ax.spines.items():
        spine.set_visible(False)
    ax.tick_params(bottom = "off", top = "off", left = "off", right = "off", labelbottom = "off")
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    ax.set_yticks([0, 100])
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha = 0.3)
    ax.set_title(other_cats[index])
    
    if index == 0:
        ax.text(2003, 90, 'Women')
        ax.text(2005, 5, 'Men')
    elif index == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2003, 31, 'Women')
        ax.tick_params(labelbottom = "on")

pyplot.get_backend()
pyplot.savefig("gender_degrees.png")
pyplot.show()


# In[ ]:




