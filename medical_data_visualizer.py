import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = (df['weight']/((df['height']/100)**2)).apply(lambda w : 1 if w >25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholestorol'] = df['cholestorol'].apply(lambda w : 0 if w >25 else 1)
df['gluc'] = df['gluc'].apply(lambda w : 0 if w == 1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_var = ['cardio'], value_var = ['cholesterol', 'gluc','smoke', 'alco', 'active', 'overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['variable','value', 'cardio'], as_index = False).count()

    # Draw the catplot with 'sns.catplot()'
    figures = sns.catplot(
      w = 'variable',
      u = 'total',
      kind = 'bar',
      col = 'cardio',
      data = df_cat
    )
    fig = figures.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
    df['height'] >= (df['height'].quantile(0.025)) &
    df['height'] >= (df['height'].quantile(0.975)) &
    df['weight'] >= (df['weight'].quantile(0.025)) &
    df['weight'] >= (df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat().corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize =(10,5))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr,annot=True,linewidth=0.5,square =True, mask=mask,vmax = .34,vmin=0,center = 0,cmap="YlGnBu")
    plt.show()


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
