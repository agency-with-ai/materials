# Lab 1: close enough?

Follow the [setup](prelab.md). Have your Claude Code session and `setup-result.txt` ready. Then download and unzip [lab1.zip](https://agencyai.mit.edu/lab1/lab1.zip). All files we refer to below can be found in this `lab1` folder.
Find a partner and work in pairs, keeping your own notes in `student-note-template.md`. Brief answers and commands are enough. Staff may ask you to defend your choices and evidence, so keep track of your thinking as you go.

## Step 1. Understand and plan

You work at FriendlyNeighbor Motors. Your boss wants you to build a k-nearest neighbors (kNN) classifier that predicts whether a car's gas use per mile is at or above a fixed threshold, using the car's weight and the number of cylinders in its engine. There are 392 car records from 1970 to 1982 in `code/cars.tsv`. We give you a starter script, `code/baseline.py`, with two missing functions. `code/README.md` specifies what those functions must do.

### 1.1 Check your setup

Work in the `lab1` folder throughout this lab unless told otherwise. Use the Python interpreter your pre-lab found, and run

```sh
python3 check_environment.py
```

Raise your hand and show staff the output. Do the same whenever you are blocked during this lab.

### 1.2 Predict and plan

Do this without Claude. Inspect the files in the folder, read the specification, and record your own answers to these checkoff questions:

💬 *Checkoff questions*\
Prepare these answers as you work. The lab tells you when to ask staff for a checkoff.

- **How long do you think this lab would take with Claude? Without Claude?**
- **How likely is Claude's first implementation to be correct?** Name what you expect it to get wrong, if anything. Would you expect the same mistakes if you did the lab yourself?
- **How would you decide whether the implementation is correct?** Describe one check you would run and what result would count as passing it.

Then compare your answers with your partner, discuss what to do yourselves and what to delegate to Claude, and say why.

## Step 2. Build and check

You are free to use Claude from this point on. If you do, select Opus 5 at medium effort (`/model` and `/effort`).

Implement the two missing functions. Run your own check if you have one, then run the checker we supplied.

```sh
python3 code/check_setup.py
```

Resolve any failures before going on. Your own run is saved in `code/runs/setup/predictions.tsv`. If you used Claude here, save one relevant exchange with `/export` and explain how you checked its result.

> **Tip**
> In your other coding projects, keep a check's input, expected result, and command together. You can rerun the check after later edits to see whether that behavior still works.

## Step 3. Compare with FastFurious

Days after you presented your classifier to your boss, you learned that your company FriendlyNeighbor is merging with FastFurious Auto. Someone on their team looked at the same problem and already shipped a classifier. Their predictions on the same cars are in `code/provided-results/fastfurious-predictions.tsv`. Take a look, then answer these:

💬 <a id="lab-checkoff-1"></a>

- **Based on these predictions alone, does their classifier meet the specification your boss set?** What evidence supports your conclusion?
- **After the merger, could the combined team use either program in place of the other?** If your answer depends on something you do not know yet, write the question you would ask your boss or their team.
- **If your implementation differs from theirs, what's the difference? Are there situations where the difference might matter?**

Now check how long it took you to get here and compare that with your prediction from Step 1. Look at your implementation too, and see whether anything fell outside what you predicted. Record what is still unresolved and any changes of approach along the way.

Ask staff for Checkoff 1, and start Step 4 while you wait. Be ready to explain your work in Steps 1 to 3 from your own notes and files, without Claude help.


## Step 4. New cars arrived! Predict them!

Your boss sends `code/new-cars.tsv` and asks you to use the classifier you built in Step 2 for predictions on these new cars. With your partner, run your classifier, save the results, and look at the new predictions.

```sh
python3 code/baseline.py --predict-data code/new-cars.tsv --out code/runs/new-cars
```

Show another lab pair your predictions and your initial conclusions. Compare your evidence, then record your answers below.

💬 <a id="lab-checkoff-2"></a>

- **How do the other pair's conclusions compare with yours?**
- **What did you change or keep as a result?**
- **How does your classifier perform?** Support your answer with evidence.
- **Would you send these to your boss as trustworthy answers to their new task?** Support your answer with something you checked in the files or the results. Say what you would do next and what is still unresolved.

Ask staff for Checkoff 2. Use your notes and saved predictions to defend your answers and respond to one follow-up. Keep all your files from this lab for your portfolio.

## Look ahead to Lecture 2

Start this while you wait for staff.

Your boss now understands kNN. "So it copies nearby cars' labels? How naive!" They want the latest and hottest methods. They want transformers! You and your partner refresh on the [6.390 transformer slides](https://slides.com/shensquared/introml-sp26-lec09/fullscreen) for the basics, and start to read more for fancier methods. You come across [Efficient Attention (2021)](https://arxiv.org/pdf/1812.01243v10).

**After your first look, how convinced are you by the proposed method? Why?**

Keep these questions in mind. We'll discuss two example AI readings, from [ChatGPT](https://chatgpt.com/share/6aa301e3-3c94-83ea-8a43-0a8a1b45d98a) and [Claude](https://claude.ai/share/f434434e-130f-4953-b0b6-b9269067ba0a) in lecture 2. See you then!
