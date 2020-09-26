FROM python:3
WORKDIR /usr/news_checker
COPY ./ ./
EXPOSE 8000
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python3 manage.py migrate
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
