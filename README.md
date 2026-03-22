# Controle de Finanças - Django

Sistema web de controle financeiro pessoal desenvolvido com **Python + Django**.

O projeto permite cadastrar entradas e saídas, visualizar saldo atualizado, acompanhar o extrato completo e exportar os dados para uma planilha Excel.

---

## Preview

> Interface moderna, responsiva e com visual dark mode.

- Cadastro de entradas e saídas
- Cálculo automático de saldo
- Visualização de extrato
- Exclusão de transações
- Exportação para Excel (.xlsx)
- Layout responsivo (funciona no celular)

---

## Tecnologias Utilizadas

- Python 3.14
- Django 6
- HTML5
- CSS3 (layout moderno com gradientes e responsivo)
- Pandas
- OpenPyXL
- SQLite (banco padrão do Django)

---

## Estrutura do Projeto

controle_financas/
│
├── manage.py
├── requirements.txt
│
├── controle_financas/ # Configurações do projeto
│ ├── settings.py
│ ├── urls.py
│
└── financas/ # App principal
├── models.py # Modelos (Transacao)
├── views.py # Lógica do sistema
├── urls.py # Rotas do app
│
├── templates/
│ └── financas/
│ ├── base.html
│ └── home.html
│
└── static/
└── financas/
└── style.css

text


---

## Funcionalidades

### Cadastro de Transações
- Tipo: Entrada ou Saída
- Valor
- Descrição
- Data automática

### Cálculo Automático
- Saldo total
- Total de entradas
- Total de saídas

### Extrato
- Lista completa de transações
- Exibição com cores diferentes para entrada e saída
- Ordenação por data
- Exclusão individual

### Exportação para Excel
- Geração de arquivo `.xlsx`
- Download direto pelo navegador
- Estrutura organizada para análise financeira

---
 Objetivo do Projeto

Este projeto foi desenvolvido com foco em:

    Aprendizado sólido de Django
    Entendimento da arquitetura MVC (MTV no Django)
    Separação correta de responsabilidades (Models, Views, Templates)
    Uso de arquivos estáticos (CSS)
    Geração de arquivos via HTTP
    Boas práticas de versionamento com Git
---
Melhorias Futuras

    Sistema de autenticação (usuários)
    Filtro por mês/ano
    Gráficos com Chart.js
    Persistência com PostgreSQL
    Deploy em produção (Render / Railway / VPS)
