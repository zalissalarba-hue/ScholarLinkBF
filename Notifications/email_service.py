from flask_mail import Mail, Message

mail = Mail()

def envoyer_notification(email, sujet):

    msg = Message(
        sujet,
        recipients=[email]
    )

    msg.body = "Nouvelle opportunité disponible."

    mail.send(msg)