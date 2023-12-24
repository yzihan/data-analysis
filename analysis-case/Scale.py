import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme(style="darkgrid")

df = pd.read_csv('Scale.csv')

negatives = ["RRS", "ATQ-30"]

df_diff = pd.DataFrame(columns=["Class", "Negative feeling", "Time", "Score"])

for i in range(60):
	before = df.iloc[i * 3]
	after = df.iloc[i * 3 + 1]
	week = df.iloc[i * 3 + 2]
	before[3] = "After - Before"
	before[4] = (after[4] - before[4]) / before[4] * 100
	after[3] = "One week later - After"
	after[4] = (week[4] - after[4]) / after[4] * 100
	df_diff.loc[i * 2] = before
	df_diff.loc[i * 2 + 1] = after

df_diff.to_csv("ScaleCompare.csv")
quit()

for negative in negatives:
	g = sns.lineplot(x="Time", y="Score",
				hue="Class",
				data=df[df["Negative feeling"] == negative],
				errorbar="sd")
	g.legend_.remove()
	plt.title("Type of negative feeling: " + negative)
	plt.savefig("Scale/" + negative + ".png")
	plt.clf()