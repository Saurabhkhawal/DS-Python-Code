#!/usr/bin/env python
# coding: utf-8

# # Libraries in pthon

# In[1]:


#python library is a collection of function and methods that allows you to perform many actions withot your code


# In[2]:


# Single Dimensional numpy array


# In[3]:


import numpy as np  # numpy is used for numerical python  


# In[6]:


l1=[1,2,3,4] # list


# In[7]:


n1=np.array(l1) # creating array using numpy


# In[8]:


n1


# In[9]:


type(n1) # data type checking 


# In[10]:


# MultiDimensional numpy Array


# In[11]:


n2=np.array([[1,2,3,4],[4,3,2,1]]) # creating 2D array


# In[12]:


n2


# In[13]:


type(n2)


# In[14]:


# zeros method .print zeros 


# In[15]:


n3=np.zeros((2,3)) # frist parameter is row and 2nd parameter is col its print 2 by 3 array


# In[16]:


n3


# In[ ]:


# full() method use for define array with specific number


# In[17]:


n4=np.full((3,3),55) # initialize with number  3 by 3 array
n4


# In[18]:


# range use to print number in specific range thats we use np.arange


# In[19]:


n1=np.arange(50,101) # 50 is starting value and 101 is ending range
n1 # its print number from 50 to 100


# In[20]:


n2=np.arange(5,51,5) # here last parameter is increment value 
n2 # its print 5 to 50 numbers incred by every number by 5


# In[26]:


# initializng Numpy array with random numbers


# In[27]:


import numpy as np


# In[21]:


np.random.randint(100,200,10) # it print any 10 random numbers from range 100 to 200


# In[30]:


# checking shape of numpy array


# In[22]:


n1=np.array([[1,2,3,4],[4,3,2,1]])
n1


# In[23]:


n1.shape # its check which type of array includes rows and col . ex 1 by 2 or 2 by 3 etc


# In[24]:


n1.shape=(4,2) # here we update shape its change to (4,2) from (2,4)


# In[25]:


n1


# In[26]:


n1.shape=(8,1)
n1


# In[40]:


# joining numpy array


# In[41]:


# vstack its vertical stack 


# In[43]:


import numpy as np


# In[44]:


n1=np.array([1,2,3]) # creating 1st numpy array


# In[45]:


n2=np.array([4,5,6]) # creating 2nd numpy array


# In[49]:


np.vstack((n1,n2)) # its join numpy array in vertical manner


# In[51]:


np.hstack((n1,n2)) # its join numpy array in horizontal manner


# In[54]:


np.column_stack((n1,n2)) # its join numpy arrays in column vise


# In[55]:


# numpy intersection and difference 


# In[56]:


n1=np.array([1,2,3,4,5,6])


# In[57]:


n2=np.array([5,6,7,8,9])


# In[61]:


np.intersect1d(n1,n2) # intersect1d() function show the common element from n1 and n2 array


# In[63]:


np.setdiff1d(n1,n2) # its remove common element from n1 that are present in n2 


# In[65]:


np.setdiff1d(n2,n1) # its remove elements from n2 those are alsopresent in n1


# In[27]:


n1=np.array([10,20])


# In[68]:


n2=np.array([30,20])


# In[72]:


np.sum([n1,n2]) # its do addition of all element present in both array

# n1=10+20=30 , n2=30+20=50 , n1+n2=30+50=80


# In[74]:


np.sum([n1,n2],axis=0) # its add column value 10+30=40    20+20=40


# In[76]:


np.sum([n1,n2],axis=1) # its add value row vise like 10+20=30 in frist row


# In[28]:


n1


# In[29]:


n1=n1+1 # its add one in every elemnt of n1 array 


# In[81]:


n1


# # numpy math function

# In[82]:


# mean


# In[84]:


n1=np.random.randint(1,50,10) # here we take random 10 values from 1 to 50 numbers


# In[85]:


n1


# In[86]:


np.mean(n1) # here we calculate a mean of array n1


# In[87]:


# median


# In[88]:


np.median(n1) # here we calculating median of array n1 


# In[89]:


# standard deviation


# In[90]:


np.std(n1) # here we calculating standard deviation of array n1


