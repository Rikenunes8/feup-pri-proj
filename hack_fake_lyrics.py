from random import Random, randint
from sys import argv
import matplotlib.pyplot as plt
import pandas as pd

filename = 'data/rolling_stones_tracks.csv'

df = pd.read_csv(filename, sep=';')
possibilities = ['', 'a', 'b', 'c']

lyrics = [possibilities[randint(0, 3)] for _ in range(df.shape[0])]
df['lyrics'] = lyrics

df.to_csv('data/all.csv', sep=";", index=False)

