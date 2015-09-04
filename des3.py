from pyDes import *
import md5
import base64

class des3:
   #des1 = None

   #def __init(self):
   #    k = self.getKey()
   #    des1 = des(k,CBC,"\0\0\0\0\0\0\0\0",pad=None,padmode=PAD_PKCS5)
    

   def getKey(self,key):
       k = "jsj2015!"
       k = k+key
       m1 = md5.new()
       m1.update(k)
       return m1.hexdigest()

   def encrypt(self,json,key):
       k = self.getKey(key)
       k = k[0:8]
       #print k
       des1 = des(k,CBC,"\0\0\0\0\0\0\0\0",pad=None,padmode=PAD_PKCS5)
       tmp = des1.encrypt(json)
       res = base64.encodestring(tmp)
       return res

   def decrypt(self,data,key):
       k = self.getKey(key)[0:8]
       des1 = des(k,CBC,"\0\0\0\0\0\0\0\0",pad=None,padmode=PAD_PKCS5)
       res = base64.decodestring(data)
       return des1.decrypt(res)

if __name__ =="__main__":
   ss = "this is test"
   key = "abcdefgh"
   en = des3()
   s = en.encrypt(ss,key)
   print s 
   print en.decrypt(s,key)
