# -*- coding: utf-8 -*-

from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("🤓 [link=https://javyxu.cn/]Javy Xu", guide_style="bold cyan")
full_stack_tree = tree.add("🔧 Full-stack developer")
tree.add("🌍 GIS")

about = """\
I am a full-stack developer with expertise in Python, Golang and C++, focusing on AI engineering and cloud native"""

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="blue", title="[b]Hi there", width=60
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}
<a href="https://github.com/javyxu"><img src="https://img.shields.io/github/followers/javyxu.svg?label=GitHub&style=social" alt="GitHub"></a></pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)