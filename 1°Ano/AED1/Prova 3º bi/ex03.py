def verifica_email(email):
    if '@' in email and ',' not in email and email[0].isalnum():
        email_splitado = email.split('@')
        
        for part in email_splitado:
            if part == '':
                salva_invalido(email)
                return
                
        dominio = email_splitado[-1].split('.')
        nome = email_splitado[0]
        
        for char in nome:
            if not char.isalpha() and char not in '._-':
                salva_invalido(email)
                return
        
        for part in dominio:
            if part == '':
                salva_invalido(email)
                return
    
    else:
        salva_invalido(email)
        return
    

def salva_invalido(email):
    with open('emails_invalidos.txt', mode='a', encoding='utf-8') as file_2:
        file_2.write(email + '\n')
        
    
caracteres_inv = []    
    
with open('emails.txt', mode='r', encoding='utf-8') as file:
    for linha in file:
        linha = linha.replace('\n', '')
        verifica_email(linha)
    
print('emails separados')
