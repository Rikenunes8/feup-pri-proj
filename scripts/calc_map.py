import pandas as pd

PREFIX = 'simple1_'
PATH = 'solr/results/m2/'
N = 8

s = 0
for i in range(1, N+1):
    df = pd.read_csv(PATH + PREFIX + 'metrics_results_' + str(i) + '.csv')
    s += df.values.tolist()[0][1]
print(s/N)
    