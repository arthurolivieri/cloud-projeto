# **Implantação da aplicação na AWS com Kubernetes**

Esta API foi implantada na AWS utilizando Kubernetes para orquestração de containers, garantindo escalabilidade, alta disponibilidade e gerenciamento eficiente dos recursos. Segue explicação sobre seu funcionamento e configuração:

---

## **1. Infraestrutura com Kubernetes**
- **Cluster Kubernetes (EKS):**
  Implantou-se a API em um cluster Kubernetes gerenciado pela Amazon Elastic Kubernetes Service – EKS. Ele gerencia os pods (unidades mínimas) que contêm a aplicação de consulta felia no FastAPI e o banco de dados Postgres.

- **Dois pods:**
  - Um pod executa o contêiner com a aplicação, gerenciando as requisições.
  - Outro pod executa o banco de dados Postgres garantindo a persistência dos dados.

- **Configuração por YAML:**
  Nos arquivos YAML (`app-deployment.yaml` e `postgres-deployment.yaml`) definiu-se os recursos do Kubernetes, incluindo especificações de contêniners, variáveis de ambientes e abertura de portas, para a comunicação dos serviços.

---

## **2. Load Balancing**
- **Load Balancer:**
  O load balancer faz a distribuição das requisições entre os pods, de modo a garantir balanceamento de carga e constante disponibilidade.

- **Endereço de Acesso:**
  O Load Balancer cria o endereço público que permite o acesso à API. Toda requisição feita no endereço vai para o cluster Kubernetes, que encaminha para o pod correto.

---

## **3. Vantagens da Arquitetura**
- **Escalabilidade:** O Kubernetes escala automaticamente os pods, correspondendo às necessidades de demanda.
- **Alta Disponibilidade:** O uso do Load Balancer é uma garantia de que a API permaneça disponível, mesmo com possíveis falhas em pods específicos.
- **Gerenciamento Eficiente:** O Kubernetes torna mais fácil e direto o gerenciamento de aplicações e recursos, possibilitando monitoramento e atualizações.

---