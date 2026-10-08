import matplotlib.pyplot as plt
import seaborn as sns

PROJECT_COLORS = ["#2DD61D", "#3410FF"]

def bar_plot_project(x, height, title, x_label, y_label):
    fig, ax = plt.subplots(figsize=(15, 5))

    ax.bar(
        x=x,
        height=height,
        color=PROJECT_COLORS[0],
        edgecolor='black',
        linewidth=2
    )

    ax.grid(axis='y', color=PROJECT_COLORS[1], linestyle='--', alpha=0.7)

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    return fig, ax


def hist_plot_project(x, title, x_label, y_label='Count'):
    fig, ax = plt.subplots(figsize=(15, 5))

    ax.hist(
        x=x,
        color=PROJECT_COLORS[0],
        edgecolor='black',
        linewidth=2
    )

    ax.set_title(title)
    ax.set_xlabel(x_label)

    if y_label != 'Count':
        ax.set_ylabel(y_label)
    


    return fig, ax


def scatter_plot_project(x, y, title, x_label, y_label):
    fig, ax = plt.subplots(figsize=(15, 5))

    ax.scatter(
        x=x,
        y=y,
        color=PROJECT_COLORS[0],
        edgecolors='black'
    )

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    ax.set_title(title)

    return fig, ax

def reg_plot_project(df, x_name, y_name, title):
    fig, ax = plt.subplots(figsize=(15, 5))

    sns.regplot(
        data=df,
        x=x_name,
        y=y_name,
        ax=ax,
        scatter_kws={
            'color': PROJECT_COLORS[0],
            'edgecolor': 'black'
        },
        line_kws={
            'color': PROJECT_COLORS[1],
            'linewidth': 2
        }
    )

    ax.set_title(title)

    return fig, ax

def boxp_plot_project(df, x_name, y_name, title):
    fig, ax = plt.subplots(figsize=(15, 5))

    sns.boxplot(
        data=df,
        x=x_name,
        y=y_name,
        boxprops=dict(
            facecolor=PROJECT_COLORS[0],
            edgecolor='black',
            linewidth=2
        ),
        medianprops=dict(
            color=PROJECT_COLORS[1],
            linewidth=2
        ),
        whiskerprops=dict(
            color='black',
            linewidth=2
        ),
        capprops=dict(
            color='black',
            linewidth=2
        ),
        ax=ax
    )

    ax.set_title(title)

    return fig, ax

