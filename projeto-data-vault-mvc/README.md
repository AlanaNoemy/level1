# Operação Data Vault — Level 1 (MVC)

Refatoração do Level 0 para MVC com Python e SQLite. Mantém os campos `id`, `nome`, `crime` e `periculosidade` e usa o mesmo nome de banco `vault_original.db`.

## Arquivos
- `model.py`: banco de dados, validação, cadastro, listagem, remoção e filtro.
- `view.py`: interface de terminal.
- `controller.py`: coordenação do fluxo e tratamento de entradas inválidas.
- `main.py`: ponto de entrada.

## Execução
Na pasta do projeto, execute `python main.py`.

## Teste sugerido
Cadastre três registros com níveis 3, 7 e 9. Tente cadastrar `alto` e `15` (ambos devem gerar mensagem de erro, sem encerrar a aplicação). Escolha a opção 4 e digite `7` (deve listar apenas os registros de níveis 7 e 9). Remova um registro por ID e liste novamente.

## Git
```bash
git checkout -b feature/mvc
git add model.py view.py controller.py main.py
git commit -m "feat: refatoracao completa para o padrao MVC"
git checkout main
git merge feature/mvc
```

**Atenção:** faça o merge no repositório existente do Level 0, não em um novo repositório. O banco de dados não é incluído no ZIP. Para reutilizar os registros antigos, mantenha `vault_original.db` na pasta de execução do projeto. O arquivo `.gitignore` evita versionar dados potencialmente sensíveis.

## Observações
A interface continua usando índices posicionais, como no exemplo do professor. O filtro usa `>=` e valida o intervalo de 1 a 10. Esta implementação não inclui a operação Update, portanto oferece Create, Read e Delete, além de filtro, mas ainda não CRUD completo.
