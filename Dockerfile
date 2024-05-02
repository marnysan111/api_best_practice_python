FROM python:3

WORKDIR /usr/src

COPY ./ /usr/src

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "main:app" , "--reload", "--host=0.0.0.0", "--port=8080"]