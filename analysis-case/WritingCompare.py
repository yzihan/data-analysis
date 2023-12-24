import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import seaborn as sns
import pandas as pd

sns.set_theme(style="darkgrid")
barWidth = 0.32

df = pd.read_csv("Writing.csv")
df.reset_index()

wordTypes = ["I-words (I, me, my)", "Positive Tone", "Negative Tone"]
dataTypes = ["Control (raw data)", "Control (reframed)", "Test (raw data)", "Test (reframed)"]
lineColors = [(0.792, 0.824, 0.894), (0.792, 0.824, 0.894), (0.906, 0.835, 0.824), (0.906, 0.835, 0.824)]
lineTypes = ["--", "-", "--", "-"]
periodDrop = [[], [], [], []]
reframeDrop = [[[], []], [[], []], [[], []], [[], []]]

for i, row in df.iterrows():
	periodDrop[i % 4].append([(row[2] - row[1]) / row[1] * 100, (row[3] - row[2]) / row[2] * 100])

for i in range(4):
	for j in range(1, 4):
		reframeDrop[i][0].append((df.iloc[i + 4][j] - df.iloc[i][j]) / df.iloc[i][j] * 100)
		reframeDrop[i][1].append((df.iloc[i + 12][j] - df.iloc[i + 8][j]) / df.iloc[i + 8][j] * 100)

print(periodDrop)
print(reframeDrop)

periodDrop = np.array(periodDrop)
reframeDrop = np.array(reframeDrop)

# for i in range(3):

# 	br = []
# 	br.append(np.arange(len(periodDrop[0][0])))
# 	br.append([x + barWidth + 0.025 for x in br[0]])
# 	br.append([x + barWidth + 0.025 for x in br[1]])
# 	br.append([x + barWidth + 0.025 for x in br[2]])
	
# 	for j in range(4):
# 		plt.bar(br[j], periodDrop[i][j], color = lineColors[j], linestyle = lineTypes[j], edgecolor = "black", width = barWidth, label = dataTypes[j])
	
# 	plt.xticks([r + barWidth + 0.15 for r in range(len(periodDrop[0][0]))],
# 			['During - Before', 'After - During'])
# 	plt.title("Percent Increase: " + wordTypes[i])
# 	# plt.legend()
# 	plt.savefig("Writing/" + wordTypes[i] + " - Comparison.png")
# 	plt.clf()

for i in range(3):

	br = []
	br.append(np.arange(len(reframeDrop[0][0])))
	br.append([x + barWidth + 0.025 for x in br[0]])
	
	plt.bar(br[0], reframeDrop[i][0], color = lineColors[0], linestyle = "-", edgecolor = "black", width = barWidth, label = "Control")
	plt.bar(br[1], reframeDrop[i][1], color = lineColors[2], linestyle = "-", edgecolor = "black", width = barWidth, label = "Test")
	
	plt.xticks([r + barWidth - 0.15 for r in range(len(reframeDrop[0][0]))],
			['Before', 'During', 'After'])
	plt.title("Percent Increase: " + wordTypes[i])
	# plt.legend()
	plt.savefig("Writing/" + wordTypes[i] + " - Reframe Comparison.png")
	plt.clf()
