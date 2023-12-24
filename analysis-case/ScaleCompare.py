import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

sns.set_theme(style="darkgrid")

df = pd.read_csv('ScaleCompare.csv')

feelings = ["RRS", "ATQ-30"]
classes = ["Control", "Test"]
times = ["After - Before", "One week later - After"]



for feeling in feelings:
	for time in times:
		for classe in classes:
			mean = df.loc[(df['Class'] == classe) & (df['Negative feeling'] == feeling) & (df['Time'] == time), ['Score']].mean()
			print(feeling, classe, time, mean)

		kruskal = stats.kruskal(
			df.loc[(df['Class'] == "Control") & (df['Negative feeling'] == feeling) & (df['Time'] == time), ['Score']],
			df.loc[(df['Class'] == "Test") & (df['Negative feeling'] == feeling) & (df['Time'] == time), ['Score']]
		)
		print(feeling, time, kruskal)
