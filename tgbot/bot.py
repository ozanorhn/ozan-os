import subprocess
import json
import os
import telegramify_markdown
from telegram import Update
from telegram.constants import ParseMode
from telegram.error import BadRequest
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    ContextTypes, filters
)

BOT_TOKEN = "8691640575:AAHHmZK5avLkwlBqWkUI8OLMDjGqxU-u-p4"
ALLOWED_USER_ID = 8256935721
WORKING_DIR = "/root/ozan-os"
CLAUDE_BIN = "/root/.local/bin/claude"

sessions = {}


def authorized(update):
    return update.effective_user and update.effective_user.id == ALLOWED_USER_ID


async def start(update, context):
    if not authorized(update):
        return
    chat_id = update.effective_chat.id
    sessions.pop(chat_id, None)
    await update.message.reply_text(
        "Bereit. Schreib einfach drauflos.\n\n"
        f"Arbeitsverzeichnis: {WORKING_DIR}\n\n"
        "/new - neue Konversation\n"
        "/cd <pfad> - Arbeitsverzeichnis aendern"
    )


async def new_conversation(update, context):
    if not authorized(update):
        return
    chat_id = update.effective_chat.id
    sessions.pop(chat_id, None)
    await update.message.reply_text("Neue Claude-Konversation.")


async def change_dir(update, context):
    global WORKING_DIR
    if not authorized(update):
        return
    if not context.args:
        await update.message.reply_text(f"Aktuell: {WORKING_DIR}")
        return
    new_path = context.args[0]
    if os.path.isdir(new_path):
        WORKING_DIR = new_path
        await update.message.reply_text(f"Wechsel zu {WORKING_DIR}")
    else:
        await update.message.reply_text(f"Pfad existiert nicht: {new_path}")


async def chat(update, context):
    if not authorized(update):
        print(f"Unauthorized: {update.effective_user.id}", flush=True)
        return
    chat_id = update.effective_chat.id
    user_message = update.message.text
    print(f"[MSG] {chat_id}: {user_message[:60]}", flush=True)

    await context.bot.send_chat_action(chat_id=chat_id, action="typing")

    cmd = [CLAUDE_BIN, "-p", user_message, "--output-format", "json"]
    if chat_id in sessions:
        cmd += ["--resume", sessions[chat_id]]

    try:
        result = subprocess.run(
            cmd,
            cwd=WORKING_DIR,
            capture_output=True,
            text=True,
            timeout=300
        )

        if result.returncode != 0:
            sessions.pop(chat_id, None)
            await update.message.reply_text(
                f"Claude-Fehler:\n{result.stderr[-1000:]}"
            )
            return

        data = json.loads(result.stdout)
        reply = data.get("result", "(keine Antwort)")
        print(f"[REPLY] {len(reply)} chars", flush=True)
        session_id = data.get("session_id")
        if session_id:
            sessions[chat_id] = session_id

        formatted = telegramify_markdown.markdownify(reply)
        for i in range(0, len(formatted), 4000):
            chunk = formatted[i:i+4000]
            try:
                await update.message.reply_text(chunk, parse_mode=ParseMode.MARKDOWN_V2)
            except BadRequest:
                await update.message.reply_text(reply[i:i+4000])

    except subprocess.TimeoutExpired:
        await update.message.reply_text("Timeout - Claude hat zu lange gebraucht.")
    except json.JSONDecodeError:
        await update.message.reply_text(
            f"Konnte Antwort nicht parsen:\n{result.stdout[-1000:]}"
        )
    except Exception as e:
        await update.message.reply_text(f"{type(e).__name__}: {e}")


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("new", new_conversation))
    app.add_handler(CommandHandler("cd", change_dir))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    print("Bot laeuft...")
    app.run_polling()


if __name__ == "__main__":
    main()
