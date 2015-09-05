from pyDes import *
import md5
import base64
import des

class des3:

    

   def getKey(self,key):
       k = "jsj2015!"
       k = k+key
       m1 = md5.new()
       m1.update(k)
       return m1.hexdigest()

   def encrypt(self,json,key):
       k = self.getKey(key)[0:24]
       #k = k[0:8]
       des1 = triple_des(k,CBC,"abcdefgh",pad=None,padmode=PAD_PKCS5)
       tmp = des1.encrypt(json)
       #des1 = des.DES()
       #des1.input_key(k)
       #tmp = des1.encode(json)
       res = base64.encodestring(tmp)
       return res

   def decrypt(self,data,key):
       k = self.getKey(key)[0:24]
       des1 = triple_des(k,CBC,"abcdefgh",pad=None,padmode=PAD_PKCS5)
       #des1 = des.DES()
       #des1.input_key(k)
       res = base64.decodestring(data)
       return des1.decrypt(res)
       #return des1.decode(res)

if __name__ =="__main__":
   ss = "this is test"
   key = "12345678"
   en = des3()
   s = en.encrypt(ss,key)
   print s 
   print en.decrypt(s,key)
