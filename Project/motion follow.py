
#sends movement location to file

import cv2
import numpy as np



f=open('new.txt','w')

cam = cv2.VideoCapture(0)


t0 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t1 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t2 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)


while True:
  f=open('new.txt','w')   
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)
  res=cv2.bitwise_and(d1, d2)

  cv2.imshow('feed',t1)

  ht,wd=res.shape

  left=res[0:ht,0:(4*wd/10)]
  mid=res[0:ht,(4*wd/10):(6*wd/10)]
  right=res[0:ht,(6*wd/10):wd]

  m_left=np.mean(left)
  m_mid=np.mean(mid)
  m_right=np.mean(right)

  
  if max(m_left,m_right,m_mid)>1:
      if max(m_left,m_right,m_mid)==m_right:       
          f.write('1')
          print 'right'
      elif max(m_left,m_right,m_mid)==m_left:          
          f.write('2')
          print 'left'
      else:
        f.write('0')
  else:
     f.write('0')  
  
  t0 = t1
  t1 = t2
  t2 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
  f.close()
  key = cv2.waitKey(10)

  if key == 27:
    break

 


