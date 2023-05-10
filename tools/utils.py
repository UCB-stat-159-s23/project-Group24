import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
pd.reset_option("mode.chained_assignment", None)

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

# Capture critical time points in DQQ model
def find_ts(df_for_t, state):
    t0_time_window = 100
    t3_time_window = 120  # First x days chunk to find t1
    t4_time_window = 60  # Time window to get std
    t4_std_threshhold = 1.2

    df_for_t['delta'] = df_for_t[f'{state}_rolling'] - df_for_t[f'{state}_rolling'].shift(1)
    df_for_t['delta_2'] = df_for_t[f'delta'] - df_for_t[f'delta'].shift(1)
    df_for_t['delta_3'] = df_for_t[f'delta_2'] - df_for_t[f'delta_2'].shift(1)

    # Get t0
    df_for_t['sign_change'] = df_for_t[f'{state}_rolling'] * df_for_t[f'{state}_rolling'].shift(1)
    if df_for_t['sign_change'].head(t0_time_window).min() < 0:

        two_day_after_t0 = df_for_t['sign_change'].head(t0_time_window).idxmin()
        t0 = df_for_t[df_for_t['index_num'] == df_for_t.loc[two_day_after_t0]['index_num'] - 2].index[0]
        rate_t0 = df_for_t.loc[t0][f'{state}_rolling']

    else:
        two_day_after_t0 = df_for_t['delta_2'].head(t0_time_window).idxmin()
        t0 = df_for_t[df_for_t['index_num'] == df_for_t.loc[two_day_after_t0]['index_num'] - 2].index[0]
        rate_t0 = df_for_t.loc[t0][f'{state}_rolling']

    # Get t1
    t1 = df_for_t['delta'].rolling(window=7).mean().head(t3_time_window).idxmin()
    rate_t1 = df_for_t.loc[t1][f'{state}_rolling']

    # Get t2
    t2 = df_for_t[f'{state}_rolling'].head(t3_time_window).idxmin()
    rate_t2 = df_for_t[f'{state}_rolling'].head(t3_time_window).min()

    # Get t3

    t3 = df_for_t[(df_for_t['index_num'] > df_for_t.loc[t2]['index_num']) & (df_for_t['index_num'] < 168)][
        'delta'].rolling(window=7).mean().head(t3_time_window).idxmax()
    rate_t3 = df_for_t.loc[t3][f'{state}_rolling']

    # Get t4

    t4 = None

    i = 0
    while (t4 is None):

        if (i >= len(df_for_t) - t4_time_window):
            # t4_time_window -= 10
            t4_std_threshhold += 0.05
            i = 0

        date_i = df_for_t.iloc[i].name

        if (8 > int(date_i[:2]) > int(t3[:2])) or (int(date_i[:2]) == int(t3[:2]) and int(date_i[-2:]) > int(t3[-2:])):

            std_i = df_for_t[f'{state}_rolling'][i:i + t4_time_window].std()
            # std_list.append(std_i)
            if std_i <= t4_std_threshhold:
                t4 = df_for_t.iloc[i].name
                rate_t4 = df_for_t.loc[t4][f'{state}_rolling']

        i += 1

    T = {
        't0': t0,
        'rate_t0': rate_t0,
        't1': t1,
        'rate_t1': rate_t1,
        't2': t2,
        'rate_t2': rate_t2,
        't3': t3,
        'rate_t3': rate_t3,
        't4': t4,
        'rate_t4': rate_t4,

    }
    return T