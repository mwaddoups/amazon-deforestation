import matplotlib.pyplot as plt
import matplotlib
import warnings
import matplotlib.pyplot as mpl
from scipy.stats import percentileofscore

def plot_deforestation(year_area):
    years = list(int(x) for x in year_area.keys())
    size = [v  for v in year_area.values()]
    N = len(size)

    warnings.warn('Increasing default font size in mpl.rcParams["font.size"] to 14...')
    mpl.rcParams['font.size'] = 14

    fig, ax = plt.subplots(figsize=(15, 10))
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

def plot_carbon_emissions(carbon_data, emissions_data):
    mpl.rcParams['font.size'] = 14

    years = list(int(x) for x in carbon_data.keys())
    size = [v / 1e6 for v in carbon_data.values()]
    N = len(size)

    fig, ax = plt.subplots(figsize=(15, 10))
    ax.grid(axis='y')
    cmap = lambda s: 0.5 - 0.5 * (percentileofscore(size, s) / 100)
    ax.bar(years, size, edgecolor='black', label='Equivalent emissions from deforestation',
        color=[(cmap(s), cmap(s), cmap(s)) for s in size], alpha=0.7)

    ax.step(
        sorted(years), 
        [emissions_data.get(str(y), None) for y in sorted(years)],
        color='red',
        linestyle='--',
        label='Brazilian emissions from fossil fuel and industry'
    )
    ax.set_title('Equivalent carbon emission from deforestation')
    ax.set_xlabel('Year')
    ax.set_ylabel('Carbon emission equivalent (millions of tons)')
    ax.get_yaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, p: f'{x:,.0f}'))

    ax.set_xticks(years)
    ax.legend()

    plt.show()
