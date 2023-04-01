FROM python:3.9 
# Or any preferred Python version.
ADD . .
RUN pip install peewee TeleBot pandas
CMD ["python", "./main.py"] 
# Or enter the name of your unique directory and parameter set.