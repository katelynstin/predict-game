FROM python:3

WORKDIR predict_test/
COPY . /predict_test

#RUN git pull

EXPOSE 8080

RUN pip install -r requirements.txt

CMD ["make", "start"]
