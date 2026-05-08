# Healthcare Claims ETL: AI-Powered CI/CD Pipeline

![CI Status](https://img.shields.io/badge/CI-AI--Generated-blue)
![Domain](https://img.shields.io/badge/Domain-Healthcare-green)
![Python](https://img.shields.io/badge/Python-3.9+-yellow)

## 📖 Overview
This project demonstrates a production-grade **Continuous Integration (CI)** pipeline for a Healthcare Claims ETL system. In the healthcare domain, data integrity and code reliability are paramount. This repository uses **Generative AI (Llama 3.1 8b)** to architect its own deployment workflows, ensuring that every Pull Request (PR) is rigorously linted, tested, and validated before merging.

### 🏥 Business Use Case
A hospital network needs to transfer daily claims data from their local SQL databases to a centralized **Azure SQL** warehouse for insurance processing. The pipeline must handle sensitive records, requiring high code quality standards to prevent data leaks or processing errors.

## 🏗️ Architecture
```mermaid
graph LR
    A[Hospital DB] --> B[Python ETL Module]
    B --> C[Azure SQL]
    
    subgraph CI/CD Pipeline (GitHub Actions)
    D[PR Trigger] --> E[flake8 Linting]
    E --> F[pytest Execution]
    F --> G[Coverage Report]
    end
    
    B -.-> D
```

## 🛠️ Tech Stack
- **Engine**: Python 3.x
- **Infrastructure as Code**: GitHub Actions (AI-Generated)
- **Quality Assurance**: `flake8`, `pytest`, `pytest-cov`
- **AI Orchestration**: Groq Llama 3.1 8b
- **Database Targets**: SQL Server / Azure SQL

## 🚀 Key Features
- **Automated Quality Gates**: PRs are blocked unless they pass linting and unit tests.
- **AI-Generated Infrastructure**: Deployment YAML is generated programmatically to minimize manual configuration errors.
- **Healthcare Optimized**: Designed with modularity to handle complex schema requirements.

## 📂 Project Structure
- `src/`: Core ETL logic.
- `tests/`: Unit and integration tests.
- `.github/workflows/`: AI-generated CI/CD pipelines.
- `archive.md`: Detailed engineering log and decision record.

---
*Created by Antigravity (Senior Data Engineer)*