# In[91]:


# save and load Numpy


# In[92]:


n1


# In[96]:


np.save("myarray",n1) # this function save the array with the given name. we save our array n1 as name "myarray"


# In[97]:


new_n1=np.load("myarray.npy") # this function load the saved array. here we load our array file using save file name "myarray.npy"


# In[95]:


new_n1


# # Python Pandas

# # Series

# In[1]:


import pandas as pd # importing pandas library


# In[2]:


s1=pd.Series([1,2,3,4,5]) # series is a one dimensional array and its provide index number of every element 


# In[3]:


s1


# In[104]:


type(s1)


# In[105]:


# changing index 


# In[106]:


s1=pd.Series([1,2,3,4,5],index=["a","b","c","d","e"]) # here using index we providig index value to our array


# In[107]:


s1 # now index change from number to alphabets 


# In[108]:


# creating series using dictionary


# In[109]:


pd.Series({"k1":10,"k2":20,"k3":40}) # in series using dictionary we take index as key and number as values 


# In[110]:


s5=pd.Series({"k1":10,"k2":20,"k3":40},index=["k3","k1","k4","k2"]) # giving index as a index method


# In[111]:


s5


# In[112]:


# extracting indivisual element from series means calling elementlist/array 


# In[113]:


l1=[1,2,3,4,5,6,7,8,9]


# In[116]:


s1=pd.Series(l1)


# In[117]:


s1


# In[118]:


s1[4] # its extract element of index number 4


# In[121]:


s1[:5] # its extract element from  1 to 5


# In[122]:


s1[-5:] # its extract last 5 element 


# In[124]:


s1+5 # its add 5 to every indivisual element of s1 series


# In[126]:


s1+l1 # its add 2 series object to each other 


# # DataFrame

# In[132]:


pd.DataFrame({"name":["srk","msd","dhoni"],"marks":[75,100,67]}) # creating dataframe. "name","marks" are colmns and their values are rows


# In[7]:


import pandas as pd
cars=pd.read_csv("C:\\Users\\SAURABH\\Downloads\\Q7.csv") # here we reading our file 


# In[8]:


cars


# In[135]:


cars.head() # extracting starting 5 records 


# In[136]:


cars.tail() # extracting last 5 records 


# In[138]:


cars.shape # checking how many col and rows , here in our dataframe 32 rows and 4 columns 


# In[140]:


cars.describe() # its describe the statistic values of data frame like mean ,std ,count... etc 


# In[144]:


# iloc[] function
cars.iloc[0:11,2:] #  it fetch 0 to 11 rows and starting 2 col


# In[147]:


cars.loc[1:10,("Score","Weigh")] # its fetching Score and Weigh colums and 1 to 10 rows

# in loc function we directly gives coumn names .


# In[1]:


# drop fumction is used for delete the mentioned row col


# In[13]:


cars.drop("Weigh",axis=1)

# here we drop column Weigh 
# in drop() function 1st parameter is column name that u want to drop 
# and 2nd parameter is axis . is axis=1 it means u want to drop column
# if axis =0 it means u want to drop rows 


# In[15]:


# lets check how to drop rows


# In[16]:


cars.drop([1,2,3],axis=0)

# using above code we drop rows those index number are  1,2,3 
# see output 1,2,3 index number rows are not visible


# In[17]:


# pandas basic function


# In[18]:


cars # our data set that is we load above 


# In[20]:


cars.min() # fetch the minimum value from every column of data set


# In[22]:


cars.mean() # its calculate mean/average  value of every column of data set


# In[23]:


cars.median() # its calculate median value of every column of data set


# In[24]:


cars.max # fetch the maximum value from every column of data set


# In[25]:


cars.std() # its calculate standard deviation 


# In[26]:


# some additonal function of pandas


# In[27]:


cars.head()


# In[28]:


def double_make(s): # here we make a one method that double our colun value 
    return s*2


# In[29]:


cars[["Points","Score","Weigh"]].apply(double_make) 

# 1st parameter is column name that on we apply our method . 
# and last apply method .
# befor applying this method our data be like
# in points 1)3.90 ,after aplying method its become a  7.80


# In[30]:


