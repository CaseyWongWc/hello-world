#%pip install rich

from rich.console import Console
from rich.markdown import Markdown
import builtins

console = Console()
old_print = builtins.print

def print(*args, sep=" ", end="\n", **kwargs):
    text = sep.join(str(x) for x in args)
    console.print(Markdown(text + end))