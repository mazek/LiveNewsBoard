
FROM ubuntu

MAINTAINER Marcin Mazurek <marcin.mazurek@allegrogroup.com>

# Install necessary packages.
RUN apt-get update && apt-get install -y python-pip sqlite git
RUN pip install flask flask-httpauth


RUN git clone https://github.com/mazek/LiveNewsBoard.git /root/

# Initialize sqlite db.
RUN python /root/lwb/lwb_db.py

# Clean-up
RUN apt-get clean

EXPOSE 5000
CMD /root/lwb/python lwb.py
