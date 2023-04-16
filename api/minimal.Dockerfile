FROM python:3.11.2-bullseye
ENV PYTHONUNBUFFERED=1

WORKDIR /api

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["bash", "./minimal.sh" ]

  