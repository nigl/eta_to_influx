from influxdb import DataFrameClient
import os

class InfluxClient:
    def __init__(self, database="db0", username="admin", password="admin"):
        self.client = DataFrameClient(host=os.environ["INFLUX_HOST"], port="8086", username=username, password=password)
        self.database = database

    @staticmethod
    def get_numeric_data(df):
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        return df.select_dtypes(include=numerics)

    def insert_pandas(self, df):
        numeric_df = self.get_numeric_data(df)
        self.client.write_points(numeric_df, 'raw', time_precision="s", batch_size=1000, database=self.database)
