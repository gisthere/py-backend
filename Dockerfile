
FROM alpine
COPY manipulator.py /manipulator.py
RUN  apk add python3

 
# FROM alpine
# COPY controller.py controller.py
# RUN apk add python3 
# CMD ["python3", "controller.py"]

# WORKDIR /code
# ENV FLASK_APP app.py
# ENV FLASK_RUN_HOST 0.0.0.0
# RUN apk add py3-numpy
# RUN apk add python3 
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt
# COPY . .
# CMD ["flask", "run"]
# sudo docker inspect 1e75ae5c225f --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'