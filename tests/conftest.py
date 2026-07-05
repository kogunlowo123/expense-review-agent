"""Test configuration for Expense Review Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "expense-review-agent", "category": "Finance"}
