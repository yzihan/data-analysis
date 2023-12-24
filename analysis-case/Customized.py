import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

sns.set_theme(style="darkgrid")

df = pd.read_csv('Customized.csv')

aspects = ["Helpful", "Collaborative", "Free Expression", "Bystander View", "Empathy", "Interpretations", "Learning", "Ownership", "Long-term Usage", "Over-reliance"]
periods = ["Period 1", "Period 2", "Period 3", "Period 4"]

for aspect in aspects:
	g = sns.lineplot(x="Period", y="Points",
				hue="Class",
				data=df[df["Aspect"] == aspect],
				errorbar="sd")
	g.legend_.remove()
	plt.title("Aspect: " + aspect)
	plt.savefig("Customized/" + aspect + ".png")
	plt.clf()

pvalues = [[], [], [], []]

for i, period in enumerate(periods):
	for aspect in aspects:
			control = df[df["Period"] == period]
			control = control[control["Aspect"] == aspect]
			control = control[control["Class"] == "Control"]
			control = control["Points"].values.tolist()
			test = df[df["Period"] == period]
			test = test[test["Aspect"] == aspect]
			test = test[test["Class"] == "Test"]
			test = test["Points"].values.tolist()
			statistic, pvalue = stats.kruskal(control, test)
			pvalues[i].append(pvalue)

df = pd.DataFrame(pvalues) 
df.to_csv('CustomizedPValue.csv') 