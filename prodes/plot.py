import matplotlib.pyplot as plt
import matplotlib
import warnings
import matplotlib.pyplot as mpl
from scipy.stats import percentileofscore


def plot_deforestation(year_area):
    years = list(int(x) for x in year_area.keys())
    size = [v  for v in year_area.values()]
    N = len(size)

    fig, ax = plt.subplots(figsize=(15, 10))
    warnings.warn('Increasing default font size in mpl.rcParams["font.size"] to 14...')
    mpl.rcParams['font.size'] = 14
    ax.grid(axis='y')
    ax.bar(years, size, edgecolor=(0, 0.3, 0),
           color=[(0, 0.9 - 0.7 * (percentileofscore(size, s) / 100), 0) for s in size], alpha=0.7)
    ax.set_title('Deforestation in the Amazon Basin (by year)')
    ax.set_xlabel('Year')
    ax.set_ylabel('Tree area lost (km$^2$)')
    ax.get_yaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, p: f'{x:,.0f}'))

    ax.set_xticks(years)

    plt.show()
