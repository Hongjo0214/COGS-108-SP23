#!/usr/bin/env python
# coding: utf-8

# # D1 : Python Introduction & GitHub
# 
# This workbook is meant to refresh your memory on Python Programming, to get you comfortable working within a Jupyter Notebook (this week's workbook is *meant* to be programmatically-simple, and help you gain familiarity with GitHub; others will be more involved). Workbooks used in section will not be graded for correctness, but rather for effort. These are meant to get you more practice *and* help you in assignment completion. (Occasionally, they'll even use the same dataset.)
# 
# And, they are meant to be exploratory, so if you look up something or try something that's not *quite* what we asked, leave that code in there. Same goes for code that's not quite right or errors. Feel free to leave that in there and to add notes or comments for yourself (or for us). These are meant to help you get more experience with the technical content. 
# 
# Note, if you're stuck in these workbooks, you can use the COGS108 Tutorials to look information up, search on the Internet, and talk with your classmates/TA/IA.
# 
# Workbooks for discussion section will always be broken down into three parts. Sometimes you may not get through everything. That's OK! Answers will be released the following week.
# 
# In this workbook, you'll get practice with the following:
# - working in a Jupyter Notebook
# - math vs. programing variables
# - dictionaries
# - indexing
# - functions

# ## General Instructions:
# 
# Whenever you see:
# 
# ```python
# # YOUR CODE HERE
# raise NotImplementedError()
# ```
# 
# You need to **replace (meaning: delete) these lines of code with some code that answers the question**. Make sure you remove the 'raise' line when you do this (or your notebook will raise an error, regardless of any other code.
# 
# You should write the answer to the questions in those cells (the ones with `# YOUR CODE HERE`), but you can also add extra cells to explore / investigate things if you need / want to. 
# 
# Any cell with `assert` statements in it is a test cell. You should not try to change or delete these cells. Note that there might be more than one assert that tests a particular question. 
# 
# If a test does fail, reading the error that is printed out should let you know which test failed, which may be useful for fixing it.
# 
# Note that some cells, including the test cells, may be read only, which means they won't let you edit them. If you cannot edit a cell - that is normal, and you shouldn't need to edit that cell.

# ## Part I: Variables
# 
# Throughout these workbooks, there will be instructions for you to follow. Be sure that you get practice following the directions as specified. While these will not be autograded, it's good to get practice now so that you don't lose unecessary points due to lack of attention to detail in your assignments later.
# 
# There will be assert cells throughout. If you successfully accommplish the stated programming task and run the cell, the assert cell should run without a problem. However, if you make an error in your code, the assert cell may error.

# 
# **Q1. Define a list called `numbers` including the values 1-5 (inclusively)**

# In[84]:


numbers = [1, 2, 3, 4, 5]


# In[85]:


assert isinstance(numbers, list)
assert len(numbers) == 5


# **Q2. Define a tuple called `letters` that contains the individual letters a-e (inclusively)**

# In[86]:


letters = ("a", "b","c", "d", "e")


# In[87]:


assert isinstance(letters, tuple)
assert len(letters) == 5


# Now that you've defined a few variables, let's start working with a few variables to remind ourselves of the difference between programming variables and math variables.
# 
# In algebra, the following doesn't make a whole lot of sense:
# $$x = x + 1$$
# 
# If you try to subtract 1 from each side, you're stuck with something nonsensical. However in programming, `x = x + 1` is a totally reasonable statement.
# 

# **Q3a. Define a variable x to have the value 10**

# In[89]:


x = 10


# In[90]:


assert x==10


# **Now that you've done that, run the following cell.**

# In[91]:


x = x + 1


# **Q3b. Assign what you think the value of x is now to the variable `y`**
# 
# Then run the assert statement. If you don't get an error, you're doing well on programmatic variables and how they differ from mathematical variables.

# In[93]:


y = 11


# In[94]:


assert x==y
assert x == 11
assert y == 11


# Dictionaries are a fundamental aspect to programming in Python. We'll create a dictionary here using the variables `numbers` and `letters` we already created.
# 
# **Q4. Create a Pyton dict `dictionary` where the keys are the elements in the `letters` variable and their values are the corresponding elements in `numbers`.**

# In[95]:


dictionary = dict(zip(letters, numbers))   


# In[96]:


assert sorted(dictionary.items()) == [
    ('a', 1),
    ('b', 2),
    ('c', 3),
    ('d', 4),
    ('e', 5),
]


# **Q5.** You realize you want to add a key-value pair to `dictionary`. **Add the key value par `'f':6 ` to your dictionary. Print `dictionary`**

# In[98]:


dictionary['f'] = 6


# In[100]:


assert sorted(dictionary.items()) == [
    ('a', 1),
    ('b', 2),
    ('c', 3),
    ('d', 4),
    ('e', 5),
    ('f', 6)
]


# ## Part II: Functions
# 
# In addition to knowing how to work with and operate on dictionaries, knowing how to define and write helpful functions is and incredibly important skill to have. We'll write a few simple functions here.

# **Q6. Write a function `sum_odd` that adds the values in a tuple together and then returns a boolean describing whether or not the sum of the values in the tuple is an odd number.**

# In[101]:


def sum_odd(x):
    listSum = sum(x) % 2 != 0
    return listSum


# **Q7. Use this function to determine if the sum of the `numbers` list you generated earlier is odd.** 

# In[102]:


sum_odd(numbers)


# **Q8. Create a variable `even` that would produce the value 'False' from the `sum_odd` function.**

# In[103]:


even = (1,1)


# In[104]:


assert sum_odd(even) == False


# ## Part 3: `git` and GitHub

# **Q9. Work through the [Hello World GitHub Guide](https://guides.github.com/activities/hello-world/), carrying out all 5 steps**, being sure to understand what you're doing in each step. Note that we won't *actually* know if you do this or not; however, completing and understanding this guide will help you complete A1. So, if git and GitHub are new to you, please do this! (If you're already familiar with GitHub, then you could skip this part.)

# **If you've worked through this workbook with ease and have full understanding of what was going on in each step, feel free to help out a classmate or move on to completing A1.**
