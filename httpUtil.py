import httplib
import urllib
import json

class httpClient:
   client = None
   Timeout = 30
   port = 8080
   
   def get(self,url,path):
       self.client = httplib.HTTPConnection(url,self.port,timeout=self.Timeout);
       self.client.request("GET",path)
       res = self.client.getresponse()
       #self.client.close()
       return res

   def post(self,url,path,params):
       self.client = httplib.HTTPConnection(url,self.port,timeout=self.Timeout)
       self.client.request("POST",path,params)
       res = self.client.getresponse()
       #self.client.close()
       return res

   def close(self):
       self.client.close()

if __name__ == "__main__":
   client = httpClient()
   res = client.get("127.0.0.1","/")
   params = {"uname":"aaa","pwd":"123456"}
   #print res.read()
   res = client.post("127.0.0.1","/login",json.dumps(params))
   print res.status
   print res.read()
   client.close()
    
