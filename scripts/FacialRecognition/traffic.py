#!/usr/bin/python2.7

import rospy
from std_msgs.msg import String
global akhil
global n
n=0


def traffic():
        global pub
        global pub1
        global akhil
        global pub2
        sen=akhil
	v=['GET','GRASP','TAKE','PICK UP','DELIVER','PUT','PLACE','TELL','SAY','GO','NAVIGATE','ENTER','FIND']
	pl=['EXIT','TABLE','COUNTER','KITCHEN','BEDROOM','LIVING','CORRIDOR','OFFICE','DINNING','BAR','SINK','','']
	obj=['PRINGLES','IT','APPLE','CRACKERS','COKE','TEA','BEER','BISCUITS','SOAP','','','','']
        per=['','','akhil','','','','','','','','','','']
	po =['','','3.805 5.42--','','','','','','','','','','']
        i=0
               
	j=0
	k=0
	verbs=['','','']
	place=['','','']
	person=['','','']
	vas=['','','']
        words = akhil.split()
	print len(words)
	while(i<len(words)):
   	    j=0
    	    while(j<len(v)):
       
        	if(words[i]==v[j]):
         
         		verbs[k]=words[i]
         		
         		k=k+1
         		break
       		j=j+1
    		print i   
    	    i=i+1
 
	i=0	
	k=0

	while(i<len(words)):
    	   j=0
    	   while(j<len(pl)):
       
       		if(words[i]==pl[j]):
         
         		place[k]=words[i]
         		
         		k=k+1
         		break
       		j=j+1
    		print i   
    	   i=i+1 


  
	i=0
	k=0

	while(i<len(words)):
    	    j=0
    	    while(j<len(obj)):
       
       		if(words[i]==obj[j]):
         
         		person[k]=words[i]
         		
         		k=k+1
        	 	break
       		j=j+1
    		print i   
    	    i=i+1


	i=0
	k=0

	while(i<len(words)):
    	   j=0
    	   while(j<len(obj)):
       
       		if(words[i]==per[j]):
         
         		vas[k]=words[i]
         		
         		k=k+1
        	 	break
       		j=j+1
    		print i   
    	   i=i+1



        i=0
        n=0
        print place
	while(i<len(pl)):
	  if(place[n]==pl[i] and place[n]!=''):
	     pub.publish(str(po[i]))
          if(person[n]==per[i] and person[n]!=''):
             pub1.publish(str(person[i]))
          if(vas[n]==obj[i] and vas[n]):
             pub2.publish(str(vas[i]))
          i=i+1
           


def traff():
    global n
    n=n+1
    traffic()
    
def akhil(data):
    global akhil
    akhil=data.data
    traffic()
    
    




def listener():
    global pub
    global pub1
    global pub2
    rospy.init_node('traffic1',anonymous=True)
    rospy.Subscriber('/traff',String,traffic)
    rospy.Subscriber('/akhil',String,akhil)
    pub = rospy.Publisher('/posision', String, queue_size=10)
    pub1= rospy.Publisher('/object', String, queue_size=10)
    pub2 = rospy.Publisher('/person',String, queue_size=10)
    rospy.spin()
    
    
    
    




if __name__=='__main__':
   listener()

