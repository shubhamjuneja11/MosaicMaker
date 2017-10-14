
# coding: utf-8

# In[217]:

from PIL import Image
from PIL import ImageDraw
import os


# In[218]:

from PIL import Image
from PIL import ImageDraw
scale=20
image=Image.open('sj.jpg')
w=image.width#/scale
h=image.height#/scale
mywidth=w
myheight=h
ib=Image.new('RGB',(w,h))
colors=[]
i=j=0

imgdraw=ImageDraw.Draw(ib)
while(i<w):
    j=0
    while(j<h):
        c=image.getpixel((i,j))
        colors.append(c)
        imgdraw.rectangle(((i,j),(i+scale,j+scale)),fill=c)
        j+=scale
        
    i+=scale


# In[219]:

allimages=[]
allimagespath=[]
smallscale=scale
for file in os.listdir('/home/shubhamjuneja11/pics'):
    im=Image.open('pics/'+file)
    im=im.resize((smallscale,smallscale))
    allimages.append(im)
    allimagespath.append('pics/'+file)
allcolors=[]
for f in allimages:
    w=f.width
    h=f.height
    i=0
    ar=ab=ag=0
    c=0
    while(i<w):
        j=0
        while(j<h):
            
            r,g,b=f.getpixel((i,j))
            ar+=r
            ab+=b
            ag+=g
            j+=1
        i+=1
    
    ar/=(w*h)
    ab/=(w*h)
    ag/=(w*h)
    x=(ar,ag,ab)
    allcolors.append(x)   


# In[220]:

mypixel=[]
counter=0
for i in colors:
    r,g,b=i
    mind=1000
    mini=0
    innercounter=0
    for j in allcolors:
        r1,g1,b1=j
        x=abs(r-r1)
        y=abs(g-g1)
        z=abs(b-b1)
        x=(x+y+z)/3
        if(x<mind):
            mind=x
            mini=innercounter
        innercounter+=1
    mypixel.append(mini)
    z+=1
    counter+=1
    
        


# In[221]:

k=0
i=0
while(i<mywidth):
    j=0
    while(j<myheight):
        image.paste(allimages[mypixel[k]],(i,j))
        k+=1
        j+=scale
        #print(allimages[mypixel[k]])
    i+=scale


# In[223]:

image


# In[224]:

image.save('sexy.jpg')


# In[ ]:



