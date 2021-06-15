import requests
import json
import time
#import certifi
try:
    response = requests.get('https://api.thedogapi.com/v1/images/search')
    items = json.loads(response.text)
    b=items[0][u'breeds'][0][u'id']
except:
    b=1
#time.sleep(5)
a=int(input("input number: "))
numbers = [1, 2, 3, 4, 5, 6, 7]
evens = [x for x in numbers if x % 2 == 0]
y = map(lambda evens: evens + 1 , evens)
print(a)
print(b)
print(evens)
k= dict([(1,a),(2,b)])
print(k)
def b(dict):
    def t(dict):
        z=3
        while dict[1]>1 :
            dict[z]=dict[1]//2
            dict[1]=dict[1]-dict[z]
            z+=1
        for i in range(10):
            dict[z]=dict[2]//2
            dict[2]=dict[2]-dict[z]
            z+=1
        dict[z]=a*-1
        vasa=list(dict.values())
        vasa.append(a)
        print(vasa)
        teta=sum(vasa)
        return teta
    return t(dict)
ent=b(k)
beta=ent+sum(evens)
print(beta)
