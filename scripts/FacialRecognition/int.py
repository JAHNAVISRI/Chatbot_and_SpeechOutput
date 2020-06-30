#!/usr/bin/python2.7

import rospy
from std_msgs.msg import String
global out

def database():
	global pub;
	global pub1;
	global out;
        o = ['you']
	a = ['male','female']
	b = ['child', 'adult', 'old']
	c = ['Stationary','Kids wear','dipers']
        d = ['Shaving set','sprays','haircolour','clothing']
	e = ['haircolour','medicines']
	f = ['Stationary','Kids wear','dipers']
	g = ['sprays','haircolour','clothing']
	h = ['clothing','haircolour,medicines']
	i = 0
	j = 0
	sen = out
	words = out.split()
	print len(words)
	while(i<len(words)):
   	    j=0
    	    while(j<len(o)):       
        	if(words[i]==o[j]):         
         		break
       		j=j+1
    	    print i   
    	    i=i+1
 
	i=0	
	k=0


def one():
	rospy.init_node('int',anonymous=True)
	rospy.Subscriber('/recognised_speech',String,database)
	rospy.Subscriber('/akhil',String,akhil)






if __name__=='__main__':
	one()
	
	
