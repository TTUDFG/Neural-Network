## 1 Overview

In this first assignment, you will work in groups of six students per group, while
designing, coding, training, and testing a Single-Layer Perceptron (SLP) and a Shallow
Multi-layer Neural Network (SMNN) on a simple dataset of digits (and, for extra credit,
characters) that you develop. Then you wlll add noise to the input images to stress your
NNs and re-test the SLP & SMNN on the noise-corrupted data, optimizing the SLP and
SMNN configurations so you get the very best possible results.

The **purpose of this assignment** is to have fun"getting your feet wet" with Python
and its associated NN libraries such as Keras, PyTorch, and TensorFlow. You will also
develop the important skill of making a proper test and training dataset (albeit a simple
one) and to properly test and document your SLP's and SMNN's performance with
noiseless and noisy data (real stuff!!). Then you can optimize your SLP for best
performance before generating and reporting your final results in a written report.
These are important skills for your development as a graduate student, and for your
future research and development work..

## 2 Groups

Coding, testing, and documentation will be performed by **twenty (20) independent
groups of six (6) people per group, which should be structured by functionality,
as follows:**

```
● Design, Coding, Test, and Documentation: All studentsin each group
● Code Manager: One student who supervises and participatesin code
design, development, and version management. This includes production of
a Jupyter notebook (https://jupyter.org/
● (Links to an external site.)
● ) for each group, for each programming assignment.
● Data Manager: One student who supervises and participatesin data-set
development and/or acquisition and availability to the group. This includes
developing noise perturbation algorithms to make noisy versions of one or
more datasets for algorithm testing purposes.
● Test Manager: One student who supervises and participatesin algorithm
testing and analysis of test results
● Documentation Manager: One student who supervisesand participates in
documentation (code commenting and production of reports). The report
(one per group per programming assignment) summarizes theory, algorithm,
```

```
and code design & development, also algorithm test & analysis results.
Format of the report will be specified in each Programming Assignment.
```
**_Link to Discussion_** for Group Member Selection:

**CAP6615 - Spring 2022 -- DISCUSSION: Form Programming Assignment Groups,
Each of Six Students**

**>>> YOU MUST FORM YOUR GROUPS NOW, AND KEEP THEM THROUGHOUT
THE SEMESTER <<<**

## 3 Duration of Assignment

**Assignment-Date: Thu 13 Jan 2022. Due-Date:Fri 28 Jan 2022 : 11.59pm.
Time = 15 days**

## 4 Evaluation 20 points max + 4

## Extra-Credit points

**>>> Projects will be evaluated by group -- each group member will be assigned
the score for their group project <<<**

**Scoring Rubric, per Step listed in Section 5**

**Score = 0** : Nothing done, no answer & no results

**Score = 1 or 2 pts** : Some result, ranges from not-very-goodto
setup-is-ok-but-results-are-incorrect

**Score = 3 pts** : Correct result, clear explanation

## 5 Stepwise Directions (with point allocations

## per step)

**Step 1 - (2 pts) Design** and **build** a _simple_ dataset

X


```
of for character recognition of 10 16x16-pixel images of well-formed typeset (not
handwritten) digits 0 through 9 (256 pixels per image) from online exemplars or from
the following characters.
```
### ○ Example Digits:

# 0 1 2 3 4 5 6 7

# 8 9

```
Hint : You can use gimp (www.gimp.org
```
Links to an external site.

```
) to capture the above digits, then coerce them into the correct size.
○ For this assignment, choose numerals 0 through 9 inclusive, as
shown above
○ Make one 16x16-pixel image per character from the above array --
image should be black and white only, with no greyvalues. This
will be your dataset for the regular problems. Extra credit will have
more characters.
○ In Step 7 (Documentation), make a nice figure with your digits
images laid out in an array format (e.g., 2 rows x 5 col).
```
```
Step 2 - (3 pts) Design and develop a single-layerperceptron (SLP) in Python, using
libraries such as PyTorch (and, if necessary, Tensor Flow). Your SLP must function in
autoassociative mode (i.e., as an associative memorythat accepts an element of
```
```
X
```
```
(i.e., a 16x16-pixel image) as input, and when the SLP is functioning correctly outputs
the same element of
```
```
X
).
```
```
○ Here is some example code to get you started:
https://github.com/vrajkp/Single_layer_perceptron
○ (Links to an external site.)
```

#### ○

```
○ Recommendation: Use double-precision floating-point
computation, for better accuracy
○ In Step 7 (Documentation), list your code with manycomments
```
**What This Means in Practice:** Your result will bea Fully-Connected Network with
Image Output: Here, we have 16x16 = 256 inputs, and _n_ = 256x256 = 64K weights, and
256 output nodes that are valued ideally at 0 or 1, but will actually vary over the interval
[0,1]. So your output image will be 16x16 pixels (256 pixel values), hence the 256 output
nodes. To properly form the input vector **x** = ( _x_ 1 , _x_ 2 , ..., _x_ 256 ) you will assemble the 256
output nodes in normal (row-wise) scanning order to form the 16x16-pixel output image.

