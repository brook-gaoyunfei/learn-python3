from email.mime.text import MIMEText
from email import encoders 
from email.header import Header 
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s): 
    name, addr = parseaddr(s) 
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = '17647306306@163.com'
password = 'ZMXJXSCNWEUCDTFX'
to_addr	= '17647306306@163.com'
smtp_server = 'smtp.163.com'

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8') 
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr) 
msg['To'] = _format_addr('管理员 <%s>' % to_addr) 
msg['Subject'] = Header('邮件测试', 'utf-8').encode()


server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string()) 
server.quit()
