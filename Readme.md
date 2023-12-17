# NGINX DDoS mitigation
This project hosts code to demonstrate how Nginx can be used to mitigate the impact of Dos/DDoS attacks using load balancing, rate-limiting and caching techniques. See `paper.pdf` with the detailed explaination of this problematic, as well as experiments and evaluation results (SK language). 

# Create the environment

The following docker-compose command creates containers with the following:
- Gunicorn flask python server: Default worker count is one, number of replicas is set to 3.
- Nginx server
- Locust: Distributed setup containing one master and 3 worker nodes

```
docker-compose up --build --scale locust-worker=3
```

# Run the DDoS simulation
Open localhost:8089 in your browser to run the simulation.