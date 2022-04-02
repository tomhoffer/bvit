FROM ubuntu

RUN apt update
RUN apt install libpcre3 libpcre3-dev zlib1g zlib1g-dev libssl-dev build-essential wget tar -y
RUN wget http://nginx.org/download/nginx-1.21.6.tar.gz
RUN tar -zxvf nginx-1.21.6.tar.gz

# Copy configuration
RUN rm -f /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/


# Create directory for content caching (if enabled)
RUN mkdir /cache

WORKDIR nginx-1.21.6
RUN ./configure --sbin-path=/usr/bin/nginx --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --pid-path=/var/run/nginx.pid
RUN make
RUN make install

EXPOSE 8081
CMD ["/usr/bin/nginx", "-g", "daemon off;"]
