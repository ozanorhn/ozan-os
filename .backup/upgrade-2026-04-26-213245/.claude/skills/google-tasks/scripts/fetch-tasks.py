#!/usr/bin/env python3
"""
Fetches all Google Tasks and outputs them as structured Markdown.
Requires: gws CLI (https://github.com/googleworkspace/cli)

Usage:
  python3 fetch-tasks.py
  python3 fetch-tasks.py --json       # raw JSON output
  python3 fetch-tasks.py --overdue    # only overdue tasks
"""

import subprocess
import json
import sys
from datetime import date, datetime

def gws(*args):
    result = subprocess.run(
        ["gws"] + list(args),
        capture_output=True, text=True
    )
    # gws writes "Using keyring backend: keyring" to stdout — filter it
    output = "\n".join(
        line for line in result.stdout.splitlines()
        if "keyring" not in line.lower()
    )
    return json.loads(output) if output.strip() else {}

def parse_due(due_str):
    if not due_str:
        return None
    return datetime.fromisoformat(due_str.replace("Z", "+00:00")).date()

def categorize(tasks, today):
    overdue, due_today, upcoming, no_date = [], [], [], []
    for t in tasks:
        if t.get("status") == "completed":
            continue
        due = parse_due(t.get("due"))
        if due is None:
            no_date.append(t)
        elif due < today:
            overdue.append((due, t))
        elif due == today:
            due_today.append(t)
        else:
            upcoming.append((due, t))
    overdue.sort(key=lambda x: x[0])
    upcoming.sort(key=lambda x: x[0])
    return overdue, due_today, upcoming, no_date

def fmt_task(t, due=None):
    title = t.get("title", "")
    notes = t.get("notes", "")
    due_str = f" *(fällig: {due.strftime('%d.%m.')})*" if due else ""
    note_str = f"\n    > {notes.replace(chr(10), ', ')}" if notes else ""
    return f"- [ ] {title}{due_str}{note_str}"

def main():
    raw_json = "--json" in sys.argv
    only_overdue = "--overdue" in sys.argv
    today = date.today()

    # Fetch all task lists
    lists_data = gws("tasks", "tasklists", "list")
    task_lists = lists_data.get("items", [])

    if raw_json:
        all_tasks = {"lists": []}
        for lst in task_lists:
            tasks_data = gws("tasks", "tasks", "list",
                             "--params", json.dumps({"tasklist": lst["id"]}))
            all_tasks["lists"].append({
                "title": lst["title"],
                "tasks": tasks_data.get("items", [])
            })
        print(json.dumps(all_tasks, indent=2, ensure_ascii=False))
        return

    sections = []
    all_overdue = []

    for lst in task_lists:
        tasks_data = gws("tasks", "tasks", "list",
                         "--params", json.dumps({"tasklist": lst["id"]}))
        tasks = tasks_data.get("items", [])
        if not tasks:
            continue

        overdue, due_today, upcoming, no_date = categorize(tasks, today)
        all_overdue.extend(overdue)

        if only_overdue:
            continue

        lines = [f"### {lst['title']}"]
        if overdue:
            for due, t in overdue:
                lines.append(fmt_task(t, due) + " ⚠️")
        if due_today:
            for t in due_today:
                lines.append(fmt_task(t) + " 📅 heute")
        if upcoming:
            for due, t in upcoming:
                lines.append(fmt_task(t, due))
        if no_date:
            for t in no_date:
                lines.append(fmt_task(t))

        if len(lines) > 1:
            sections.append("\n".join(lines))

    # Summary callout
    overdue_count = len(all_overdue)
    if overdue_count > 0:
        print(f"> [!warning] {overdue_count} überfällige Task(s)")
        for due, t in sorted(all_overdue, key=lambda x: x[0]):
            print(f"> - **{t['title']}** (seit {due.strftime('%d.%m.')})")
        print()

    print("\n".join(sections))

if __name__ == "__main__":
    main()
