from gcmda.utils import find_ts
import pandas as pd
import numpy as np
import os
import warnings
pd.reset_option("mode.chained_assignment", None)
warnings.filterwarnings('ignore')

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
data_path = f'{PROJECT_PATH}/data'

def test_find_ts():
    classes = ['retail_and_recreation_percent_change_from_baseline',
               'grocery_and_pharmacy_percent_change_from_baseline',
               'parks_percent_change_from_baseline',
               'transit_stations_percent_change_from_baseline',
               'workplaces_percent_change_from_baseline',
               'residential_percent_change_from_baseline']

    df = pd.read_csv(f'{data_path}/2020_US_Region_Mobility_Report.csv',
                     usecols=['sub_region_1', 'date'] + classes)
    df.columns = ['state', 'date'] + classes

    df['date'] = df.apply(lambda x: x['date'][-5:], axis=1)

    df_full = df.dropna(axis=0, how='any')

    # for state in state_date.columns:
    for state in ['US', 'California']:

        for i in range(len(classes)):
            category = classes[i]

            state_date = pd.pivot_table(df_full, index='date', columns='state', values=category, aggfunc=np.mean)

            US_avg = []

            for date_pt, date_df in df_full.groupby('date'):
                US_avg.append(date_df[category].mean())

            state_date['US'] = US_avg
            state_date['US_rolling'] = state_date['US'].rolling(window=7).mean()

            state_date[f'{state}_rolling'] = state_date[f'{state}'].rolling(window=7).mean()

            state_date['index_num'] = np.array(range(len(state_date)))
            if category[0:7] == "transit":

                ts = find_ts(state_date[[f'{state}', f'{state}_rolling', 'index_num']], state)

    for key in ts.keys():
        assert ts[key] is not None