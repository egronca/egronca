import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
def make_overweight(df):
    height_m = df["height"]/100
    BMI = df["weight"]/(height_m*height_m)
    if BMI > 25:
        return 1
    else:
        return 0

df["overweight"] = df.apply(make_overweight, axis=1)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
def normalise(value):
    if value == 1:
        return 0
    elif value >1:
        return 1
        
df["cholesterol"] = df["cholesterol"].apply(normalise)
df["gluc"] = df["gluc"].apply(normalise)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    
    # First filter to include just the columns of interest
    df_cat = df.filter(["id", "cholesterol", "gluc", "smoke", "alco", "active", "overweight", "cardio"])

    # Then use pd.melt
    df_cat = pd.melt(df_cat, id_vars = "cardio", value_vars = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'] , value_name = "value")
    df_cat = df_cat.sort_values(by = "variable")
    
    fig = sns.catplot(x='variable', hue='value', data=df_cat, kind='count', col='cardio')
    fig.set_ylabels('total')
    fig = fig.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['height'] >= df['height'].quantile(0.025)) & 
            (df['height'] <= df['height'].quantile(0.975)) & 
            (df['weight'] >= df['weight'].quantile(0.025)) & 
            (df['weight'] <= df['weight'].quantile(0.975)) &
            (df['ap_lo'] <= df['ap_hi'])]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', fmt=f".{1}f", ax=ax)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
