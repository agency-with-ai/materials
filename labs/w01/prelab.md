# Before Lab 1: get Claude Code working

Set up Claude Code to run Python on your laptop before the first lab. You can help each other, but complete the check on your own laptop.

## 1. Install Claude Code

Subscribe to Claude Pro before installing; the course reimburses the subscription at the end of the semester. If you would rather not use Claude, contact staff for an alternative setup.

If Claude Code is already installed, go to Step 2. Otherwise, use the command below for your system. The [official installation guide](https://code.claude.com/docs/en/quickstart) has more options.

On macOS, Linux, or WSL, open a terminal and run

```sh
curl -fsSL https://claude.ai/install.sh | bash
```

On Windows, open PowerShell and run

```powershell
irm https://claude.ai/install.ps1 | iex
```

## 2. Open the setup folder in Claude Code

[Download and unzip lab1-setup.zip](https://agencyai.mit.edu/lab1/lab1-setup.zip). Keep the resulting `lab1-setup` folder with your course work.

Open a new terminal in `lab1-setup`, the folder containing `check_environment.py`, and run

```sh
claude
```

Sign in if prompted. If you use Claude Code in an editor or the desktop app, open the setup folder there instead.

Paste this prompt into Claude.

```prompt
Check my local Python setup using check_environment.py.

1. Find an installed Python 3.10+ interpreter and report its path and version. If none is available, explain how to install it for my OS and stop.

2. Read and run check_environment.py with that interpreter. It uses only the standard library. Leave the checker unchanged. Resolve environment problems or report the exact error and what remains blocked.

3. After the check passes, read setup-result.txt and give me the exact command to repeat the check from this folder. Report any unresolved issue.
```

Read Claude's permission requests and ask it to explain any action you do not understand.

## 3. Check the result yourself

Open a second terminal in `lab1-setup` and run the command Claude gave you. It should print your Python version and executable path, followed by

```
PASS: Python can write files and launch a process that reads them.
```

Open `setup-result.txt` and confirm that it matches the terminal output. Keep this folder and your Claude conversation for lab, including the command you used. Use the same Python interpreter in class.

## If setup is blocked

Ask staff for help before lab. Send your operating system, the command that failed, the exact error or sign-in message, and what you tried. Leave out passwords and sign-in tokens. If you are still blocked when lab starts, show staff that information.
