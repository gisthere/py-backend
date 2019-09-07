# FROM alpine
# ENV FLASK_APP app.py
# ENV FLASK_RUN_HOST 0.0.0.0
# COPY requirements.txt requirements.txt
# RUN apk add --no-cache --update python3 && pip3 install --upgrade pip setuptools
# RUN pip3 install -r requirements.txt
# COPY . .
# CMD ["flask", "run"]

# FROM alpine
# COPY manipulator.py /manipulator.py
# RUN  apk add python3
# CMD ["python3", "manipulator.py"]
 
# FROM alpine
# COPY controller.py controller.py
# RUN apk add python3
# CMD ["python3", "controller.py"] 

# sudo docker inspect 1e75ae5c225f --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'