FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y lib32z1 xinetd patchelf --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m ctf

WORKDIR /home/ctf

RUN cp -R /lib* /home/ctf && \
    cp -R /usr/lib* /home/ctf

RUN mkdir /home/ctf/dev && \
    mknod /home/ctf/dev/null c 1 3 && \
    mknod /home/ctf/dev/zero c 1 5 && \
    mknod /home/ctf/dev/random c 1 8 && \
    mknod /home/ctf/dev/urandom c 1 9 && \
    chmod 666 /home/ctf/dev/*

RUN mkdir /home/ctf/bin && \
    cp /bin/sh /home/ctf/bin && \
    cp /bin/ls /home/ctf/bin && \
    cp /bin/cat /home/ctf/bin

COPY ./ctf.xinetd /etc/xinetd.d/ctf
COPY ./start.sh /start.sh
COPY ./src /
RUN chmod +x /start.sh && \
    mv /tcmail . && \
    mv /libtcmail.so ./lib && \
    mv /flag.txt . && \
    chmod 444 ./flag.txt && \
    chmod 555 ./tcmail && \
    chmod 555 ./lib/libtcmail.so

RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail

EXPOSE 9999

CMD ["/start.sh"]