# 📊 **Calculadora de IMC**

Uma aplicação web simples desenvolvida com **Python** e **Streamlit** para calcular o **Índice de Massa Corporal (IMC)** de um usuário, exibindo a classificação junto com uma mensagem personalizada. Ideal para praticar **entrada e saída de dados**, **operações aritméticas**, **condicionais** e conceitos de **frontend lowcode** com Streamlit.

---
## 🧩 **Situação-Problema**

Você foi contratado por uma **clínica de nutrição** para desenvolver uma ferramenta simples e acessível que ajude pacientes a calcularem seu **IMC (Índice de Massa Corporal)** diretamente pelo navegador.  

A clínica precisa que o sistema:

- Solicite **peso** e **altura** dos usuários;
- Calcule automaticamente o IMC;
- Exiba a **classificação** (como "peso normal", "sobrepeso", etc.);
- Mostre uma **mensagem personalizada** com base no resultado.

O objetivo é tornar o processo de triagem mais rápido e educativo, permitindo que os próprios pacientes compreendam sua situação antes da consulta.

Como desenvolvedor(a), você decidiu utilizar **Python** e a biblioteca **Streamlit** para construir uma interface web leve, funcional e de fácil manutenção.

---

## 🎯 **Objetivo Educacional**
- Trabalhar com **entrada de dados** através de formulários simples.
- Realizar **operações aritméticas** para calcular o IMC.
- Utilizar **condicionais** para classificar o IMC e fornecer um feedback personalizado.
- Criar interfaces **lowcode** com **Streamlit** para construir uma aplicação simples e funcional.

---

## 📝 **Enunciado**

O projeto consiste em uma aplicação web que realiza os seguintes passos:

1. O usuário insere o **peso** (em kg) e a **altura** (em metros).
2. O sistema calcula o **IMC** utilizando a fórmula:
    IMC = peso / (altura ** 2)
3. A aplicação exibe a **classificação do IMC** com base nos seguintes parâmetros:
- **Abaixo do peso**: IMC < 18.5
- **Peso normal**: 18.5 ≤ IMC < 24.9
- **Sobrepeso**: 25.0 ≤ IMC < 29.9
- **Obesidade**: IMC ≥ 30
4. Exibe uma **mensagem personalizada** dependendo da classificação.

### Exemplo de uso:
1. O usuário insere o peso (exemplo: 70 kg) e altura (exemplo: 1.75 m).
2. O cálculo do IMC é feito automaticamente e o resultado é mostrado.

**Saída esperada**:
Seu IMC é 22.86 — Classificação: Peso Normal ✅


---

## 💻 **Como executar**

**Pré-requisito**: Python 3.8 ou superior

### Passos:

1. Clone este repositório ou baixe os arquivos:

```bash
git clone https://github.com/TJfiles/projeto_imc.git
cd projeto_imc
```

2. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

3. Execute o aplicativo Streamlit:
```bash
streamlit run app.py
```

4. Abra o navegador e acesse o endereço fornecido pelo Streamlit (geralmente http://localhost:8501).

Pronto! Agora você pode inserir o peso e altura para calcular o IMC. 🎉

---

## **🧠 Conceitos trabalhados**

- Entrada de dados com st.number_input
- Operações aritméticas para cálculo do IMC
- Condicionais (if/elif/else) para classificação do IMC
- Exibição dinâmica com Streamlit
- Criação de interfaces web simples com frontend lowcode

---
## **📂 Estrutura do projeto**
```
projeto_imc/
├─ app.py                # Arquivo principal do Streamlit
├─ logo.png              # Logo do projeto
├─ requirements.txt      # Dependências do projeto
├─ README.md             # Este arquivo

```
---
## **📝 Licença**

Este projeto está sob a licença MIT — sinta-se à vontade para usar, modificar e distribuir. ✨

## **🔧 Tecnologias utilizadas**
- Python 3.x
- Streamlit