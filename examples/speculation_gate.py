"""
Example: Speculation / Authority Split

This example demonstrates how speculative reasoning can generate proposals
without execution authority, and how a separate gate enforces admissibility
before any side effects occur.
"""

def speculate(input_prompt):
    """
    Exploration mode.
    Free to generate ideas, revisions, and possibilities.
    Produces proposals only. No side effects.
    """
    return {
        "proposal": f"Suggested action based on: {input_prompt}",
        "confidence": 0.42,
    }


def authorize(proposal, capability):
    """
    Authority gate.
    Execution is refused unless explicit capability is present.
    """
    if capability != "EXECUTE":
        return {"status": "REFUSED", "reason": "NO_CAPABILITY"}

    return execute(proposal)


def execute(proposal):
    """
    Execution mode.
    Side effects are allowed only after passing the gate.
    """
    return {
        "status": "EXECUTED",
        "result": proposal["proposal"],
    }
