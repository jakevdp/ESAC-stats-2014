import matplotlib.pyplot as plt

def plot_venn_diagram():
    fig, ax = plt.subplots(subplot_kw=dict(frameon=False, xticks=[], yticks=[]))
    ax.add_patch(plt.Circle((0.3, 0.3), 0.3, fc='red', alpha=0.5))
    ax.add_patch(plt.Circle((0.6, 0.3), 0.3, fc='blue', alpha=0.5))
    ax.add_patch(plt.Rectangle((-0.1, -0.1), 1.1, 0.8, fc='none', ec='black'))
    ax.text(0.2, 0.3, '$x$', size=30, ha='center', va='center')
    ax.text(0.7, 0.3, '$y$', size=30, ha='center', va='center')
    ax.text(0.0, 0.6, '$I$', size=30)
    ax.axis('equal')
