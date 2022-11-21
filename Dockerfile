# create a python enviroment inside a container
FROM python:3.10

ADD . .

# install dependencies
RUN pip install -r requirements.txt



EXPOSE 5000
# start celery worker
RUN celery -A jobs.celery worker --loglevel=info &
# start celery beat
RUN celery -A jobs.celery beat --loglevel=info &



# command to run on container start
CMD [ "python", "./app.py", ]


