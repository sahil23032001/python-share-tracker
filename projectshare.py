from tkinter import *
import colorama
from colorama import Fore, Back , Style
import array 
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
#nifty sensex------------------------------------------------------------------------------- 
stock_url="https://www.moneycontrol.com/"
price=requests.get(stock_url)
soup=BeautifulSoup(price.text,'html.parser')
mainframs=soup.find(class_='scrollBar srl_MA').getText().strip().split()
    
top_sensex=mainframs.index("Sensex")+1
top_sensex=float(mainframs[top_sensex])

top_nifty= mainframs.index("50")+1
top_nifty=float(mainframs[top_nifty])
Sensex=top_sensex
Nifty=top_nifty

#stocks with analaysis
# 3 stocks only --- 
idea_url="https://in.finance.yahoo.com/quote/IDEA.NS?p=IDEA.NS&.tsrc=fin-srch"
idea_price=requests.get(idea_url)
idea_soup=BeautifulSoup(idea_price.text,'html.parser')
idea_mainframe=idea_soup.find('span',{'data-reactid' :'52'}).getText().strip().split()

idea_final=float(idea_mainframe[0])

#tata motors
tata_url="https://in.finance.yahoo.com/quote/TATAMOTORS.NS?p=TATAMOTORS.NS&.tsrc=fin-srch"
tata_price=requests.get(tata_url)
tata_soup=BeautifulSoup(tata_price.text,'html.parser')
tata_mainframe=tata_soup.find('span',{'data-reactid' :'52'}).getText().strip().split()
tata_final=float(tata_mainframe[0])

#itc
rel_url="https://in.finance.yahoo.com/quote/ITC.NS?p=ITC.NS&.tsrc=fin-srch"
rel_price=requests.get(rel_url)
rel_soup=BeautifulSoup(rel_price.text,'html.parser')
rel_mainframe=rel_soup.find('span',{'data-reactid' :'52'}).getText().strip().split()
rel_final=float(rel_mainframe[0])




    

