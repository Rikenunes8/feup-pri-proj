import pandas as pd

PREFIX = 'simple_'
PATH = 'solr/results/m2/'
N = 8

l = []
for i in range(1, N+1):
    df = pd.read_csv(PATH + PREFIX + 'metrics_results_' + str(i) + '.csv')
    l += [[i] + df.values.tolist()[0]]

df = pd.DataFrame(l, columns=['Query', 'Average Precision', 'Precision at 10'])
df.to_csv(PATH + PREFIX + 'metrics_results.csv', index=False)

for (a, b, c) in l:
    print(f'{a} & {b:.4f} & {c:.3f} \\\\')


