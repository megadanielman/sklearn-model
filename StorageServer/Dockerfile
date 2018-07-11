FROM minio/minio

ENV MINIO_ACCESS_KEY="minioaccess"
ENV MINIO_SECRET_KEY="miniosecret"

VOLUME ["/minio/data", "/minio/config"]
EXPOSE 9000

CMD ["minio","server","/minio/data"]
