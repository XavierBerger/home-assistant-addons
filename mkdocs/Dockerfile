ARG BUILD_FROM
FROM $BUILD_FROM

# Install Operating System requirements for add-on
RUN apk add --no-cache \
        python3 \
        py3-pip \
        nginx \
    && \
    mkdir -p /run/nginx
    
# Prepare virtual environement for Python
RUN python3 -m venv /opt/venv

# Install Python requirements for add-on
COPY requirements.txt .
RUN . /opt/venv/bin/activate && pip3 install --no-cache-dir -r requirements.txt
RUN . /opt/venv/bin/activate && pip3 install --no-cache-dir mkdocs-macros-plugin
RUN . /opt/venv/bin/activate && pip3 install --no-cache-dir mkdocs-glightbox
RUN . /opt/venv/bin/activate && pip3 install --no-cache-dir mkdocs-awesome-pages-plugin
COPY rootfs /
