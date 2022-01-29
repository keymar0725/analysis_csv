#!/usr/bin/env python
# coding: utf-8

# In[125]:


#!/usr/bin/env python3

import csv
import sys

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import pandas as pd


# In[262]:


def output_graph(file_path):
    print(f"{file_path}")
    reader = csv.reader(open(file_path))
    data = [row for row in reader]
    x = []
    y = []
    z = []
    d = []

    for row in data[1:]:
        if row[1] == '':
            continue
        x.append(float(row[1]))
        y.append(float(row[2]))
        z.append(float(row[3]))
        a = np.sqrt(float(row[1])**2 + float(row[2])**2 + float(row[3])**2)
        d.append(float(a))

    # Plot
    fig, axes = plt.subplots(2, 2, figsize=(9, 7), dpi=90)
    
    for ax, c, i, s in zip(axes.ravel(), ['orange','r','b','g'], [d,x,y,z], ['d','x','y','z']):
        ax.set_title(f"${s}$")
        ax.plot(i, '.-', color=c)
        print(s,'(mean/ error/ std)')
        print(np.mean(i), 
              '/', abs(max(i)) - np.mean(i), 
              '/', np.std(i))
        print('---')
        


# In[263]:


file2_paths = ['./csv_2/0_1.csv.converted.csv', 
              './csv_2/0_2.csv.converted.csv', 
              './csv_2/0_3.csv.converted.csv', 
             './csv_2/1_2.csv.converted.csv', 
             './csv_2/1_3.csv.converted.csv', 
             './csv_2/2_3.csv.converted.csv']


# In[265]:


output_graph(file2_paths[0])


# In[266]:


output_graph(file2_paths[1])


# In[267]:


output_graph(file2_paths[1])


# In[268]:


output_graph(file2_paths[2])


# In[269]:


output_graph(file2_paths[3])


# In[270]:


output_graph(file2_paths[4])


# In[271]:


output_graph(file2_paths[5])


# In[ ]:




