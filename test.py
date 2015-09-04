from des3 import *
from httpUtil import *
import json

def test():
    key = "test"
    params = {"uname":"sss","pwd":"123"} 
    Des3 = des3()
    pm = Des3.encrypt(key,json.dumps(params))
    client = httpClient()
    res = client.post("127.0.0.1","/login",pm)
    print res.read()
    client.close()

if __name__ == "__main__":
   test()
