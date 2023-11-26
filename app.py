from flask import Flask, render_template, url_for, request
from email.message import EmailMessage
import ssl
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_data', methods=['POST', 'GET'])
def process_data():
    if request.method == 'POST':
        user_input = request.form.get('userInput')
        selected_option = request.form.get('selectedOption')

        # Process the user input and selected option here using Python
        # For example, you can print the data to the console
        print(f'User Input: {user_input}')
        print(f'Selected Option: {selected_option}')

        # You can also perform more complex logic or database operations here

        return "Data processed successfully"  # Return a response to the client
    
@app.route('/send_email', methods=['POST'])
def send_email_route():

    if request.method == 'POST':  
        # Add any necessary logic to get recipient's email and name from the form data
        recipient_email = request.form.get('email')
        recipient_option = request.form.get('selectedOption')

        # Call the send_email function
        #send_email(recipient_email)
        print(f'User Input: {recipient_email}')
        print(f'Selected Option: {recipient_option}')

        send_email(recipient_email,recipient_option)
        
        # You can redirect the user to a thank you page or return a success message
        return "Email sent successfully!"



#def send_email(email_recipent,name):
def send_email(email, option):
    email_sender = 'saintkeyproducts@gmail.com'
    email_password = 'rbue tdrd nvyn wtat'
    email_receiver = email
    

    # Default subject and body
    subject = 'Default Subject'
    body = 'Default body'

    # Using if-elif-else to mimic switch-case behavior
    if option == 'Boxing Shoe':
        subject = 'MDB Label Boxing Shoes Order Confirmation'
        body = """Hello Saint,

Thank you for purchasing the MDB Label Boxing Shoes.

Please reply with your shipping address and shoe size to complete your order.

Did you know? You can elevate your athletic experience by upgrading to the SASN Sprint & Spar Bundle! Add a SASN Running Bag to your boxing shoe order for just $16 extra

Peace to the Saints

-Saint Key 
    """
    elif option == 'Running Bag':
        subject = 'SASN Running Bag Order Confirmation'
        body = """Hello Saint,

Thank you for your purchase of the SASN Running Bag. 

Please reply with your shipping address to complete your order.

You will receive a confirmation as soon as I have an estimated delivery date and tracking number for your purchase.

Peace to the Saints.

-Saint Key
"""
    elif option == 'Bundle':
        subject = 'SASN Sprint & Spar Bundle Order Confirmation'
        body = """Hello Saint,

Thank you for choosing the 'SASN Sprint & Spar Bundle', featuring the MDB Label Boxing Shoes and SASN Running Bag.

Please reply with your shipping address and shoe size to complete your order.

You will receive a confirmation as soon as I have an estimated delivery date and tracking number for your purchase.

Peace to the Saints.

-Saint Key
"""

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