**Step 3 - (3 pts) Train** your SLP on the 10 images thatcomprise the dataset developed
in Step 1), above. You will want to test your SLP to ensureit functions correctlyas an
autoassociative memory before you go on to Step 4. **Document your training results** ,
as discussed here:

```
○ You get credit for showing your preliminary test results and
discussing the number of training epochs (iterations through the
backpropagation algorithm), then explaining why you need that
many iterations.
```
**Step 4 - (3 pts) Test** your SLP on the entire datasetthat you trained on in Step 3),
above -- with no noise introduced into the input dataset, using the following procedure:

```
○ Step 4a: Apply your trained SLP in autoassociativemode to the
dataset
○ X
○ , collecting output data in a test dataset
○ Y
○
```
(You will want to develop a script to do this, as well as another script to compute _Fh_ and
_Ffa_ , as defined below)

```
○ Step 4b: Computemetrics(described below) called fraction-of-hits
(Fh) and fraction-of-false-alarms (Ffa) :
```
Fh=numberof"black"pixelsinoutputimageb∈YthatoccurintheCORRECTplacesinthecorre
spondingnoiselessinputimagea∈Xtotalnumberofblackpixelsinnoiselessinputimagea∈X

Ffa=numberof"black"pixelsinoutputimageb∈YthatoccurintheWRONGplacesinthecorresp
ondingnoiselessinputimagea∈Xtotalnumberof"white"pixelsinnoiselessinputimagea∈X


**What This Means in Practice:** Consider this (nearly trivial) example where the input
image **a** = (0, 1, 1, 0, 1) and the (erroneous) output image from the autoassociative SLP
is **b** = (0, 0, 1, 1, 1). The resulting _Fh_ value is2 / 3 = 0.66... and the resulting _Ffa_ value
is 1 / 2 = 0.5. (Check this out carefully, so you understand how these metrics work - we
will be using them again!!)

_Hint_ : There are simple algorithms for computing _Fh_ and _Ffa --_ using image
thresholding, then differencing, then summation ... play around and discover how these
important metrics can be computed very efficiently!!

```
○ Step 4c: Graph Fh as a function of Ffa for each exemplarin the
input dataset -- your output will look like a scatter plot with Fh on
the ordinate (vertical axis, ranging in value from 0 to 1) and Ffa on
the abscissa (horizontal axis, ranging in value from 0 to 1). You
can use a small triangle or small hollow circle for each data point.
```
**What This Means in Practice:** When you use a neuralnetwork as a classifier, it is
important to develop a perfomance metric for classification accuracy that is easily
understood. This simple graph will be a precursor to a more sophisticated metric that
we will develop in Programming Assignment #2, called _Receiver Operating
Characteristic_ ( _ROC_ ) - so it is important to get thisright now. This is an important skill
for you to know in your future research & development work in Artificial Intelligence.

**Step 5 - (3 pts) Perturb** your dataset (the 10 imagesthat you developed in Step 1),
above) by adding noise, and saving the performance results, so you can display them
as described in Step 6.

```
○ Noise will be Gaussian-distributed with approximately10 percent
cross-section (e.g., 25 noise pixels out of 16x16 = 256 pixels per
image) and have zero mean, and standard deviation of (0.001,
0.002, 0.003, 0.005, 0.01, 0.02, 0.03, 0.05, and 0.1) [yes, that's
nine cases!!].
○ Algorithm : (1) generate random noise with std-devas described
above, (2) add noise values to input image every 10 pixels or so
(chosen randomly), (3) renormalize the noise-corrupted image so
all of its pixels have values in the interval [0,1].
```
**What This Means in Practice:** Neural networks generallydo not perform well in the
presence of noisy input, even when the noise cross-section is small (e.g., 10 percent, as
in this assignment). So it is important to learn how to make noisy data (real world
input!!!) to test your NN by stressing it with some uncertainty.

**Step 6 - (3 pts) Display Data from your Tests in Step 5),** above, as follows:


**Step 6a:** Gather your results into a table of _Fh_ and _Ffa_ versus test-image-ID, with one
column per each value of the standard deviation, like this:

**Table of Autoassociative Single-Layer Perceptron Response
to Noisy Input**

```
Number of Inputs = 16x16 = 256
```
```
Number of Weights = 256x256 = 64K
```
```
Number of Outputs = 16x16 = 256
```
**-- Gaussian Noise Standard Deviation (
percent cross-section) --**

**Test stdev - 0 stdev = 0.001 stdev = 0.
... stdev = 0.**

**Image Fh Ffa Fh Ffa Fh Ffa
... Fh Ffa**

