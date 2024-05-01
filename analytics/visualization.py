import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("whatweb.csv", encoding='utf-8')

print(df.columns)

country_counts = df['Country code'].value_counts(normalize=True) * 100

plt.figure(figsize=(10, 6)) 
country_counts.plot(kind='pie', autopct='%1.1f%%', startangle=240)
plt.axis('equal')  
plt.title('hosted countries')
plt.tight_layout()  
plt.show()

plt.figure(figsize=(10, 6))  
df['HTTP server'].value_counts().plot(kind='bar')
plt.xlabel('HTTP Server')
plt.ylabel('Frequency')
plt.title('Histogram of HTTP Server')
plt.xticks(rotation=45) 
plt.tight_layout()
plt.show()

country_counts = df['Framework'].value_counts(normalize=True) * 100

plt.figure(figsize=(10, 6))  
country_counts.plot(kind='pie', autopct='%1.1f%%', startangle=350)
plt.axis('equal')  
plt.title('Frameworks used')
plt.tight_layout()  
plt.show()
