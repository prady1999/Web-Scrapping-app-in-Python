import requests
from bs4 import BeautifulSoup
import smtplib,ssl

url="https://www.amazon.in/gp/product/B07DJ8K2KT/ref=s9_acss_bw_cg_Top_1a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-4&pf_rd_r=CFJDPHNSPB9S6Z3JKEB0&pf_rd_t=101&pf_rd_p=59c09f4a-89e0-49aa-b2f0-f3c48b279683&pf_rd_i=1389401031"

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
def check_price():
    page=requests.get(url,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    title=(soup.find(id='productTitle').get_text()).strip()
    price=soup.find(id='priceblock_ourprice').get_text()
    x=price[2:8]
    x=float(x.replace(',',''))

    if x>45000:
        send_mail()
def send_mail():
    to = 'pradyumnberiwal1999@gmail.com'
    gmail_user = 'pradyumnberiwal@gmail.com'
    gmail_pwd = 'wavpqcszowbjksla'
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo() # extra characters to permit edit
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Price Fell Down \n'
    print (header)
    msg = header + '\n https://www.amazon.in/gp/product/B07DJ8K2KT/ref=s9_acss_bw_cg_Top_1a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-4&pf_rd_r=CFJDPHNSPB9S6Z3JKEB0&pf_rd_t=101&pf_rd_p=59c09f4a-89e0-49aa-b2f0-f3c48b279683&pf_rd_i=1389401031 \n\n'
    smtpserver.sendmail(gmail_user, to, msg)
    print('done')
    smtpserver.quit()







check_price()
