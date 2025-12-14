---

# GeniRoute-v0

**Sistema Inteligente de Previsão Operacional para Entregas (GenAI + ML)**

## Descrição do Projeto

O **GeniRoute** é um projeto acadêmico-experimental que simula como **Inteligência Artificial e GenAI** podem ser utilizadas para apoiar decisões operacionais em plataformas de delivery, como o iFood.

O sistema prevê **atrasos médios em entregas** com base em dados operacionais e variáveis externas (clima, trânsito, eventos), e gera **explicações e recomendações automáticas** para restaurantes e operadores logísticos.

O projeto foi desenvolvido com foco em:

* Machine Learning supervisionado
* Explainable AI
* Arquitetura modular em Python
* Interface interativa com Streamlit

---

## Objetivo

Demonstrar, de forma prática, como modelos preditivos e GenAI podem:

* Antecipar gargalos operacionais
* Ajudar restaurantes a se prepararem para horários críticos
* Apoiar decisões baseadas em dados
* Melhorar a experiência do cliente final

---

## Arquitetura do Sistema

O sistema é composto por quatro camadas principais:

```
Dados Sintéticos → Modelo de ML → Camada GenAI → Interface (App)
```

### 1. Geração de Dados Sintéticos

Simula cenários reais de operação, incluindo:

* Volume de pedidos
* Horário
* Chuva
* Feriados
* Dias de jogo
* Nível de trânsito

### 2. Modelo de Machine Learning

Um modelo de **Random Forest Regressor** é treinado para prever o atraso médio das entregas em minutos.

### 3. Camada GenAI (Explainable AI)

A partir da previsão do modelo, o sistema:

* Explica os fatores que influenciam o atraso
* Gera recomendações operacionais
* Simula um agente GenAI de apoio à decisão

*(Nesta versão, a explicação é rule-based, mas a arquitetura suporta integração com LLMs reais.)*

### 4. Interface com Streamlit

Dashboard interativo onde o usuário pode:

* Ajustar parâmetros operacionais
* Gerar previsões
* Visualizar explicações e recomendações

---

## Tecnologias Utilizadas

* Python
* Pandas / NumPy
* Scikit-learn
* Streamlit
* Machine Learning supervisionado
* Conceitos de GenAI e Explainable AI

---

## 📁 Estrutura do Projeto

```
geniroute-v0/
│
├── app/
│   └── app.py              # Interface Streamlit
│
├── genai/
│   ├── advisor.py          # Camada GenAI (explicações)
│   └── __init__.py
│
├── model/
│   ├── train_model.py      # Treinamento do modelo
│   ├── predictor.py        # Predição
│   └── __init__.py
│
├── utils/
│   └── data_generator.py   # Geração de dados sintéticos
│
├── synthetic_data.csv
├── requirements.txt
└── README.md
```

---

## Como Executar o Projeto

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Gere os dados sintéticos:

```bash
python utils/data_generator.py
```

3. Treine o modelo:

```bash
python model/train_model.py
```

4. Execute o app:

```bash
streamlit run app/app.py
```

---

## Observações Finais

Este projeto tem caráter **educacional** e foi desenvolvido como forma de aprendizado prático em:

* Inteligência Artificial
* Machine Learning
* Sistemas Inteligentes
* Arquitetura de software em Python

Ele pode ser facilmente expandido para:

* Uso de dados reais
* Integração com APIs externas
* Uso de Large Language Models (LLMs)
* Análises mais avançadas de risco e otimização

---

