# 📊 Data Pipeline com Airflow (ETL de Dados Financeiros)

Pipeline de engenharia de dados completo utilizando **Apache Airflow**, responsável por extrair, transformar e carregar dados financeiros de ações para um banco PostgreSQL (Supabase).

---

## 🚀 Visão Geral

Este projeto implementa um pipeline ETL automatizado que:

1. **Extrai** dados financeiros da API Alpha Vantage
2. **Transforma** os dados aplicando tipagem e métricas
3. **Carrega** os dados em um banco PostgreSQL (Supabase)
4. **Orquestra** todo o fluxo com Apache Airflow

---

## 🏗️ Arquitetura do Projeto

```
            +----------------------+
            |  Alpha Vantage API   |
            +----------+-----------+
                       |
                       v
                [ Extract ]
                       |
                       v
                [ Transform ]
                       |
                       v
                  [ Load ]
                       |
                       v
            +----------------------+
            |   PostgreSQL DB      |
            |     (Supabase)       |
            +----------------------+
                       ^
                       |
               Apache Airflow
               (Orquestração)
```

---

## ⚙️ Tecnologias Utilizadas

* 🐍 Python
* 🌪️ Apache Airflow
* 🐳 Docker & Docker Compose
* 🐘 PostgreSQL (Supabase)
* 📊 Pandas
* 🔗 SQLAlchemy
* 🌐 Requests
* 🔐 Python-dotenv

---

## 📁 Estrutura do Projeto

```
data-pipeline-airflow/
│
├── dags/
│   └── financial_pipeline.py
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── database/
│   ├── actions.json
│   └── actions.csv
│
├── config/
│   └── .env
│
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## 🔄 Pipeline ETL

### 🔹 Extract

* Consome dados da API Alpha Vantage
* Converte os dados para formato estruturado (JSON)
* Salva em arquivo local

### 🔹 Transform

* Converte tipos de dados (float, int, datetime)
* Ordena por data
* Calcula métrica:

```python
price_change_percent = ((close - open) / open) * 100
```

* Exporta para CSV

### 🔹 Load

* Insere dados no PostgreSQL
* Evita duplicidade com:

```sql
ON CONFLICT (symbol, date) DO NOTHING
```

---

## 🗄️ Modelagem do Banco

### Tabela: `stocks`

| Campo  | Tipo       |
| ------ | ---------- |
| symbol | VARCHAR PK |
| name   | VARCHAR    |

---

### Tabela: `stock_prices`

| Campo                | Tipo         |
| -------------------- | ------------ |
| id                   | BIGSERIAL PK |
| symbol               | VARCHAR FK   |
| date                 | DATE         |
| open                 | NUMERIC      |
| high                 | NUMERIC      |
| low                  | NUMERIC      |
| close                | NUMERIC      |
| volume               | BIGINT       |
| price_change_percent | NUMERIC      |
| created_at           | TIMESTAMP    |

---

## 🐳 Como Executar o Projeto

### 🔧 Pré-requisitos

* Docker
* Docker Compose

---

### ▶️ Passos

```bash
# Clonar repositório
git clone https://github.com/senseyluiz/data-pipeline-airflow.git

# Acessar pasta
cd data-pipeline-airflow

# Subir ambiente
docker-compose up --build
```

---

## 🌐 Acessar Airflow

```
http://localhost:8080
```

### Login:

* **Usuário:** admin
* **Senha:** admin

---

## ▶️ Executar Pipeline

1. Ativar DAG `financial_data_pipeline`
2. Clicar em **Trigger DAG**
3. Acompanhar execução via interface

---

## 📊 Exemplo de Dados

```json
{
  "symbol": "IBM",
  "date": "2026-05-01",
  "open": 234.55,
  "close": 232.20,
  "price_change_percent": -1.00
}
```

---

## 🔒 Variáveis de Ambiente

Arquivo `.env`:

```
DB_HOST=...
DB_PORT=...
DB_DATABASE=...
DB_USER=...
DB_PASSWORD=...
APIKEY=...
```

---

## 🧠 Aprendizados

* Construção de pipeline ETL completo
* Orquestração com Airflow
* Containerização com Docker
* Integração com API externa
* Modelagem de dados relacional
* Controle de duplicidade no banco
* Debug em ambiente distribuído

---



## 👨‍💻 Autor

**Luis Henrique** -
Engenheiro de Dados | Backend | Arquitetura

---

## ⭐ Considerações Finais

Este projeto representa um pipeline de dados real, simulando cenários encontrados no mercado, com foco em escalabilidade, organização e boas práticas de engenharia de dados.
