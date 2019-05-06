
# coding: utf-8

# In[1]:


print("Hello world")


# In[2]:


listL1=[2,4,6,8,10]


# In[3]:


listL2=[1,3,5,7,13]


# In[4]:


print(listL1)


# In[5]:


print(listL2)


# In[6]:


sumL1=listL1[0]+listL1[2]+listL1[3]+listL1[1]+listL1[4]


# In[7]:


sumL2=listL2[0]+listL2[2]+listL2[3]+listL2[1]+listL2[4]


# In[8]:


print(sumL1)


# In[10]:


print(sumL2)


# In[11]:


MulL1=listL1[0]*2+listL1[2]*2+listL1[3]*2+listL1[1]*2+listL1[4]*2


# In[12]:


print(MulL1)


# In[13]:


sum=0
for num in listL1
 sum=sum+num
print(sum)


# In[14]:


sum=0
for num in listL1:
 sum=sum+num
print(sum)


# In[15]:


angle=list(range(0,360,30))
print(angle) 


# In[50]:


angle.append(360)
print(angle)


# In[17]:


i=angle.index(90)
print(i)
j=angle.index(270)
print(j)


# In[19]:


k=len(angle)
print(k)


# In[37]:


revIn1=(len(angle)-1)-angle.index(90)
print(revIn1)


# In[38]:


revIn2=(len(angle)-1)-angle.index(270)
print(revIn2)


# In[41]:


angle[revIn1]



# In[54]:


revListN=[]
for i in range(revIn1,revIn2):
   # print(angle[i])
    revListN.append(angle[i])
print(revListN)


# In[69]:



print(angle[revIn1:revIn2:-1])


# In[ ]:



# 5. Clue
arr[x:y:-1]


# In[76]:


List1=[1,2,4,6,8]


# In[71]:


list2=List1.copy()


# In[78]:


List1.remove(List1[3])


# In[79]:


print(List1)


# In[81]:


List2=List1.copy()
print(List2)


# In[82]:


import numpy as np


# In[85]:


import tensorflow as tf


# In[86]:


tup={1,2,3,4}


# In[87]:


print(tup)


# In[89]:


tup.add(10)


# In[90]:


print(tup)


# In[94]:


type(tup)


# In[95]:


tup=(1,2,3,4)
type(tup)


# In[96]:


tup=tup+(10,)


# In[97]:


print(tup)


# In[99]:


print(tup[3])


# In[102]:


list1=list(tup)


# In[103]:


print(list1)


# In[104]:


list1.remove(list1[3])


# In[105]:


print(list1)


# In[106]:


tup=tuple(list1)


# In[107]:


print(tup)


# In[112]:


states={'Bihar':[23456,'Patna',True],'Telangana':[35000000,'Hyderabad',True], 'Andhra Pradesh':[2300000,'Hyderabad',False]}


# In[113]:


print(states.get('Bihar'))


# In[114]:


pi=3.14
def deg_rad(angle):
    va=angle*pi/180
    return(va)


# In[115]:


deg_rad(360)


# In[116]:


deg_rad_inline=lambda angle,rotate: angle/360*22/7+rotate
deg_rad_inline(30,deg_rad(90))