**----- ---- ---- ----- ----- ----- -----
----- -----**

```
"0"
```
```
"1"
```
**: <** **_Fh_** **and** **_Ffa_** **values go here, should be
formatted as 0.** **_nn_** **>**

```
:
```
```
"9"
```
**Step 6b:** Make a very nice-appearing scatter-plot graphof _Fh_ versus _Ffa_ with each
noise standard deviation ( _stdev_ ) value representedon alogarithmically-scaled abscissa
whose values range from 0 to 0.1 in steps of 0.001, and with the _Fh_ and _Ffa_ values
represented on thelinearly-scaled ordinatewhosevalues range from 0 to 1 in steps of
0.1. Please label the abscissa as "Gaussian Noise Level (stdev, at 10 pct xsecn)" and
the ordinate as " _Fh_ and _Ffa_ ". The graph should havea title in the frame that says,
"Graph of _Fh_ and _Ffa_ vs. Noise Standard Deviationfor noise-corrupted Alphanumeric
Imagery (16x16 pixels) for Autoassociative Single-Layer Perceptron".


```
Example Graph (drafted manually, from notional[i.e., fake] data):
```
```
Note : As you progress through this assignment, youmight also want to
attempt training your network on noisy input ... but be careful: the number of images
that can be correctly retrieved from your associative memory will likely be less than
0.15 N , where N = 16x16 = 256 is the number of inputs. So 0.15 N ~ 38 training-set
images.
```
**IMPORTANT:** Make sure you optimize your SLP for bestperformance before
generating and reporting your results.

**What This Means in Practice:** The purpose of thisstep is to get you accustomed to
reporting your performance results in a tabular form (for accuracy) and in a graphical
form (for ease of viewing). This skill will be important in this course, and will be key to
your success as an engineer or research scientist. This programming assignment is
easy - basic stuff - and as we move into the other programming assignments, there will
be more detailed metrics and thus more detailed reporting (tabularly and graphically).
So it's best to learn these skills now.

**Step 7 - (2 pts + 1 extra-credit point for quality of appearance) Document your
network parameters and results** (e.g., number of weights,number of input and output
data values, any assumptions you make about the activation function _f_ that is used for
thresholding the network output --- _and_ the configurationof your training set(s).
Documentation should be in a PDF file with one-inch margins and 12-point
TimesNewRoman type at 1.5-line spacing, which _must_ be organized as follows:

```
● Title Block = "CAP 6615 - Neural Networks - ProgrammingAssignment 1 --
Single-Layer Perceptron", followed by your group members' names and
"Spring Semester 2022" and "28 Jan 2022" (each on a separate line)
● Body of Report must contain the following information,denoted by Section
Number, as shown below:
```
1. Network parameters
2. Python code for your SLP (and put it in _one_ file withextension .py
    -- to be turned in to Canvas)
3. Training set configuration (show images in the training set in a
    nicely formatted figure)
4. SLP output results for noiseless input in terms of _Fh_ and _Ffa_ graph
    (as described in Step 4 above


5. Pseudocode and Python code for algorithms you used to compute
    _Fh_ and _Ffa_
6. SLP output results for noise-corrupted input as table and graph of
    _Fh_ and _Ffa_ (as described in Steps 4 thru 6, above)
7. Discussion (in detail) of why your perceptron performed the way it
    did, and how you could improve its performance in future.

## Extra Credit (4 points = 2 pct of Final Score)

**Step 8 (1 point) - Build a Two- or Three-Layer Shallow Multilayer Neural Net
(SMNN)** that functions as an autoassociative memory,and optimize it for classifying the
training/test set developed in Step 1 (similar to Steps 2 and 3).

**Step 9 (2 points) - Test Your Optimized SMNN on the Noise-Corrupted Data** per
Steps 4 through 6) -- This will be easy, because you will have already developed the
algorithms and scripts for Fh, Ffa, tabulating, and graphing your results.

**Step 10 (1 point) - Add an Appendix to Your Report,** in which you present and
discuss your SMNN results, in the same way you did for the SLP in Parts 1 through 7 of
Step 7), above.

## 6 Turn Assignment In To Canvas

## DUE-DATE: Friday 28 Jan 2022

**>>> Select one group member as your leader, and that person will turn in the
result to Canvas**

**File-1:** Your group's PDF documentation, from Step7, above (and Step 10, if you do
the extra credit).

**File-2:** Your groups' data, in a ZIP file; and

**File-3:** Your group's Python code ( _documented_ ) **ina Jupyter notebook** (.ipynb file
extension)

**>>> The other group members do not have to turn in anything -- all group
members receive the same score**

**>>> NOTE: This might initially seem like a lot of work, but (a) there will be six of
you per group, and (b) you can automate most of the computation with scripts -
leaving you plenty of time to play with & optimize the NN parameters <<<**


