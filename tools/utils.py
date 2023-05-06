import matplotlib.pyplot as plt
import seaborn as sns

# define a function to visualize the mobility trends by date
def mobility_trends_by_date(data, category, plot_title):
    fig, ax = plt.subplots(figsize=(12,4))
    sns.lineplot(data=data, x='date', y=category, estimator='mean' , errorbar=None)
    plt.axhline(y=0, linestyle='dashed', color='red')
    plt.xticks([])
    plt.xlim('2020-02-15', '2022-10-14')
    plt.title('{title} percent change from baseline by date'.format(title=plot_title))
    plt.ylabel('percent change from baseline')
    figname = category+'_by_date.png'
    plt.savefig('figures/'+figname);

# define a function to visualize the mobility trends by year and month
def mobility_trends_by_year_month(data, category, plot_title):
    fig, ax = plt.subplots(figsize=(12,4))
    sns.lineplot(data=data, x='year_month', y=category, estimator='mean' , errorbar=None)
    plt.axhline(y=0, linestyle='dashed', color='red')
    plt.xticks(rotation=90)
    plt.xlim('2020-02', '2022-10')
    plt.title('{title} percent change from baseline by year and month'.format(title=plot_title))
    plt.ylabel('percent change from baseline')
    figname = category+'_by_year_month.png'
    plt.savefig('figures/'+figname);