ARG BUILD_FROM
FROM $BUILD_FROM

# Install Operating System requirements for add-on
RUN apk add --no-cache python3
RUN apk add --no-cache py3-pip

# Prepare virtual environement for Python
RUN python3 -m venv /opt/venv

# Install Python requirements for add-on
COPY requirements.txt .
RUN . /opt/venv/bin/activate && pip3 install --no-cache-dir -r requirements.txt

# Python 3 HTTP Server serves the current working dir
# So let's set it to our add-on persistent data directory.
WORKDIR /data

COPY rootfs /
