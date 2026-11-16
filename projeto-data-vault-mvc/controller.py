from model import SuspeitoModel
from view import SuspeitoView


class SuspeitoController:
    def __init__(self, model=None, view=None):
        self.model = model if model is not None else SuspeitoModel()
        self.view = view if view is not None else SuspeitoView()

    def iniciar(self):
        while True:
            opcao = self.view.exibir_menu()
            if opcao == '1':
                nome, crime, nivel = self.view.obter_dados_suspeito()
                try:
                    self.model.salvar_suspeito(nome, crime, nivel)
                    self.view.mostrar_mensagem('Registro arquivado com sucesso!')
                except ValueError as erro:
                    self.view.mostrar_mensagem(f'Erro de validação: {erro}')
            elif opcao == '2':
                self.view.mostrar_lista(self.model.listar_todos())
            elif opcao == '3':
                suspeito_id = self.view.obter_id_remocao()
                try:
                    if self.model.deletar_suspeito(suspeito_id):
                        self.view.mostrar_mensagem('Registro removido do cofre.')
                    else:
                        self.view.mostrar_mensagem('ID não encontrado.')
                except ValueError:
                    self.view.mostrar_mensagem('Erro: O ID deve ser um número inteiro.')
            elif opcao == '4':
                minimo = self.view.obter_periculosidade_minima()
                try:
                    dados = self.model.filtrar_por_periculosidade(minimo)
                    self.view.mostrar_lista(dados)
                except ValueError as erro:
                    self.view.mostrar_mensagem(f'Erro de validação: {erro}')
            elif opcao == '0':
                self.view.mostrar_mensagem('Encerrando sistema...')
                break
            else:
                self.view.mostrar_mensagem('Opção inválida!')
