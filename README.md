# 🎬 Obs-Flix: Backend de Micro-Streaming com Observabilidade Nativa

Este projeto consiste em uma API de backend para um serviço de streaming
(estilo Netflix) desenvolvida em **Python (FastAPI)**. O diferencial
desta implementação não é apenas a funcionalidade, mas a sua arquitetura
voltada para a **Observabilidade (o11y)**, pronta para ser monitorada e
analisada em ambientes de produção.

O sistema demonstra a implementação prática dos pilares da
observabilidade (**Métricas, Logs e Visualização**) utilizando o padrão
de mercado **OpenMetrics**.

------------------------------------------------------------------------

# 🛠️ Stack Tecnológica

O ambiente é orquestrado via **Docker Compose**, garantindo paridade e
facilidade de deploy.

  Tecnologia        Função
  ----------------- -------------------------------------------
  **Python 3.11**   Linguagem Base
  **FastAPI**       Framework Web de Alta Performance
  **Prometheus**    Coleta e Armazenamento de Métricas (TSDB)
  **Grafana**       Visualização Analítica e Dashboards
  **Docker**        Containerização e Infra como Código

------------------------------------------------------------------------

# 🚀 Como Executar o Projeto

## Pré-requisitos

-   Ter o **Docker Desktop** instalado e rodando em sua máquina.

------------------------------------------------------------------------

## Passo a Passo

### 1️⃣ Clone este repositório

``` bash
git clone https://github.com/fabioreis12/obs-flix
cd obs-flix
```

### 2️⃣ Suba o ambiente completo

``` bash
docker-compose up --build
```

O Docker irá:

-   baixar as imagens necessárias
-   criar os containers
-   configurar a rede entre API, Prometheus e Grafana automaticamente.

------------------------------------------------------------------------

# 📉 Endpoints e Dashboards Disponíveis

Após o deploy, as seguintes URLs estarão acessíveis:

  --------------------------------------------------------------------------------------
  Serviço              URL                             Credenciais      Descrição
  -------------------- ------------------------------- ---------------- ----------------
  API Backend          http://localhost:8000           \-               Ponto de entrada
                                                                        da API

  Swagger Docs         http://localhost:8000/docs      \-               Documentação
                                                                        interativa da
                                                                        API

  Métricas Brutas      http://localhost:8000/metrics   \-               Endpoint
                                                                        OpenMetrics

  Prometheus           http://localhost:9090           \-               Console de
                                                                        monitoramento

  Grafana              http://localhost:3000           admin / admin    Dashboard de
                                                                        visualização
  --------------------------------------------------------------------------------------

------------------------------------------------------------------------


# 📈 Verificando a Observabilidade
1. Geração de Dados
Acesse a documentação no link /docs e execute algumas chamadas no endpoint /watch/{movie_id}. Utilize IDs existentes (1, 2, 3) e IDs inexistentes para gerar métricas de sucesso e erro.

2. Consultando Métricas no Prometheus
No painel do Prometheus (localhost:9090), você pode executar queries como:

http_request_duration_seconds_sum: Para analisar a latência média das requisições.

http_requests_total: Para verificar o volume de tráfego por endpoint.

3. Endpoint de Métricas Brutas
O backend expõe um endpoint compatível com o padrão OpenMetrics em:

http://localhost:8000/metrics

# 🖼️ Visualizando os Dados no Grafana

O Grafana permite criar painéis analíticos robustos baseados nas
métricas coletadas pelo Prometheus.

### Como configurar o Grafana localmente

1️⃣ Acesse: http://localhost:3000

Login: admin / admin

2️⃣ Vá em: Connections → Data Sources

3️⃣ Clique em: Add data source

4️⃣ Selecione **Prometheus**

5️⃣ No campo **Connection URL** utilize: http://prometheus:9090

6️⃣ Clique em **Save & Test**

Agora você pode criar dashboards utilizando métricas como:

    http_request_duration_seconds_sum

------------------------------------------------------------------------

### Instrumentação Não-Invasiva

Utiliza a biblioteca:

    prometheus-fastapi-instrumentator

Isso permite coletar métricas padrão como:

-   latência
-   erros
-   tráfego

sem poluir a lógica de negócio do `main.py`.

------------------------------------------------------------------------

### Logs Estruturados

O sistema já nasce com logs configurados para:

-   troubleshooting
-   correlação de eventos
-   análise em produção

------------------------------------------------------------------------

# 🎯 Próximos Passos (Roadmap)

-   [ ] Distributed Tracing com **OpenTelemetry + Jaeger**
-   [ ] Alerting no **Grafana baseado em SLOs**
-   [ ] Dashboard Provisioning automático via JSON

------------------------------------------------------------------------

# 👨‍💻 Autor

**Fabio de Souza Reis**

GitHub https://github.com/fabioreis12
