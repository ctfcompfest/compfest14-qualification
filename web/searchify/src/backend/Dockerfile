FROM python:3-alpine

COPY flag.txt /flag_0ac73b4846fea622e906199d592eaa85
COPY src /opt/searchify
COPY patch.sh /tmp/patch.sh

RUN pip install -r /opt/searchify/requirements.txt
RUN /tmp/patch.sh
RUN rm /tmp/patch*

WORKDIR /opt
USER nobody

EXPOSE 5000

CMD ["flask", "run", "-h", "0.0.0.0"]
