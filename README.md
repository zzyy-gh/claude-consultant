# The Consultant

A multi-perspective thinking partner built on Claude Code. Instead of answering from a single viewpoint, it spawns specialist agents with competing perspectives, synthesizes their insights, and learns alongside you over time.

## How It Works

1. **You ask a question** — anything: strategy, technical decisions, life choices, analysis
2. **Perspectives are chosen** — the orchestrator picks 2-5 specialist viewpoints that create productive tension (e.g., a game theorist, a stoic philosopher, a devil's advocate)
3. **Specialists analyze in parallel** — each pushes their perspective boldly, with epistemic honesty about assumptions and certainty
4. **Emergent exploration** — as responses come in, new agents are spawned if unexpected topics or tensions surface that warrant additional perspectives. The analysis is not limited to the initial plan.
5. **Consolidation** — agreements, conflicts, and deeper patterns across all specialists (initial and emergent) are synthesized into a direct response
6. **Continuous learning** — the consultant stores learnings throughout the conversation, not just at the end. It learns topic insights, perception patterns, reasoning methods, and how to understand you better

The consultant is a thinking partner, not a vending machine. It asks clarifying questions, challenges your framing when it sees a better angle, expresses genuine curiosity, and proactively explores adjacent topics. Agents are spawned freely for any supporting process — research, fact-checking, asset analysis — not just specialist perspectives.

The knowledge store accumulates compressed, domain-agnostic principles. A lesson learned from biology might later inform a business decision. The stored forms are optimized for the agent, not for human readability — but the agent can explain them on request.

Conversations are automatically saved when they become substantive — you can also save manually at any time.

## Setup

Open Claude Code in this directory:

```bash
cd claude-consultant
claude
```

Claude Code reads `CLAUDE.md` and becomes The Consultant. Just ask it anything.

To include supporting materials (documents, data, images), drop them in the `assets/` folder before asking your question. The consultant will read and incorporate them into the analysis.

## Checking What It's Learned

- Say **"knowledge"** — the agent decodes and explains stored principles in plain language
- Say **"stats"** — view knowledge store statistics
- Say **"save"** — save the current conversation to `conversations/`
- Conversations are auto-saved when they become substantive

## Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Instructions that define the consultant behavior |
| `knowledge.py` | CLI tool for the persistent knowledge store |
| `knowledge_store/` | Where learned principles are persisted |
| `conversations/` | Saved conversation summaries with timestamps |
| `assets/` | Drop files here to support your queries (PDFs, data, docs, images) |

## Philosophy

Built on the idea that understanding emerges from bounded perspectives in productive tension — not from omniscience. Inspired by [thoughts on superintelligent AI agents](thoughts%20on%20superintelligent%20ai%20agents%20v1.md).
