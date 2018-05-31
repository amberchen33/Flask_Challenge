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
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)   
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