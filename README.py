# Grabbed from: https://github.com/koaning/koaning/

from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

# tree = Tree("🙂 [link=https://giopaglia.github.io/]Gio Pagliarini", guide_style="bold bright_black")

soletree = Tree("☀️ Sole.jl", guide_style="bold bright_black")

tree1 = Tree("📦 Julia Packages", guide_style="bold bright_black")
# tree1 = tree.add("📦 Julia Packages", guide_style="bright_black")
tree1.add("[bold link=https://github.com/aclai-lab/Sole.jl]Sole.jl[/]                  - [bright_black]framework for symbolic modeling and learning")
tree1.add("[bold link=https://github.com/aclai-lab/SoleLogics.jl]SoleLogics.jl[/]            - [bright_black]model checking engine")
tree1.add("[bold link=https://github.com/aclai-lab/SoleModels.jl]SoleModels.jl[/]            - [bright_black]analysis and rule extraction from symbolic models")
tree1.add("[bold link=https://github.com/aclai-lab/SoleData.jl]SoleData.jl[/]              - [bright_black]optimized data structures for learning symbolic models")
tree1.add("[bold link=https://github.com/aclai-lab/ModalDecisionTrees.jl]ModalDecisionTrees.jl[/]    - [bright_black]CART-like learning of trees and forests based on modal logic")

tree2 = Tree("🎙️ Talks", guide_style="bold bright_black")
# tree2 = tree.add("🎙️ Talks", guide_style="bright_black")
tree2.add("[bold link=https://www.youtube.com/watch?v=pfejOC_T5cQ]Symbolic AI workflows with Sole.jl (JuliaCon2024)[/]")
tree2.add("[bold link=https://www.youtube.com/watch?v=HTRhOmQIObg]Third Millennium Symbolic Learning with Sole.jl (JuliaCon2023)[/]")
tree2.add("[bold link=https://www.youtube.com/watch?v=HTRhOmQIObg]Decision Trees, Meet Modal Logics (JuliaCon2022)[/]")


tree2 = Tree("🎙️ Talks", guide_style="bold bright_black")
# tree2 = tree.add("🎙️ Talks", guide_style="bright_black")
tree2.add("[bold link=https://www.youtube.com/watch?v=pfejOC_T5cQ]Symbolic AI workflows with Sole.jl (JuliaCon2024)[/]")
tree2.add("[bold link=https://www.youtube.com/watch?v=HTRhOmQIObg]Third Millennium Symbolic Learning with Sole.jl (JuliaCon2023)[/]")
tree2.add("[bold link=https://www.youtube.com/watch?v=HTRhOmQIObg]Decision Trees, Meet Modal Logics (JuliaCon2022)[/]")



soletree.add(tree1)
soletree.add(tree2)

projectstree = Tree("🛠️ Utilities", guide_style="bold bright_black")
projectstree.add("[bold link=https://github.com/giopaglia/bitsofus]bitsofus[/]                     - [bright_black]Takeout data enhancer utilities")
projectstree.add("[bold link=https://github.com/giopaglia/rooflini]rooflini[/]                     - [bright_black]Python plot roofline analyses ")
projectstree.add("[bold link=https://github.com/giopaglia/academic-grandfolks]academic-grandfolks[/]          - [bright_black]Trace one's academic genealogy")


console.print(projectstree)
console.print("")
console.print(soletree)
console.print("")

