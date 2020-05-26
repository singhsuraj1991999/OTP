'''OTP sending system using smtplib'''
print('hello gays this is next day of prectice')
import smtplib
import random
output=random.randrange(000000,999999)
send_id='singhsuraj1991999@gmail.com'
password='Suraj@1999'
rec_id='singhsuraj1999919@gmail.com'
message='verification code:',output
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(send_id,password)
print('login successful')
server.sendmail(send_id,rec_id,str(message))
print('email has send to this add:',rec_id)

