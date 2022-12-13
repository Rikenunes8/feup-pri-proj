from sys import argv
import pandas as pd


if len(argv) != 2: 
    raise Exception("Identify the query number")

N_QUERIES = 8
N_DOCUMENTS = 30
prefix = argv[1]
path_prefix = 'solr/results/m2/'

# read metrics_results file
all_rr = []
for i in range(1, N_QUERIES + 1):
    relevance_results = pd.read_csv(f'{path_prefix}{prefix}relevance_results_{i}.csv')
    rr = relevance_results['Relevance'].values.tolist()
    rr = list(map(lambda x: '1' if x else '0', rr))
    all_rr.append([f'Q{i}'] + rr)

for x in all_rr:
    x = x + [' '] * (N_DOCUMENTS - len(x) + 1)
    print(' & '.join(x) + ' \\\\')
    print('\\hline')

