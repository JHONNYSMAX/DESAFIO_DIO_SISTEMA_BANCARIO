# 💰 Sistema Bancário em Python

Desafio de Projeto da **DIO - Digital Innovation One**  
Projeto: **Criando um Sistema Bancário com Python**

---

## 📘 Descrição

Este é um sistema bancário simples implementado em Python.  
Ele permite que o usuário realize operações bancárias básicas através do terminal.

O projeto tem como objetivo consolidar conhecimentos fundamentais de programação, como:

- Controle de fluxo (condições e loops)
- Entrada e saída de dados
- Manipulação de variáveis
- Simulação de transações

---

## 🚀 Funcionalidades

O programa oferece as seguintes opções:

- **[d] Depósito:** Adiciona valor ao saldo, se for válido.
- **[s] Saque:** Retira valor do saldo, respeitando limites de valor e quantidade de saques diários.
- **[e] Extrato:** Exibe o histórico de movimentações e saldo atual.
- **[t] Transferência:** Simula a transferência para outra conta, subtraindo do saldo.
- **[q] Sair:** Encerra o programa com uma mensagem de despedida.

---

## 📌 Regras de Operação

- 💸 O **limite de saque** por operação é de **R$ 500,00**.
- ⛔ O **número máximo de saques diários** é de **3 vezes**.
- 🚫 Não é permitido inserir valores negativos ou nulos nas transações.

---

## 💻 Exemplo de Execução

```text
[d] Depositar
[s] Sacar
[e] Extrato
[t] Transferir
[q] Sair

=> d
Informe o valor do depósito: 1000
Depósito de R$ 1000.00 realizado com sucesso!


🧠 Como Funciona
A lógica é baseada em estruturas condicionais simples.
Aqui estão os principais trechos de código:

🔹 Depósito
if opcao == "d":
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

🔹 Saque

       if opcao == "s":
    valor = float(input("Informe o valor do saque: "))
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")




▶️ Como Executar o Código

1. Tenha o Python instalado na sua máquina.

2. Salve o código no arquivo sistema_bancario.py.

3. Execute pelo terminal com o comando:

bash

python sistema_bancario.py


📚 Conclusão
Esse projeto é uma excelente introdução prática à programação com Python.
Ajuda a reforçar a lógica de programação e a estruturação de pequenos sistemas.

🧑‍💻 Autor
Desenvolvido por Jhonnys Max Sampaio da Silva como parte dos desafios de projeto da DIO.

📝 Licença
Este projeto está sob a licença MIT - sinta-se livre para usar e modificar.





