FROM alpine

RUN apk update \
    && apk add --no-cache python3 build-base libstdc++ python3-dbg python3-dev git bash \
    && apk add zlib-dev jpeg-dev freetype-dev py3-gunicorn \
    && python3 -m ensurepip

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .


#CMD ["/usr/bin/gunicorn", "app:app" "-b", "0.0.0.0:5009"]
#CMD ["/usr/bin/gunicorn", "--config", $conf_gunicon , "app:app" ]


