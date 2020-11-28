import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Virginia Wikipedia Page
url = 'https://en.wikipedia.org/wiki/Virginia'
page = urllib.request.urlopen(url)

# Title Page
soup = BeautifulSoup(page, 'lxml')
print(soup.title.string)

right_table=soup.find('table', class_='toccolours')
# print(right_table)

i=0
for row in right_table.find_all('tr'):
    cells=row.findAll('td')
    i+=1
print(i)

for column in right_table.find_all('tr'):
    cells = column.findAll('td')

#Array for rows and columns
A=[]
B=[]
C=[]

# Capturing Population Table
for row in right_table.findAll('tr'):
    cells=row.findAll('td')
    if len(cells)==4:
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[3].find(text=True))


# Creating the Data Frame
df=pd.DataFrame(A,columns=['Census'])
df['Population']=B
df['Percent']=C
print(df)

#Plotting
a=np.array([A[1],A[6],A[11],A[16],A[21],A[23]])
b=np.array([B[1],B[6],B[11],B[16],B[21],B[23]])
c=np.array([C[1],C[6],C[11],C[16],C[21],C[23]])

plt.figure(figsize=(10,20))
plt.plot(a, color = 'green',  linestyle = '-.', label='Census')
plt.plot(b, linewidth=5, label='Population')
plt.plot(c, color = 'red', linestyle = '--', label='Percent')
plt.title('Historical Population for Virginia', fontsize=15, fontweight='bold')
plt.legend(loc='upper left', fontsize=15)
plt.xticks(range(0,len(a)), a)
plt.xlabel('Year', fontweight='bold')
plt.ylabel('Year                                   Population                                   Percent', fontweight='bold')
plt.show()
