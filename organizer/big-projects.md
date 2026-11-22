# Big projects: use graphify

A big project is one with many modules or many documents, where an agent would otherwise spend a lot of tokens grepping through files to find its way around. For big projects, graphify should be used before any specialist starts work.

Graphify turns a folder of code, docs, and other files into a knowledge graph. Agents then read a summary report and query the graph instead of searching raw files. It works best in Claude Code and in other tools that support skills.

Follow these steps for a big project:

1. **Check whether graphify is installed.** Look for the `graphify` skill in the discovered skills. If it is missing, do not install it on your own. Ask the user for permission first, and give the install command: `pip install graphifyy && graphify install`. Continue without it only if the user says no.
2. **Build the graph once.** Run `/graphify .` at the project root. Building the graph has a one-time cost, because graphify uses Claude to extract concepts from documents and images, so report that cost in the cost notes.
3. **Read the report first.** Read `graphify-out/GRAPH_REPORT.md` before you plan. It lists the central components and how the parts of the project are grouped. Use it to decide which agent owns which area.
4. **Brief each agent to use the graph.** Tell each specialist to read `graphify-out/GRAPH_REPORT.md` and to query the graph for its area before it searches raw files. Raw searches are still allowed when the graph does not answer the question.
5. **Rebuild after large changes.** When a run changes many files, rebuild the graph before the next run that depends on it, and say so in the report.

Do not build a graph for a small project. The one-time cost is only worth paying when many agents will navigate the same codebase.

