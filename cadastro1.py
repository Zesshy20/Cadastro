opcao = ""
cadastro = {}

while opcao != '5':
    print('Entre com a opcao desejada: ')
    print('1 - Inserir   2 - Consultar   3 - Alterar   4 - Deletar   5 - Sair do programa')
    opcao = input('Opção escolhida: ')
    if opcao == '1':
        print('Vamos inserir um usuário.')
        nome = input('Nome: ')
        email = input('E-mail: ')
        email = email.lower() #deixa o email em letra minúscula
        telefone = input('Telefone (apenas números): ')
        cpf = input('Entre com o CPF: ')
        #removendo pontos ou traços do CPF
        cpf = cpf.split(".")
        cpf = ''.join(cpf)
        cpf = cpf.split('-')
        cpf = ''.join(cpf)
        #o cpf é a chave primária
        dados_usuario = cadastro.get(cpf)
        #verifica se o usuário existe, só cadastra se for novo
        if dados_usuario is None:
            cadastro.update({cpf: {'Nome': nome, 'E-mail': email, 'Telefone': telefone}})
            print(cadastro)
        else:
            print('CPF já cadastrado no sistema. Para atualizar informações, use a opção 3.')
        
    elif opcao == '2':
        print('Vamos consultar um usuário.')
        cpf = input('Entre com o CPF do usuário: ')
        #removendo pontos ou traços do CPF
        cpf = cpf.split(".")
        cpf = ''.join(cpf)
        cpf = cpf.split('-')
        cpf = ''.join(cpf)
        dados_usuario = cadastro.get(cpf)
        #verifica se o usuário existe
        if dados_usuario is None:
            print('Usuário não encontrado.')
        else:
            nome = dados_usuario.get('Nome')
            email = dados_usuario.get('E-mail')
            telefone = dados_usuario.get('Telefone')
            print(f'Nome: {nome}')
            print(f'E-mail: {email}')
            print(f'Telefone: {telefone}')
    
    elif opcao == '3':
        print('Vamos alterar dados do usuário.')
        cpf = input('Entre com o CPF do usuário: ')
        #removendo pontos ou traços do CPF
        cpf = cpf.split(".")
        cpf = ''.join(cpf)
        cpf = cpf.split('-')
        cpf = ''.join(cpf)
        dados_usuario = cadastro.get(cpf)
        #verifica se o usuário existe
        if dados_usuario is None:
            print('Usuário não encontrado.')
        else:
            nome = dados_usuario.get('Nome')
            email = dados_usuario.get('E-mail')
            telefone = dados_usuario.get('Telefone')
            opcao_alteracao = ''
            while opcao_alteracao != '4':
                print(f'Nome: {nome}')
                print(f'E-mail: {email}')
                print(f'Telefone: {telefone}')
                print('Qual dado deseja alterar?')
                print('1 - Nome   2 - E-mail   3 - Telefone   4 - Sair')
                opcao_alteracao = input('Entre com sua opção: ')
                if opcao_alteracao == '1':
                    nome = input('Entre com o nome: ')
                    cadastro.update({cpf: {'Nome': nome, 'E-mail': email, 'Telefone': telefone}})
                elif opcao_alteracao == '2':
                    email = input('Entre com o e-mail: ')
                    cadastro.update({cpf: {'Nome': nome, 'E-mail': email, 'Telefone': telefone}})
                elif opcao_alteracao == '3':
                    telefone = input('Entre com o telefone: ')
                    cadastro.update({cpf: {'Nome': nome, 'E-mail': email, 'Telefone': telefone}})
                elif opcao_alteracao == '4':
                    break
                else:
                    print('Opção inválida.')

    elif opcao == '4':
        print('Vamos deletar um usuário.')
        cpf = input('Entre com o CPF do usuário: ')
        #removendo pontos ou traços do CPF
        cpf = cpf.split(".")
        cpf = ''.join(cpf)
        cpf = cpf.split('-')
        cpf = ''.join(cpf)
        dados_usuario = cadastro.get(cpf)
        #verifica se o usuário existe
        if dados_usuario is None:
            print('Usuário não encontrado.')
        else:
            print(f'Nome: {dados_usuario.get('Nome')}')
            print(f'E-mail: {dados_usuario.get('E-mail')}')
            print(f'Telefone: {dados_usuario.get('Telefone')}')
            opcao_delete = input('Deseja deletar os dados? S/N   ')
            if opcao_delete == 'S':
                del cadastro[cpf]
            elif opcao_delete == 'N':
                pass
            else:
                print('Opção inválida.')

    elif opcao == '5':
        print('Obrigado por usar os nossos serviços.')
    else:
        print('Opção inválida. Tente novamente.')