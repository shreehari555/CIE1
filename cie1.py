# -*- coding: utf-8 -*-
"""CIE1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TPzlQf60N85pCdwdi01cFGmLweVm5dwb
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/content/mtcars.csv')
plt.hist(df['mpg'],bins=10,edgecolor='k')
plt.title("Histogram of MPG")
plt.xlabel("MPG")
plt.ylabel("Frequency")
plt. grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/content/mtcars.csv')
transmission_counts = df['am'].value_counts()
transmission_counts.plot(kind='bar')
plt.title("Frequency Distribution of Transmission Type")
plt.xlabel('Transmission Type')
plt.ylabel("Frequency")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/content/mtcars.csv')
plt.scatter(df['mpg'],df['wt'],color="blue")
plt.title('Scatter Plot')
plt. xlabel('mpg')
plt.ylabel('wt')
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df=pd. read_csv('/content/mtcars.csv')
plt. boxplot(df['mpg'])
plt.title("Boxplot")
plt.xlabel("MPG")
plt.show()

import pandas as pd
series_A = pd.Series([1, 2, 3, 4, 5])
series_B = pd.Series([2, 4, 6, 8, 10])
notcommon_items = pd.Series(list(set(series_A) & set(series_B)))
print(notcommon_items)