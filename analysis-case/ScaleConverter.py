import pandas as pd

df = pd.read_csv('ScaleQuestionnaire.csv')
df.reset_index()

li = []

negatives = ["RRS", "Depression-PHQ-9", "Anxiety-GAD-7", "ATQ-30"]
times = ["Before", "After", "1-week"]
columns = ["Class", "Negative feeling", "Time", "Score"]

for i, row in df.iterrows():
	for j in range(15):
		for k in range(3):
			li.append([("Control" if i < 4 else "Test"), negatives[i % 4], times[k], row[j * 4 + k + 1]])

df = pd.DataFrame (li, columns = columns)
df.to_csv("Scale.csv")