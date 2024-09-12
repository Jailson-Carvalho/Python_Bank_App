'''
PROJETO

Fomos contratados por um grande banco para desenvolver o seu novo sistema. 
Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. 
Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

Operação de depósito
Deve ser possível depositar valores positivos para a minha conta bancária. 
A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. 
Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

Operação de saque
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. 
Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. 
Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

Operação de extrato
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. 
Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45

'''

# Menu para ser exibido as opçõe aos usuários
menu = '''
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Sair
=> '''

# Variávei para receber os inputs
saldo = 0
limite = 500
extrato = ''
qtd_saque = 0
LIMITE_SAQUE = 3

# loop  que continuará executando até que um comando break seja encontrado. Isso é útil para criar um menu interativo que o usuário pode acessar repetidamente até escolher sair.
while True: 
    # Exibe o menu e coleta a entrada do usuário. O valor inserido será armazenado na variável opcao, que é uma string. 
    opcao = input(menu)
    
    # Verifica se a opção escolhida pelo usuário é "1"
    if opcao == '1':
        # Solicita ao usuário o valor do depósito e converte o valor digitado de string para float para garantir que cálculos matemáticos possam ser feitos.
        valor = float(input("Informe o valor a ser depositado: "))
        
        #  Verifica se o valor inserido é maior que zero. Apenas valores positivos podem ser depositados.
        if valor > 0:
            # Se o valor for válido, ele é adicionado ao saldo existente do usuário.
            saldo += valor
            # Adiciona uma linha ao extrato com o valor depositado. O formato .2f é usado para exibir o valor com duas casas decimais.
            extrato += (f'Valor depositado: R$ {valor:.2f}\n')
        # Se o valor for inválido (por exemplo, menor ou igual a zero), uma mensagem de erro é exibida.  
        else:
            print("Opção inválida!")
            
            
    # Verifica se a opção escolhida é "2".
    elif opcao == '2':
        # Solicita ao usuário o valor do saque e converte a entrada para float.
        valor = float(input("Informe o valor a ser sacado: "))
        # verifica se o saldo é menor que o valor solicitado para saque.
        excedeu_saldo = saldo < valor
        # verifica se o valor solicitado é maior que o limite de saque permitido.
        excedeu_limite = valor > limite
        # verifica se o número de saques já atingiu o limite diário (por exemplo, 3).
        excedeu_numero_saque = qtd_saque >= LIMITE_SAQUE
        
        # Se o saldo for insuficiente para o saque, exibe uma mensagem de erro.
        if excedeu_saldo:
            print("Saldo Insuficiente!")
        #  Se o valor do saque for maior que o limite permitido (R$ 500,00 neste caso), exibe uma mensagem informando o limite.
        elif excedeu_limite:
            print("Você só pode sacar R$ 500,00 por vez.")
        # Se o usuário já atingiu o limite de saques diários, exibe uma mensagem.
        elif excedeu_numero_saque:
            print(
                "Você já realizou três saques hoje. O limite de saque são três por dia.")
        
        # Verifica se o valor de saque é maior que zero (apenas saques com valores positivos são permitidos).
        elif valor > 0:
            # Deduz o valor solicitado do saldo.
            saldo -= valor
            # Adiciona uma linha no extrato com o valor sacado.
            extrato += f"Saque: R$ {saldo:.2f}\n"
            # Incrementa o contador de saques, para controlar o limite diário.
            qtd_saque +=1
    
    # Verifica se a opção escolhida é "3", o que geralmente corresponde à exibição do extrato.        
    elif opcao == '3':
        # Exibe um cabeçalho para o extrato.
        print("_______________EXTRATO_______________")
        
        # Se o extrato estiver vazio (nenhuma movimentação foi realizada), exibe uma mensagem indicando isso. Caso contrário, exibe o conteúdo do extrato.
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        # Exibe o saldo atual formatado com duas casas decimais.
        print(f"\nSaldo: R$ {saldo:.2f}")
        # Exibe uma linha de rodapé para o extrato.
        print("_____________________________________")
    
    # Verifica se a opção escolhida é "4", o que indica que o usuário deseja sair do programa. Se for o caso, exibe uma mensagem de encerramento e usa o comando break para sair do loop, finalizando o programa.
    if opcao == '4':
        print("Operação encerrada")
        break