FROM arm32v7/debian:buster

#install with apt-get, because it is faster than pip install
RUN apt-get update && apt-get install -y python3-dev python3-pip python3-pandas python3-click python3-influxdb git

WORKDIR /app
# copy code
COPY . /app/eta_to_influx
# alternatively use git clone
#RUN git clone https://github.com/nigl/eta_to_influx.git

#set config for eta columns
ENV ETA_VARIABLE_DICT=/app/eta_to_influx/eta_variable_dict.csv

# default time delay
ENV time_delay_seconds=60

ENTRYPOINT python3 /app/eta_to_influx/python/eta_input_handler.py
