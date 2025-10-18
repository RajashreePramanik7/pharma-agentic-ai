# agents/master_agent.py
from datetime import datetime
from .iqvia_agent import IQVIAAgent
from .exim_agent import EXIMAgent
from .patent_agent import PatentAgent
from .trials_agent import TrialsAgent
from .web_intelligence_agent import WebAgent
from .report_agent import ReportAgent

class MasterAgent:
    def __init__(self):
        self.iqvia = IQVIAAgent()
        self.exim = EXIMAgent()
        self.patent = PatentAgent()
        self.trials = TrialsAgent()
        self.web = WebAgent()
        self.report = ReportAgent()

    def analyze_molecule(self, molecule, sources=["market","patent","trials","web","trade"]):
        
        results = {}

        if "market" in sources:
            results["market"] = self.iqvia.get_market_data(molecule)
        if "trade" in sources:
            results["trade"] = self.exim.get_trade_data(molecule)
        if "patent" in sources:
            results["patent"] = self.patent.get_patent_info(molecule)
        if "trials" in sources:
            results["trials"] = self.trials.get_trial_info(molecule)
        if "web" in sources:
            results["web"] = self.web.get_web_insights(molecule)

        # Generate PDF report
        report_file = f"static/reports/{molecule}_report_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
        results["report_file"] = report_file.replace("\\", "/")  # ensure forward slashes

        return results
