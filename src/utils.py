import matplotlib.pyplot as plt

PROJECT_COLORS = ["#2DD61D", "#3410FF"]

def bar_plot_project(x, y, title, x_label, y_label):
    fig, ax = plt.subplots(figsize=(15, 5))

    ax.bar(
        x=x,
        height=y,
        color=PROJECT_COLORS[0],
        edgecolor='black',
        linewidth=2
    )

    ax.grid(axis='y', color=PROJECT_COLORS[1], linestyle='--', alpha=0.7)

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    return fig, ax