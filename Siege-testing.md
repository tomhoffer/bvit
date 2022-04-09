# Default rate limiting setup limit_req_zone $binary_remote_addr zone=myratelimit:10m rate=1r/s;
```
siege -v -r 2 -c 5 http://localhost:8081
```
# Vysledok:
** Preparing 5 concurrent users for battle.
The server is now under siege...
HTTP/1.1 503     0.00 secs:     197 bytes ==> GET  /
HTTP/1.1 503     0.00 secs:     197 bytes ==> GET  /
HTTP/1.1 503     0.00 secs:     197 bytes ==> GET  /
HTTP/1.1 503     0.00 secs:     197 bytes ==> GET  /
HTTP/1.1 200     0.00 secs:      21 bytes ==> GET  /
HTTP/1.1 503     0.01 secs:     197 bytes ==> GET  /
HTTP/1.1 503     0.01 secs:     197 bytes ==> GET  /
HTTP/1.1 503     0.01 secs:     197 bytes ==> GET  /
HTTP/1.1 503     0.01 secs:     197 bytes ==> GET  /
HTTP/1.1 503     0.01 secs:     197 bytes ==> GET  /

Transactions:		           1 hits
Availability:		       10.00 %
Elapsed time:		        0.01 secs
Data transferred:	        0.00 MB
Response time:		        0.05 secs
Transaction rate:	      100.00 trans/sec
Throughput:		        0.17 MB/sec
Concurrency:		        5.00
Successful transactions:           1
Failed transactions:	           9
Longest transaction:	        0.01
Shortest transaction:	        0.00

# Zaver: 
5 concurrentnych klientov naraz spravilo poziadavku. Iba prva z nich bola obsluzena, ostatne prekrocili rate 1r/s takze boli rejected. Dalsia vlna requestov prisla skor nez o jednu sekundu takze boli odmietnute tiez.

# Rate limiting + burst limit_req zone=myratelimit burst=5;
** Preparing 5 concurrent users for battle.
The server is now under siege...
HTTP/1.1 200     0.01 secs:      21 bytes ==> GET  /
HTTP/1.1 200     1.01 secs:      21 bytes ==> GET  /
HTTP/1.1 200     2.00 secs:      21 bytes ==> GET  /
HTTP/1.1 200     3.01 secs:      21 bytes ==> GET  /
HTTP/1.1 200     4.01 secs:      21 bytes ==> GET  /
HTTP/1.1 200     4.99 secs:      21 bytes ==> GET  /
HTTP/1.1 200     4.99 secs:      21 bytes ==> GET  /
HTTP/1.1 200     5.00 secs:      21 bytes ==> GET  /
HTTP/1.1 200     4.99 secs:      21 bytes ==> GET  /
HTTP/1.1 200     4.99 secs:      21 bytes ==> GET  /

Transactions:		          10 hits
Availability:		      100.00 %
Elapsed time:		        9.00 secs
Data transferred:	        0.00 MB
Response time:		        3.50 secs
Transaction rate:	        1.11 trans/sec
Throughput:		        0.00 MB/sec
Concurrency:		        3.89
Successful transactions:          10
Failed transactions:	           0
Longest transaction:	        5.00
Shortest transaction:	        0.01

# Zaver
1r/s + 5 burst size znamena, ze 1 request prejde, dalsich 5 pojde do queue kde budu obsluzene neskor a requesty nad limit budu odmietnute

