FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN apt update
RUN apt install gettext -y
RUN python manage.py collectstatic --noinput
CMD uwsgi --http=0.0.0.0:80 --module=django-divio-blog.wsgi
