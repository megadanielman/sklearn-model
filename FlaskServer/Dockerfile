FROM registry.access.redhat.com/rhscl/python-36-rhel7
ADD . /flaskServer
WORKDIR /flaskServer
ENV MINIO_ACCESS "minioaccess"
ENV MINIO_SECRET "miniosecret"
ENV FLASK_APP="index.py"
RUN python3 -m pip install -r /flaskServer/requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD ["index.py"]