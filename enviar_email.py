from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)


app.config['MAIL_SERVER']='SERVIDOR_EMAIL'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'ENDEREÇO_EMAIL'
app.config['MAIL_PASSWORD'] = 'SENHA_EMAIL'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Título', sender = 'REMETENTE_EMAIL', recipients = ['DESTINO_EMAIL'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)