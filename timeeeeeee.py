import numpy as np
import matplotlib.pyplot as plt

#Enter TS DATA
time_series = np.array([1,
2,
3,
4,
5,
6,
7,
8,
9,
10,
11,
12,
13,
14,
15,
16,
17,
18,
19,
20
])

q = int(input("Enter value of q: "))

n = len(time_series)
Tline = np.zeros(n)

#Calc Mk values
#Odd
if len(time_series) % 2 == 1:
    for i in range(q, n - q):
        Tline[i] = np.mean(time_series[i - q:i + q + 1])
#Even
else:
    d = 2 * q
    for i in range(q, n - q):
        Tline[i] = (0.5 * time_series[i - q] + np.sum(time_series[i - q + 1:i + q]) + 0.5 * time_series[i + q]) / d


seasonal_effect = np.zeros(n)
for i in range(n):
    sum_diff = 0
    count = 0
    for j in range(-(n // q), n // q):
        if 0 <= i + j * q < n:
            sum_diff += time_series[i + j * q] - Tline[i + j * q]
            count += 1
    if count > 0:
        seasonal_effect[i] = sum_diff / count

avg_seasonality = np.mean(seasonal_effect)
adjusted_seasonal = seasonal_effect - avg_seasonality

print("Calculated Trend:", Tline)
print("Extracted Seasonality:", adjusted_seasonal)

plt.figure(figsize=(10, 6))

plt.subplot(311)
plt.plot(time_series, label="Original Data")
plt.legend(loc='upper left')

plt.subplot(312)
plt.plot(Tline, label="Trend", color='orange')
plt.legend(loc='upper left')

plt.subplot(313)
plt.plot(adjusted_seasonal, label="Seasonality", color='green')
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()
