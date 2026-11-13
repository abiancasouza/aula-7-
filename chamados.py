chamados = [
  { "id": 1, "titulo": "Erro no login", "prioridade": "Alta", "status": "Aberto", "usuario": "Ana Silva" },
  { "id": 2, "titulo": "Tela branca no app", "prioridade": "Crítica", "status": "Aberto", "usuario": "Bruno Costa" },
  { "id": 3, "titulo": "Atualizar cadastro", "prioridade": "Baixa", "status": "Em progresso", "usuario": "Carlos Souza" },
  { "id": 4, "titulo": "Boleto não gerado", "prioridade": "Média", "status": "Aberto", "usuario": "Daniela Lima" },
  { "id": 5, "titulo": "Botão quebrado", "prioridade": "Baixa", "status": "Aberto", "usuario": "Eduardo Rocha" },
  { "id": 6, "titulo": "Lentidão na busca", "prioridade": "Média", "status": "Em progresso", "usuario": "Fernanda Alves" },
  { "id": 7, "titulo": "Recuperar senha", "prioridade": "Alta", "status": "Aberto", "usuario": "Gabriel Santos" },
  { "id": 8, "titulo": "Erro no Pix", "prioridade": "Crítica", "status": "Aberto", "usuario": "Amanda Melo" },
  { "id": 9, "titulo": "Mudar foto de perfil", "prioridade": "Baixa", "status": "Fechado", "usuario": "Igor Ribeiro" },
  { "id": 10, "titulo": "Exportar PDF falhou", "prioridade": "Média", "status": "Aberto", "usuario": "Juliana Vieira" },
  { "id": 11, "titulo": "Carrinho esvaziando", "prioridade": "Alta", "status": "Em progresso", "usuario": "Lucas Martins" },
  { "id": 12, "titulo": "Cupom inválido", "prioridade": "Média", "status": "Aberto", "usuario": "Mariana Dias" },
  { "id": 13, "titulo": "Página 404 no FAQ", "prioridade": "Baixa", "status": "Aberto", "usuario": "Nicolas Ferreira" },
  { "id": 14, "titulo": "Atraso na entrega", "prioridade": "Alta", "status": "Aberto", "usuario": "Patricia Gomes" },
  { "id": 15, "titulo": "Email de boas-vindas", "prioridade": "Baixa", "status": "Fechado", "usuario": "Rodrigo Ramos" },
  { "id": 16, "titulo": "Estorno pendente", "prioridade": "Alta", "status": "Em progresso", "usuario": "Sabrina Oliveira" },
  { "id": 17, "titulo": "Alerta de segurança", "prioridade": "Crítica", "status": "Aberto", "usuario": "Thiago Barbosa" },
  { "id": 18, "titulo": "Link quebrado no menu", "prioridade": "Baixa", "status": "Aberto", "usuario": "Vanessa Cunha" },
  { "id": 19, "titulo": "Nota fiscal sumiu", "prioridade": "Média", "status": "Aberto", "usuario": "Willian Cardoso" },
  { "id": 20, "titulo": "Modo escuro travando", "prioridade": "Baixa", "status": "Em progresso", "usuario": "Yasmim Lopes" },
  { "id": 21, "titulo": "Erro na API de CEP", "prioridade": "Alta", "status": "Aberto", "usuario": "Arthur Antunes" },
  { "id": 22, "titulo": "Notificação duplicada", "prioridade": "Baixa", "status": "Aberto", "usuario": "Beatriz Mendes" },
  { "id": 23, "titulo": "Sessão expirando rápido", "prioridade": "Média", "status": "Em progresso", "usuario": "Caio Nogueira" },
  { "id": 24, "titulo": "Erro no cartão de crédito", "prioridade": "Crítica", "status": "Aberto", "usuario": "Diana Prince" },
  { "id": 25, "titulo": "Traduzir termo em inglês", "prioridade": "Baixa", "status": "Fechado", "usuario": "Elton John" },
  { "id": 26, "titulo": "Chat de suporte offline", "prioridade": "Alta", "status": "Aberto", "usuario": "Fábio Assunção" },
  { "id": 27, "titulo": "Upload de comprovante", "prioridade": "Média", "status": "Aberto", "usuario": "Gisele Bündchen" },
  { "id": 28, "titulo": "Histórico sumiu", "prioridade": "Alta", "status": "Em progresso", "usuario": "Heitor Villa" },
  { "id": 29, "titulo": "Termos de uso desatualizados", "prioridade": "Baixa", "status": "Aberto", "usuario": "Isabela Garcia" },
  { "id": 30, "titulo": "Erro 500 no checkout", "prioridade": "Crítica", "status": "Aberto", "usuario": "Jorge Ben" },
  { "id": 31, "titulo": "Ajustar margem do header", "prioridade": "Baixa", "status": "Em progresso", "usuario": "Karina Bacchi" },
  { "id": 32, "titulo": "Filtro por data quebrado", "prioridade": "Média", "status": "Aberto", "usuario": "Leonardo Dicaprio" },
  { "id": 33, "titulo": "Assinatura não renovada", "prioridade": "Alta", "status": "Aberto", "usuario": "Marta Vieira" },
  { "id": 34, "titulo": "Áudio do vídeo não funciona", "prioridade": "Média", "status": "Aberto", "usuario": "Neymar Junior" },
  { "id": 35, "titulo": "Atualizar política de privacidade", "prioridade": "Baixa", "status": "Fechado", "usuario": "Otávio Mesquita" },
  { "id": 36, "titulo": "Queda do servidor interno", "prioridade": "Crítica", "status": "Em progresso", "usuario": "Paula Toller" },
  { "id": 37, "titulo": "Convite por email falhou", "prioridade": "Baixa", "status": "Aberto", "usuario": "Quintino Aires" },
  { "id": 38, "titulo": "Extrato em branco", "prioridade": "Alta", "status": "Aberto", "usuario": "Renata Vasconcellos" },
  { "id": 39, "titulo": "ícone errado no painel", "prioridade": "Baixa", "status": "Aberto", "usuario": "Samuel Rosa" },
  { "id": 40, "titulo": "Duplicidade de cobrança", "prioridade": "Crítica", "status": "Aberto", "usuario": "Tais Araújo" },
  { "id": 41, "titulo": "Validação de CNPJ", "prioridade": "Média", "status": "Em progresso", "usuario": "Umberto Eco" },
  { "id": 42, "titulo": "Mensagem de erro confusa", "prioridade": "Baixa", "status": "Aberto", "usuario": "Valéria Valenssa" },
  { "id": 43, "titulo": "Problema com fonte negrito", "prioridade": "Baixa", "status": "Aberto", "usuario": "Wagner Moura" },
  { "id": 44, "titulo": "Links de redes sociais fora do ar", "prioridade": "Média", "status": "Aberto", "usuario": "Xuxa Meneghel" },
  { "id": 45, "titulo": "Sem sinal de geolocalização", "prioridade": "Alta", "status": "Em progresso", "usuario": "Yuri Gagarin" },
  { "id": 46, "titulo": "Página recarregando sozinha", "prioridade": "Alta", "status": "Aberto", "usuario": "Zeca Pagodinho" },
  { "id": 47, "titulo": "Gráfico de vendas travado", "prioridade": "Média", "status": "Aberto", "usuario": "Alinne Moraes" },
  { "id": 48, "titulo": "Impossível remover endereço", "prioridade": "Média", "status": "Em progresso", "usuario": "Beto Jamaica" },
  { "id": 49, "titulo": "Vazamento de memória na aba", "prioridade": "Crítica", "status": "Aberto", "usuario": "Cláudia Raia" },
  { "id": 50, "titulo": "Ajustar alinhamento do rodapé", "prioridade": "Baixa", "status": "Fechado", "usuario": "Dado Dolabella" }
]


