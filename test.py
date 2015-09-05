from des3 import *
from httpUtil import *
import json

def test():
    account = "test"
    params = {"uname":"sss","pwd":"123","account":"test"} 
    Des3 = des3()
    pm = Des3.encrypt(json.dumps(params),account)
    client = httpClient(8080)
    res = client.post("127.0.0.1","/login",pm)
    print res.read()
    client.close()

if __name__ == "__main__":
   test()
