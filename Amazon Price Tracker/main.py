import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
from email.mime.text import MIMEText

subject = "PRICE REDUCED!!!"
body = "Hey Tarun! Hope you're doing well. Please note that the \'SS Kashmir Willow Leather Ball Cricket Bat, Exclusive Cricket Bat for Adult Full Size with Full Protection Cover\" is now available at a price of $50.00. Please find the link below: https://www.amazon.com/SS-Kashmir-Willow-Cricket-Handle/dp/B00LFDCI5G/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.8sHjM__SdIh1wfLwIAp9ySDXdjneR19Y0x0QBd5g7Pv0ntUKWWOaqsA_tE0bXXq3XjhJ8hZs_XSMV_iP2vbwzpCMdVlJYQ0Sl2n1FY4SLcMdFpyi81xupJE6JiW1xzsp2nmSGFBpnyJ4K5FV0FLJg9EdqdUvUZs_4Z2BE4v58NCw1-S1IMOQbZl-BD5TjfwkIUB2cgvp-QKStQdbbNx3L_VA7jsF4Ayl-peavpRAwiyntrwqwsTXWzk1iZiWJzTEA3pyhkfWe_g0azfjYHISZ2AjezexaCbGqAW_qskfNKY.LSgEJDoXDbFwOF_h-30Pc8TbgVpqdC1VzTywE5A8j-c&dib_tag=se&keywords=cricket%2Bbat&qid=1716929918&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
sender = "tarun05rawat@gmail.com"
recipients = ["rawattar@msu.edu","tarunrawat3011@gmail.com"]
password = "pvkd xslo ewtj fpbm"

response = requests.get("https://www.amazon.com/SS-Kashmir-Willow-Cricket-Handle/dp/B00LFDCI5G/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.8sHjM__SdIh1wfLwIAp9ySDXdjneR19Y0x0QBd5g7Pv0ntUKWWOaqsA_tE0bXXq3XjhJ8hZs_XSMV_iP2vbwzpCMdVlJYQ0Sl2n1FY4SLcMdFpyi81xupJE6JiW1xzsp2nmSGFBpnyJ4K5FV0FLJg9EdqdUvUZs_4Z2BE4v58NCw1-S1IMOQbZl-BD5TjfwkIUB2cgvp-QKStQdbbNx3L_VA7jsF4Ayl-peavpRAwiyntrwqwsTXWzk1iZiWJzTEA3pyhkfWe_g0azfjYHISZ2AjezexaCbGqAW_qskfNKY.LSgEJDoXDbFwOF_h-30Pc8TbgVpqdC1VzTywE5A8j-c&dib_tag=se&keywords=cricket%2Bbat&qid=1716929918&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1",
                        headers={
                          "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
                          "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
                          "sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\""
                        })
amazon_page = response.text

soup = BeautifulSoup(amazon_page,"lxml")

price1 = float(soup.find(name="span",class_ = "a-price-whole").getText())

price2 = float(soup.find(name="span",class_ = "a-price-fraction").getText())


final_price = price1 + (price2/100)

target_price = 60.0

if final_price < target_price:
  connection = smtplib.SMTP(host='smtp.gmail.com',port=587)
  connection.starttls()
  connection.login(user=sender,password=password)
  connection.sendmail(from_addr=sender,to_addrs=recipients,msg=f"Subject:{subject}\n\n{body}")
  connection.close()








