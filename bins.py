import random 
import time
import sys
import os
#RR = "\033[32;m"
RR = ""
def f(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(1./170)
f(RR+"[#] si el numero es rechasado cambia los ultimos 4 dijitos del bin")
time.sleep(2)
os.system("clear")                
f(RR+"█▀▀█ ▀█▀ █▄░▒█ █▀▀▀█")
f(RR+"█▀▀▄ ░█░ █▒█▒█ ▀▀▀▄▄")
f(RR+"█▄▄█ ▄█▄ █░░▀█ █▄▄▄█")

vy= float(input("tiempo de retardo: "))
gh = 0
while True:
    i = random.randrange(1,19)
    if i == 1:
            d =("20101027")
    if i == 2:    
            d =("61829101")
    if i == 3:
            d = ("67152801") 
    if i == 4:
            d = ("81910183")  
    if i == 5:
            d = ("61389191")
    if i == 6:    
            d = ("08281998")
    if i == 7:
            d = ("92837271")
    if i == 8:
            d = ("62810271")
    if i == 9:
            d = ("74788668")
    if i == 10:
            d = ("47619179")
    if i == 12:    
            d = ("61639101")
    if i == 13:
            d = ("46130173") 
    if i == 14:
            d = ("51291736")  
    if i == 15:
            d = ("37883178")
    if i == 16:    
            d = ("81377317")
    if i == 17:
            d = ("88371938")
    if i == 18:
            d = ("17371838")
    if i == 19:
            d = ("64784819")                
    x = random.randrange(1,4)    
    if x == 1:
            c ="4480"
    if x == 2:
           c="4850" 
    if x == 3:        
        c="4822"      
    if x == 4:        
        c="4811"        
    n = random.randrange(1,3)    
    if n == 1:
        v = "5256"
    if n == 2:
            v = "4589"
    if n == 3:
            v = "5289"
    if n == 4:
           v = "0275"
    if n == 5:
            v = "4509"
    if n == 6:
            v = "4201"        
    s = random.randrange(1,12)    
    if s == 1:
        k = "443"
    if s == 2:
            k = "423"
    if s == 3:
            k = "891"
    if s == 4:
           k = "251"
    if s == 5:
            k = "091"
    if s == 6:
            k = "251"        
    if s == 8:
        k = "256"
    if s == 8:
            k = "459"
    if s == 9:
            k  = "529"
    if s == 10:
           k = "451"
    if s == 11:
            k = "651"
    if s == 12:
            k = "781"     
    e = random.randrange(1,12)    
    if e == 1:
        qk = "06/25"
    if e == 2:
            qk = "09/28"
    if e == 3:
            qk = "07/24"
    if e == 4:
           qk = "02/28"
    if e == 5:
            qk = "05/26"
    if e == 6:
            qk = "04/26"        
    if e == 8:
        qk = "02/26"
    if e == 8:
            qk = "04/29"
    if e == 9:
            qk  = "03/26"
    if e == 10:
           qk = "09/24"
    if e == 11:
            qk = "07/26"
    if e == 12:
            qk = "10/29"            
    gg = f"cvc:{k}"     
    op = f"MM/AA:{qk}"  
    xc =f"VISA:{c}{d}{v}"    
    time.sleep(vy)
    print(xc, gg, op)
