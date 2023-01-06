# 1 Overview

In this fourth programming assignment, you will work in your programming groups of six
students per group, while designing, coding, training, and testing a Recurrent Neural
Network (RNN) and Convolutional Neural Network (CNN) for time series prediction.
You will choose two datasets (time series) of financial data from a site whose URL will
be provided. Then you wlll configure, train, and use the RNN to identify and predict
"next value(s)" in the time series, given a generic pattern to search for.

The purpose of this assignment is to have fun developing an RNN and CNN with
Python and its Pytorch and TensorFlow libraries, to make them work together, and to
learn how to process financial data with RNNs and CNNs, then properly test and
document your algorithm's performance with noisy (i.e., erroneous) data (real stuff!!).
Then you can optimize your algorithm for best performance before generating and
reporting your final results.

# 2 Groups

Coding, testing, and documentation will be performed by **independent groups of six
(6) people per group.** You may exchange informationbetween groups, but programs
and reports are not to be plagiarized between groups.

```
>>> PLEASE USE THE SAME GROUP AS YOU HAVE BEEN USING THROUGHOUT
THIS SPRING SEMESTER <<<
```
# 3 Duration of Assignment

**Assignment-Date:DUE-DATE= Fri 08 April 2022. Time to Complete =21 days**

# 4 Evaluation 40 points max (plus Extra Credit

# of up to 8 points !)

**>>> Projects will be evaluated by group -- each group member will be assigned
the score for his or her group project <<<**

**Scoring Rubric, per Step or Substep** (on a 3-pointscale -- see Section 5, below)

**Score = 0** : Nothing done, no answer & no results


**Score = 1 or 2 pts** : Some result, ranges from not-very-good to
setup-is-ok-but-results-are-incorrect

**Score = 3 pts** : Correct result, clear explanation

# 5 Stepwise Directions (with point allocations per

# step)

**Step 1 - (3 pts) Select S&P500 Dataset** and **SchillerP/E-10 Dataset** from the
following URLs, as you did for Programming Assignment #3 - **and ensure that the
datasets are synchronized(same sampling interval,identical start & end times)** :

**https://www.nasdaq.com/market-activity/index/spx/historical**

**https://www.multpl.com/sitemap**

**Step 2 - (6 pts) Develop and test/verify a** **_correlation-based_** **algorithm** to correlate
when the Schiller P/E ratio is very high (spikes upward significantly) and the S&P500 is
also high (peaking or ready to peak). Thus, your algorithm will act as a predictor of
when to "sell" the S&P500 index (as if it were a stock or Exchange-Traded Fund (ETF))
by outputting a correlation coefficient in the range [-1, 1], where values in the range [0.9,
1] (or similar range) would be your "sell indicator". This is an extension of the basic
concept of Step 1 in Programming Assignment 2, and here is a URL that will help you
get started with data:

**https://www.longtermtrends.net/sp500-price-earnings-shiller-pe-ratio/**

You will use this algorithm as a "reference" to determine how well the Schiller P/E
predicts market bottoms or sell-offs.

```
○ TO-DOCUMENT and VERIFY: Make an overlay of the Schiller
P/E (if possible, from 1 Jan 1960 to 31 Dec 2020) ,onto the
S&P500 for the same period, then pretend you have $1 million
invested in the S&P500 as-of 1 Jan 1960 and see how well
your "sell" signal from the above-described algorithm helps
you to make money selling the S&P500 at its peaks (assuming
that you BUY at local minima). If you cannot findenough data
to begin at 1 Jan 1960, then use the data available to you.
○ Why are we doing this? Some students have asked aboutthis ...
the purpose of the correlation algorithm is to determine how many
"brute-force" correlations (with non-NN computations) will generate
a SELL signal, and how well you could do moneywise with this type
```

```
of approach. Please feel free to experiment with dataset size,
correlation methods, etc.
```
**Step 3 - (6 pts) Design** and **develop** a convolutionalneural network (CNN) in Python
that will recognize A-B-C-D-wave patterns in the S&P500 data (see Figure 1, below),
using libraries such as PyTorch (and, if necessary, Tensor Flow). Later in this
assignment, you will use this to enhance predictions made by your recurrent neural
network (RNN) that you implemented in Python for Programming Assignment 3.

```
A-B-C-D Wave Pattern: SELL
B /+\ D
| / Here, A = +3, B = -2,
/\v / C C = +4, D = -
A / \/
/
BUY
```
**Figure 1:** Notional diagram of A-B-C-D-wave pattern,where the extent of A
approximately equals the extent of C.

Your CNN **_must_** detect the ABCD wave, and your RNN **_must_** use the CNN output (and
your Programming Assignement 3 result) to accurately predict the next value in a
subset of your training data (S&P500, informed by Schiller P/E, from 1960 to present
date) **and to predict the correct SELL signal**.

