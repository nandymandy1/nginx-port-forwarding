FROM python:alpine3.7 
# COPY . /app
VOLUME flaskApp 
WORKDIR /flaskApp
COPY requirements.txt /flaskApp
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT ["python"]
CMD ["app.py"]