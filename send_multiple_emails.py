import smtplib as m

obj = m.SMTP("smtp.gmail.com",587)
obj.ehlo()
obj.starttls()
obj.login(" enter your gmail----------------", "enter your password---------")
subject = "test Python"
body ="I LOVE TO CODING WITH THE PYTHON"
massage = "subject:{}\n\n{}".format(subject,body)
listadd = ["mmkr976@gmail.com",
           "sudhanshu3454@gmail.com"]
obj.sendmail("anmahkumar9878@gmail.com", listadd, massage)
print("send mail")
obj.quit()