import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# October 2024 & 2025

# Soybeans 
soybeans_oct = {
    "China": [17070161, 5931978],
    "Mexico": [3879430, 4376494],
    "EU-27": [3599600, 3923900],
    "Egypt": [1629968, 3316889],
    "Japan": [1582041, 1910346],
    "Indonesia": [2134640, 1742046],
    "Bangladesh": [342266, 1179635],
    "Taiwan": [728323, 1024339],
    "Pakistan": [1291, 946658],
    "Vietnam": [723424, 876151]
}

# Corn 
corn_oct = {
    "Mexico": [20742297, 21713689],
    "Japan": [10599844, 12597390],
    "South Korea": [2394291, 6567850],
    "Colombia": [5678086, 6534087],
    "EU-27": [1354739, 4005084],
    "Taiwan": [1531704, 2507648],
    "Guatemala": [917750, 1440225],
    "Canada": [1865792, 1297505],
    "Vietnam": [5093, 1190436],
    "Honduras": [872174, 971975]
}

# Wheat 
wheat_oct = {
    "Mexico": [3162123, 3735788],
    "South Korea": [1557054, 2119643],
    "Philippines": [2328366, 2063016],
    "Japan": [1713358, 1858329],
    "Nigeria": [452493, 1386329],
    "Indonesia": [674266, 891204],
    "Colombia": [408949, 846574],
    "Taiwan": [892804, 809688],
    "Vietnam": [425547, 744455],
    "Thailand": [538130, 740653],
    "World Total": [18515601, 21147041]
}

# November 2024

# Soybeans 
soybeans_nov = {
    "China": 23185841,
    "Mexico": 4349898,
    "EU-27": 4858609,
    "Egypt": 1971908,
    "Japan": 1742776,
    "Indonesia": 2337326,
    "Bangladesh": 544643,
    "Taiwan": 985613,
    "Pakistan": 2146,
    "Vietnam": 880155
}

# Corn 
corn_nov = {
    "Mexico": 23031350,
    "Japan": 11269501,
    "South Korea": 2533426,
    "Colombia": 6263717,
    "EU-27": 1539106,
    "Taiwan": 1614387,
    "Guatemala": 999842,
    "Vietnam": 76093,
    "Canada": 1999924,
    "Honduras": 972061
}

# Wheat 
wheat_nov = {
    "Mexico": 3363998,
    "South Korea": 1673668,
    "Philippines": 2530313,
    "Japan": 1883247,
    "Nigeria": 452493,
    "Indonesia": 674778,
    "Taiwan": 972780,
    "Colombia": 450421,
    "Vietnam": 427361,
    "Thailand": 599137
}

#Soyabeans Oct graph Horizontal Bar Graph 
def october_soy_graph():
    soy_countries = list(soybeans_oct.keys())
    soy_2024 = [soybeans_oct[c][0] for c in soy_countries]
    soy_2025 = [soybeans_oct[c][1] for c in soy_countries]
    y = np.arange(len(soy_countries))
    plt.barh(y, soy_2024, color='skyblue', label='2024')
    plt.barh(y, soy_2025, color='orange', left=soy_2024, label='2025')  
    plt.yticks(y, soy_countries)
    plt.ticklabel_format(style='plain', axis='x') 
    plt.xlabel('Metric Tons')
    plt.title('Soybean Exports: October 2024 vs 2025')
    plt.legend()
    plt.show()

#Corn Bar graph October Vertical 
def october_corn_graph():
    corn_countries = list(corn_oct.keys())
    corn_2024 = [corn_oct[c][0] for c in corn_countries]
    corn_2025 = [corn_oct[c][1] for c in corn_countries]
    x = np.arange(len(corn_countries))
    width = 0.25
    plt.bar(x - width/2, corn_2024, width=0.3, color='lightgreen', label='2024')
    plt.bar(x + width/2, corn_2025, width=0.3, color='coral', label='2025')  
    plt.xticks(x, corn_countries, rotation=45, ha='right')
    plt.ticklabel_format(style='plain', axis='y')  
    plt.ylabel('Metric Tons')
    plt.title('Corn Exports: October 2024 vs 2025')
    plt.legend()
    plt.show()

#October Wheat Line Graph
def october_wheat_graph():
    wheat_countries = list(wheat_oct.keys())
    wheat_2024 = [wheat_oct[c][0] for c in wheat_countries]
    wheat_2025 = [wheat_oct[c][1] for c in wheat_countries]
    plt.figure(figsize=(12,6))
    for i, country in enumerate(wheat_countries):
        plt.plot([2024, 2025], [wheat_2024[i], wheat_2025[i]], marker='o', label=country)
    plt.xticks([2024, 2025])
    plt.ylabel('Metric Tons')
    plt.title('Wheat Exports: October 2024 vs 2025')
    plt.legend()
    plt.ticklabel_format(style='plain', axis='y') 
    plt.show()


#-----------------------------
#November Graphs
#----------------------------- 

#November 2024 Soyabeans Pie Chart 
def november_soy_graph():
    soy_countries_nov = list(soybeans_nov.keys())
    soy_values_nov = list(soybeans_nov.values())
    plt.pie(soy_values_nov, startangle=140)
    plt.title('Soybean Exports: November 2024')
    plt.legend(soy_countries_nov, title="Countries")
    plt.show()


#November 2024 Corn Bar Graph Horizontal
def november_corn_graph():
    corn_countries_nov = list(corn_nov.keys())
    corn_values_nov = list(corn_nov.values())
    y = np.arange(len(corn_countries_nov))
    plt.barh(y, corn_values_nov, color='skyblue', label='2024')
    plt.yticks(y, corn_countries_nov)
    plt.ticklabel_format(style='plain', axis='x') 
    plt.xlabel('Metric Tons')
    plt.title('Corn Exports: November 2024')
    plt.show()

#November 2024 Wheat Area Chart
def november_wheat_graph():
    wheat_countries_nov = list(wheat_nov.keys())
    wheat_values_nov = list(wheat_nov.values()) 
    x = np.arange(len(wheat_countries_nov))
    plt.fill_between(x, wheat_values_nov, color='skyblue')
    plt.plot(x, wheat_values_nov, color='blue')
    plt.xticks(x, wheat_countries_nov, rotation=45, ha='right')
    plt.ticklabel_format(style='plain', axis='y') 
    plt.ylabel('Metric Tons')
    plt.title('Wheat Exports: November 2024')
    plt.show()

# -----------------------------
# Tkinter GUI
# -----------------------------

root = tk.Tk()
root.title("U.S. Export Graphs")

#makes october graph buttons
tk.Label(root, text="October 2024 & 2025").pack()
tk.Button(root, text="Soybeans", command=october_soy_graph, width=30, height=2).pack()
tk.Button(root, text="Corn", command=october_corn_graph, width=30, height=2).pack()
tk.Button(root, text="Wheat", command=october_wheat_graph, width=30, height=2).pack()

#makes november graph buttons
tk.Label(root, text="November 2024").pack()
tk.Button(root, text="Soybeans", command=november_soy_graph, width=30, height=2).pack()
tk.Button(root, text="Corn", command=november_corn_graph, width=30, height=2).pack()
tk.Button(root, text="Wheat", command=november_wheat_graph, width=30, height=2).pack()

root.mainloop()

