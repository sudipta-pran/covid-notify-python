import requests
import time
import smtplib
from email.message import EmailMessage
from credentials import email_id, password

msg = EmailMessage()
content = ''

while True:
    response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict',
                            params={'district_id': '17', 'date': '13-05-2021'},
                            headers={'Accept': '*/*', 'Accept-Lanhuage': 'hi_IN',
                                     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'},
                            )
    data = response.json()
    items = data['sessions']
    for item in items:
        print(f"Available center: {item['name']}")
        content += '''<p>Available center: {name}</p>
                    <p>Vaccine Available: {available}</p>
                    <p>Address: {address}</p><br/><br/>
                    '''.format(
            name=item['name'],
            available=item['available_capacity'],
            address=item['address']
        )
    msg['Subject'] = 'Covid Vaccination Alerts'
    msg['From'] = email_id,
    msg['To'] = 'example@gmail.com'
    msg.set_content(content, subtype='html')
    # SMTP server details. See instruction video for gmail, or use comapny mail
    server = smtplib.SMTP('yourSMTPserver', 587)
    server.login(email_id, password)
    server.send_message(msg)
    server.quit()
    content = ''
    time.sleep(60)
