from bs4 import BeautifulSoup
import requests
import smtplib
import time

url = 'http://myexternalip.com/raw'
fromaddr = 'sample@email.com'
toaddrs  = 'samplereciver@mail.it'
username = 'samplesender@email.com'
password = 'my_password'
server = smtplib.SMTP('smtp.sample.com:587')

while 1:

        try:
            in_file = open("IPextLog.txt","r")
            lastIP = in_file.read()
            in_file.close()
        except:
            print("FILE error")
        
        try:
            response = requests.get(url)
            IPext0 = BeautifulSoup(response.text, "html.parser")
            IPext= str(IPext0)

            if(IPext!=lastIP):

                try:
                    out_file = open("IPextLog.txt","w")
                    out_file.write(IPext)
                    out_file.close()
                except:
                    print("FILE error")

                print("IP has changed\r\n")
                print(IPext)
                msg = (IPext)
                try:
                    server.starttls()
                    server.login(username,password)
                    server.sendmail(fromaddr, toaddrs, msg)
                    server.quit()
                    print()    
                    print("New IP has been sent!")
                except:
                    print("MAIL error")
            
            else:
                print("IP hasn't changed\r\n")
                print(IPext)

        except:
            print("GET error")
        
        time.sleep(1800)
