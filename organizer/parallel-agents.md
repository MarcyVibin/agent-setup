# Parallel agents of the same kind

You may spawn several agents of the same type at once, such as three `frontend-developer` agents, each with its own slice of the work. This is faster. It is not free: every agent you spawn pays a fixed start-up cost before it does any work, for its system prompt, its role file, and the skills it loads. In practice that is tens of thousands of tokens per agent, even for a tiny task. Splitting pays off only when it saves more than that.

Splitting can also save tokens. One agent working through a long task re-reads its whole growing history on every turn, so its cost grows faster than its work. Several agents with short, separate histories can cost less in total than one long-running agent.

## When to split

Split one specialist's work into parallel agents only when all of these are true:

- **The slices are independent.** No slice needs another slice's output, and no slice makes a decision the others must follow. Decide shared things before you split, and put them in the brief or in a shared file such as `design/DESIGN.md`, a spec, or an API contract.
- **Each slice is substantial.** Each slice needs many steps of its own, roughly ten or more tool calls, or a separate long file to write. If a slice is a quick edit, keep it in one agent.
- **The files do not overlap.** Each agent owns its own files, and you name them in its brief. Two agents must never edit the same file. If they would, either do not split, or have one agent own the shared file and the others write only to their own files. In a git repository where overlap cannot be avoided, use `isolation: "worktree"` for each agent and merge the results yourself.
- **The result can be checked as a whole.** You can run one integration check after the agents finish, such as a build, a test run, or `tools/shot.py` on the whole site.

If any of these is false, run the work in one agent. A wrong split costs more than it saves, because the merge and the rework are paid on top.

## How to split

1. **Cap the count.** Use at most four parallel agents of one kind unless the user asks for more. Each extra agent adds its start-up cost and makes the merge harder.
2. **Give every sibling the same opening.** Start every brief with the same text: role file, shared context, shared rules. Put the part that differs, the slice and its files, at the end. The siblings stay consistent, and you write less.
3. **Give each one its boundaries.** Each brief names the files the agent may change, the files it must not touch, and the shared decisions it must follow.
4. **Merge, then check once.** After all the siblings report, run one integration check on the whole result. Use a single reviewer for the whole result, not one per slice, unless the slices are large enough to need their own review.
5. **Judge together.** When siblings produce alternatives to compare, such as design directions, one judge compares them side by side. Separate agents scoring their own work are not comparable.

## Good and bad splits

- **Good:** three design directions in the exploration round. Each `design-director` agent builds one mockup in its own `design/mockups/direction-X/` folder, then one `design-director` compares all three and recommends one.
- **Good:** five independent pages of a site whose design tokens are already fixed in `DESIGN.md`, one `frontend-developer` per page, each owning its own page file, with shared CSS changes left to one owner.
- **Good:** researching four unrelated competitors, one `researcher` each.
- **Bad:** splitting one page into hero, services, and FAQ agents that all edit the same `index.html` and `styles.css`.
- **Bad:** splitting a two-line fix, a single small file, or any task that finishes in a few tool calls.
- **Bad:** splitting work whose slices must agree on something that is not yet decided, such as the type scale or an API shape.

Report parallel runs in the cost notes: which agents ran side by side, and why the split was worth it.
