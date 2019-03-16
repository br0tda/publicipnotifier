from bs4 import BeautifulSoup
import requests
import smtplib
import time

while 1:

        in_file = open("IPextLog.txt","r")
        lastIP = in_file.read()
        in_file.close()
        
        url = 'http://myexternalip.com/raw'
        response = requests.get(url)
        IPext0 = BeautifulSoup(response.text, "html.parser")

        IPext= str(IPext0)
        
        if(IPext!=lastIP):
            out_file = open("IPextLog.txt","w")
            out_file.write(IPext)
            out_file.close()
            print("IP has changed\r\n")
            print(IPext)
            fromaddr = 'sample@email.com'
            toaddrs  = 'samplereciver@mail.it"
            msg = (IPext)
            username = 'samplesender@email.com'
            password = 'my_password'
            server = smtplib.SMTP('smtp.sample.com:587')
            server.starttls()
            server.login(username,password)
            server.sendmail(fromaddr, toaddrs, msg)
            server.quit()
            print()    
            print("New IP has been sent!")
        
        else:
            print("IP hasn't changed\r\n")
            print(IPext)
        
        time.sleep(1800)
