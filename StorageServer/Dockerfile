FROM minio/minio

ENV MINIO_ACCESS_KEY="minioasccess"
ENV MINIO_SECRET_KEY="miniosecret"

VOLUME ["/minio/data", "/minio/config"]

RUN chgrp -R 0 /minio \
 && chmod -R g+rwX /minio

EXPOSE 9000

CMD["minio","server"]
