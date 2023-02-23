FROM bitnami/python:3.7.13-debian-10-r13

RUN apt-get update && apt-get install -y xvfb \
    chromium-driver 

WORKDIR /app

COPY screenshot.py /app/

# Install Python dependencies
RUN pip3 install --no-cache-dir \
    selenium \
    PyVirtualDisplay

# ENTRYPOINT to run Python script
ENTRYPOINT ["python3", "screenshot.py"]
