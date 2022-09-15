FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY cloud.py .
ARG password_db
ENV PASSWORD_DB_OS ${password_db}
ARG user_db
ENV USER_DB_OS ${user_db}
CMD [ "python","/app/cloud.py" ]