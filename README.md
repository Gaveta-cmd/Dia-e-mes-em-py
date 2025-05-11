# 🎉 Contador de Dias para o Aniversário

Este é um script simples em **Python** que calcula quantos dias faltam ou já se passaram desde o seu aniversário com base em datas fornecidas manualmente pelo usuário.

## 📌 Como Funciona

O usuário informa:
- O **dia** e o **mês** de seu aniversário.
- O **dia** e o **mês** atuais.

O script então calcula:
- Se **hoje é o aniversário** do usuário.
- Quantos **dias faltam** para o próximo aniversário.
- Ou quantos **dias se passaram** desde o último aniversário.

> A lógica considera **30 dias por mês**, como simplificação.

## 📄 Exemplo de Execução

```bash
Qual dia vc nasceu: 15
Qual o mes: 5
Que dia é hj: 10
Que mes é hj: 5
Faltam 5 dias do seu aniversário!
```

## 📦 Estrutura do Projeto

```plaintext
contador_aniversario.py   # Script Python principal
README.md                 # Este arquivo de documentação
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**

## 🔍 Observação

O cálculo é uma estimativa simplificada. Ele **não leva em conta os diferentes tamanhos dos meses** (28, 30, 31 dias) nem anos bissextos.

## 🧠 Possíveis Melhorias

- Usar a biblioteca `datetime` para cálculos reais de datas.
- Permitir verificar automaticamente a data atual.
- Adicionar suporte a anos.

## 📄 Licença

Este projeto é livre para uso e modificação com fins educacionais.
