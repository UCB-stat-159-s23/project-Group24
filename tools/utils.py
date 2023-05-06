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

# define a function to visualize the mobility trends by category
def mobility_trends_by_category(data, category, plot_title):
    states = data['state'].dropna().unique()
    state_index = 0
    fig, ax = plt.subplots(nrows=11, ncols=5, figsize=(20,20))

    for row in range(11):
        for col in range(5):
            try:
                state_data = data[data['state'] == states[state_index]]
                sns.lineplot(data=state_data, x='year_month',y=category, errorbar=None, ax=ax[row,col])
                ax[row,col].axhline(y=0, linestyle='dashed', color='red')
                ax[row,col].set_xticks([])
                ax[row,col].set_xlabel('')
                ax[row,col].set_ylabel('')
                ax[row,col].set_title(states[state_index])
                state_index = state_index + 1
            except IndexError:
                pass
    fig.suptitle('{title} mobility trends by state'.format(title=plot_title), fontsize=24, fontweight='bold')
    figname = category+'_mobility_trends_by_state.png' 
    plt.savefig('figures/'+figname)
	

def load_data(*path):
	US_2020 = pd.read_csv('data/2020_US_Region_Mobility_Report.csv', low_memory=False)
US_2021 = pd.read_csv('data/2021_US_Region_Mobility_Report.csv', low_memory=False)
US_2022 = pd.read_csv('data/2022_US_Region_Mobility_Report.csv', low_memory=False)