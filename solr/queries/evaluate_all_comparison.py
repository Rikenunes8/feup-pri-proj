# SETUP
import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay
import numpy as np
import json
import requests
import pandas as pd
from sys import argv


def relevant_results(results, relevant, idx):
    return [doc for doc in results[:idx] if doc in relevant]


number_queries = 7
prefixes = ['m3/simple_schema_', 'm3/updated_schema_']
labels = ['Simple Schema', 'Updated Schema']
colors = ['blue', 'red']
for query_n in range(1, number_queries+1):
    fig, ax = plt.subplots()

    dfs = []
    for index, prefix in enumerate(prefixes):
        df = pd.read_csv(f"solr/results/{prefix}relevance_results_" + str(query_n)+'.csv')
        relevant = df[df['Relevance'] == True]['Document'].tolist()
        results = df['Document'].tolist()
        dfs.append(df)

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

        precision_recall_match = [(k, v)
                                for k, v in zip(recall_values, precision_values)]
        recall_precision_interpolated = []
        for i in np.arange(0.0, 1.1, 0.1):
            try:
                recall_precision_interpolated.append(
                    (i, max([v for k, v in precision_recall_match if k >= i])))
            except:
                recall_precision_interpolated.append((i, 0))

        df['Precision'] = precision_values
        df['Recall'] = recall_values

        dfs.append(df)

        disp = PrecisionRecallDisplay(precision=np.array([v for k, v in recall_precision_interpolated]), recall=np.array([k for k, v in recall_precision_interpolated]))
        disp.plot(color=colors[index], label=labels[index], ax=ax)  


    plt.ylim(0, 1.05)
    plt.title('Precision-Recall Curve for query '+str(query_n))
    plt.savefig(
        f"solr/results/m3/comparison_precision_recall_"+str(query_n)+'.svg')
