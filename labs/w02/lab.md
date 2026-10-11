# Lab 2: connect four

Find a classmate to form a team. In this lab, you practice the four-question reading recipe from Lecture 2 on a set of papers.

- **Motivation.** Why should this problem be solved?
- **Solution.** How did the authors solve the problem, and how do they know the method is any good?
- **Old idea.** How did people before them attempt to solve this problem?
- **Delta.** What did the authors do differently?

Everything you need is in [lab2.zip](https://agencyai.mit.edu/lab2/lab2.zip); take a quick look after your download. Keep your own copy of `student-note-template.md`, separate from your partner's. Brief notes are fine, as long as you keep the excerpts that support them. The lab has two checkoffs. During each, you may use your notes, the papers, and your saved conversations, but not Claude.

## Step 1. Skim the focal paper

With your partner, choose a pair of papers below. Each pair includes a **focal paper**, which proposes the method your team is considering, and an earlier **predecessor** paper that the focal paper builds on.

<div data-tab-group="paper-pair">

[Paper pairs](reading-pairs.md)

</div>

**Without Claude,** skim the focal paper's abstract, introduction, figures, and conclusion. Keep the reading question in mind throughout; after reading your pair of papers, you will answer that question in Step 3.

In your notes, draft your initial impression of the four questions. It's completely fine if you don't have immediate answers. If you're confused or stuck, write down your questions and where you got lost (e.g., section number, equation number). This list of specific questions makes a great seed for your next round of reading.

## Step 2. Ask Claude, then check one claim

Each of you starts a separate Claude conversation. Set `/model` to Opus 5.5 and `/effort` to medium. Opus 5.5 is new, so run `claude update` if you do not see it.

### 2.1 Ask Claude
Give Claude the focal paper PDF, your Step 1 explanation, and your questions. Write a prompt asking it to challenge your explanation or explain where you got stuck. If you are not sure where to start, adapt the following, by replacing each `<...>` with your own text.

```prompt
Here is my explanation of this paper and the parts I got lost on: <your Step 1 notes>. Challenge my explanation of the problem and the method, and explain the parts I got lost on. Point to the sections, equations, or figures that support your answer.
```

With your partner, briefly compare what Claude told each of you.

### 2.2 Check one claim

Choose one claim from Claude's answer and open the part of the paper it cites. If Claude gives no location, or the location does not exist, find the relevant part yourself. Decide whether the paper supports Claude's claim, contradicts it, or leaves it unresolved.

In your notes, record the claim, where you checked, what you found there, and your verdict. If you find nothing relevant, say where you looked and mark the claim unresolved.

<a id="lab-checkoff-1"></a>

**Ask staff for Checkoff 1.** Show your initial explanation, the questions you wrote down, and your claim check. Be ready for questions about the paper itself.

## Step 3. Read both papers and assess Claude's answers

### 3.1 Write your own answers

**Without Claude,** read your pair of papers closely to answer the four questions and your reading question below. Use what staff asked you at Checkoff 1 to decide which parts to read most closely. Answer the four questions again, from the papers rather than from memory, and leave your Step 1 answers as they are so you can compare them in 3.3. Include source locations and excerpts beside your answers.

💬 *Checkoff questions*\
Prepare these answers as you work. The lab tells you when to ask staff for a checkoff.

- **Motivation. Why should this problem be solved?**
- **Solution. How did the authors solve the problem, and how do they know the method is any good?**
- **Old idea. How did people before them attempt to solve this problem?** Start with the predecessor, and name any other earlier approach the focal paper discusses.
- **Delta. What did the authors do differently?** What are the consequences of each difference, good or bad?
- **Reading question. Answer the question from your chosen pair.**

Write your answers in your notes.

### 3.2 Ask Claude to compare the papers

In the same conversation from Step 2, turn to the predecessor paper. Adapt this prompt by replacing each `<...>` with your own text.

```prompt
Answer my reading question, <your reading question>, by comparing <focal paper title> with <predecessor title>. Also explain how earlier work solved the problem, what the focal paper does differently, and what the evidence leaves unsettled. Point to the sections, equations, or figures that support your answer.
```

Read Claude's response and answer these questions in your notes.

💬

- **How does Claude's answer to your reading question compare with your own answer in 3.1?**
- **What, if anything, can you still not answer?** What could you do now to close that gap, such as rereading a section, working through an equation, or trying a small example?

If a question remains unresolved, explain what you checked, where you got stuck, and what would help.

### 3.3 Find the gap in your reading

**Without Claude,** compare your Step 1 answers with your 3.1 answers and with Claude's answer in 3.2.

💬

- **Which of the four questions did your Step 1 skim get most wrong, or leave empty?** Point to the part of the paper you had to read to fix it.
- **What will you do differently when you read the next paper?** Base one change on the part of the paper you pointed to above.

## Step 4. Skim a new paper with the recipe

**Without Claude,** skim your pair's later paper, which builds on both, the way you skimmed the focal paper in Step 1. Make the change you named in 3.3.

- Normalization paper pair: [Group Normalization, arXiv v3](https://arxiv.org/abs/1803.08494v3) (2018)
- Image editing paper pair: [MagicBrush, arXiv v3](https://arxiv.org/abs/2306.10012v3) (2023)

💬

- **What are the Motivation, Solution, Old idea, and Delta of the later paper?**
- **Which of the four questions came out differently this time?** Compare your Step 4 answers with your Step 1 answers for the focal paper. Say how much of the difference your change can account for, and what else could explain it. If nothing came out differently, say that.

<a id="lab-checkoff-2"></a>

**Ask staff for Checkoff 2.** Be ready to explain your answers in Steps 3 and 4, including the change you tried.

## Reflect and share

The questions below help us learn from each other's usage. Your answers also give you material for the AI use examples in your [portfolio](https://agencyai.mit.edu/syllabus/#grading). Start the reflection while you wait for Checkoff 2.

- **How did Claude help you understand the papers, compared with how your partner helped?** Give one example of each from your conversation and your discussions.
- **About how long did the lab take?** Label the total as measured or estimated. What evidence, if any, supports a claim that Claude saved you time?

Everyone is encouraged to share. Post your exported conversation in the **Labs** category of the [course forum](https://agencyai.mit.edu/forum/). Add two sentences drawn from your first answer above, naming what Claude helped you check and what still required your own reading. You can post anonymously on the forum, and save your post to submit again through Canvas at the end of the semester for grading.

