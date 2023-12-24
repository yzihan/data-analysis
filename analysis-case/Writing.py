import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import seaborn as sns
import pandas as pd

sns.set_theme(style="darkgrid")

df = pd.read_csv("Writing.csv")
df.reset_index()

wordTypes = ["I-words (I, me, my)", "Positive Tone", "Negative Tone", "Cognitive Processes"]
dataTypes = ["Control (raw data)", "Control (reframed)", "Test (raw data)", "Test (reframed)"]
lineColors = [mcolors.CSS4_COLORS["steelblue"], mcolors.CSS4_COLORS["steelblue"], mcolors.CSS4_COLORS["darksalmon"], mcolors.CSS4_COLORS["darksalmon"]]
lineTypes = ["--", "-", "--", "-"]
time = ["Before", "During", "After"]
mean = [[], [], [], []]
sd = [[], [], [], []]

for i, row in df.iterrows():
	for j in range(1, 4):
		mean[i % 4].append(row[j])
	for j in range(4, 7):
		sd[i % 4].append(row[j])

mean = np.array(mean)
sd = np.array(sd)

for i in range(4):
	for j in range(4):
		plt.plot(time, mean[i][j * 3 : (j + 1) * 3], color=lineColors[j], linestyle=lineTypes[j], label=dataTypes[j])
		plt.fill_between(time, mean[i][j * 3 : (j + 1) * 3] - sd[i][j * 3 : (j + 1) * 3], mean[i][j * 3 : (j + 1) * 3] + sd[i][j * 3 : (j + 1) * 3], color=lineColors[j], alpha=0.16)
	# plt.legend(title = "Class")
	plt.title("LIWC Analysis: " + wordTypes[i])
	plt.savefig("Writing/" + wordTypes[i] + ".png")
	plt.clf()
