from data_from_xml import get_dict_all_columns
from influx_client import InfluxClient

import click
import pandas as pd
import os
import datetime
import time

@click.command()
def data_import():
    time_delay_seconds = int(os.environ["time_delay_seconds"])
    
    while(True):
       value_dict = get_dict_all_columns(os.environ["ETA_VARIABLE_DICT"], os.environ["ETA_URL"])
       # save data in influx db
       utc_dt = datetime.datetime.utcnow()
       cleaned_dict = {key: value_dict[key].replace(",", ".") for key in value_dict}
       df = pd.DataFrame(cleaned_dict, index=[utc_dt])
       df = df.apply(lambda x: pd.to_numeric(x, errors='ignore'))
       client = InfluxClient("eta")
       client.insert_pandas(df)
       time.sleep(time_delay_seconds)

if __name__ == '__main__':
    data_import()
