# Expense Review Agent

[![CI](https://github.com/kogunlowo123/expense-review-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/expense-review-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Finance | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Expense review agent that validates expense reports against company policy, flags outliers, checks receipt authenticity, calculates reimbursements, and generates compliance reports.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `validate_expense` | Validate expense report against company policy |
| `flag_outliers` | Flag unusual expenses based on historical patterns |
| `verify_receipt` | Verify receipt authenticity and match to expense claim |
| `calculate_reimbursement` | Calculate total reimbursement with per diem and mileage rates |
| `generate_compliance_report` | Generate expense compliance report by department |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/expense-review/process` | Process transaction |
| `POST` | `/api/v1/expense-review/analyze` | Analyze data |
| `POST` | `/api/v1/expense-review/validate` | Validate |
| `POST` | `/api/v1/expense-review/report` | Generate report |
| `GET` | `/api/v1/expense-review/audit` | Get audit trail |

## Features

- Expense
- Review
- Compliance
- Reporting

## Integrations

- Netsuite
- Quickbooks
- Xero
- Sap
- Oracle Financials

## Architecture

```
expense-review-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── expense_review_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**ERP + Accounting Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.
