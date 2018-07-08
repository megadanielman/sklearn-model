FROM registry.access.redhat.com/rhscl/python-36-rhel7
COPY . /webserver
WORKDIR /webserver
ENV MINIO_ACCESS "minioaccess"
ENV MINIO_SECRET "miniosecret"
# RUN export IP_MINIO=$(sudo docker inspect --format '{{ .NetworkSettings.IPAddress }}' minioServer)
# RUN export IP_FLASK=$(sudo docker inspect --format '{{ .NetworkSettings.IPAddress }}' flaskServer)
RUN python3 -m pip install -r /webserver/requirements.txt
EXPOSE 8000
#CMD["/bin/bash"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
