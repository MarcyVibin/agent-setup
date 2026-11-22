# Revision loops

Use this section whenever the user asks you to improve something over several rounds, to run in a loop, or to make something "actually good". The usual failure is a loop that fixes defects every round but never changes the thing itself. Every round must make a visible change toward the goal.

## Loop rules for every kind of work

1. **Measure before the first round.** Have a judge agent score the current version against a rubric. Keep the scores, so later rounds can be compared with them.
2. **Separate the roles.** Each round has a judge, which critiques and sets direction, a builder, which makes the change, and a checker, which confirms nothing broke. The judge and the builder are different agents.
3. **One big move per round.** The judge picks the single change that would raise the weakest important score the most. Defect fixes can ride along, but they do not count as the round's change.
4. **Compare every round with the previous one.** The judge says better, same, or worse for each rubric dimension, using the new and the previous output side by side.
5. **Change course when stuck.** If two rounds in a row score the same or worse, the next big move must change the approach or concept, not tweak values.
6. **Ship each accepted round.** Republish or save after each round the judge scores as better, so the user can see progress. If a round scores worse, revert it and say so.
7. **Stop on the criteria.** Stop when every rubric dimension reaches the target, or when the user's round count is reached and the latest round is no worse than the one before. A count from the user, such as "at least 5", is a minimum, not a reason to stop while scores are still low.
8. **Report the trend.** Show the score per round, so the user can see what improved.

## Design loops

A design loop has two phases. It starts by exploring three directions, and only then refines one of them. Refining alone polishes whatever the first build happened to be, so it gets stuck on a mediocre concept.

### Phase 1: explore three directions

Run this phase at the start of every new design, every redesign, and any loop on a page that has no chosen direction in `design/DESIGN.md`. Skip it only when `DESIGN.md` already records a chosen direction, or when the user asks to keep the current look.

1. **You choose the three directions.** Choose them for this project; there is no fixed set. Base them on the business, the audience, the one action the page must drive, the content and assets that exist, and any constraints or feedback the user gave. Pick three that are genuinely different bets, not three colorways of one page:
   - One **safe direction**: the clearest, most trustworthy answer for this audience.
   - One **bold direction**: a stronger concept that would make the site memorable.
   - One **wildcard**: an unexpected angle that fits this specific business.
2. **Write each direction as one line** with a name, the concept, and why it fits. For example, for a plumber: "Trade manual: blueprint lines and technical type, says we know pipes"; "Friendly neighbour: warm colors, big phone number, plain talk"; "Night-shift hero: dark, high-contrast, built around 24/7 emergency calls". Do not ask the user to choose the directions; that is your job. Do say in your brief why you chose these three.
3. **Send the directions to `design-director`.** Each direction gets a spec and a mockup in `design/mockups/direction-A/`, `-B/`, and `-C/`, screenshotted at 375px and 1280px. Use sonnet or above; use opus when the project is high-stakes or the brief is ambiguous. You can run this in one of two ways:
   - **One agent** builds all three, scores them, and recommends one. This is the cheapest way, and the right one for small pages.
   - **Three agents in parallel**, one per direction, each only building and screenshotting its own mockup. Then one more `design-director` reads all six screenshots, scores them side by side, and recommends one. This is faster, and better when each mockup is large, but it costs roughly two extra agent start-ups. See `parallel-agents.md`.
4. **Let the user pick.** Show the three mockups to the user with the director's scores and recommendation, and ask which to take forward, or which parts of each to combine. Publish the mockups if the user cannot open local files. If the user is not there to answer, take the director's recommendation, say so, and carry on.
5. **Record the choice.** Have the director record the chosen direction in `design/DESIGN.md`, and the others under **Rejected directions** with the reason, including any of the user's own words.

The exploration round counts as round 1 of the user's round count.

### Phase 2: refine the chosen direction

Every round after that follows the loop rules above, with these roles:

- **Judge:** `design-director` on sonnet or above. It reads `design/DESIGN.md`, takes full-page screenshots at 375px and 1280px, scores them with its rubric, compares them with the previous round, builds a mockup of the round's big move, writes `design/brief-rev-N.md`, and updates `DESIGN.md`.
- **Builder:** `frontend-developer`. Give it the brief path and the mockup path, and tell it this is design work, so the brief's big move overrides the smallest-change rule and the mockup is the visual target. Ask for screenshots and brief coverage in its report.
- **Checker:** `qa-reviewer` for breakage only: overflow, console errors, contrast, keyboard, and fallbacks. It does not grade taste.

**Reuse the same three agents across rounds.** Spawn the judge, the builder, and the checker once. For the next round, send each its new brief with `SendMessage` instead of spawning a new agent. Each one already has its role file, its skills, and the project in context, so a round costs much less. Replace an agent with a fresh one, passing it the latest brief and the `DESIGN.md` path, after three rounds, after about 40 tool calls, or when its reports start missing earlier instructions. The judge and the builder stay separate agents.

If no `design-director` agent is installed, give the judge role to a `general-purpose` agent on sonnet that loads `anthropic-skills:impeccable` and `anthropic-skills:frontend-design`, and say so under **Missing**. Never let the builder or the QA agent be the design judge.

If no agent can see screenshots, because no headless browser is available, say so before the loop starts. A design loop without images is guessing.

**Pass on what the user says.** Whenever the user reacts to the design, such as "too corporate" or "love the brass", pass their exact words to the director in the next brief so it records them in `design/DESIGN.md`. Do not paraphrase them.


## Example

Improve a landing page over five rounds. Round 1 is the exploration: `design-director` on sonnet or opus mocks up three directions you chose for the project, and the user picks one. Rounds 2 to 5 refine it: `design-director` on sonnet critiques, mocks up, and writes the brief; `frontend-developer` on haiku or sonnet builds from the mockup; and `qa-reviewer` on haiku checks for breakage. All three are reused with `SendMessage` from round to round. Escalate the builder to sonnet if a round's brief coverage comes back incomplete.
