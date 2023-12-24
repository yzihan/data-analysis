import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

from scipy import stats

sns.set_theme(style="darkgrid")

df = pd.read_csv('Nasa.csv')
 
# who v/s fare barplot
g = sns.barplot(x = 'Dimensions',
			y = 'Points',
			hue = 'Class',
			data = df,
			palette = [(0.792, 0.824, 0.894), (0.906, 0.835, 0.824)],
			errorbar = "sd",
			capsize = 0.1,
			edgecolor = "0"
			)
			
g.legend_.remove()

dimensions = ["Mental Demand", "Physical Demand", "Temporal Demand", "Performance", "Effort", "Frustration"]

for dimension in dimensions:
	control = df[df["Dimensions"] == dimension]
	control = control[control["Class"] == "Control"]
	control = control["Points"].values.tolist()
	test = df[df["Dimensions"] == dimension]
	test = test[test["Class"] == "Test"]
	test = test["Points"].values.tolist()
	print(dimension, stats.kruskal(control, test))
 
# Show the plot
plt.show()