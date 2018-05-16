import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import config as cfg

from_addr = cfg.addr.get('from')
to_addr = cfg.addr.get('to')

body = """
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy 
eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam 
voluptua. At vero eos et accusam et justo duo dolores et ea rebum. 
Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor 
sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam 
nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed 
diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. 
Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor 
sit amet.
"""

def main():
    # Create mail
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'My awesome email'
    msg.attach(MIMEText(body, 'plain'))

    smtp_server = smtplib.SMTP(cfg.smtp.get('server'), 587)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(
        user=cfg.smtp.get('login'), password=cfg.smtp.get('password')
    )
    
    smtp_server.sendmail(from_addr, to_addr, msg.as_string())
    smtp_server.quit()

    print('done')


if __name__ == '__main__':
    main()
