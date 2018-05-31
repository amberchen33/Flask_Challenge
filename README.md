## Flask_Prime_Challenge
The application is for client to polls the server to get the results of calculating prime number between the start and end number. The results are cached in Redis. 

## The Basics

A Flask application looks like this:
```
from flask import Flask, request
import datetime
import _thread
import time
import redis
import math
app = Flask(__name__)

inputs = {}

def isPrime(num):
    if num == 1:
        return 0
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return 0
    return 1
    
def Threadfun(id, start, end):
    ans=[]
    for i in range(int(start), int(end) +1):
       if isPrime(i):
           ans.append(i) 
    
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)  # Redis runs on the port 6379 
    print(id, ans)
    r.set(id, ans)
    return

@app.route("/get_prime")
def get_prime():
    start = request.values.get('start')
    end = request.values.get('end')
    if not start or not end:
        return ('error: not get start or end parameters', 500)
    id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    inputs[id] = [start, end, []]
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)   
    r.set(id, [])
    _thread.start_new_thread(Threadfun, (id, start, end))
   
    return "%s" % (id)

@app.route("/get_result")
def get_result():
    id = request.values.get('id')
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)   
    return "%s, %s" % (id, r.get(id))

if __name__ == '__main__':
    app.run()
```

In the code above:
1. The ```isPrime``` function is used to tell if the number is a prime number.
2. The ```Threadfun``` function conducts the calculation since we want to run multiple tasks simultaneously while generate a unique ID.
3. The ```app.route``` decorator maps /get_prime to a view function get_prime.
4. The ```app.route``` decorator maps /get_result to a view function get_result.
5. Lastly, a builder constructs a spoken response and displays results in the Flask app.

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
$ git clone https://github.com/amberchen33/Flask_Challenge.git
$ cd Flask_Challenge
$ run python server.py
```
## Features

### Calculating prime numbers and returning a unique ID
* Set HTTP endpoint as **/get_ prime** 
* Set the parameters following the format :
**start=a&end=b**, which a and b represent your start and end number seperately. 
* Go to http://127.0.0.1:5000/get_prime?start=a&start=b  
* For example, we want to have prime numbers between 2 and 2000,000, the link will look like:
```
$ http://127.0.0.1:5000/get_prime?start=2&end=2000000
```

* The request will return unique ID for the task, which is determined by the date and time you send the request.
* If you fail to put the right parameters that are requested, the server will return message **error: not get start or end parameters**

### Use the unique ID to see the result of the task:
* Set HTTP endpoint as **/get_result** 
* Set the unique ID following the format :
**id=c**, which c represents the unique ID you got from above.
* Go to http://127.0.0.1:5000/get_result?id=c

* A great example looks will like this:
```
$ http://127.0.0.1:5000/get_result?id=20180531120444
```
The request will return the unique ID and the list of the requested prime number.

### Unit Test
```
$ run python testing.py
```
The testing.py looks like this :

```
import unittest
import requests

class TestStringMethods(unittest.TestCase):

    def test_get_prime_success(self):
        r = requests.get('http://127.0.0.1:5000/get_prime?start=2&end=1000')
        self.assertEqual(r.status_code, 200)

    def test_get_prime_fail(self):
        r = requests.get('http://localhost:5000/get_prime')
        self.assertEqual(r.status_code, 500)
        self.assertEqual(r.text, 'error: not get start or end parameters')

if __name__ == '__main__':
    unittest.main()
```

We can test our request here to see if we get the result we want.
If the request we set matches then you will get OK, otherwise you will get FAILED.

