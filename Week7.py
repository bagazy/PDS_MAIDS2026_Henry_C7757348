# using list
import warnings

import pandas as pd
import numpy as np
warnings.filterwarnings("ignore")
product_data=[['e-book', 2000], ['plants', 6000], ['Pencil', 3000]]


#2d list, similar to 2d array
indexes=[1,2,3]
columns_name=['product', 'unit_sold']
product_df = pd.DataFrame(data=product_data, index=indexes, columns=columns_name)
print(product_df)


# using dictionaries
product_data={'product': ['e-book', 'plants', 'Pencil'], 'unit_sold':
[2000, 5000, 3000]}
product_df = pd.DataFrame(data=product_data)
print(product_df)


# using numpy array
products = np.array([['','product','unit_sold'], [1, 'E-book',2000],
[2, 'Plants', 6000], [3, 'Pencil', 3000]])
product_pf = pd.DataFrame(data=products[1:,1:],index=products[1:,0 ],
columns=products[0,1:])
print(product_pf) # output is same as of first case




import pandas as pd
df = pd.read_csv('dirtydata (2).csv')
print(df.head(10))



#Print information about the data:
print(df.info())
print(df.isna().sum())
print(df.duplicated())


#Remove Rows
import pandas as pd
df = pd.read_csv('dirtydata (2).csv')
new_df = df.dropna()
print(new_df.to_string())

#Replace Empty Values
import pandas as pd
df = pd.read_csv('dirtydata (2).csv')
df.fillna(130)
print(df.to_string())


#Replace Only For Specified Columns
import pandas as pd
df = pd.read_csv('dirtydata (2).csv')
df["Calories"].fillna(130)


#Replace Using Mean, Median, or Mode
#Mean = the average value (the sum of all values divided by number of values).
import pandas as pd
df = pd.read_csv('dirtydata (2).csv')
x = df["Calories"].mean()
df["Calories"].fillna(x)

#Median = the value in the middle, after you have sorted all values ascending
import pandas as pd
df = pd.read_csv('dirtydata (2).csv')
x = df["Calories"].median()
df["Calories"].fillna(x)


#Mode = the value that appears most frequently.
import pandas as pd
df = pd.read_csv('dirtydata (2).csv')
x = df["Calories"].mode()[0]
df["Calories"].fillna(x)


#Convert Into a Correct Format
import pandas as pd
df = pd.read_csv('dirtydata (2).csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')


#Removing Rows
df.dropna(subset=['Date'], inplace = True)


#Replacing Values
df.loc[7, 'Duration'] = 45


#Removing Rows
for x in df.index:
   if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)


#Discovering Duplicates
print(df.duplicated())

#Removing Duplicates
df.drop_duplicates(inplace = True)





import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
plt.plot(xpoints, ypoints)
plt.show()


#Default X-Points
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)
plt.show()


import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()


#The subplot() Function
#Draw 2 plots on top of each other:
import matplotlib.pyplot as plt
import numpy as np
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 1, 1)
plt.plot(x,y)


import matplotlib.pyplot as plt
import numpy as np
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 1)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 2)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 3)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 4)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 5)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 6)
plt.plot(x,y)
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')
plt.show()




import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar()
plt.show()



import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, color = "red")
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()

#With Pyplot, you can use the pie() function to draw pie charts. By default the
#plotting of the first wedge starts from the x-axis and moves counterclockwise:


import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show()



from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(size=1000), hist=False)
plt.show()


# importing packages
import seaborn as sns
# loading dataset
data = sns.load_dataset("iris")
# draw lineplot
sns.lineplot(x="sepal_length", y="sepal_width", data=data)


# importing packages
import seaborn as sns
import matplotlib.pyplot as plt



# loading dataset
data = sns.load_dataset("iris")
def graph():sns.lineplot(x="sepal_length", y="sepal_width", data=data)



# Adding the subplot at the specified
# grid position
plt.subplot(121)
graph()
# Adding the subplot at the specified
# grid position
plt.subplot(122)
graph()
plt.show()

#Using subplot2grid() method
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
# loading dataset
data = sns.load_dataset("iris")
def graph():sns.lineplot(x="sepal_length", y="sepal_width", data=data)


# adding the subplots
axes1 = plt.subplot2grid (
(7, 1), (0, 0), rowspan = 2, colspan = 1)
graph()
axes2 = plt.subplot2grid (
(7, 1), (2, 0), rowspan = 2, colspan = 1)
graph()
axes3 = plt.subplot2grid (
(7, 1), (4, 0), rowspan = 2, colspan = 1)
graph()


#Using FacetGrid() method, FacetGrid class helps in visualizing distribution of one
#variable as well as the relationship between multiple variables separately within
#ubsets of your dataset using multiple panels


# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
# loading dataset
data = sns.load_dataset("iris")
plot = sns.FacetGrid(data, col="species")
plot.map(plt.plot, "sepal_width")
plt.show()



# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
# loading dataset
data = sns.load_dataset("flights")
plot = sns.PairGrid(data)
plot.map(plt.plot)
plt.show()


#A barplot
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
# loading dataset
data = sns.load_dataset("iris")
sns.barplot(x='species', y='sepal_length', data=data)
plt.show()


# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
# loading dataset
data = sns.load_dataset("iris")
sns.boxplot(x='species', y='sepal_width', data=data)
plt.show()


#Pairplot
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
# loading dataset
data = sns.load_dataset("iris")
sns.pairplot(data=data, hue='species')
plt.show()



#Heatmap
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
# loading dataset
data = sns.load_dataset("tips")
# correlation between the different parameters
tc = data.corr()
sns.heatmap(tc)
plt.show()