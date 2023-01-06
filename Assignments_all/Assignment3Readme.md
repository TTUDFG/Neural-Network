# 1 Overview

In this third programming assignment for CAP6615, you will work in groups of six
students per group (as in Programming Assignments 1 and 2), while designing, coding,
training, and testing a Recurrent Neural Network (RNN) for time series prediction. You
will choose one dataset (time series) of financial data from a site whose URL will be
provided. Then you wlll configure, train, and use the RNN to identify and predict "next
value(s)" in the time series, given a generic pattern to search for.

The purpose of this assignment is to have fun developing an RNN with Python and
its Pytorch, TensorFlow, and/or SciKit libraries, also to learn how to process financial
data with RNNs, then properly test and document your RNN's performance with noisy
data (real stuff!!). Then you can optimize your RNN for best performance before
generating and reporting your final results.

# 2 Groups

Coding, testing, and documentation will be performed by **the same groups of six (6)
students you have used thus far.** You may exchangeinformation between groups, but
programs and reports are not to be plagiarized between groups.

**>>> PLEASE USE THE SAME GROUP AS PROGRAMMING ASSIGNMENTS 1 & 2 -
AND KEEP THIS GROUP THROUGHOUT THE SEMESTER <<<**

# 3 Duration of Assignment

**Assignment-Release-Date = Thu 17 February 2022**

## Assignment-DUE-Date = Fri 18 March 2022.

**Alloted Time = Three (3) Weeks** (excluding Spring Break)

# 4 Evaluation 30 points max

**>>> Projects will be evaluated by group -- each group member will be assigned
the score for his or her group project <<<**

**Scoring Rubric, per Step or Substep** (on a 3-pointscale -- see Section 5, below)

**Score = 0** : Nothing done, no answer & no results


```
Score = 1 or 2 pts : Some result, ranges from not-very-good to
setup-is-ok-but-results-are-incorrect
```
```
Score = 3 pts : Correct result, clear explanation
```
# 5 Stepwise Directions (with point allocations per

# step)

```
Step 1 - (3 pts) Dataset Assembly
```
```
Select S&P500 (Symbol = SPX) Dataset from the following URL:
```
```
https://www.nasdaq.com/market-activity/index/spx/historical
```
**Links to an external site.**

```
You will have to subsample the above-referenced data if you want weekly or monthly
resolution.
```
```
Next, choose an S&P-related index, such as the Schiller P/E ratio, from this site:
```
```
https://www.multpl.com/sitemap
```
**Links to an external site.**

```
-or- https://finance.yahoo.com/quote/%5EGSPC/history/
```
**Links to an external site.**

```
.Study this graph of the Schiller P/E ratio, to determine when stocks on the S&P500 are
under- or over-valued:
```
```
https://www.longtermtrends.net/sp500-price-earnings-shiller-pe-ratio/
```
```
then correlate the above graph (mentally) with the S&P500 -- or you can overlay the
Schiller PE graph (above URL) onto the S&P500 graph (topmost URL in this step). The
purpose of this is to determine how well the Schiller P/E predicts market bottoms or
sell-offs.
```
```
● TO-DOCUMENT: Make an overlay of the Schiller P/E for a longer time
interval, for example, from 1 Jan 1960 to 31 Dec 2021, onto the S&P
```

```
for the same period. (as noted above, you may have to subsample the S&P
(SPX) data.
```
**Why are we doing this?** It is important to build yourskills in assembling and
correlating data sets. These are useful skills for business, industry, government (albeit
less so), and academia.

**Step 2 - (6 pts) Design and develop a recurrent neural network (RNN)** in Python,
using libraries such as PyTorch (and, if necessary, Tensor Flow). Your RNN **_must_**
predict the next value in a subset of your training data (S&P500, from 1960 to present
date - in the Extra Credit portion of this assignment, this would be informed by Schiller
P/E), For example, if your subset has monthly resolution and goes from 31 Jan 1972 to
31 Dec 2006, then your next (RNN-predicted) data point would be for 31 January 2007
(whatever its value might be). As another example, if your data resolution is weekly,
then your sampling window would be 26 data samples (approx. six months) and you
would predict the next week, then the one after that, and so forth out to four sampling
intervals or weeks).

```
● TO-DOCUMENT: Make a diagram of your RNN architecture,including input,
hidden, and output layers as well as weights between each two successive
layers.
```
**Why are we doing this?** It is important to learn howto build RNNs (for example, for
time series analysis). Also, we will be using this RNN as a basis for further
development of feature-based stock market price predictors in Programming
Assignment 4..

