from flask import request, flash
from flask_mail import Message

def send(app, mail):
    # Obtiene los datos del formulario de contacto enviado por el usuario
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        # Crea un objeto Message para enviar un correo electrónico
        msg = Message(subject = f'Mensaje de contacto de {subject}', # ponemos el proposito del correo
                      sender=app.config['MAIL_USERNAME'], #usamos el correo que destinamos para el envio de mensajes
                      recipients=['joel.flores.developer@gmail.com']) # Agrega aquí la dirección de correo electrónico del destinatario
        
        # Agrega el contenido del mensaje
        msg.body = f'De: {name} <{email}>\n\n{message}'
        
        # Envía el correo electrónico
        mail.send(msg)
        
        flash('nos podremos en contacto')