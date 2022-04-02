FROM ubuntu

RUN apt update
RUN apt install build-essential curl tar -y
RUN apt install wget -y
RUN apt install libpcre3 libpcre3-dev zlib1g zlib1g-dev libssl-dev -y

RUN wget http://nginx.org/download/nginx-1.21.6.tar.gz
RUN tar -zxvf nginx-1.21.6.tar.gz

WORKDIR nginx-1.21.6

RUN ./configure --sbin-path=/usr/bin/nginx --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --with-pcre --pid-path=/var/run/nginx.pid --with-http_ssl_module

RUN make
RUN make install
RUN nginx -V
RUN rm -f /etc/nginx/nginx.conf

COPY nginx.conf /etc/nginx/

EXPOSE 8081
CMD ["/usr/bin/nginx", "-g", "daemon off;"]
