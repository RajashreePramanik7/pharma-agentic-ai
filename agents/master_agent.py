from agents.iqvia_agent import run as iqvia_run
from agents.exim_agent import run as exim_run
from agents.trials_agent import run as trials_run
from agents.patent_agent import run as patent_run
from agents.web_intelligence_agent import run as web_run
from agents.report_agent import generate_report


class MasterAgent:
    """
    Master Agent = Orchestrator
    """

    def handle_prompt(self, prompt: str) -> dict:
        """
        Entry point from FastAPI
        """
        tasks = self._decompose_prompt(prompt)

        results = {}

        if "market" in tasks:
            results["market"] = iqvia_run(tasks["market"])

        if "exim" in tasks:
            results["exim"] = exim_run(tasks["exim"])

        if "trials" in tasks:
            results["trials"] = trials_run(tasks["trials"])

        if "patents" in tasks:
            results["patents"] = patent_run(tasks["patents"])

        if "web" in tasks:
            results["web"] = web_run(tasks["web"])

        summary = self._synthesize(prompt, results)

        report_url = generate_report(
            prompt=prompt,
            results=results,
            summary=summary
        )

        return {
            "prompt": prompt,
            "summary": summary,
            "results": results,
            "report_url": report_url
        }

    # ---------------------------------
    # Prompt Decomposition
    # ---------------------------------
    def _decompose_prompt(self, prompt: str) -> dict:
        """
        Simple rule-based decomposition.
        Later replace with LLM classification.
        """

        prompt_lower = prompt.lower()

        tasks = {}

        if "market" in prompt_lower or "sales" in prompt_lower:
            tasks["market"] = {"query": prompt}

        if "export" in prompt_lower or "import" in prompt_lower:
            tasks["exim"] = {"query": prompt}

        if "trial" in prompt_lower or "clinical" in prompt_lower:
            tasks["trials"] = {"query": prompt}

        if "patent" in prompt_lower or "ip" in prompt_lower:
            tasks["patents"] = {"query": prompt}

        # always do web search
        tasks["web"] = {"query": prompt}

        return tasks

    # ---------------------------------
    # Synthesis
    # ---------------------------------
    def _synthesize(self, prompt: str, results: dict) -> str:
        """
        Combine agent outputs into a readable answer.
        """

        response = f"### Research Summary for:\n**{prompt}**\n\n"

        if "market" in results:
            response += "## Market Insights\n"
            response += results["market"]["summary"] + "\n\n"

        if "exim" in results:
            response += "## EXIM Trends\n"
            response += results["exim"]["summary"] + "\n\n"

        if "trials" in results:
            response += "## Clinical Trials\n"
            response += results["trials"]["summary"] + "\n\n"

        if "patents" in results:
            response += "## Patent Landscape\n"
            response += results["patents"]["summary"] + "\n\n"

        if "web" in results:
            response += "## Web Intelligence\n"
            response += results["web"]["summary"] + "\n\n"

        response += "### Recommendation\n"
        response += (
            "Based on the above data, this molecule shows potential for "
            "repurposing with moderate competition and identifiable unmet needs."
        )

        return response
