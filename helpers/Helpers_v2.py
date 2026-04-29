"""
Helpers v2 — Casey's "kill the triple-quote" upgrade
====================================================

OLD WAY (your driver.ipynb cells right now):
    ohokay = '''11.1 Modules
    [200 lines of zybooks textbook]
    [200 lines of activity prompt]
    [escaped quotes everywhere making your eyes bleed]'''

    setin("True","False","True")
    def participation_activity_11_1_3():
        # actual code buried at the bottom

NEW WAY:
    notes("11.1.2")          # loads notes/11_1_2.md (you write the textbook ONCE)
    quiz("11.1.2", [...])    # 3 lines, runs the activity
    lab("11.1.8", code)      # writes + runs a lab solution

You keep:
- Run-all-from-top-to-bottom flow  ✅
- Self-contained cells  ✅
- The Problem class for sandboxing  ✅
- Your "iteration history" pattern  ✅

You drop:
- 200-line triple-quoted strings in cells  ❌
- Repeated boilerplate per problem  ❌
- "Where does the code start?" hunt  ❌

USAGE (in your driver.ipynb):
    # First cell (after setup):
    from Helpers_v2 import notes, quiz, lab, scratch, setin

    # Then each problem becomes ~3 lines:
    notes("11.1.2")
    setin("True", "False", "True")
    quiz("11.1.2", [
        ("car_sticker_price", True),
        ("todays_temperature", False),
        ("inventory_quantity", True),
    ])
"""

import os
import builtins
import shutil
import subprocess
from pathlib import Path
#
from rich.console import Console
from rich.markdown import Markdown
import builtins

console = Console()
old_print = builtins.print

def print(*args, sep=" ", end="\n", **kwargs):
    text = sep.join(str(x) for x in args)
    console.print(Markdown(text + end))

#
# ============================================================
# PATHS — adjust if your folder structure differs
# ============================================================
ROOT = Path.cwd()
NOTES_DIR = ROOT / "notes"          # markdown files for textbook content
ANSWERS_DIR = ROOT / "answers"      # markdown files for your reasoning/answers
WORKSPACES = ROOT / "_workspaces"   # sandboxes for Problem class

NOTES_DIR.mkdir(exist_ok=True)
ANSWERS_DIR.mkdir(exist_ok=True)
WORKSPACES.mkdir(exist_ok=True)


# ============================================================
# notes() — replaces ohokay = '''wall of text'''
# ============================================================

def notes(section_id, text=None):
    """
    Show notes for a zybooks section.

    First time: pass text= to save it. notes("11.1.2", text="...")
    After that: just notes("11.1.2") to display.

    section_id like "11.1.2" → saved to notes/11_1_2.md
    """
    fname = section_id.replace(".", "_") + ".md"
    path = NOTES_DIR / fname

    if text is not None:
        path.write_text(text, encoding="utf-8")
        print(f"📝 Saved notes/{fname}")

    if path.exists():
        content = path.read_text(encoding="utf-8")
        print(f"━━━ 📖 Section {section_id} ━━━")
        print(content)
        print(f"━━━ end {section_id} ━━━\n")
    else:
        print(f"⚠️  No notes for {section_id} yet. Pass text= to save them.")


# ============================================================
# quiz() — replaces def participation_activity_X_Y_Z(): ...
# ============================================================

def quiz(section_id, questions, prompt_label="Answer"):
    """
    Run a multi-question participation activity.

    questions = list of (question_text, expected_answer) tuples.
    Uses your existing setin() for staged inputs.

    Example:
        setin("True", "False", "True")
        quiz("11.1.2", [
            ("car_sticker_price", True),
            ("todays_temperature", False),
            ("inventory_quantity", True),
        ])
    """
    print(f"━━━ ✏️  Quiz {section_id} ━━━")
    correct = 0
    for i, (item, expected) in enumerate(questions, 1):
        try:
            answer = input(f"  {i}) {item}: ")
        except EOFError:
            print(f"  ⚠️  No more staged inputs at question {i}")
            break

        ok = str(answer).strip().lower() == str(expected).strip().lower()
        if ok:
            print(f"     ✅ Correct!")
            correct += 1
        else:
            print(f"     ❌ Got '{answer}', expected '{expected}'")

    total = len(questions)
    print(f"━━━ Score: {correct}/{total} ━━━\n")
    return correct, total


# ============================================================
# lab() — replaces big triple-quoted lab code with sandbox run
# ============================================================

def lab(section_id, code, inputs=None, files=None):
    """
    Run a lab solution in an isolated workspace.

    code     = string of your Python solution
    inputs   = list of strings to feed stdin (if any)
    files    = dict {filename: content} of supporting files

    Example:
        lab("11.10", '''
        with open("data.txt") as f:
            print(f.read())
        ''', files={"data.txt": "hello\\nworld\\n"})
    """
    sandbox = WORKSPACES / section_id.replace(".", "_")
    if sandbox.exists():
        shutil.rmtree(sandbox)
    sandbox.mkdir(parents=True)

    # Write supporting files
    if files:
        for fname, content in files.items():
            (sandbox / fname).write_text(content, encoding="utf-8")

    # Write the solution
    solution = sandbox / "solution.py"
    solution.write_text(code, encoding="utf-8")

    # Run it
    print(f"━━━ 🧪 Lab {section_id} ━━━")
    stdin_text = "\n".join(inputs) + "\n" if inputs else None
    result = subprocess.run(
        ["python", "solution.py"],
        cwd=sandbox,
        capture_output=True,
        text=True,
        input=stdin_text,
    )
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(f"⚠️  stderr:\n{result.stderr}")
    print(f"━━━ end lab {section_id} (exit {result.returncode}) ━━━\n")
    return result.returncode == 0


# ============================================================
# scratch() — quick sandbox for experimentation
# ============================================================

def scratch(code, name="scratch", inputs=None, files=None):
    """
    Throwaway sandbox for trying things.
    Same as lab() but lives at _workspaces/scratch/ (overwritten each time).
    """
    return lab(name, code, inputs=inputs, files=files)


# ============================================================
# setin() — keep your existing input-staging helper
# ============================================================

def setin(*inputs):
    """
    Stage input() responses for replay.
    setin("a", "b", "c")  →  next 3 input() calls return "a","b","c"
    setin()               →  reset to normal
    """
    if inputs:
        input_iter = iter(inputs)
        def mock_input(prompt=""):
            try:
                value = next(input_iter)
                print(f"{prompt}{value}")
                return value
            except StopIteration:
                raise EOFError("No more inputs for testing")
        if not hasattr(builtins, "_original_input_backup"):
            builtins._original_input_backup = builtins.input
        builtins.input = mock_input
    else:
        if hasattr(builtins, "_original_input_backup"):
            builtins.input = builtins._original_input_backup