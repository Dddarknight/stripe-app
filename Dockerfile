FROM python:3.9

WORKDIR /

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt \
    && rm -rf /root/.cache/pip

COPY . .

CMD python manage.py runserver 0.0.0.0:8000