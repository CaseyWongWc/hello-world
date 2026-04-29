#!/bin/bash
# 🔄 autosave.sh — auto git commit & push every 20 seconds
# Usage:
#   Start:  bash autosave.sh start
#   Stop:   bash autosave.sh stop
#   Status: bash autosave.sh status

PIDFILE=".autosave.pid"

run_loop() {
    echo "🟢 Autosave started! Saving every 20 seconds. (PID: $$)"
    while true; do
        sleep 20
        # Only commit if there are actual changes
        if ! git diff --quiet || ! git diff --cached --quiet || [ -n "$(git status --porcelain)" ]; then
            TIMESTAMP=$(date +"%H:%M:%S")
            git add .
            git commit -m "🔄 autosave @ $TIMESTAMP"
            git push
            echo "[✅ $TIMESTAMP] Changes saved & pushed!"
        else
            echo "[$(date +"%H:%M:%S")] No changes — skipping."
        fi
    done
}

case "$1" in
  start)
    if [ -f "$PIDFILE" ] && kill -0 "$(cat $PIDFILE)" 2>/dev/null; then
        echo "⚠️  Autosave is already running! (PID: $(cat $PIDFILE))"
        echo "    Run: bash autosave.sh stop    to stop it first."
        exit 1
    fi
    run_loop &
    echo $! > "$PIDFILE"
    echo "💾 PID saved to $PIDFILE — run 'bash autosave.sh stop' to stop."
    ;;
  stop)
    if [ -f "$PIDFILE" ]; then
        PID=$(cat "$PIDFILE")
        if kill -0 "$PID" 2>/dev/null; then
            kill "$PID"
            rm "$PIDFILE"
            echo "🔴 Autosave stopped! (was PID: $PID)"
        else
            echo "⚠️  Process not found — it may have already stopped."
            rm -f "$PIDFILE"
        fi
    else
        echo "❌ No autosave process found. Start it with: bash autosave.sh start"
    fi
    ;;
  status)
    if [ -f "$PIDFILE" ] && kill -0 "$(cat $PIDFILE)" 2>/dev/null; then
        echo "🟢 Autosave is RUNNING (PID: $(cat $PIDFILE))"
    else
        echo "🔴 Autosave is STOPPED"
    fi
    ;;
  *)
    echo "Usage: bash autosave.sh [start|stop|status]"
    echo ""
    echo "  start   — begin auto-saving every 20 seconds"
    echo "  stop    — stop the autosave loop"
    echo "  status  — check if autosave is running"
    ;;
esac