```
○ TO-DOCUMENT: Make a diagram of your CNN architecture,
including input, hidden, and output layers as well as
dimensions of each layer and show pictorially how it works
with your RNN architecture from Programming Assignment 3.
You will include this diagram in your report.
○ Why are we doing this? The purpose of this step isto (1)
develop a CNN that can recognize ABCD wave patterns and output
some measure of confidence or caution when the peak of the
pattern is detected, (2) use the CNN output (e.g., a stream of
metrics produced by the CNN) as input to the RNN, which will
predict (for one, two, three, and four samples in future from the
current time) the S&P500 value (e.g., close price) on that day, and
(3) assess the correctness of your result in a way that can be used
to train your CNN+RNN algorithm (see Step 5, below).
```

**Step 4 - (6 pts) Train** your CNN and RNN on your Training Set (S&P500 data and/or
Schiller P/E data, from Step 1, above) then test to ensure it functions correctly when
predicting the next one, two, three, and four trading data (average price or close price -
either is o.k.) before you go on to Step 5. **Documentyour training results** , as
discussed here:

```
○ TO-DOCUMENT: You get credit for showing your preliminary
test results and discussing the number of training epochs
(iterations through whatever backpropagation algorithm you
use, and why this is so ...
```
**Step 5 - (6 pts) Test** your CNN and RNN accuracy overTest Data on which you did not
train, to determine how well your neural networks generalize -- specifically, in terms of
predicting the next one, two, three, and four datapoints in the dataset from 1 Jan 1980
(or whenever your dataset begins) through the present day (or whenever your dataset
ends). To determine response to _input nonergodicity_ ,it is suggested that you use a
sliding sampling window of _N_ datapoints for testingyour algorithm, sliding the window
along the test data and applying your CNN+RNN algorithm to determine how well (at
each data point in the Test Data) your algorithm predicts the next one to four datapoints.

```
○ Accuracy will be computed in terms of error defined as
```
**prediction_error := (predicted_price - actual_price) / actual_price**

( _Hint_ : You will want to develop a script to do this,as there will be multiple execution
runs)

```
○ TO-DOCUMENT: Graph prediction_error as a functionof
timestamp (e.g., DD/MM/YYYY) for all data in the TrainingSet,
as shown in Figure 2. Produce a similar graph for the Test Set
(clearly, there will be some overlap between the two graphs,
depending on the length of your sampling window). Here is an
example of the type of graph you should produce (you can
MS-Excel for this):
```
```
Figure 2: Notional example of Price Prediction AccuracyGraph (between
magenta-colored braces), and how the sliding window approach works to generate the
individual traces on the graph for predicting one to four days ahead of current time.
```

**Step 6 - (3 pts) Optimize your CNN+RNN algorithm's performance** to yield
maximum achievable accuracy (e.g., minimum _prediction_error_ ) over the entire Training
Set and Test Set. Repeat Step 5 graphing operation to show this optimized result. Be
sure to change the graph title to include the phrase "Optimized Over All Data".

**Step 7 - (3 pts) Enhance your CNN+RNN algorithm's functionality** to generate a
**SELL** signal when the S&P500 is about to peak, thenuse the algorithm you developed
in Step 2 of this assignment to check your CNN+RNN algorthm's profitability against.the
correlation-based result you computed in Step 2.

```
○ TO-DOCUMENT: Make a simple graph or table of howmuch
money you have left at the end of your trading activity, say, at
each SELL point (with no tax or commission-fees penalties) -
assuming you start with $1 million.
○ Comment: The purpose of this step is to TEST impartiallythe
performance of your algorithm on real data without input
uncertainty. Then, you will compare the result of this step with the
results of Step 8 (below).
```
**Step 8 - (3 pts) Determine the Effect of Input Data Perturbations** (Price Uncertainty)
**on your CNN+RNN Algorithm:**

In real-time trading (which the pro's do - and sometimes "lose their shirts"), there may
be some uncertainty in the reported prices. This is because the prices that we see on a
site such as bigcharts.com are delayed at least 10-15 minutes, so there might be some
"settling time". In real-time trading, especially in less-liquid commodities, there are
occasional price inaccuracies and (very occasionally) time-lags in data reporting. If you
are wagering large amounts of money on a particular financial instrument, and your
algorithm is not robust, then you too can "lose your shirt". So, here is what we will do to
give you an idea of this effect, and how it can corrupt the output of your CNN+RNN:

**8a)** Using your Optimized CNN+RNN algorithm(from Step 6, above) corrupt your
Test Set that you used in Step 5, above:

```
○ Add noise to the S&P 500 price data - NOT to the SchillerP/E
data. This is practicable, because the "Schiller P/E 10" is an
ensemble measure, whereby input uncertainties tend to be
somewhat "averaged out".
○ Noise will be Gaussian-distributed with 10 percentcross-section
(e.g., 18 noise corrupted values out of each 180-value sampling
window) and have zero mean, and standard deviation of (0.001,
0.002, 0.003, 0.005, 0.01, 0.02, 0.03, 0.05, and 0.1) -- assuming
that the source dataset (from 1, above) has normalized value range
```

