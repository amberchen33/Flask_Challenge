### Flask_Prime_Challenge
The application is for client to polls the server to get the results of calculating prime number between the start and end number. The results are cached in Redis. 

### Prerequisites

Download, extract and compile Redis with:

```$ wget http://download.redis.io/releases/redis-4.0.9.tar.gz
$ tar xzf redis-4.0.9.tar.gz
$ cd redis-4.0.9
$ make
```

### The binaries that are now compiled are available in the src directory. Run Redis with:

```
$ src/redis-server
```
or follow the instruction here:
https://redis.io/download

# Install instructions
```
git clone https://github.com/amberchen33/Flask_Challenge.git
cd Flask_Challenge
run python server.py
```
go to http://127.0.0.1:5000/get_prime? and set the start and end number follow the format like
start=a&end=b, which a and b represent your start and end number seperately. 

For example
```
http://127.0.0.1:5000/get_prime?start=2&end=2000000
```
