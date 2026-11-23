<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<h3 align="center">agent-setup</h3>

<p align="center">
    My set of Claude Code subagents, plus the notes the organizer uses to coordinate them and a screenshot tool for design reviews.
    <br />
    <br />
    <a href="https://github.com/MarcyVibin/agent-setup/issues">Report Bug</a>
    &middot;
    <a href="https://github.com/MarcyVibin/agent-setup/issues">Request Feature</a>
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#requirements">Requirements</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

---

## About The Project

Each Markdown file in the top folder defines one [Claude Code subagent](https://docs.claude.com/en/docs/claude-code/sub-agents): a front-matter block (`name`, `description`, `tools`) followed by the instructions for that role. The agents name the skills they load, and fall back to the same working discipline when a skill is not installed.

| Agent | What it does |
| --- | --- |
| [planner](planner.md) | Turns a request into a spec and ordered, testable tickets before any code is written |
| [frontend-developer](frontend-developer.md) | UI components, pages, styling and client-side behaviour |
| [backend-developer](backend-developer.md) | APIs, services, data access, background jobs and integrations |
| [design-director](design-director.md) | Critiques screenshots, scores them against a rubric and writes the design brief; never edits application code |
| [qa-reviewer](qa-reviewer.md) | Read-only review of changes for correctness, accessibility and code quality |
| [security-auditor](security-auditor.md) | Audits code, dependencies and configuration and reports prioritised findings |
| [legal-reviewer](legal-reviewer.md) | Reviews contracts and NDAs against a playbook and drafts redlines; does not give final legal advice |
| [marketing](marketing.md) | Copy, pricing and offers, campaigns and positioning |
| [researcher](researcher.md) | Source-backed research and creative writing grounded in it |
| [docs-writer](docs-writer.md) | READMEs, guides and agent instructions, checked against the code |
| [rune-expert](rune-expert.md) | Answers questions about the Rune Rust GPU UI framework from a local copy of its source |

The [organizer/](organizer) folder holds reference notes for coordinating several agents on one goal:

- [big-projects.md](organizer/big-projects.md): build a knowledge graph with graphify before many agents navigate a large codebase
- [parallel-agents.md](organizer/parallel-agents.md): when splitting work across agents of the same kind pays off
- [revision-loops.md](organizer/revision-loops.md): design and review loops with a judge
- [sub-organizers.md](organizer/sub-organizers.md): handing a large slice of work to a sub-organizer

[tools/shot.py](tools/shot.py) takes screenshots of a page at several widths and reports horizontal overflow, console errors and missing or unexpectedly visible elements. [tools/test_shot.py](tools/test_shot.py) is its self-check.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Claude Code][ClaudeCode-badge]][ClaudeCode-url]
* [![Python][Python.org]][Python-url]
* [![Playwright][Playwright-badge]][Playwright-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Getting Started

### Requirements

- [Claude Code](https://docs.claude.com/en/docs/claude-code/overview)
- The skills the agents refer to (for example `mattpocock-skills`, `superpowers` and `anthropic-skills`). Without them the agents say so and work without.
- For `tools/shot.py`: Python 3 and Playwright with a Chromium or Chrome browser

### Installation

Clone the repository:

```sh
git clone https://github.com/MarcyVibin/agent-setup.git
cd agent-setup
```

Copy the agent files into your user-level agents folder, so every project can use them:

```sh
mkdir -p ~/.claude/agents
cp *.md ~/.claude/agents/
```

For a single project, copy them into `.claude/agents/` in that project instead.

For the screenshot tool:

```sh
pip install playwright
playwright install chromium
```

---

## Usage

Claude Code picks an agent by its `description`, or you can ask for one by name, for example "use the planner agent to break this feature into tickets".

Take screenshots of a local site at two widths:

```sh
python3 tools/shot.py ./my-site --widths 375,1280 --out /tmp/shots
```

`shot.py` prints a JSON summary and exits with code 1 if a check fails. Check the tool itself with `python3 tools/test_shot.py`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Contact

Marc Steger - marc.steger06@gmail.com

Project Link: https://github.com/MarcyVibin/agent-setup

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Badge Links -->

[ClaudeCode-badge]: https://img.shields.io/badge/Claude%20Code-Subagents-D97757?style=for-the-badge
[ClaudeCode-url]: https://docs.claude.com/en/docs/claude-code/overview

[Python.org]: https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[Playwright-badge]: https://img.shields.io/badge/Playwright-Screenshots-2EAD33?style=for-the-badge&logo=playwright&logoColor=white
[Playwright-url]: https://playwright.dev/

[contributors-shield]: https://img.shields.io/github/contributors/MarcyVibin/agent-setup.svg?style=for-the-badge
[contributors-url]: https://github.com/MarcyVibin/agent-setup/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/MarcyVibin/agent-setup.svg?style=for-the-badge
[forks-url]: https://github.com/MarcyVibin/agent-setup/network/members

[stars-shield]: https://img.shields.io/github/stars/MarcyVibin/agent-setup.svg?style=for-the-badge
[stars-url]: https://github.com/MarcyVibin/agent-setup/stargazers

[issues-shield]: https://img.shields.io/github/issues/MarcyVibin/agent-setup.svg?style=for-the-badge
[issues-url]: https://github.com/MarcyVibin/agent-setup/issues
