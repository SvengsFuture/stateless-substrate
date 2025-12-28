# Speculation / Authority Split

**Invariant:** Speculation may be free; authority must be explicit.

## Model
Exploration → Proposal (data) → Commit Gate (proof + capabilities) → Execution (side effects)

## What this prevents
- Speculative statements becoming durable “facts” by accident
- Mode confusion (exploration behavior leaking into execution)
- Cascades caused by retries/elaboration under uncertainty

## What this does not solve
- Planning quality or “general intelligence”
- Human intent ambiguity
- Distributed consensus / global invariants
- Learning, memory, or model training

## Reference
See `example.py` (or your Python gate file) for the minimal enforcement pattern.