## Start early , and have fun enjoying this

## introductory exploration of perceptrons and

## shallow NNs!!

#### ______________________________________________________________________

#### ________________________

```
If you have questions, please ask in class, or email the TA at msk@cise.ufl.edu or the
instructor at mssz@cise.ufl.edu.
______________________________________________________________________
________________________
```
# Rubric

```
A1 Rubric
```
```
Criteria Ratings Pts
```
```
This criterion is linked to a Learning Outcome
```
```
Dataset
```
```
Step 1 - (2 pts) Design and build a simple dataset
LaTeX: X of for character recognition of 10
16x16-pixel images of well-formed typeset (not
handwritten) digits 0 through 9 (256 pixels per
image) from online exemplars or from the following
characters.
```
```
2 pts
```
```
Full
Marks
```
```
0 pts
```
```
No
Marks
```
```
2 pts
```

This criterion is linked to a Learning Outcome

Build SLP

Step 2 - (3 pts) Design and develop a single-layer
perceptron (SLP) in Python, using libraries such as
PyTorch (and, if necessary, Tensor Flow). Your SLP
must function in autoassociative mode (i.e., as an
associative memory that accepts an element of
LaTeX: X (i.e., a 16x16-pixel image) as input, and
when the SLP is functioning correctly outputs the
same element of LaTeX: X).

```
3 pts
```
```
Full
Marks
```
```
0 pts
```
```
No
Marks
```
```
3 pts
```
This criterion is linked to a Learning Outcome

Train SLP

Step 3 - (3 pts) Train your SLP on the 10 images
that comprise the dataset developed in Step 1),
above. You will want to test your SLP to ensure it
functions correctly as an autoassociative memory
before you go on to Step 4. Document your training
results, as discussed here:

```
3 pts
```
```
Full
Marks
```
```
0 pts
```
```
No
Marks
```
```
3 pts
```
This criterion is linked to a Learning Outcome

Test SLP

Step 4 - (3 pts) Test your SLP on the entire dataset
that you trained on in Step 3), above -- with no
noise introduced into the input dataset, using the
following procedure:

```
3 pts
```
```
Full
Marks
```
```
0 pts
```
```
No
Marks
```
```
3 pts
```

This criterion is linked to a Learning Outcome

Dataset - Perturbed

Step 5 - (3 pts) Perturb your dataset (the 10
images that you developed in Step 1), above) by
adding noise, and saving the performance results,
so you can display them as described in Step 6.

```
3 pts
```
```
Full
Marks
```
```
0 pts
```
```
No
Marks
```
```
3 pts
```
This criterion is linked to a Learning Outcome

Display Perturbed

Step 6 - (3 pts) Display Data from your Tests in
Step 5), above, as follows:

Step 6a: Gather your results into a table of Fh and
Ffa versus test-image-ID, with one column per
each value of the standard deviation, like this:

Step 6b...

```
3 pts
```
```
Full
Marks
```
```
0 pts
```
```
No
Marks
```
```
3 pts
```
This criterion is linked to a Learning Outcome

Document parameters and results

Step 7 - (2 pts + 1 extra-credit point for quality of
appearance) Document your network parameters
and results (e.g., number of weights, number of
input and output data values, any assumptions you
make about the activation function f that is used for
thresholding the network output --- and the
configuration of your training set(s). Documentation

```
3 pts
```
```
Full
Marks
```
```
0 pts
```
```
No
Marks
```
```
3 pts
```

should be in a PDF file with one-inch margins and
12-point TimesNewRoman type at 1.5-line spacing,
which must be organized as follows:

This criterion is linked to a Learning Outcome

Build SMNN

Step 8 (1 point) - Build a Two- or Three-Layer
Shallow Multilayer Neural Net (SMNN) that
functions as an autoassociative memory, and
optimize it for classifying the training/test set
developed in Step 1 (similar to Steps 2 and 3).

```
1 pts
```
```
Full
Marks
```
```
0 pts
```
```
No
Marks
```
```
1 pts
```
This criterion is linked to a Learning Outcome

Test SMNN

Step 9 (2 points) - Test Your Optimized SMNN on
the Noise-Corrupted Data per Steps 4 through 6) --
This will be easy, because you will have already
developed the algorithms and scripts for Fh, Ffa,
tabulating, and graphing your results.

```
2 pts
```
```
Full
Marks
```
```
0 pts
```
```
No
Marks
```
```
2 pts
```
This criterion is linked to a Learning Outcome

Appendix

Step 10 (1 point) - Add an Appendix to Your
Report, in which you present and discuss your
SMNN results, in the same way you did for the SLP
in Parts 1 through 7 of Step 7), above.

```
1 pts
```
```
Full
Marks
```
```
0 pts
```
```
No
Marks
```
```
1 pts
```
Total Points: 24


