# Lab 7: scrappy scrape

Last week, we had our midterm checkpoint. As it turns out, the country is also having its midterm… election! In this lab, you and your partner will explore an election question through data.

## Step 1. What will you predict, and what data do you need?

Start by brainstorming a few yes/no election questions and the data each question would need. To predict a continuous outcome, such as a vote margin, turn it into yes/no, for example winning by more than five points. A past election with known results works too. If you need some inspiration, here are some ideas:

| Question | Possible data |
|---|---|
| Will a district change parties? | Previous margins, incumbency, district characteristics |
| Will a race finish within five percentage points? | Polling gaps, fundraising, news coverage |
| Will a ballot measure pass? | Measure wording, topic, polling |
| Will the polling leader win? | Poll margins, sample sizes, field dates |
| Will an early lead hold? | Timestamped partial returns, locations still reporting |

Choose one question and fill in a data-needs table with the following attributes. Do this without the help of Claude.

- **Outcome.** What yes/no outcome are you predicting? When is your prediction cutoff (e.g., early voting vs. general election)?
- **Training data.** What does each example represent? What are the features?
- **Population.** Which races, places, or elections should your predictions apply to?
- **Expectation.** Which feature do you expect to help most, and why?

With your data-needs table ready, ask staff for checkoff.

💬 *Checkoff questions*

- **What are you predicting, and what does each training example represent?**
- **Which features would be available at your prediction cutoff, and which do you expect to help most?**

## Step 2. Get scrappy (after all, [we are young, scrappy, and hungry!](https://www.youtube.com/watch?v=lZ4UmlFNdSI))

Feel free to work with Claude from this point on; except when otherwise noted. 

1. **Find your data.** Find two or three candidate sources. Before inspecting their records or documentation, predict which fits best. Then compare their coverage, label definitions, and reuse terms against your data-needs table. Did your choice change? Use past elections for training and evaluation if current outcomes are unresolved or you need more examples. If your question needs historical snapshots you cannot find, revise the question to one that the data can support.
2. **Scrape at least one source.** Collect features from web pages, such as past results tables, ballot summaries, or dated news headlines. Save the raw pages, URLs, retrieval times, and extraction code. Check publication and update dates against your cutoff. Keep outcome labels separate from features, and mark unresolved outcomes as unknown.
3. **Check your data.** Trace five records back to their sources without Claude and note any mismatches. Check the dataset for duplicates, inconsistent labels, and features unavailable at your cutoff. Save your dataset, source documentation, and findings for Lab 8.
4. **Train a logistic classifier** Train and score only records with known outcomes; save predictions for unresolved cases separately. Choose a held-out set that matches your task, such as a later election. Keep duplicates and repeated observations of the same case in one split. Fit preprocessing only on training data. Save the split, predictions, and command that reproduces the run.
5. **Compare with a simple rule.** For example, for district flips, the rule could predict no flip everywhere; for ballot measures, it could always predict the more common training-set outcome. Evaluate both models on the same held-out examples using the same metric. Record the class counts and a confusion matrix alongside each score.

Investigate the checkoff questions below and ask staff for checkoff when you're ready.

💬 *Checkoff questions*

- **How does your classifier perform compared with the simple rule?**
- **Did the scraped features help?** If you have other features, compare the classifier with and without the scraped ones on the same split.
- **Could your model face distribution shift?** Revisit covariate shift, label shift, and concept shift on [this Lecture 7 slide](https://slides.com/shensquared/agencyai-fa26-lec07#/17/0/1). Which might affect predictions across places or elections? State what changes, what you assume stays fixed, and what evidence you would check. Name one population, label, or time period your data does not cover. Would you collect more data or narrow your question?
- **What surprised you?** Revisit your expectations from Step 1. Inspect feature weights and individual predictions, including mistakes or suspicious successes. For known outcomes, check whether later reporting or a scraped result gave away the answer. Explain what the evidence supports and what remains unknown.

## A thought for your project

As you return to your project, what similar data problem might affect it, and how would you check for it? Keep this question in mind; no checkoff is required.