PRIORIDADES = ("Crítica", "Alta", "Média", "Baixa")
STATUS = ("Aberto", "Em progresso", "Resolvido", "Fechado")


def exibir_chamado(chamado):
    print(
        f'ID: {chamado["id"]} | {chamado["titulo"]} | '
        f'Prioridade: {chamado["prioridade"]} | '
        f'Status: {chamado["status"]} | '
        f'Usuário: {chamado["usuario"]}'
    )


def pesquisar_usuarios():
    nome = input("Digite o nome (ou parte do nome) do usuário: ").strip().casefold()
    resultados = [
        chamado for chamado in chamados
        if nome in chamado["usuario"].casefold()
    ]

    if not resultados:
        print("Nenhum chamado encontrado para esse usuário.")
        return

    for chamado in resultados:
        exibir_chamado(chamado)


def pesquisar_chamados_prioridade():
    print("Prioridades:", ", ".join(PRIORIDADES))
    prioridade = input("Digite a prioridade: ").strip().casefold()
    resultados = [
        chamado for chamado in chamados
        if chamado["prioridade"].casefold() == prioridade
    ]

    if not resultados:
        print("Nenhum chamado encontrado com essa prioridade.")
        return

    for chamado in resultados:
        exibir_chamado(chamado)


def pesquisar_chamados_status():
    print("Status:", ", ".join(STATUS))
    status = input("Digite o status: ").strip().casefold()
    resultados = [
        chamado for chamado in chamados
        if chamado["status"].casefold() == status
    ]

    if not resultados:
        print("Nenhum chamado encontrado com esse status.")
        return

    for chamado in resultados:
        exibir_chamado(chamado)


