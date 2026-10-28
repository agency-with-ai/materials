# Lab 5: giddy up
In Lecture 5, we met [Baby Anigans](https://github.com/agency-with-ai/baby-anigans). Baby Anigans wants to be helpful, but she can fail sometimes: e.g., she can read a grading policy page, find the text on a deadline auto extension, yet still leave the auto extension out of her answer.

In this lab, you'll start by reading her harness to understand what may have caused such failures. You and your Claude will then help Baby Anigans catch or prevent a failure like this. Finally, you'll swap out the LLM and the harness to explore how the two work in tandem for your agentic tasks.

Work with a partner in a Baby Anigans clone, but keep your own notes. Run commands from the root of your Baby Anigans clone. File paths below are relative to that folder. Save your code diff, model experiments, harness comparisons, and feature ideas.

## Step 1. Reading Baby Anigans

Follow the [guide](https://github.com/agency-with-ai/baby-anigans/blob/main/AGENTS.md#setup) and use `qwen3:1.7b` with Ollama.

1. **Read `agent.py` and draw the system.** Show how your question reaches the LLM, how tool calls reach Python, and how tool results return to the LLM. Include the checks that decide whether an answer is accepted.
2. **Create your own reference and question.** Create a short file containing some invented info, and write a question your reference file can answer.
3. **Build a command.** Read the example command for your setup in the repo's [running guide](https://github.com/agency-with-ai/baby-anigans/blob/main/AGENTS.md). Focus on how to set a flag to select an input file and to save a trace. Adapt the command to use your invented file and question and to save the run trace to `baseline.jsonl`.
4. **Run and read the trace through your diagram.** Run your command, then read `baseline.jsonl` alongside your diagram. Follow how requests, tool calls, and results move through the system. Check the answer against what you wrote in your file.
5. **Who did what?** Annotate your diagram to show which steps were human actions, which were LLM choices, and which were Python execution. Use the code and traces to support your labels.

Keep your diagram, commands, and traces for the before-and-after comparison.

## Step 2. Diagnose the failure and suggest a change

In [Lecture 5](https://slides.com/shensquared/agencyai-f26-lec05#/12), we compared two runs of Baby Anigans answering "Are labs due in session?", once with `qwen3:1.7b` and once with Claude Opus 5.5. Both run traces are in the repo, as `example/lab-deadline.jsonl` and `example/lab-deadline-claude-opus-5-5.jsonl`. The reference file they read was `example/input.md`, and the answer is in its **Labs** section.

1. **Compare the traces with the source.** On your Step 1 diagram, mark where the deadline auto extension reached each LLM and whether it survived into the answer. Point to the relevant tool result and request.
2. **Explain the failure.** Each partner explains one trace. What did Python check, and what did it leave to the LLM? Use `run_agent`, `FileTools`, or `Evidence` to support your explanation.
3. **Suggest one harness change.** Point to the relevant code and explain how your idea could help while keeping `qwen3:1.7b`. You'll implement and test it in Step 3.

💬 *Checkoff questions*

- Have your diagram, diagnosis, and initial change idea ready.
- **What explains the omitted deadline auto extension?** Use the source and saved traces to show what reached the LLM and what the answer left out.
- **What might you change, and why?** Point to the relevant code and explain how your idea addresses the failure. You do not need a finished implementation or test plan yet.



## Step 3. Implement and test a change

Start this step while you wait for staff. Possible changes include a read limit, the compaction prompt, or an answer check. See the repo's [testing guide](https://github.com/agency-with-ai/baby-anigans/blob/main/AGENTS.md#testing-a-harness-change) for examples and direct checks.

1. **Specify one change.** Use your Step 2 idea. Write two tests, one showing the intended effect and one showing a remaining limitation. Each partner predicts the before-and-after results independently; then you compare predictions. Record these before editing.
2. **Run before editing.** Save the original results for both tests and run the repo's tests. Choose cases that exercise your change, not just your invented question from Step 1.
3. **Implement and rerun.** Make only the proposed change. Repeat both tests and your Step 1 question with the same input files, LLM, and settings. Rerun the repo's tests. Save the diff and separately named before-and-after results.
4. **Explain what changed.** Show your partner the first observable effect in a request, tool result, or check. Compare with your predictions. What does the change enforce, what could be LLM variation, and what can still go wrong? If you revise, record why and repeat the comparison and tests.

## Step 4. Giddy up

### 4a. Swap in fancier models

What happens if Baby Anigans gets a stronger LLM? Follow the [Parley setup instructions](https://github.com/agency-with-ai/baby-anigans/blob/main/AGENTS.md#frontier-models-through-parley) to set `PARLEY_API_KEY` to your Parley API key, then choose a frontier model. Try questions and files of your choice. Be mindful of the Parley monthly credit limit.

Explore what Baby Anigans can do with the stronger LLM. What works well, and what surprises you? Save a trace of a run, especially if you found something interesting!

### 4b. Compare Pi with Claude Code

[Pi](https://github.com/earendil-works/pi) is a minimal, extensible agent harness that you can make your own. ([OpenClaw](https://github.com/openclaw/openclaw) was originally built on Pi.) Ask Claude Code to install Pi and configure it to use Opus 5.5 through Parley.

```prompt
Help me install the Pi coding agent and connect it to Parley. Pi repository: https://github.com/earendil-works/pi Parley endpoint (OpenAI-compatible): https://parley.api.mit.edu/v1 Claude model: claude-opus-5-5 Parley API key: read it from the PARLEY_API_KEY environment variable. Reference the variable in the configuration; do not print or copy the key. Show me how to start Pi interactively.
```
Choose a small coding task. Compare the experience with Claude Code and keep notes on what you tried and noticed. What are the features of Claude Code that you would want to duplicate? What feature might you hope to change?

For inspiration, you can browse [Pi’s package catalog](https://pi.dev/packages) to see extensions, skills, prompt templates, and themes people have built.

### Checkoff 2

💬 *Checkoff questions*

- **What did your change do in both tests, and what can it still not guarantee?** Show the before-and-after results from Step 3 for the intended effect and the remaining limitation.
- **What did you try with the hosted LLM?** Show one saved run from 4a and explain what you noticed.
- **How does Pi compare with Claude Code?** Describe what you tried and which features you would duplicate or change.
- **Where would you apply this lesson in your project?** Identify one instruction that needs enforcement or one piece of information that must survive a fresh session. Name the check you would use.
