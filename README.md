# Sistema Bancário - Versão 2

Esse programa simula um sistema bancário básico com funcionalidades como criação de usuários, criação de contas correntes, saque, depósito e visualização de extrato.

## Funcionalidades

### 1. Criar Usuário

Permite criar um novo usuário do banco. É necessário informar o nome e o CPF do usuário. O programa verifica se o CPF já está cadastrado antes de criar um novo usuário.

### 2. Criar Conta Corrente

Cria uma nova conta corrente vinculada a um usuário existente. É necessário informar o CPF do usuário. O número da conta é sequencial, iniciando em 1, e a agência é fixa ("0001").

### 3. Sacar

Permite realizar um saque em uma conta corrente. O usuário deve informar o valor do saque. A função verifica se o valor é válido, se está dentro do limite diário e se há saldo suficiente.

### 4. Depositar

Permite realizar um depósito em uma conta corrente. O usuário deve informar o valor do depósito. A função verifica se o valor é positivo.

### 5. Extrato

Exibe o extrato da conta corrente, incluindo todas as transações de depósito e saque, bem como o saldo atual.

### q. Sair

Encerra o programa.

## Funções Modulares

### `criar_usuario(usuarios)`

Cria um novo usuário com nome e CPF. Armazena o usuário em uma lista e verifica se o CPF já está cadastrado.

### `criar_conta(contas, usuarios)`

Cria uma nova conta corrente vinculada a um usuário existente, usando a lista de usuários. O número da conta é sequencial e a agência é fixa.

### `saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques)`

Realiza um saque na conta corrente. Verifica se o valor é válido, se está dentro do limite e se há saldo suficiente.

### `deposito(saldo, valor, extrato)`

Realiza um depósito na conta corrente. Verifica se o valor é positivo.

### `extrato(saldo, extrato)`

Exibe o extrato da conta corrente, incluindo transações e saldo.

### `main()`

Função principal que interage com o usuário através do menu. Chama as funções correspondentes de acordo com a seleção.

## Como Executar

1. Certifique-se de ter o Python instalado.
2. Execute o programa em um ambiente que suporta entrada de terminal.
3. Siga as instruções na tela para realizar as operações desejadas.

## Contribuição

Contribuições são bem-vindas! Se você encontrar problemas ou tiver sugestões para melhorias, sinta-se à vontade para abrir uma issue neste repositório. Caso queira contribuir com código, por favor, abra um pull request para revisão.

## Agradecimentos

Agradeço ao Professor Guilherme Arthur de Carvalho da DIO pelas aulas e ensinamentos.

**Desenvolvido com ❤️ e Python.**