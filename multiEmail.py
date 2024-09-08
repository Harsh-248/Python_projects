import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('your_email','your_password') # personal email and login
subject = "test message" #subject to send
body = "This is a test message from Python" #body to send
message = "subject:{}\n\n{}".format(subject, body)
listadd =["enoaf@gmail.com,efbiuw@gmail.com"] #list of email address of every person whom you have to send mail
ob.sendmail('your_email',listadd,message) #sender email,listadd,message
print("Send mail")
ob.quit()