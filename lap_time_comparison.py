import pandas as pd
import matplotlib.pyplot as plt

# 예시 데이터 (직접 만든 샘플)
data = {
    "Driver": ["Verstappen", "Verstappen", "Verstappen",
               "Hamilton", "Hamilton", "Hamilton",
               "Leclerc", "Leclerc", "Leclerc"],
    "LapTime": [88.2, 87.9, 88.5,
                89.1, 88.7, 89.0,
                88.8, 88.6, 88.9]
}

df = pd.DataFrame(data)

# 평균 랩타임 계산
avg_lap = df.groupby("Driver")["LapTime"].mean()

print("Average Lap Times:")
print(avg_lap)

# 그래프
avg_lap.plot(kind='bar')

plt.title("F1 Driver Average Lap Time Comparison")
plt.ylabel("Lap Time (seconds)")
plt.xlabel("Driver")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("lap_time_graph.png", dpi=300)
plt.show()
