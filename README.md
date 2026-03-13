# 🎬 Obs-Flix: Backend de Micro-Streaming com Observabilidade Nativa

Este projeto consiste em uma API de backend para um serviço de streaming (estilo Netflix) desenvolvida em **Python (FastAPI)**. O diferencial desta implementação não é apenas a funcionalidade, mas a sua arquitetura voltada para a **Observabilidade (o11y)**, pronta para ser monitorada em ambientes de produção.

## 🚀 Proposta Técnica

O sistema foi desenhado para demonstrar a implementação prática dos pilares da observabilidade:
- **Métricas:** Instrumentação automática para coleta de latência, taxa de erro e volume de requisições.
- **Logs:** Registro estruturado de eventos críticos e fluxos de erro.
- **Ambiente:** Infraestrutura como código utilizando Docker para garantir paridade entre ambientes.

---

## 🛠️ Stack Tecnológica

- **Linguagem:** Python 3.11
- **Framework:** FastAPI (High performance)
- **Métricas:** Prometheus (OpenMetrics standard)
- **Containerização:** Docker & Docker Compose
- **Easter Egg:** Módulo `antigravity` (Pythonic culture)

---

## 🏗️ Como Executar o Projeto

O projeto utiliza **Docker Compose** para orquestrar o serviço da API e o servidor de monitoramento simultaneamente.

### Pré-requisitos
- Docker Desktop instalado e rodando.

### Passo a Passo
1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/obs-flix.git](https://github.com/SEU_USUARIO/obs-flix.git)
   cd obs-flix