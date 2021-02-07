FROM arm32v7/debian:buster

#install with apt-get, because it is faster than pip install
RUN apt-get update && apt-get install -y python3-dev python3-pip python3-pandas python3-click python3-influxdb

# copy code
COPY eta_to_influx /app/eta_to_influx

#copy config for eta columns
COPY eta_variable_dict.csv /app/eta_variable_dict.csv
ENV ETA_VARIABLE_DICT=/app/eta_variable_dict.csv

# default time delay
ENV time_delay_seconds=60


ENTRYPOINT python3 /app/eta_to_influx/eta_input_handler.py
