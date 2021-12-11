FROM python:3.9.5-slim
ENV PYTHONUNBUFFERED=1
ENV APP_HOME=/code
WORKDIR $APP_HOME

ADD src/requirements.txt $APP_HOME/
RUN pip install -r /code/requirements.txt

COPY src/ $APP_HOME
RUN python3 manage.py migrate
CMD python3 manage.py runserver 0.0.0.0:8000
