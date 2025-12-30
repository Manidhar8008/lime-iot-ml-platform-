import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/lime_vehicles_sample.csv", parse_dates=["timestamp"])
print(df.head())


