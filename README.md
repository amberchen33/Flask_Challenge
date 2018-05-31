## Flask_Prime_Challenge
The application is for client to polls the server to get the results of calculating prime number between the start and end number. The results are cached in Redis. 

## Prerequisites

Download, extract and compile Redis with:

```$ wget http://download.redis.io/releases/redis-4.0.9.tar.gz
$ tar xzf redis-4.0.9.tar.gz
$ cd redis-4.0.9
$ make
```

The binaries that are now compiled are available in the src directory. Run Redis with:

```
$ src/redis-server
```
or follow the instruction here:
https://redis.io/download


## Install instructions
```
git clone https://github.com/amberchen33/Flask_Challenge.git
cd Flask_Challenge
run python server.py
```

* go to http://127.0.0.1:5000/ and put HTTP endpoint as **/get_ prime** 
* set the parameters following the format :
**start=a&end=b**, which a and b represent your start and end number seperately. 

* For example, we want to have prime number between 2 and 2000,000
```
http://127.0.0.1:5000/get_prime?start=2&end=2000000
```

The request will return unigque ID for the task, which is determined by the date and time you send the request.

### Use the unique ID to see the result of the task:
* go http://127.0.0.1:5000/ and put HTTP endpoint as **/get_result** 
* set the unique ID following the format :
**id=c**, which c represents the unique ID you got from above.

* A great example looks will like this:
```
http://127.0.0.1:5000/get_result?id=20180531120444
```
