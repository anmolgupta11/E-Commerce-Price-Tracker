import requests
from bs4 import BeautifulSoup  # library for website scraping 
import smtplib # library for sending e-mail
import time 

# as an example, I have taken a product from Amazon
URL = 'https://www.amazon.in/Canon-1500D-Digital-Camera-S18-55/dp/B07BS4TJ43/ref=sr_1_1?dchild=1&keywords=dslr&qid=1594041967&sr=8-1'

# for your own User Agent, simply google "my user agent"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

# function which checks prices
def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[2:4]+price[5:8])

    if(converted_price < 24000.0):
        send_mail()

    print(converted_price)
    print(title.strip())

# function for sending email to the user when the prices fell for a product
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() # EHLO is a command sent by an email server to identify itself when connecting to another email
    server.starttls()
    server.ehlo()

    # in server.login(), the first argument is the mail ID (please don't spam :3) whereas the 
    # second argument is the Google app password I have set which works with 2 factor authentication and no third party can access it
    server.login('anmol.gupta.che17@itbhu.ac.in', 'qyzinjbjdsiisirw')


    subject = 'Hey Anmol, Price fell down for your product!!!'
    body = 'Hey! \nThe price of your product has fallen below your desired price of Rs. 24000! \nCheck it here: https://www.amazon.in/Canon-1500D-Digital-Camera-S18-55/dp/B07BS4TJ43/ref=sr_1_1?dchild=1&keywords=dslr&qid=1594041967&sr=8-1' 

    msg = f"Subject: {subject}\n\n{body}"

    # server.sendmail() has 3 arguments, first is the mail from which the notification is to be sent, 
    # second argument is the mail that will receive the notification and third is the message
    server.sendmail('anmol.gupta.che17@itbhu.ac.in', 'mail.anmolgupta@gmail.com', msg)

    print("EMAIL HAS BEEN SENT")

    server.quit()

while(True):
    check_price()
    time.sleep(3600) # putting sleep time = 1 hr
