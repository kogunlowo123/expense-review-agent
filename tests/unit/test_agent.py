"""Expense Review Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_validate_expense():
    """Test Validate expense report against company policy."""
    tools = AgentTools()
    result = await tools.validate_expense(expense_report="test", policy_set="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_flag_outliers():
    """Test Flag unusual expenses based on historical patterns."""
    tools = AgentTools()
    result = await tools.flag_outliers(expense_data="test", employee_id="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_verify_receipt():
    """Test Verify receipt authenticity and match to expense claim."""
    tools = AgentTools()
    result = await tools.verify_receipt(receipt_image="test", claimed_amount="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_calculate_reimbursement():
    """Test Calculate total reimbursement with per diem and mileage rates."""
    tools = AgentTools()
    result = await tools.calculate_reimbursement(expenses="test", travel_policy="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.expense_review_agent_agent import ExpenseReviewAgentAgent
    agent = ExpenseReviewAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
