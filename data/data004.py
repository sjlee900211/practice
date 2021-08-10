import matplotlib.pyplot as plt
import numpy as np

english_scores = np.array(df['english'])
# 캔버스 생성
# figsize로 가로 세로 크기 지정
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

freq, _, _ = ax.hist(english_scores, bins = 10, range=(0, 100))
ax.set_xlabel('score')
ax.set_ylabel('person number')
ax.set_xticks(np.linspace(0, 100, 10+1))
ax.set_yticks(np.arange(0, freq.max()+1))
plt.show()

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
freq,_,_=ax.hist(english_scores, bins = 25, range = (0, 100))
ax.set_xlabel('score')
ax.set_ylabel('person number')
ax.set_xlicks(np.linspace(0,100,25+1))
ax.set_yticks(np.arange(0, freq.max()+1))
plt.show()

fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()

weights = np.ones_like(english_scores)/ len(english_scores)
rel_freq,_,_= ax1.hist(english_scores, bins=25, range=(0,100), weights=weights)

cum_rel_freq = np.cumsum(rel_freq)
class_value = [(i+(i+4))//2 for i in range(0,100,4)]

ax2.plot(class_value, cum_rel_freq,
         ls='--', marker='o', color='gray')
ax2.grid(visible=False)

ax1.set_xlabel('score')
ax1.set_ylabel('relative frequency')
ax2.set_ylabel('cumulative relative frequency')
ax1.set_xticks(np.linspace(0,100,25+11))

plt.show()

fig = plt.figure(figsize=(5,6))
ax=fig.add_subplot(111)
ax.boxplot(english_scores, labels=['english'])

plt.show()