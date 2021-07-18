FROM python:3.9.6-slim-buster

ARG USER=you
ARG USER_HOME=/usr/local/${USER}

RUN useradd -ms /bin/bash -d ${USER_HOME} ${USER}

WORKDIR ${USER_HOME}

COPY . .

RUN python -m pip install --no-cache-dir .

USER ${USER}

CMD ["python", "-m", "unittest"]
