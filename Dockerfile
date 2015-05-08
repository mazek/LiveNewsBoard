FROM ubuntu

MAINTAINER Marcin Mazurek <marcin.mazurek@allegrogroup.com>

# Install necessary packages.
RUN apt-get update && apt-get install -y python-flask python-flask-httpauth sqlite


RUN mkdir /root/lwb
RUN git clone https://github.com/mazek/LiveNewsBoard.git /root/lwb/

# Initialize sqlite db.
RUN /root/lwb/python lwb_db.py

# Clean-up
RUN apt-get clean

EXPOSE 5000
CMD /root/lwb/python lwb.py
