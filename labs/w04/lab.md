# Lab 4: fork in the road

In this lab, you will use subagents and the command line to investigate two repositories that could help you build your Lab 3 project. You'll compare them against your spec, choose one, and make one small change.

Work with a partner, but keep your own notes and spec. Clone [Repos Map](https://github.com/agency-with-ai/repos-map) for your notes and results, and work from that folder. Unless stated otherwise, paths below are relative to `repos-map`. Use Opus 5.5 at medium effort throughout the lab.

## Step 1. Find repositories for your project

Start Claude and give it your project spec from Lab 3. Ask it to find repositories for a capability your project needs.

```prompt
My project spec is in <path to your spec>. I need <capability>, within these constraints: <constraints>. Suggest existing repositories that could provide it, and explain how each one fits my requirements and constraints.
```

Check that each suggested repository exists, then choose two candidates. Ask Claude to clone them into `repos/first` and `repos/second`.

## Step 2. Investigate and compare

### 2a. Investigate with subagents

Read `.claude/agents/repo-reader.md`. This file defines the subagent's model, tools, and system prompt.

> **Tip**
> You can use this file as a template for custom subagents in your other Claude Code projects. Read more at the [subagent guide](https://code.claude.com/docs/en/sub-agents#write-subagent-files).

Exit Claude, then enter your first candidate's repository and start a fresh session.

```sh
cd repos/first
# The line below gives Claude access to repos-map, including the repo-reader subagent.
claude --add-dir ../..
```

Ask Claude for two independent readings of the code.

> **Tip**
> When delegating to a fresh agent, include the requirement, constraints, and paths it needs. Write the task so someone who missed your earlier conversation could carry it out.

```prompt
Use the repo-reader subagent twice, independently. Give each this question about the current repository. Could this repository satisfy <requirement> from my project spec at <absolute path to your spec>? Trace one relevant example through the code, citing files. Note dependencies and changes needed to meet the requirement. Save their answers separately in ../../notes/first-subagents.md.
```

If Claude starts the Explore subagent instead of our defined `repo-reader`, it's most likely that you omitted `--add-dir ../..` from the command above when starting Claude. Retry.

### 2b. Compare with command-line sessions

Once both answers are saved, exit Claude and return to `repos-map`. Read `compare-agents.sh`. Its `run_agent` function gives each session the same tools as `repo-reader`. Run it with the same question and model.

> **Tip**
> Claude wrote this script, which was tested on a throwaway project. Use the same approach to save time on repetitive tasks. Scripts can overwrite or delete files, so it's crucial to understand each command before running them. Use `man <command>` for available command manuals and `man bash` for Bash syntax.

On Windows, Bash and Claude setup may have [gotchas](https://code.claude.com/docs/en/setup#set-up-on-windows). Ask staff for help if you run into a command error.

```sh
bash compare-agents.sh repos/first "Could this repository satisfy <requirement> from my project spec at <absolute path to your spec>? Trace one relevant example through the code, citing files. Note dependencies and changes needed to meet the requirement."
```

The script runs two fresh sessions in parallel and saves the question, answers, and measurements in `results/`. Compare the subagent reports with the command-line results for answers, context, time, and estimated cost. You may ask Claude for help, but check one claim against the code yourself. Record your comparison and evidence in `notes/`.

### 2c. Investigate the second candidate and choose

Open Claude in `repos-map`. Ask it to use `repo-reader` once to investigate `repos/second`, giving the subagent the same question and spec path. Save its report in `notes/second.md`.

Compare the two candidates against your spec and check the cited code. Choose the candidate you want to build on. If neither fits, narrow the capability and investigate again.

Review your notes and results, then commit them.

💬 *Checkoff questions*\
Prepare these answers as you work. The lab tells you when to ask staff for a checkoff.

- **Which repository did you choose, and what shows that it fits?** Point to the code you inspected.
- **What gap separates it from your project spec?**

Ask staff for Checkoff 1 with your notes and both investigations ready. Together you will agree on one small change and how to check it.

## Step 3. Bridge one gap to your project

### 3a. Set up the repository
Fork the chosen repository for your project on GitHub. Ask Claude to set up your local copy to push changes to your fork. Follow the repository's setup instructions and run a demo or sample command related to your planned change, so you know how the code behaves now.

### 3b. Plan the change

Trace the relevant code and plan the change. Name a test input and the result you expect. Choose an existing behavior to check as well, so you can tell whether your change breaks it. Have your partner read the plan.

### 3c. Make and check the change

Use Claude to implement the change you agreed on at Checkoff 1.

Read the diff, then check both the new behavior and the existing behavior from your plan. When a result surprises you, investigate it before asking Claude for a fix. Save the commands and outputs for your checkoff.

Commit the code change inside the chosen repository. Record the fork URL and commit in `notes/`.

### 3d. Explain it without Claude

Close Claude, and explain the change and your evidence to your partner. Then update your project spec with your decision about using the repository, the work that remains, and your open questions.

💬

- **What gap did you bridge between the repository and your project?** Show the relevant requirement and the change.
- **Does the change work, and does the existing behavior still work?** Show the checks and results.
- **What did the agents and the command line help you learn?** Compare answers, context, time, and cost. Explain what you checked yourself.
- **What comes next for the project?** Show the updated spec.

Ask staff for Checkoff 2. Bring your spec, the diff, and your saved commands and outputs.

## Optional practice. Compare agents on another repository

Choose one of these repositories and clone it into `repos/warmup`.

[Browser Use](https://github.com/browser-use/browser-use) | [Qwen Audio Agent](https://github.com/QwenAudio/qwen-audio-agent) | [Paperclip](https://github.com/paperclipai/paperclip) | [Pi](https://github.com/earendil-works/pi)

Repeat 2a and 2b, using `repos/warmup` in place of `repos/first`. Use the question below for both the subagents and the script, and save this exercise's notes under `notes/warmup/`.

```prompt
What does this repository do? Trace one concrete example from input to output, citing files.
```

## Look ahead to Lecture 5

Lecture 5 opens the harness that ran your subagents. It covers what loads before you type, how permissions and hooks enforce rules, and how to keep a record of what an agent changed.