# Ten isty experiment, len so zvysenym poctom concurrent connections
** Preparing 10 concurrent users for battle.
The server is now under siege...
HTTP/1.1 503     0.01 secs:     197 bytes ==> GET  /
HTTP/1.1 503     0.01 secs:     197 bytes ==> GET  /
HTTP/1.1 503     0.01 secs:     197 bytes ==> GET  /
HTTP/1.1 503     0.01 secs:     197 bytes ==> GET  /
HTTP/1.1 200     0.01 secs:      21 bytes ==> GET  /
HTTP/1.1 503     0.00 secs:     197 bytes ==> GET  /
HTTP/1.1 503     0.00 secs:     197 bytes ==> GET  /
HTTP/1.1 503     0.01 secs:     197 bytes ==> GET  /
HTTP/1.1 503     0.01 secs:     197 bytes ==> GET  /
HTTP/1.1 503     0.01 secs:     197 bytes ==> GET  /
HTTP/1.1 200     1.01 secs:      21 bytes ==> GET  /
HTTP/1.1 200     2.01 secs:      21 bytes ==> GET  /
HTTP/1.1 200     3.01 secs:      21 bytes ==> GET  /
HTTP/1.1 200     4.01 secs:      21 bytes ==> GET  /
HTTP/1.1 200     5.01 secs:      21 bytes ==> GET  /
HTTP/1.1 200     5.00 secs:      21 bytes ==> GET  /
HTTP/1.1 200     5.00 secs:      21 bytes ==> GET  /
HTTP/1.1 200     4.99 secs:      21 bytes ==> GET  /
HTTP/1.1 200     5.00 secs:      21 bytes ==> GET  /
HTTP/1.1 200     4.99 secs:      21 bytes ==> GET  /

Transactions:		          11 hits
Availability:		       55.00 %
Elapsed time:		       10.00 secs
Data transferred:	        0.00 MB
Response time:		        3.65 secs
Transaction rate:	        1.10 trans/sec
Throughput:		        0.00 MB/sec
Concurrency:		        4.01
Successful transactions:          11
Failed transactions:	           9
Longest transaction:	        5.01
Shortest transaction:	        0.00

# Zaver
Zvyseny pocet concurrent connections presiahol burst rate a bol odmietnuty

# Default rate limiting + burst + delay  limit_req zone=myratelimit burst=5 delay=3
With this configuration, first 3 requests (delay) are passed without delay, next 2 requests (burst - delay) are delayed in such a way that the overall rate is not greater than specified, further excessive requests will be rejected because the total burst size has been exceeded, subsequent requests will be delayed.

~ siege -v -r 1 -c 6 http://localhost:8081
** SIEGE 4.1.2
** Preparing 6 concurrent users for battle.
The server is now under siege...
HTTP/1.1 200     0.00 secs:      21 bytes ==> GET  /
HTTP/1.1 200     0.01 secs:      21 bytes ==> GET  /
HTTP/1.1 200     0.01 secs:      21 bytes ==> GET  /
HTTP/1.1 200     0.01 secs:      21 bytes ==> GET  /
HTTP/1.1 200     1.01 secs:      21 bytes ==> GET  /
HTTP/1.1 200     2.00 secs:      21 bytes ==> GET  /

Transactions:		           6 hits
Availability:		      100.00 %
Elapsed time:		        2.00 secs
Data transferred:	        0.00 MB
Response time:		        0.51 secs
Transaction rate:	        3.00 trans/sec
Throughput:		        0.00 MB/sec
Concurrency:		        1.52
Successful transactions:           6
Failed transactions:	           0
Longest transaction:	        2.00
Shortest transaction:	        0.00

➜  ~ siege -v -r 1 -c 7 http://localhost:8081
** SIEGE 4.1.2
** Preparing 7 concurrent users for battle.
The server is now under siege...
HTTP/1.1 503     0.01 secs:     197 bytes ==> GET  /
HTTP/1.1 200     0.01 secs:      21 bytes ==> GET  /
HTTP/1.1 200     0.01 secs:      21 bytes ==> GET  /
HTTP/1.1 200     0.01 secs:      21 bytes ==> GET  /
HTTP/1.1 200     0.01 secs:      21 bytes ==> GET  /
HTTP/1.1 200     1.01 secs:      21 bytes ==> GET  /
HTTP/1.1 200     2.01 secs:      21 bytes ==> GET  /

Transactions:		           6 hits
Availability:		       85.71 %
Elapsed time:		        2.01 secs
Data transferred:	        0.00 MB
Response time:		        0.51 secs
Transaction rate:	        2.99 trans/sec
Throughput:		        0.00 MB/sec
Concurrency:		        1.53
Successful transactions:           6
Failed transactions:	           1
Longest transaction:	        2.01
Shortest transaction:	        0.01

# Zaver
1 Request ktory presiahol rate limiting + burst + delay uz bol odmietnuty