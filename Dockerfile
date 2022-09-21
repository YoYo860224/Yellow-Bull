FROM python:3.6

ENV TZ=Asia/Taipei

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app/src
COPY src/YellowBull.py ./
CMD [ "python", "YellowBull.py" ]
