import smtplib
EMAIL = ""
PASSWORD = ""
RECEPIENT_EMAIL = ""

class NotificationManager:
    def __init__(self):
        self.email = EMAIL
        self.password = PASSWORD
        self.recipient_email = RECEPIENT_EMAIL

    def send_email(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        '''Send email using smtplib you should define all the parameters listed in the function call'''
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(from_addr=self.email, to_addrs=self.recipient_email, msg=f"Subject:Book your flight now/n/nPrice is lower than expected book your flight now! Only ${price} to fly from {origin_city}-{origin_airport} to {destination_city}-{destination_airport}, from {out_date} to {return_date}.")