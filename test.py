from des3 import *
from httpUtil import *
import json
import urllib

def test():
    account = "test"
    params = {"name":"111","password":"testwotbs$xo","identity":"420381197708165033","account":"test"} 
    Des3 = des3()
    pm = Des3.encrypt(json.dumps(params),account)
    param = {"account":account,"params":pm}
    client = httpClient(8080)
    #res = client.post("101.201.170.163","/service/identity",json.dumps(param))
    res = client.post("127.0.0.1","/login",json.dumps(param))
    print Des3.decrypt(pm,account)
    print res.read()
    client.close()

if __name__ == "__main__":
   test()
