# Lab 6: checkpoint

This is our midterm checkpoint lab. (Can you believe it? It's already midterm.) Today, you'll look back at your work and start shaping your final submission of three `SKILL.md` files and a project summary, with help from staff.

Use your project files and notes to brainstorm which recurring workflows could become skills. Then talk with staff about your ideas, how your project is going, and what belongs in your project summary. Work on your own, except for a short swap with a partner in Step 2. Do this lab without Claude, with one exception in Step 1. Keep everything you write today as drafts to build your final submission.

## Step 1. Pick a workflow to turn into a skill

A good skill starts as something you keep having to do, whether you run a script, do it by hand, or ask Claude for it again. It has come up at least twice, and you know what a good result looks like. Typical examples include reading a repository before changing it, comparing two traces, and preparing a figure.

1. **List your repeats.** Look back over your work so far. For each workflow you've run at least twice, write down
   - what you were trying to get done,
   - anything that went wrong or had to be corrected, if something did, and
   - how you check the result.

> **Tip**
> If your memory fails you, ask Claude. It can look through your past Claude Code sessions for tasks you asked for more than once. Keep only the ones you recognize.

```prompt
Look through my past Claude Code sessions in ~/.claude/projects/ and list the tasks I asked for more than once. For each task, quote one of my requests and give the dates of the sessions. Don't suggest skills or rewrite anything.
```

2. **Read a good skill.** Open [`verification-before-completion`](https://github.com/obra/superpowers/blob/3be5aad3dd2400ef23b15680969f4bcd3b6d7b8b/skills/verification-before-completion/SKILL.md). This skill asks Claude to check a claim and read the output before saying anything works. Note where it does each of these three things, and anything it misses.
   - The description says what the skill does, when to use it, and what it won't do.
   - The body holds the author's own decisions and checks.
   - Each step ends in a result someone can check, and the skill says when to stop or ask.

   Claude Code reads only a skill's `name` and `description` when a session starts, and loads the rest when a request matches. So the description decides whether your skill auto-loads or gets misused. Read the [Claude Code skills guide](https://code.claude.com/docs/en/skills) and [skill-authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) for more details.

3. **Choose a candidate and write its description.** Pick the workflow where your own decisions and checks matter most, or would save you the most tedious work. Give it a lowercase, hyphenated name such as `comparing-traces`, then write its description in two or three sentences. You may leave the body for after the checkoff.

💬 *Checkoff questions*

- **Which workflows keep coming up?** Walk staff through your list. They'll suggest which workflow to build first, and why.
- **What makes `verification-before-completion` a good skill, and what does it miss?** Point to its description and to one step that ends in a check.
- **When should your skill load, and what won't it do?** Read your description aloud with Claude closed.

## Step 2. Draft your project summary

Start this step while you wait for staff.

Your final project submission will include a one-page summary and your project repository. Download the template, [summary.md](summary.md), and save it in your repository. Today we start drafting it from your Lab 3 spec.

- Your spec's goal becomes your Project scope.
- Its acceptance checks become your Evidence.
- Its open questions go under Limits or What's next.

1. **Fill in all six headings** for your own project in `summary.md`.
2. **Swap setup notes with a partner.** If your repository has no README or AGENTS.md yet, write the setup steps there first. Ask your partner to read them and your Evidence command, and point to the first step they couldn't do without asking you. Fix that step. If your project can't be shared, skip the swap and tell staff at the checkoff.

The following are two examples. The first is one small finished result, and the second is a semester-sized project halfway through. Both examples leave out Provenance to save space, and their numbers are made up for illustration. Your progress may vary, but aim for their level of detail, and keep Provenance in your own summary.

<details>
<summary>Example: one small result, Baby Anigans read limit</summary>

**Project scope.** Students ask Baby Anigans, the course's small agent, about course policy, and its answers sometimes leave out a fact the policy file states, such as the deadline auto extension. The goal is answers that keep every relevant fact while still running on a small local LLM. A hosted LLM already keeps the fact, as the Lab 5 Claude trace shows, so the question is whether a harness change can close the gap without a bigger model.

**Claim.** Raising `MAX_READ` in `FileTools` from 20 to 60 lines keeps the deadline auto extension in Baby Anigans' answer under `qwen3:1.7b`, where the unchanged harness drops it.

**Evidence.** Test question "Are labs due in session?" against `example/input.md`. The metric is whether the answer names the auto extension. Before, in `before-1.jsonl` to `before-3.jsonl`, the answer omits it in 3 of 3 runs. After, in `after-1.jsonl` to `after-3.jsonl`, it names it in 3 of 3. The before traces show the auto extension sits past line 20 of the file, beyond the first read. The comparison is the unchanged harness on the same question, file, and LLM. The repository's tests pass before and after. Reproduce with `uv run agent.py "Are labs due in session?" --file example/input.md --trace after-1.jsonl`.

**Limits.** One question and one file. Three runs on a small LLM do not rule out variation. The limit changes how much reaches the LLM per call, not what the LLM does with it. In my second test, a section that starts past line 60 still loses its last paragraph in the answer.

**What's next.** Whether a larger read limit is the right fix, or whether the harness should instead check the answer against the file. The run that settles it is my second test under both versions.

</details>

<details>
<summary>Example: a semester project, Write like Feynman</summary>

**Project scope.** Can a model write a short technical explanation that reads like Feynman's? It is for students and teachers who want an idea explained to a particular audience. A plain request to write like a famous author is the obvious way, and my reading map points to example passages as a better one. Since the spec, I narrowed the scope to explanations of 200 words or fewer.

**Claim.** Readers who haven't seen the original passages mistake drafts built from Feynman's own writing for his work more often than drafts from a plain "write like Feynman" request.

**Evidence.** Twelve reserved passages, each with a factual brief. The metric is how often readers pick the generated draft as the original. The comparison is a plain "write like Feynman" request with the same model, briefs, and word limits. So far only the one-day version has run. On three passages I judged the example-passage draft closer to the original in 3 of 3 pairs, and all six drafts passed the fact and copying checks. The reader study, 20 readers voting on 12 pairs, runs next. Reproduce the one-day result with `python compare.py --passages reserved/day1 --method examples --judge self`.

**Limits.** Three passages, judged by me, and I knew which draft was which. The model may have memorized some passages, even reserved ones. The reader study will measure resemblance to Feynman, not whether an explanation is correct or useful.

**What's next.** How many readers are enough. A pilot with 5 readers on 4 pairs shows how much the votes vary before I recruit 20.

</details>

💬 *Checkoff questions*\
Ask staff for Checkoff 2 with `summary.md` open and your repository at the revision it describes.

- **What's your claim, and what supports it so far?** Point to a run and the command that reproduces it, or to the first run you'll do.
- **What can't your evidence rule out yet?**
- **Where did your partner get stuck?** Show the step and your fix.
- **Which parts did Claude write, and how did you check them?** Work you can't justify earns no credit, however polished.

