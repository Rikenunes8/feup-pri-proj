# SETUP
import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay
import numpy as np
import json
import requests
import pandas as pd
from sys import argv

if len(argv) != 2: raise Exception("Identify the query number")
query_n = int(argv[1])

QRELS_FILE = 'solr/qrels/q'+str(query_n)+'_qrel.txt'
QUERY_URL_FILE = 'solr/queries/q'+str(query_n)+'_query.txt'

# Read qrels to extract relevant documents
relevant = list(map(lambda el: el.strip(), open(QRELS_FILE).readlines()))
# Get query results from Solr instance
results = requests.get(open(QUERY_URL_FILE).readline()).json()['response']['docs']


def relevant_results(results, relevant, idx):
    return [doc for doc in results[:idx] if doc['id'] in relevant]

# METRICS TABLE
# Define custom decorator to automatically calculate metric based on key
metrics = {}
metric = lambda f: metrics.setdefault(f.__name__, f)

@metric
def ap(results, relevant):
    """Average Precision"""
    precision_values = [
        len(relevant_results(results, relevant, idx)) / idx 
        for idx in range(1, len(results))
    ]
    return sum(precision_values)/len(precision_values)

@metric
def p10(results, relevant, n=10):
    """Precision at N"""
    return len(relevant_results(results, relevant, n))/n

def calculate_metric(key, results, relevant):
    return metrics[key](results, relevant)

# Define metrics to be calculated
evaluation_metrics = {
    'ap': 'Average Precision',
    'p10': 'Precision at 10 (P@10)'
}

# Calculate all metrics and export results as LaTeX table
df = pd.DataFrame([['Metric','Value']] +
    [[evaluation_metrics[m], calculate_metric(m, results, relevant)] for m in evaluation_metrics]
)

with open('solr/results/metrics_results_'+str(query_n)+'.tex','w') as tf:
    tf.write(df.to_latex())



# PRECISION-RECALL CURVE
# Calculate precision and recall values as we move down the ranked list
precision_values = [
    len(relevant_results(results, relevant, idx)) / idx 
    for idx, _ in enumerate(results, start=1)
]

recall_values = [
    len(relevant_results(results, relevant, idx)) / len(relevant)
    for idx, _ in enumerate(results, start=1)
]

precision_recall_match = {k: v for k,v in zip(recall_values, precision_values)}

# Extend recall_values to include traditional steps for a better curve (0.1, 0.2 ...)
recall_values.extend([step for step in np.arange(0.1, 1.1, 0.1) if step not in recall_values])
recall_values = sorted(set(recall_values))

# Extend matching dict to include these new intermediate steps
for idx, step in enumerate(recall_values):
    if step not in precision_recall_match:
        if recall_values[idx-1] in precision_recall_match:
            precision_recall_match[step] = precision_recall_match[recall_values[idx-1]]
        else:
            precision_recall_match[step] = precision_recall_match[recall_values[idx+1]]

disp = PrecisionRecallDisplay([precision_recall_match.get(r) for r in recall_values], recall_values)
disp.plot()
plt.savefig('solr/results/precision_recall_'+str(query_n)+'.svg')
