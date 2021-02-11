#urnEletronica
candidato_prefeito_1 = 0
candidato_prefeito_2 = 0
votos_brancos = 0
anulados = 0

def msg():
    mensagem = input('INICIAR?SIM OU NÃO?')
    mensagem.lower()
    return mensagem

def verdade_falso():
    mensagem =msg()
    if mensagem == 'sim':
        return True
    else:
        return False    

def resultado():
    if candidato_prefeito_1 > candidato_prefeito_2:
        print('VENCEDOR:',candidato_prefeito_1)
    elif candidato_prefeito_2 > candidato_prefeito_1:
        print('VENCEDOR:',candidato_prefeito_2)
    elif candidato_prefeito_1 == candidato_prefeito_2:
        print('EMPATE ,SEGUNDO TURNO!:')    
    else:
        print('NENHUM RECEBEU VOTOS!')
    
    print('-'*50)        
    print(
        'QUANTIDADES DE VONTANTES: ',
         anulados+votos_brancos+candidato_prefeito_2+candidato_prefeito_1
         )
    print('NULOS:',anulados)
    print('EM BRANCOS:',votos_brancos)  
    print('QUANTIDA CANDIDATOS 01:',candidato_prefeito_1)      
    print('QUANTIDA CANDIDATOS 02:',candidato_prefeito_2)

button_power = verdade_falso()

while button_power:
    voto = int(input('DIGITE O CODIGO DO SEU CANDIDATO: '))
    
    if voto == 1:
        candidato_prefeito_1 += 1
        print('Votação realizada! Candidato 1!')
        button_power = verdade_falso()
    elif voto == 2:
        candidato_prefeito_2+=1
        print('Votação realizada! Candidato 2!')
        button_power = verdade_falso()
    elif voto == 0:
        votos_brancos += 1
        print ('Voto em branco!')
        button_power = verdade_falso()
    else:
        anulados += 1
        print('Anulado!')
        button_power = verdade_falso()
        
resultado()