CONSOLE_HTML_FORMAT = """\

<div align="center">
<div id="user-content-toc">
	<ul>
		<summary><h1 style="display: inline-block;">👋</h1></summary>
	</ul>
</div>
I'm Gio (/d͡ʒo/), a computer scientist based in Ferrara, Italy.
</div>
<h2></h2>

### 💫 About Me

🤔 Interested in AI, machine learning, computation theory, open source;
<br>
📚 Studied Computer Science in 🇮🇹, 🇸🇪, 🇸🇬 & 🇦🇺;
<br>
🌱 Working on symbolic AI at <a target="_blank" href="https://planting.space/">PlantingSpace</a>;
<br>
🔭 Occasionally contributing to the <a target="_blank" href="https://github.com/aclai-lab/Sole.jl">Sole.jl</a> AI framework in Julia;
<br>
⚡ Checkout my <a target="_blank" href="https://giopaglia.github.io/">website</a>, my
<a target="_blank" href="https://linkedin.com/in/giovanni.pagliarini/">LinkedIn</a> or my <a target="_blank" href="https://giopaglia.github.io/gio/Giovanni-Pagliarini-CV-en-latest.pdf">CV</a>.


<!-- [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/giovanni.pagliarini) -->

### 💻 Things I work with

<!-- https://devicon.dev/ & https://github.com/simple-icons/simple-icons -->

<div align="left">
<a target="_blank" href="https://julialang.org/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/julia/julia-original.svg" style="width:30px;height:30px;" alt="Julia" title="The Julia programming language is the best language in the world!!!"  /></a>
<!--   <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/julia/julia-original-wordmark.svg" style="width:30px;height:30px;" alt="Julia"  /> -->
<img width="12" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" style="width:30px;height:30px;" alt="Python" title="The Python programming language for fast prototying."  />
<img width="12" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original.svg" style="width:30px;height:30px;" alt="Jupyter" title="Jupyter for presenting results and prototyping interactive dashboards."  />
<!-- <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original-wordmark.svg" style="width:30px;height:30px;" alt="Jupyter" title="Jupyter for presenting results and prototyping interactive dashboards."  /> -->
<img width="12" />
<!-- <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/latex/latex-original.svg" style="width:30px;height:30px;" alt="LaTeX" title="LaTeX for typesetting elegant reports, whitepapers, and presentations."  />
<img width="12" /> -->
<!-- https://www.svgrepo.com/svg/376333/latex?edit=true -->
<img src="svgrepo/latex-svgrepo-com.svg" style="width:30px;height:30px;" alt="LaTeX" title="LaTeX for typesetting elegant reports, whitepapers, and presentations."  />
<img width="12" />
<img src="https://cdn.simpleicons.org/gnubash/4EAA25" style="width:30px;height:30px;" alt="Bash" title="Bash &amp; Zsh for basic automation." />
<img width="12" />
<!-- <img src="https://github.com/Zsh-art/logo/blob/main/svg/color_vertical_icon.svg" style="width:30px;height:30px;" alt="Zsh" title="Zsh for basic automation." />
<img width="12" /> -->
<img src="https://cdn.simpleicons.org/git/F05032" style="width:30px;height:30px;" alt="Git" title="Git for versioning every bit of textual data: code, notes, holiday plans, etc." />
<img width="12" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" style="width:30px;height:30px;" alt="Linux OS."  />
<img width="12" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vscode/vscode-original.svg" style="width:30px;height:30px;" alt="Visual Studio Code"/>
<img width="12" />
<img src="https://cdn.simpleicons.org/neovim" style="width:30px;height:30px;" alt="Sublime Text."  />
<img width="12" />
<img src="https://cdn.simpleicons.org/tmux" style="width:30px;height:30px;" alt="Tmux."  />
<img width="12" />
<img src="https://cdn.simpleicons.org/alacritty" style="width:30px;height:30px;" alt="Alacritty."  />
<img width="12" />
<img src="https://cdn.simpleicons.org/sublimetext" style="width:30px;height:30px;" alt="Sublime Text."  />
<img width="12" />
<img src="https://cdn.simpleicons.org/ollama" style="width:30px;height:30px;" alt="Ollama: local language models."  />
</div>



<!-- karabiner -->
<!-- cinnamon -->

<br>

<!-- ![Julia](https://img.shields.io/badge/-Julia-9558B2?style=for-the-badge&logo=julia&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Shell](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
 -->

![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white) 
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
<!-- ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) -->

<!-- 
###

<div align="left">
	<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" height="40" alt="linux logo"  />
	<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" height="40" alt="numpy logo"  />
	<img width="12" />
	<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" height="40" alt="tensorflow logo"  />
	<img width="12" />
	<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" height="40" alt="pandas logo"  />
	<img width="12" />
	<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytorch/pytorch-original.svg" height="40" alt="pytorch logo"  />
	<img width="12" />
</div>
 -->
<!-- # 📊 GitHub Stats
![](https://github-readme-stats.vercel.app/api?username=giopaglia&theme=onedark&hide_border=false&include_all_commits=false&count_private=false)<br/>
![](https://github-readme-streak-stats.herokuapp.com/?user=giopaglia&theme=onedark&hide_border=false)<br/>
![](https://github-readme-stats.vercel.app/api/top-langs/?username=giopaglia&theme=onedark&hide_border=false&include_all_commits=false&count_private=false&layout=compact)

###
 -->
<!-- <div align="left">
	<img src="https://streak-stats.demolab.com?user=giopaglia&locale=en&mode=daily&theme=onedark&hide_border=false&border_radius=5" height="150" alt="streak graph"  />
	<img src="https://github-readme-stats.vercel.app/api/top-langs?username=giopaglia&locale=en&hide_title=false&layout=compact&card_width=320&langs_count=5&theme=onedark&hide_border=false" height="150" alt="languages graph"  />
</div>
 -->
<!-- --- -->
<!-- ### 🔝 Top Contributed Repo
<div align="left">
	<img src="https://streak-stats.demolab.com?user=giopaglia&locale=en&mode=daily&theme=onedark&hide_border=false&border_radius=5" height="150" alt="streak graph"  />
	<img src="https://github-contributor-stats.vercel.app/api?username=giopaglia&limit=5&theme=onedark&combine_all_yearly_contributions=true" height="150" alt="languages graph"  />
</div>


[![](https://visitcount.itsvg.in/api?id=giopaglia&icon=6&color=1)](https://visitcount.itsvg.in) -->

<!-- Proudly created with GPRM ( https://gprm.itsvg.in ) -->

### 🚀 Projects

<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>

"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
