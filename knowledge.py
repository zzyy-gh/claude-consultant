#!/usr/bin/env python3
"""Knowledge store CLI — called by Claude Code to manage the consultant's memory.

Usage:
    python knowledge.py store '<json_array>'    Store new principles
    python knowledge.py retrieve '<tags_json>'  Retrieve by tags (returns top matches)
    python knowledge.py all                     Dump all principles
    python knowledge.py stats                   Show statistics
    python knowledge.py clear                   Clear all principles
"""

import json
import os
import hashlib
import time
import sys

STORE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "knowledge_store")
STORE_FILE = os.path.join(STORE_DIR, "principles.json")


def _ensure():
    os.makedirs(STORE_DIR, exist_ok=True)
    if not os.path.exists(STORE_FILE):
        _save({"principles": [], "meta": {"total_tasks": 0}})


def _load():
    _ensure()
    with open(STORE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save(data):
    _ensure()
    with open(STORE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def _id(content):
    return hashlib.sha256(content.encode()).hexdigest()[:12]


def cmd_store(principles_json):
    """Store principles. Input: JSON array of {encoded, tags, confidence}."""
    principles = json.loads(principles_json)
    data = _load()
    existing_ids = {p["id"] for p in data["principles"]}
    added, updated = 0, 0

    for p in principles:
        pid = _id(p["encoded"])
        if pid in existing_ids:
            for ex in data["principles"]:
                if ex["id"] == pid:
                    ex["confidence"] = min(1.0, ex["confidence"] + 0.1)
                    ex["access_count"] += 1
                    updated += 1
                    break
        else:
            data["principles"].append({
                "id": pid,
                "encoded": p["encoded"],
                "tags": p.get("tags", []),
                "connections": p.get("connections", []),
                "confidence": p.get("confidence", 0.5),
                "created": time.time(),
                "access_count": 0,
            })
            added += 1

    data["meta"]["total_tasks"] += 1
    _save(data)
    print(json.dumps({"added": added, "updated": updated, "total": len(data["principles"])}))


def cmd_retrieve(tags_json):
    """Retrieve principles matching tags. Input: JSON array of tag strings."""
    tags = set(t.lower() for t in json.loads(tags_json))
    data = _load()
    scored = []

    for p in data["principles"]:
        p_tags = set(t.lower() for t in p["tags"])
        overlap = len(tags & p_tags)
        if overlap > 0:
            score = overlap * p["confidence"] * (1 + p["access_count"] * 0.1)
            scored.append((score, p))
            p["access_count"] += 1

    if scored:
        _save(data)

    scored.sort(key=lambda x: x[0], reverse=True)
    results = [p for _, p in scored[:10]]
    print(json.dumps(results, indent=2, ensure_ascii=False))


def cmd_all():
    """Dump all principles."""
    data = _load()
    print(json.dumps(data["principles"], indent=2, ensure_ascii=False))


def cmd_stats():
    """Show statistics."""
    data = _load()
    ps = data["principles"]
    print(json.dumps({
        "total_principles": len(ps),
        "total_tasks": data["meta"]["total_tasks"],
        "avg_confidence": round(sum(p["confidence"] for p in ps) / len(ps), 2) if ps else 0,
        "top_tags": _top_tags(ps),
    }, indent=2))


def _top_tags(principles):
    counts = {}
    for p in principles:
        for t in p["tags"]:
            counts[t] = counts.get(t, 0) + 1
    return sorted(counts.items(), key=lambda x: -x[1])[:10]


def cmd_clear():
    """Clear all principles."""
    _save({"principles": [], "meta": {"total_tasks": 0}})
    print("Knowledge store cleared.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "store":
        cmd_store(sys.argv[2])
    elif cmd == "retrieve":
        cmd_retrieve(sys.argv[2])
    elif cmd == "all":
        cmd_all()
    elif cmd == "stats":
        cmd_stats()
    elif cmd == "clear":
        cmd_clear()
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