# lets make a half 
def half(s):
    return s*0.5


# In[31]:


cars[["Points","Score"]].apply(half) # its half all the elements that are present in the col Poits and Score


# In[32]:


cars


# In[35]:


cars.sort_values(by="Points") # it is sort the Points column


# # Python Matplotlib

# In[36]:


# pyhton matplotlib is a library used for data visulization 


# In[37]:


# Line Plot


# In[38]:


import numpy as np # importing numpy for array


# In[39]:


from matplotlib import pyplot as plt # or (import matplotlib.pyplot as plt):- importing pyplot from matplotlib 


# In[41]:


x=np.array([1,2,3,4,5,6,7,8,9,10]) # creating 1st array
x


# In[42]:


y= 3*x # creating 2nd array 
y


# In[47]:


plt.plot(x,y) # for creating plot 1st parameter is x-axis and 2nd parameter is y-axis 
plt.title("Line Plot") # its give the title to plot
plt.xlabel("x-label") # it gives the name to x axis
plt.ylabel("y-label") # it gives the name to y axis 
plt.show() # its show the line plot 


# In[48]:


plt.plot(x,y,color="g",linestyle=":",linewidth=5) # for creating plot

# color attribute set a color to line .
# linestyle= ":" colon symbol this attribute set the style to line here we put doted
# linewidth attribute set the width of line 

plt.title(" x vs y") # its give the title to plot
plt.xlabel("x axis") # it gives the name to x axis
plt.ylabel("y axis ") # it gives the name to y axis 
plt.show() # its show the line plot 


# In[49]:


# two lines in one plot


# In[50]:


x


# In[51]:


y1=2*x
y1 # we create y1 array for 1st line


# In[52]:


y2=3*x
y2 # we create y2 array for 2nd line 


# In[55]:


