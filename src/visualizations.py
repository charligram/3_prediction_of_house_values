import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

PROJECT_COLORS = ["#2DD61D", "#3410FF"]

def bar_plot_project(x: pd.Series, height: pd.Series, title: str, x_label: str, y_label: str):
    """
    Crea un gráfico de barras con los colores asociados al proyecto.

    Args:
        x (pd.Series): Serie que contiene los valores que irán en el eje X.
        height (pd.Series): Serie con los valores de la altura que tomaran las barras en el eje Y.
        title (str): Título del gráfico.
        x_label (str): Etiqueta del eje X.
        y_label (str): Etiqueta del eje Y.
    
    Returns:
        fig (plt.figure): Figure del gráfico.
        ax (plt.axes): Axes del gráfico.
    """
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


def hist_plot_project(x: pd.Series, title: str, x_label: str, y_label: str = 'Count'):
    """
    Crea un histograma con los colores asociados al proyecto.

    Args:
        x (pd.Series): Serie que contiene los valores que irán en el eje X.
        title (str): Título del gráfico.
        x_label (str): Etiqueta del eje X.
        y_label (str): Etiqueta del eje Y. Por defecto "Count".
    
    Returns:
        fig (plt.figure): Figure del gráfico.
        ax (plt.axes): Axes del gráfico.
    """
    fig, ax = plt.subplots(figsize=(15, 5))

    ax.hist(
        x=x,
        color=PROJECT_COLORS[0],
        edgecolor='black',
        linewidth=2
    )

    ax.grid(axis='y', color=PROJECT_COLORS[1], linestyle='--', alpha=0.7)

    ax.set_title(title)
    ax.set_xlabel(x_label)

    if y_label != 'Count':
        ax.set_ylabel(y_label)
    


    return fig, ax


def scatter_plot_project(x: pd.Series, y: pd.Series, title: str, x_label: str, y_label: str):
    """
    Crea un gráfico tipo scatter con los colores asociados al proyecto.

    Args:
        x (pd.Series): Serie que contiene los valores que irán en el eje X.
        y (pd.Series): Serie con los valores de la altura que tomaran los puntos en el eje Y.
        title (str): Título del gráfico.
        x_label (str): Etiqueta del eje X.
        y_label (str): Etiqueta del eje Y.
    
    Returns:
        fig (plt.figure): Figure del gráfico.
        ax (plt.axes): Axes del gráfico.
    """
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

def reg_plot_project(df: pd.DataFrame, x_name: str, y_name: str, title: str):
    """
    Crea un gráfico de regresión con los colores asociados al proyecto.

    Args:
        x_name (str): Nombre del feature que contiene los valores que irán en el eje X.
        y_name (str): Nombre del feature con los valores de la altura que tomaran los puntos en el eje Y.
        title (str): Título del gráfico.
    
    Returns:
        fig (plt.figure): Figure del gráfico.
        ax (plt.axes): Axes del gráfico.
    """
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

def box_plot_project(df: pd.DataFrame, x_name: str, y_name: str, title: str):
    """
    Crea un gráfico de cajas con los colores asociados al proyecto.

    Args:
        x_name (str): Nombre del feature que contiene los valores de las categorías que irán en el eje X.
        y_name (str): Nombre del feature con los valores para crear las cajas en el eje Y.
        title (str): Título del gráfico.
    
    Returns:
        fig (plt.figure): Figure del gráfico.
        ax (plt.axes): Axes del gráfico.
    """
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