**Step 3 - (6 pts) Train** your RNN on a Training Set(that you select from the S&P
data, from Step 1, above) then test to ensure it functions correctly when predicting the
next one, two, three, and four trading data values (close price) before you go on to Step

4. For example, if you are sampling monthly and your training set ends on 28 February
2007, then you will want to predict S&P price for 31 March, 30 April, 31 May, and 30
June 2007.

```
● TO-DOCUMENT: You get credit for showing your preliminarytest results and
discussing the number of training epochs (iterations through whatever training
algorithm you decide to use), and intelligently discussing why this is so ...
```
**Why are we doing this?** It is important to learn howto train RNNs (for example, for
time series analysis). Also, we will be using this RNN and some of the things we learn
in this training step, as a basis for further development of feature-based stock market
price predictors in Programming Assignment 4. _Itis very important that you get this and
the previous steps right, as you will be extending this prediction mechanism in the next_


_programming assignment - and it will be a core part of your approach to feature-based
time series prediction._

**Step 4 - (6 pts) Test** your RNN accuracy in predictingthe next one, two, three, and four
datapoints in the dataset from 1 Jan 1980 through the present day, using a sliding
sampling window of width 180 days (six months).

```
● How will you test your RNN? Accuracy will be computedin terms of error
defined as the following fraction:
```
**prediction_error := (predicted_price - actual_price) / actual_price**

Y

**Then compute and entabulate the statistics of your** **_prediction_error_** **metric** for
your Training and Test Sets -- using mean, standard deviation, skewness, and kurtosis
measures (which you should know from basic statistics). There are many C or Python
library routines to compute these metrics.

_Hint_ : You will want to develop a Linus or Windowsscriptto do this, as you will be using
this many times in this and the next programming assignment.

```
● TO-DOCUMENT: Please graph prediction_error (definedabove) as a
function of timestamp (e.g., DD/MM/YYYY) for all datain your Training and
Test Sets. Produce two graphs - one graph for the Training Set results and
one graph for the Test Set ( Hint : There might be someoverlap between the
two graphs, depending on how you select your training and test sets). Then
display in your report the statistics of prediction error (Mean, Std-dev,
Skewness, Kurtosis) as described above.
```
**Why are we doing this?** It is important for you, asa scientist and/or engineer, to
communicate your results graphically, and to provide a table (usually, of statistical
measures) that summarizes your results numerically. This is an essential part of
scientific communication - an important tool for the technical professional.

**Step 5 - (3 pts) Optimize your RNN performance** toyield maximum achievable
accuracy (e.g., minimize _predicted_error_ ) over theentire Training Set and Test Set. You
will want to divide your Training Set into two parts, one of which will be the Validation
Set that you use to tune your RNN on the S&P data. Repeat Step 4 graphing operation
to show this optimized result.

```
● TO-DOCUMENT: Display your graphs and statistics tablesfor this new set of
performance results. Discuss why you got these results, why your RNN
performed the way it did (in terms of prediction_error), and how it could be
improved.
```

**Why are we doing this?** In a sense, most R&D projects are never finished ... there is
always room for improvement. And it is very important for you to develop the ability to
fine-tune your computer codes to produce progressively better performance. This is
part of the responsibilities of a scientist and engineer.

**Step 6 - (3 pts) Investigate the effect of Input Noise and Uncertainty**

```
Step 6a) Corrupt your Test Set (from 1), above)by adding noise
○ Noise will be Gaussian-distributed with 20 percentcross-section
(e.g., one noise corrupted values out of each 5 values in your
sampling window) and have zero mean, with standard deviation of
(0.001, 0.002, 0.003, 0.005, 0.01, 0.02, 0.03, 0.05, and 0.1) --
assuming that the source dataset (from 1, above) has normalized
value range equal to the real-valued interval [0,1].
○ Algorithm : (1) generate random noise with std-devas described
above (similar to what you did in Programming Assignments 1 and
2), (2) add noise values to input image every 10 pixels or so
(chosen randomly), (3) renormalize the noise-corrupted image so
all of its pixels have values in the interval
○ [0,1]⊂R
○.
```
```
Step 6b) Repeat Tests in Step 4), above, with noise-corruptedTest Set
```
● **TO-DOCUMENT:** Gather the performance results intoa table of
_predicted_error_ versus _timestamp_ , with one row foreach value of the
standard deviation, like this:
**Table of Prediction Error for Recurrent Neural Net Applied to
S&P500 data with Noisy Input**

**Number of Inputs = <n> per sampling window
Number of Layers = <L>
Number of Outputs = <can be one to four> <== THIS MEANS THE
NUMBER OF VALUES PREDICTED**

