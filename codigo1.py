import smtplib
import ssl
import email.message
import datetime


def enviaremail():
    msg = email.message.Message()
    msg['Subject'] = (subjecto)

    body = f"{menssagem}"
    msg['From'] = ''#digitar email entre aspas
    password = '' #digitar a senha entre aspas
    msg['To'] = emailenviar
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body)

    context = ssl.create_default_context()
    with smtplib.SMTP('smtp.gmail.com', 587) as conexao:
        conexao.ehlo()
        conexao.starttls(context=context)
        conexao.login(msg['From'], password)
        try:
            conexao.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
            return True
        except:
            return False

try:
    subjecto = input('Digite o subject: ')
    menssagem = input('digite a menssagem do email: ')
    emailenviar = input('Digite o email o qual quer enviar: ')
    enviarAgora = int(input('Deseja enviar agora ou agendar? [1/2]: '))

    if enviarAgora == 1:
        print('Enviando...')
        enviaremail()
        enviado = enviaremail()
        if enviado:
            print(f'email enviado com sucesso para {emailenviar}')
        else:
            print('Email inserido invalido ou inexistente')

    elif enviarAgora == 2:
        horaEnviar = int(input('Digite a hora que quer enviar o email: '))
        minutoEnviar = int(input('Digite o minuto que quer enviar o email: '))
        print(f'Aguardando {horaEnviar}:{minutoEnviar}...')

        while True:
            if horaEnviar==datetime.datetime.now().hour and minutoEnviar==datetime.datetime.now().minute:
                print('Enviando...')
                enviaremail()
                break
        
        enviado = enviaremail()
        if enviado:
            print(f'Email enviado com sucesso para {emailenviar}')
        else:
            print('Email isnerido invalido ou inexistente')
            
except ValueError:
    print('Digite apenas numeros na selecao')