def chamada_urgente():
    resultados = [
        chamado for chamado in chamados
        if chamado["prioridade"] in ("Crítica", "Alta")
        and chamado["status"] in ("Aberto", "Em progresso")
    ]

    if not resultados:
        print("Não há chamados urgentes pendentes.")
        return

    print("Chamados urgentes:")
    for chamado in resultados:
        exibir_chamado(chamado)


def abrir_chamado():
    titulo = input("Título do chamado: ").strip()
    if not titulo:
        print("O título não pode ficar vazio.")
        return

    usuario = input("Nome do usuário: ").strip()
    if not usuario:
        print("O nome do usuário não pode ficar vazio.")
        return

    print("Prioridades:", ", ".join(PRIORIDADES))
    prioridade = input("Prioridade: ").strip().casefold()
    prioridade_escolhida = next(
        (item for item in PRIORIDADES if item.casefold() == prioridade),
        None,
    )
    if prioridade_escolhida is None:
        print("Prioridade inválida.")
        return

    novo_id = max((chamado["id"] for chamado in chamados), default=0) + 1
    novo_chamado = {
        "id": novo_id,
        "titulo": titulo,
        "prioridade": prioridade_escolhida,
        "status": "Aberto",
        "usuario": usuario,
    }
    chamados.append(novo_chamado)
    print("Chamado aberto com sucesso:")
    exibir_chamado(novo_chamado)


def atualizar_status(status_novo):
    try:
        chamado_id = int(input("Digite o ID do chamado: "))
    except ValueError:
        print("ID inválido. Digite um número.")
        return

    chamado = next(
        (item for item in chamados if item["id"] == chamado_id),
        None,
    )
    if chamado is None:
        print("Chamado não encontrado.")
        return
    if chamado["status"] == "Fechado":
        print("Esse chamado já está fechado.")
        return

    chamado["status"] = status_novo
    print(f'Chamado {chamado_id} atualizado para "{status_novo}".')


def resolver_chamado():
    atualizar_status("Resolvido")


def fechar_chamado():
    atualizar_status("Fechado")


def main():
    while True:
        print("1 - Pesquisar usuários")
        print("2 - Pesquisar por prioridade")
        print("3 - Pesquisar por status")
        print("4 - Chamado urgente")
        print("5 - Abrir chamado")
        print("6 - Resolver chamado")
        print("7 - Fechar chamado")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            pesquisar_usuarios()
        elif opcao == "2":
            pesquisar_chamados_prioridade()
        elif opcao == "3":
            pesquisar_chamados_status()
        elif opcao == "4":
            chamada_urgente()
        elif opcao == "5":
            abrir_chamado()
        elif opcao == "6":
            resolver_chamado()
        elif opcao == "7":
            fechar_chamado()
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()







