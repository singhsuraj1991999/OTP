'''OTP sending system using smtplib'''
print('hello gays this is next day of prectice')
import smtplib
import random

'''genrating random values and randrange use to get any random values (start, end)'''
output=random.randrange(000000,999999)
send_id='singhsuraj1991999@gmail.com'
password='Suraj@1999'
rec_id='singhsuraj1999919@gmail.com'
message='verification code:',output

'''stablishing the connection with gmail'''
server=smtplib.SMTP('smtp.gmail.com',587)

'''making secure the connection '''
server.starttls()

'''login into the gmail'''
server.login(send_id,password)
print('login successful')

'''sending the mail'''
server.sendmail(send_id,rec_id,str(message))
print('email has send to this add:',rec_id)