```
equal to the real-valued interval [0,1]. You can scale this
accordingly within your sampling window shown in FIgure 2.
○ Algorithm : (1) generate random noise with std-devas described
above, (2) add noise values to input image every 10 values or so
(chosen randomly), (3) DO NOT renormalize the noise-corrupted
price data (unlike what you did with imagery in Programming
Assignments 1-3) -- however, any negative values that result from
noise corruption of S&P500 price data should be set to some small
value greater than zero (you choose what that value is), for
physical realism.
```
**Hint:** You may recycle the noise generation algorithm(s)you developed for
Programming Assignments 1 through 3.

```
8b) Repeat Tests in Step 6, above, with noise-corruptedTest Set.
```
```
○ Make four graphs like that shown in Figure 2, whereeach graph is
specific to a prediction interval (e.g., one graph for the next sample
denoted by time t + 1, another for t + 2, etc.). Instead of the
prediction intervals as traces on one graph, you should use for
each prediction-interval graph the different noise level results. So
you will have nine traces (one per each noise level) on each of the
four graphs --similar in concept to what you did for Programming
Assignment 3.
○ Also, add to each graph title "Optimized" and "Noise-Corrupted
Data".
```
**IMPORTANT:** You must use your Optimized CNN+RNN forbest performance before
generating and reporting final results.

**8c) Repeat Step 7, above, to Determine How Much Money You Make or Lose**
when the input is perturbed.

○ Make a table or simple graph for each prediction interval (i.e., _t_ + 1,
_t_ + 2, etc.) of your profit (or loss ...) with resultsfor each noise level
in a separate column.
○ **Example Table for one-day lookahead prediction
Table of Prediction Error for CNN+RNN Applied to S&P500 data with
Noisy Input**

```
Number of Inputs = _____ per sampling window
Number of Layers = _____
```

```
Number of Outputs = _____
Days-Ahead Prediction = _____ <== Value ranges from 1 to 4
```
**-- Gaussian Noise Standard Deviation (10 percent
cross-section) --**

**Time stdev - 0 stdev = 0.001 stdev = 0. ...
stdev = 0.**

**Stamp Fh Ffa Fh Ffa Fh Ffa ...
Fh Ffa**

**----- ---- ---- ----- ----- ----- -----
----- -----**

**6/1/
6/2/80 <prediction_error values go here>
:
etc. So you make ONE of this kind of
table for each prediction interval (1,2,3,4 days)**

**Step 9 - (4 pts + 2 extra-credit points for quality of appearance and level of
detail&explanation) Document and discuss your network parameters and results**
(e.g., number of layers, number of input and output data values, any assumptions you
make about the activation function(s) and training algorithms/parameters, etc. --- _and_
the configuration of your RNN. Documentation should be in a PDF file with one-inch
margins and 12-point TimesNewRoman type, which must be organized as follows:

1. Title Block = "CAP 6615 - Neural Networks - Programming
    Assignment 4 -- CNN+RNN for Time Series Prediction", followed
    by your group members' names and "Spring Semester 2022" and
    "08 April 2022" (each on a separate line)
2. Network parameters
3. A **_summary_** of your Python code for your correlationalgorithm
    (Step 2), CNN and RNN algorithm (and put it in _one_ file with
    extension .py -- to be turned in to Canvas) -- **Actualcode should**
    **be placed in an Appendix at the end of this report.**
4. Training and Test set configuration (show images in a nicely
    formatted figure)
5. Unoptimized CNN+RNN output results (from Step 5), Optimized
    RNN results (from Step 6)


6. A **_summary_** of your code for algorithms you used to compute noisy
    data and prediction_error -- **Actual code should beplaced in an**
    **Appendix at the end of this report.**
7. Optimized CNN+RNN output graphs (and tables, as applicable) for
    noise-free Training and Test Set inputs, then noise-corrupted
    inputs.
8. Discussion (in detail) of why your CNN+RNN performed the way it
    did, the effect of input perturbations, and how you could improve
    their performance in future.

**Extra Credit (up to 5 points):** Modify the CNN+RNNalgorithm in this assignment to
generate aBUYsignal as well as a SELL signal. Thenoptimize your enhanced
algorithm as stated in Steps 5 and 6. Subsequently, generate a graph and table of
trading activity (assuming $1 million startup funds). Compare (in detail) the
performance of your enahnced CNN+RNN with the approaches you used in Steps 2
and 7 -- why did your enhanced algorithm work (or not work) as well as (or better than)
your basic algorithm that generated a SELL signal only?

# 6 Turn Assignment In To Canvas

# DUE-DATE: Thursday 08 April 2022: 11.59pm

**>>> Select one group member as your leader, and that person will turn in the
following files**

**>>> The other group members do not have to turn in anything**

**File-1:** Your group's PDF documentation, from Step7, above (.pdf file extension).

**File-2:** Your Training Set, Validation Set, and TestSet in separate data files within a
ZIP'd directory (.zip file extension)

**File-3:** Your group's Python code and documentation **in a Jupyter notebook** (.ipynb
file extension)

**>>> NOTE: This might initially seem like a lot of work, but (a) there will be six of
you per group, (b) you are getting 40 points total PLUS extra credit, and (c) you
can automate most of the computation with scripts - leaving you plenty of time to
play with the network parameters, noise levels, etc. <<<**