**-- Gaussian Noise Standard Deviation (10 percent
cross-section) --**

**Time stdev - 0 stdev = 0.001 stdev = 0. ...
stdev = 0.**


**Stamp Fh Ffa Fh Ffa Fh Ffa ...
Fh Ffa**

**----- ---- ---- ----- ----- ----- -----
----- -----**

**6/30/1980 <== THIS IS ONLY AN EXAMPLE TIMESTAMP VALUE, YOU
CHOOSE YOUR OWN DATES AND RESOLUTION**

```
7/31/1980 <prediction_error values go here>
:
etc.
```
Also, as you did in Step 4, graph your prediction error as a function of time, but this step
should have one graph-symbol per error level (for example, a hollow circle for zero
noise, a solid circle for stdev=0.001, a hollow triangle for stdev=0.002, etc.)

**IMPORTANT:** Optimize your RNN for best performancebefore generating and
reporting your final results. Discuss WHY your algorithm performed the way it did, and
how these behaviors could be improved. **_If you getzero prediction_error then
increase the input noise cross-section and noise standard-deviation and try again
until you "break" your RNN-based prediction algorithm._**

**Why are we doing this?** It is not enough to developan algorithm and test it on "toy"
datasets - that is something for which academics are not-so-well-liked. Instead, we
need to test our algorithms exhaustively - especially for AI applications, trying to "break"
them, so we know where to "fix" them. This highlights deficiencies that we can then
improve on.

**Step 7 - (3 pts + 2 extra-credit points for quality of appearance and clarity of
presentation) Document your network parameters and results** (e.g., number of
layers, number of input and output data values, any assumptions you make about the
activation or regularization function(s) and training algorithms/parameters, etc. Your
RNN. Documentation should be in a PDF file with one-inch margins and 12-point
TimesNewRoman type, which must be organized as follows:

1. Title Block = "CAP 6615 - Neural Networks - Programming
    Assignment 3 -- Recurrent Neural Network", followed by your group
    members' names and "Spring Semester 2022" and "18 March
    2022" (each on a separate line)
2. Network parameters
3. Discussyour Python code for your RNN **but put theactual code**
    **in an Appendix** (see below)


4. Training and Test (and, where applicable, Validation) set
    configuration
5. Unoptimized RNN output results (from Step 4), Optimized RNN
    results (from Step 5)
6. Discussyour code for algorithms you used to computenoisy data
    and prediction_error **but put the actual code in anAppendix**
    (see below)
7. Optimized RNN output graphs for noise-free Training and Test Set
    inputs, then show the same for noise-corrupted inputs.
8. Discussion (in detail) of why your RNNs performed the way they
    did, and how you could improve their performance in future.
9. **Extra Credit (Step 8, below):** Document how you usedthe
    S&P500 price data in conjunction with the Schiller P/E data to
    provide "hints" to your RNN regarding where to predict a higher or
    lower price value. Document and discuss your results as you did in
    7) and 8), above.

**Important Note:** You will need to develop Linux orWindows scripts, not only to
generate results, tables, and graphs, but also (big Helpful Hint here!) to develop entries
in your Report. If you use LaTeX for your report, then you can write scripts to make all
these things with relative ease. This is important in practice as you will be doing more
of this sort of work in CAP6615, and in your research career -- so please learn these
skills _now_.

**Step 8: Extra Credit (6 pts): "Data Fusion" --** Develop innovative ways to combine
the S&P500 price datawith the Schiller P/E data(fromStep 1, above) to provide "hints"
to your RNN regarding where to more accurately predict (for example) a higher or lower
price value. Then optimize and test your enhanced algorithm using the procedures in
Steps 4-6. This is a deliberately open-ended task description, to encourage and test
your creativity!!

# 6 Turn In Assignment To Canvas

# DUE-DATE: Friday 18 March 2021: 11.59pm

**>>> Select one group member as your leader, and that person will turn in the
following files**

**>>> The other group members do not have to turn in anything**

**File-1:** Your group's PDF documentation, from Step7, above (.pdf file extension).


**File-2:** Your Training Set, Validation Set, and Test Set in separate data files within a
ZIP'd directory (.zip file extension). **You must turnin your data as a ZIP file in order
for your group to get credit for this assignment.**

**File-3:** Your group's Python code and documentation **in a Jupyter notebook** (.ipynb
file extension)

**>>> NOTE:** This might initially seem like a lot ofwork, but (a) there will be six of you
per group, and (b) you can automate most of the computation with scripts - leaving you
plenty of time to play with the network parameters - and make an attempt at the Extra
Credit points **<<<**


