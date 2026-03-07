# The Consultant

A multi-perspective analysis system built on Claude Code. Instead of answering from a single viewpoint, it spawns specialist agents with competing perspectives, synthesizes their insights, and accumulates abstract wisdom over time.

## How It Works

1. **You ask a question** — anything: strategy, technical decisions, life choices, analysis
2. **Perspectives are chosen** — the orchestrator picks 2-5 specialist viewpoints that create productive tension (e.g., a game theorist, a stoic philosopher, a devil's advocate)
3. **Specialists analyze in parallel** — each pushes their perspective boldly without trying to be balanced
4. **Consolidation** — agreements, conflicts, and deeper patterns are synthesized into a direct response
5. **Learning** — abstract principles are extracted and stored for future tasks

The knowledge store accumulates compressed, domain-agnostic principles. A lesson learned from biology might later inform a business decision. The stored forms are optimized for the agent, not for human readability — but the agent can explain them on request.

## Setup

Open Claude Code in this directory:

```bash
cd claude-consultant
claude
```

Claude Code reads `CLAUDE.md` and becomes The Consultant. Just ask it anything.

## Checking What It's Learned

- Say **"knowledge"** — the agent decodes and explains stored principles in plain language
- Say **"stats"** — view knowledge store statistics

## Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Instructions that define the consultant behavior |
| `knowledge.py` | CLI tool for the persistent knowledge store |
| `knowledge_store/` | Where learned principles are persisted |

## Philosophy

Built on the idea that understanding emerges from bounded perspectives in productive tension — not from omniscience. Inspired by [thoughts on superintelligent AI agents](thoughts%20on%20superintelligent%20ai%20agents%20v1.md).
