#!/usr/bin/env python3
import subprocess
import json
import urllib.request
import urllib.parse
import datetime
import sys
import hashlib
import os

BOT_TOKEN = "8691640575:AAHHmZK5avLkwlBqWkUI8OLMDjGqxU-u-p4"
CHAT_ID = 8256935721
WORKING_DIR = "/root/ozan-os"
CLAUDE_BIN = "/root/.local/bin/claude"
LAST_SEND_FILE = "/root/ozan-os/tgbot/.last_alert_date"

PROMPT = (
    "Read HEARTBEAT.md and follow the instructions exactly. "
    "Reply HEARTBEAT_OK if nothing needs attention, "
    "otherwise give a brief German summary as specified."
)


def send_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = json.dumps({"chat_id": CHAT_ID, "text": text}).encode()
    req = urllib.request.Request(
        url, data=payload, headers={"Content-Type": "application/json"}
    )
    urllib.request.urlopen(req, timeout=10)


def already_sent_today():
    today = datetime.date.today().isoformat()
    try:
        with open(LAST_SEND_FILE) as f:
            return f.read().strip() == today
    except FileNotFoundError:
        return False


def mark_sent_today():
    with open(LAST_SEND_FILE, "w") as f:
        f.write(datetime.date.today().isoformat())


def log(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"[{ts}] {msg}", flush=True)


def run():
    log("Heartbeat gestartet")

    try:
        result = subprocess.run(
            [CLAUDE_BIN, "-p", PROMPT, "--output-format", "json", "--dangerously-skip-permissions"],
            cwd=WORKING_DIR,
            capture_output=True,
            text=True,
            timeout=180,
        )
    except subprocess.TimeoutExpired:
        log("Timeout")
        send_telegram("Heartbeat-Fehler: Claude hat zu lange gebraucht.")
        return

    if result.returncode != 0:
        err = result.stderr[-500:].strip()
        log(f"Claude-Fehler: {err}")
        send_telegram(f"Heartbeat-Fehler:\n{err}")
        return

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        log("JSON-Parse-Fehler")
        send_telegram(f"Heartbeat: Konnte Antwort nicht parsen.")
        return

    reply = data.get("result", "").strip()

    if reply.startswith("HEARTBEAT_OK"):
        log("OK – kein Alert")
    else:
        if already_sent_today():
            log("Alert heute bereits gesendet – übersprungen")
        else:
            log(f"Alert: {reply[:80]}...")
            send_telegram(reply)
            mark_sent_today()


if __name__ == "__main__":
    run()
