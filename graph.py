import matplotlib.pyplot as plt

def ShowGraph(x, y, label, title, xlabel, ylabel):
    plt.plot(x, y, label=label)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(x, rotation='vertical')
    plt.subplots_adjust(left=None, bottom=0.47, right=0.9,
                        top=None, wspace=None, hspace=None)
    return plt.show()
