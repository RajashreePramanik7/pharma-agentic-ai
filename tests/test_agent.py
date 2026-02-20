from agents.master_agent import run_master_agent

def test_run_master_agent():
    result = run_master_agent("Paracetamol")
    assert result["molecule"] == "Paracetamol"
    assert "insights" in result