plt.plot(x,y1,color="g",linestyle=":") # this line between x axis and y1 axis
plt.plot(x,y2,color="r",linewidth=4) # this line between x axis and y2 axis
plt.title("Two lines in ne plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True) # it set the grid to plot (means square square to background for beter understanding )
plt.show()


# In[1]:


# In above example with draw 2 lines in single plot 


# In[4]:


# subplot
import numpy as np # importing numpy library as a np
from matplotlib import pyplot as plt # importing pyplot from matplotlib 


# In[5]:


x=np.arange(1,11) # here we take a array between 1 to 10 using a range function
x


# In[10]:


y1=2*x # this 1st y axis
y1


# In[11]:


y2=3*x # this 2nd y axis
y2


# In[18]:


plt.subplot(2,1,1) # (2,1,1) parameter indicates 2 rows and 1 column and last 1 show it is 1st subplot
plt.plot(x,y1,color="g",linestyle=":")


plt.subplot(2,1,2) # (2,1,2) parameter indicates 2 rows and 1 column and last 2 show it is 2nd subplot
plt.plot(x,y2,color="r",linewidth=4)
plt.title("Two sub plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)
plt.show()

# its print the two subplots


# # Barplot

# Barplot used for categorial data

# In[12]:


import numpy as np
from matplotlib import pyplot as plt # importing numpy and matplotlib


# In[25]:


player={"msd":65,"virat":50,"jaddu":76,"raina":85} # creating 1 dictionary 


# In[26]:


names=list(player.keys()) # here we store key of player dictonary as a list in "names" variable


# In[27]:


names


# In[28]:


run=list(player.values()) # here we store values of player dictonary as a list in "run" variable


# In[29]:


run


# In[46]:


plt.bar(names,run) # plt.bar used for display barplot. here names is x-axis and run is y-axis
plt.xlabel("Players name")
plt.ylabel("Players run")
plt.title("Run Board")
plt.grid(True)
plt.show()


# In[49]:


plt.barh(names,run,color="g") # "plt.barh" used for display horizontal barplot. here names is x-axis and run is y-axis and color="g" for green color
plt.xlabel("Players name")
plt.ylabel("Players run")
plt.title("Run Board")
plt.grid(True)
plt.show()


# # Scatter Plot

# In[50]:


x=[4,2,5,7,2,4,6,2,7,9]
y=[9,3,5,1,8,5,4,3,7,1]
# here we created 2 list


# In[51]:


plt.scatter(x,y) # for displaying scatter plot we use this function and parameter x and y axis 
plt.show()


# In[59]:


x=[10,20,30,40,50,60,70,80,90]
y=[8,2,4,5,7,2,5,9,3]
plt.scatter(x,y,marker="*",c="g",s=200)
plt.show()

# "marker" use for changeing symbol of points
# c: use for color attribute
# s: use for changing size of points 


# In[61]:


# two scatter plot in one graph

x=[10,20,30,40,50,60,70,80,90]
y=[8,2,4,5,7,2,5,9,3]
z=[4,6,3,7,9,2,4,5,9]
plt.scatter(x,y,marker="*",c="g",s=100) # 1st scatter plot ingreen color star
plt.scatter(x,z,c="r",s=200) # 2nd scatter plot in red color dots format 
plt.show()


# In[62]:


# subplot : diffrentiate 2 scatter plot 

x=[10,20,30,40,50,60,70,80,90]
y=[8,2,4,5,7,2,5,9,3]
z=[4,6,3,7,9,2,4,5,9]
plt.subplot(1,2,1) # here 1st and 2nd parameter is x and y axis , last parameter is subplot 1 
plt.scatter(x,y,marker="*",c="g",s=100)
plt.subplot(1,2,2) # here 1st and 2nd parameter is x and y axis , last parameter is subplot 2
plt.scatter(x,z,c="r",s=200)
plt.show()


# # Histogram

# Histogram used for numerical values

# In[65]:


data=[2,2,2,2,4,4,5,4,7,6,7,7,3,4]


# In[72]:


plt.hist(data,color="r")# plt.hist() functon use for histogram 
plt.show()

# following histogram shows the frequncys ex.. 2 comes 4 times thats why its frequncy is 4 show in -axis.


# Hitogram working with dataset

# In[74]:


import pandas as pd
cars=pd.read_csv("C:\\Users\\SAURABH\\Downloads\\Q7.csv") # here we working with our dataset


# In[75]:


cars.head()


# In[77]:


plt.hist(cars["Points"],color="r") # here we passing our colum from dataset as parameter
plt.show()


# # BoxPlot

# In[78]:


one=[1,2,3,4,5,6,7,8,9]
two=[1,2,3,4,5,4,3,2,1]
three=[6,7,8,9,8,7,6,5,4]

# here we create 3 list for three boxplot


# In[80]:


data=list([one,two,three]) # we store our three list in data varable 


# In[81]:


plt.boxplot(data) # using it we create our boxplot 
plt.show()


# # Violin plot

# In[82]:


one=[1,2,3,4,5,6,7,8,9]
two=[1,2,3,4,5,4,3,2,1]
three=[6,7,8,9,8,7,6,5,4]


# In[83]:


data=list([one,two,three]) # passing three list 


# In[86]:


plt.violinplot(data,showmedians=True)
plt.show()

# plt.violianplot used for printing violinplot
# showmedians=True parameter used for displaying median 


# # Pie-Chart

# In[87]:


fruit=['Apple','Orange','Mango','Guava']


# In[88]:


quantity=[10,5,20,8]


# In[89]:


plt.pie(quantity,labels=fruit) # 1st parameter is numerical list (quantity) & 2nd is string (fruit)
plt.show()


# In[90]:


fruit=['Apple','Orange','Mango','Guava']


# In[91]:


quantity=[10,5,20,8]


# In[94]:


plt.pie(quantity,labels=fruit,autopct="%0.1f%%",colors=["yellow","blue","red","green"]) 
plt.show()

# here labels used for giving names for particular item and here we givs name fruits list to our label
# autopct="%0.1f%%" use for showning data in percentage
# colors[] attribute used for giving particular color to particular item 


# # DoughNut-Chart

# pronaunce as डोनट chart

# In[95]:


fruit=['Apple','Orange','Mango','Guava']
quantity=[10,5,20,8]


# In[98]:


plt.pie(quantity,labels=fruit,radius=2)  # radius gives for outside circle size
plt.pie([100],radius=1,colors=['w']) # it is inside circle 
plt.show()