#refresh function use 2 click
list1=[]#sensex
list2=[]#nifty 
list3=[]#idea
list4=[]#tata
list5=[]#Itc
def refresh():
         
           
          
          
                  global count 
                  count = count+1
                  
                  import requests
                  from bs4 import BeautifulSoup
                  stock_url="https://www.moneycontrol.com/"
                  price=requests.get(stock_url)
                        
                  soup=BeautifulSoup(price.text,'html.parser')
                  mainframs=soup.find(class_='scrollBar srl_MA').getText().strip().split()
                            
                  top_sensex=mainframs.index("Sensex")+1
                  
                  new_sensex=float(mainframs[top_sensex])
                        
                  top_nifty= mainframs.index("50")+1
                  
                  new_nifty=float(mainframs[top_nifty])
                  list1.append(new_sensex)
                  list2.append(new_nifty)
                  
                  
                  new_nifs=float(list2[0])
                  
                  new_sen=float(list1[0]) 
                  
                          #this print 
                
                  newsensex=str(new_sen)
                  newnifty=str(new_nifs)
                  c=Label(root, text=newnifty)
                  d=Label(root, text=newsensex)
                        
                  c.grid(row = 4,column=3)
                  d.grid(row=4,column=6)
                  #idea
                  idea_url="https://in.finance.yahoo.com/quote/IDEA.NS?p=IDEA.NS"
                  idea_price=requests.get(idea_url)
                  idea_soup=BeautifulSoup(idea_price.text,'html.parser')
                  idea_mainframe=idea_soup.find('span',{'data-reactid' :'52'}).getText().strip().split()
                  idea_finals=float(idea_mainframe[0])
                  list3.append(idea_finals)
                  new_ideas=float(list3[0])
                  ideas=str(new_ideas)
                  f=Label(root,text=ideas)
                  f.grid(row=6,column=5)
                  #tata
                  tata_url="https://in.finance.yahoo.com/quote/TATAMOTORS.NS?p=TATAMOTORS.NS&.tsrc=fin-srch"
                  tata_price=requests.get(tata_url)
                  tata_soup=BeautifulSoup(tata_price.text,'html.parser')
                  tata_mainframe=tata_soup.find('span',{'data-reactid' :'52'}).getText().strip().split()
                  tata_finals=float(tata_mainframe[0])
                  list4.append(tata_finals)
                  new_tatas=float(list4[0])
                  tatas=str(new_tatas)
                  t=Label(root,text=tatas)
                  t.grid(row=8,column=5)
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  #Itc
                  rel_url="https://in.finance.yahoo.com/quote/ITC.NS?p=ITC.NS&.tsrc=fin-srch"
                  rel_price=requests.get(rel_url)
                  rel_soup=BeautifulSoup(rel_price.text,'html.parser')
                  rel_mainframe=rel_soup.find('span',{'data-reactid' :'52'}).getText().strip().split()
                  rel_finals=float(rel_mainframe[0])
                  list5.append(rel_finals)
                  new_rels=float(list5[0])
                  rels=str(new_rels)
                  r=Label(root,text=rels)
                  r.grid(row=10,column=5)
                  
                  
                  
                  
                  
                  
                  
                  # color
                  if( count==1):       
                      if Nifty > new_nifs:
                          c.config(bg="red")
                      elif Nifty < new_nifs:
                          c.config(bg="green")
                      else  :
                          c.config(bg="grey")
                    
               
                      if Sensex > new_sen:
                         d.config(bg="red")
                      elif Sensex < new_sen:
                          d.config(bg="green")
                      else :
                         d.config(bg="grey")
                         
                      if idea_final>new_ideas:
                          f.config(bg="red")
                      elif idea_final < new_ideas:
                          f.config(bg="green")
                      else :
                         f.config(bg="grey") 
                         
                      if tata_final > new_tatas:
                          t.config(bg="red")
                      elif tata_final < new_tatas:
                          t.config(bg="green")
                      else :
                         t.config(bg="grey") 
                         
                         
                      if rel_final>new_rels:
                          r.config(bg="red")
                      elif rel_final < new_rels:
                          r.config(bg="green")
                      else :
                         r.config(bg="grey")    
                     
                  else:
                              import requests
                              from bs4 import BeautifulSoup
                              stock_urls="https://www.moneycontrol.com/"
                              prices=requests.get(stock_urls)
                                        
                              soups=BeautifulSoup(prices.text,'html.parser')
                              mainframss=soups.find(class_='scrollBar srl_MA').getText().strip().split()
                                            
                              top_sensexs=mainframss.index("Sensex")+1
                              newest_sensexs=float(mainframss[top_sensexs])
                                  
                              top_niftys= mainframss.index("50")+1
                              newest_niftys=float(mainframss[top_niftys])
                             
                              jain=(list2[len(list2)-2])   
                                  #this print 
                              sahil=(list1[len(list1)-2])
                              newsensex=str(newest_sensexs)
                              newnifty=str(newest_niftys)
                              c=Label(root, text=newnifty)
                              d=Label(root, text=newsensex)
                                
                              c.grid(row = 4,column=3)
                              d.grid(row=4,column=6)
                              #idea
                              idea_urls="https://in.finance.yahoo.com/quote/IDEA.NS?p=IDEA.NS"
                              idea_prices=requests.get(idea_urls)
                              idea_soups=BeautifulSoup(idea_prices.text,'html.parser')
                              idea_mainframes=idea_soups.find('span',{'data-reactid' :'52'}).getText().strip().split()
                              idea_finalss=float(idea_mainframes[0])
                              
                              ide=(list3[len(list3)-2])
                              ideas=str(idea_finalss)
                              f=Label(root,text=ideas)
                              f.grid(row=6,column=5)
                              
                              #tata
                              tata_urls="https://in.finance.yahoo.com/quote/TATAMOTORS.NS?p=TATAMOTORS.NS&.tsrc=fin-srch"
                              tata_prices=requests.get(tata_urls)
                              tata_soups=BeautifulSoup(tata_prices.text,'html.parser')
                              tata_mainframes=tata_soups.find('span',{'data-reactid' :'52'}).getText().strip().split()
                              tata_finalss=float(tata_mainframes[0])
                              
                              tat=(list4[len(list4)-2])
                              tatas=str(tata_finalss)
                              t=Label(root,text=tatas)
                              t.grid(row=8,column=5)
                              
                              
                              
                              
                              #itc
                              rel_urls="https://in.finance.yahoo.com/quote/ITC.NS?p=ITC.NS&.tsrc=fin-srch"
                              rel_prices=requests.get(rel_urls)
                              rel_soups=BeautifulSoup(rel_prices.text,'html.parser')
                              rel_mainframes=rel_soups.find('span',{'data-reactid' :'52'}).getText().strip().split()
                              rel_finalss=float(rel_mainframes[0])
                              
                              itc=(list5[len(list5)-2])
                              itcs=str(rel_finalss)
                              r=Label(root,text=itcs)
                              r.grid(row=10,column=5)
                              

                                                              
                                  #color
                              if newest_niftys > jain:
                                      c.config(bg="green")
                              elif newest_niftys < jain:
                                      c.config(bg="red")
                              else  :
                                      c.config(bg="grey")
                                    
                                 #color 
                              if newest_sensexs > sahil:
                                      d.config(bg="green")
                              elif newest_sensexs < sahil:
                                      d.config(bg="red")
                              else :
                                      d.config(bg="grey")
                                      
                              if idea_finalss > ide:
                                  f.config(bg="green")
                              elif idea_finalss < ide:
                                  f.config(bg="red")  
                              else:
                                  f.config(bg="grey")
              
                              if  tata_finalss > tat :
                                  t.config(bg="green")
                              elif tata_finalss < tat :
                                  t.config(bg="red")  
                              else:
                                  t.config(bg="grey")
                               
                              if rel_finalss > itc :
                                  r.config(bg="green")
                              elif rel_finalss < itc :
                                  r.config(bg="red")  
                              else:
                                  r.config(bg="grey")    

count = 0

root =Tk()
finalsensex=str(top_sensex)
finalnifty=str(top_nifty)
finalidea=str(idea_final)
finaltata=str(tata_final)
finalitc=str(rel_final)
#labels
S=Label(root,text='Sensex',font='Helvetica 18 bold')
N=Label(root, text='Nifty' ,font='Helvetica 18 bold')
I=Label(root, text='Idea' ,font='Helvetica 18 bold')
T=Label(root, text='Tata-Motors' ,font='Helvetica 18 bold')
R=Label(root, text='ITC' ,font='Helvetica 18 bold')
#direct print
A=Label(root, text=top_nifty)
B=Label(root, text=top_sensex)
C=Label(root,text=finalidea)
D=Label(root,text=finaltata)
E=Label(root,text=finalitc)
#
A.grid(row = 4,column=3)
B.grid(row=4,column=6)
C.grid(row=6,column=5)
D.grid(row=8,column=5)
E.grid(row=10,column=5)
#
S.grid(row=3 ,column=3)
N.grid(row=3 ,column=6)
I.grid(row=5,column=5)
T.grid(row=7,column=5)
R.grid(row=9,column=5)
#
refresh=(Button(root, text="refresh",command=refresh ))
refresh.grid(row=0,column=5)

mainloop()
