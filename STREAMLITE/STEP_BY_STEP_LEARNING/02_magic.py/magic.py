
import streamlit as st
import pandas as pd

df : pd.DataFrame = pd.DataFrame({'col1': [1,2,3],'col2':list('abc')})
# isy ak dataframe banai ak calendar ki trha
df  # 👈 Draw the dataframe

# 👉 Is line me kya ho raha hai?
# 🔹 df ek table (DataFrame) ban rahi hai jisme do columns hain:

# col1: 1, 2, 3
# col2: 'a', 'b', 'c'
# ✅ Streamlit ka fayda ye hai ke agar tum sirf df likho, to wo automatically table bana kar show kar dega! 📝
x : int = 100


'x', x  # 👈 Draw the string 'x' and then the value of x
# 📌 Yani Streamlit yahan tuple ko print kar raha hai, bina print() likhne ke.
# 📌 Tuple ka structure: ('text', value) → isme pehli cheez string aur doosri value hoti hai.

# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np

#  numpy ka use ho raha hai ek random data generate karne ke liye.
# 🔹 matplotlib ka use ho raha hai ek histogram chart banane ke liye.


arr = np.random.normal(1, 1, size=100)
# Syntax: np.random.normal(mean, standard deviation, size)

# mean = 1 → Data ka center 1 hoga.
# standard deviation = 1 → Data zyada dur nahi hoga.
# size = 100 → 100 random numbers generate honge.



fig, ax = plt.subplots()
# 🔹 fig ko likhne se Streamlit automatic chart show kar deta hai. 📊
ax.hist(arr, bins=30)

# arr → Ye data hai jo histogram me use hoga.
# bins=30 → 30 parts me divide kar raha hai data ko.
# Matlab 30 columns ya bars banengi.
# Bins jitni zyada hongi, utna detailed histogram hoga.

fig  # 👈 Draw a Matplotlib chart

# ***********ak trha sy yha ak chart taiyar hora he ************

'# Pakistan zinda bad'
# (# ka matlab hai h1 heading).

# hello world
'''
# This is the document title

This is some _markdown_.
'''