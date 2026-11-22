# Sub-organizers for very complex tasks

Use a sub-organizer only when a task is very complex. Normal tasks, including large ones, should be run directly by the top-level organizer. A sub-organizer is a general agent that loads the organizer skill with the Skill tool. There is no separate organizer agent type.

Spawn a sub-organizer only when all of these are true:

- The goal splits into two or more workstreams that are each large enough to need their own team of specialists.
- The workstreams can run independently for most of their length, so they do not need to wait on each other.
- Running them under one organizer would mix too many concerns into one plan, making the plan hard to follow or check.

**Ask the user before you spawn any sub-organizer.** This is required, not optional. Before you spawn one, stop and ask the user for permission in one short message. Say which workstreams you would split out, why a single organizer would not be enough, and roughly how many extra agents and tokens it would cost compared with running the work directly. Offer the option to run the work directly instead. Spawn a sub-organizer only after the user says yes to that specific split. If the user says no or does not answer, run the work directly with one organizer.

When the user has approved a sub-organizer:

1. **Give it one workstream only.** Write a brief with the goal of that workstream, its inputs, its done criteria, its boundaries, and the report format. Make clear which parts of the overall goal belong to other workstreams. If a graph exists, tell it where the graph report is.
2. **Set its model tier to sonnet.** Planning and coordination need judgment, so sonnet is the default. Use opus only when the decomposition itself is ambiguous and sonnet has failed to produce a usable plan, and say so when you ask the user.
3. **Limit depth to one level.** A sub-organizer must not spawn another sub-organizer, even if it has the user's permission in its brief. If it finds that its workstream needs one, it should report that back to you, and you ask the user again.
4. **Have it report in the standard format.** It returns the outcome, its team and tiers, its checks, its cost notes, its missing pieces, and its open items. Keep the report short so the top-level organizer can read it cheaply.

The top-level organizer owns the overall outcome. Check each sub-organizer's report against the overall done criteria, not only against its own workstream. Run any cross-workstream integration check yourself, using the cheapest check that proves the pieces fit together. Only then report to the user.

Count sub-organizers in the cost notes. Explain in the report why the extra cost was justified, or why a direct run would have been enough.

