import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Main Function to get all the necessary information from the site
def check_prize():
    URL = ("https://finance.yahoo.com/quote/ETH-USD?p=ETH-USD")
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    crypto_name = soup.find("h1",{"class":"D(ib) Fz(18px)"}).get_text()
    og_price = soup.find("span",{"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).get_text()
    converted_price = (og_price.replace(',', ""))
    print(crypto_name)
    f_price = float(converted_price)
    print (og_price)
    
    #Targetpoint
    if (f_price > 4000):
        send_email()
        print(crypto_name.strip())
        print(f_price)
    
# Sending the email if the requirements are met
def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

                 # email, two factor password                
    server.login('XXXXXX','XXXXXX')

    subject = "Price has reached the Targetpoint!"
    body = "Its true, go check it out !! -->  https://finance.yahoo.com/quote/ETH-USD?p=ETH-USD"

    msg= f"Subject: {subject}\n\n{body}"

    server.sendmail(
        # From-->
        'XXXXXX',
        # To-->
        'XXXXXX',
        msg
    )
    print("Message has been succefully sent! ")

    server.quit

## Checks for a change every 30 minutes
while(True):  
    check_prize()
    time.sleep(1800)
    

