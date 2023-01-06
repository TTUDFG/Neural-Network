# 1 Overview

In this second programming assignment, you will work in groups of six students per
group, while designing, coding, training, and testing a Multi-Layer Deep Neural Network
(DNN) on two datasets of characters and one set of images that you develop from
pictures provided in this assignment. You will first train your DNN on one dataset, then
test it on the second dataset of slightly different characters, to measure the degree of
generalization. Then you wlll add noise to the input images, retrain your DNN, then
stress your DNN by re-testing on the noise-corrupted data, optimizing the DNN
configurations so you get the very best possible results.

In the second part of this assignment, you will develop another DNN to recognize
images of hand gestures in American SIgn Language -- this will be a Heteroassociative
Memory (see Lessons 01 through 03) that will accept an image of a hand-sign
corresponding to a letter of the alphabet, and will output the image of the correct letter
(from whichever of the two datasets of characters you prefer).

In the extra-credit part of this assignment, you will develop a multilayer DNN to first
extract features from letters (e.g., dashes, vertical segments, caps, cups, vees, etc.)
then use the features to classify letters from both input datasets of letters (mentioned
above). This will require some "knowledge engineering" and ingenuity!!

The **purpose of this assignment** is to developa hands-on understanding of the
limitations of Deep Neural Networks in terms of generalization, in particular the
bias-variance tradeoff. You will continue to develop skills of summarizing your final
results in a written report. These are important skills for your development as a
graduate student, and for your future research and development work..

# 2 Groups

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
```

```
● Data Manager: One student who supervises and participates in data-set
development and/or acquisition and availability to the group. This includes
developing noise perturbation algorithms to make noisy versions of one or
more datasets for algorithm testing purposes.
● Test Manager: One student who supervises and participatesin algorithm
testing and analysis of test results
● Documentation Manager: One student who supervisesand participates in
documentation (code commenting and production of reports). The report
(one per group per programming assignment) summarizes theory, algorithm,
and code design & development, also algorithm test & analysis results.
Format of the report will be specified in each Programming Assignment.
```
**_Link to Discussion_** for Group Member Selection:

**CAP6615 - Spring 2022 -- DISCUSSION: Form Programming Assignment Groups,
Each of Six Students**

**>>> YOU MUST KEEP YOUR GROUPS STABLE THROUGHOUT THE SEMESTER
<<<**

# 3 Duration of Assignment

**Assignment-Date: Thu 27 Jan 2022. Due-Date:Fri 18 Feb 2022 : 11.59pm.
Time = 21 days**

# 4 Evaluation 30 points max + 8 Extra-Credit

# points

**>>> Projects will be evaluated by group -- each group member will be assigned
the score earned by their group project <<<**

**Scoring Rubric, per Step listed in Section 5**

**Score = 0** : Nothing done, no answer & no results

**Score = 1 or 2 pts** : Some result, ranges from not-very-goodto
setup-is-ok-but-results-are-incorrect

**Score = 3 pts** : Correct result, clear explanation


# 5 Stepwise Directions (with point allocations per

# step)

**Step 1 - (4 pts) Design** and **build** two _simple_ datasets,each having 36 16x16-pixel
images of well-formed typeset (not handwritten) letters A through Z and digits 0 through
9 (256 pixels per image) using the following exemplars:

_Hint_ : This is not difficult if you assign each groupmember six (6) images per dataset.
You can use _gimp_ (www.gimp.org

```
(Links to an external site.)
```
) to capture the above digits, then coerce them into the correct size and resolution.

```
○ For this assignment, choose letters A through Z and numerals 0
through 9 inclusive, as shown above
○ Make one 16x16-pixel image per character from the above array --
image should be black and white only, with no greyvalues. This
will be your dataset for the regular problems. Extra credit will have
more characters.
○ In Step 7 (Documentation), make a nice figure with your
letters-and-digits images laid out in an array format (e.g., 6 rows x
6 col).
```
**Step 2 - (3 pts) Design** and **develop** a multi-layerdeep learning neural net (DNN) in
Python, using libraries such as PyTorch or Keras (and, if necessary, Tensor Flow). As in
Programming Assignment #1, your DNN **_must_** functionin **autoassociative** mode (i.e.,
as an associative memory that accepts an element of _X_ (i.e., a 16x16-pixel image from
Dataset #1) as input, and when the DNN is functioning correctly outputs the same
element of

X


). **Do not use the single-layer perceptron (SLP) from Programming Assignment
#1 -- This assignment is about deep learning, and you will need to develop a DNN
for this assignment.**

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

**Step 3 - (3 pts) Train** your DNN on the 36 images thatcomprise Dataset #1 developed
in Step 1), above. You will want to test your DNN to ensure it functions correctly as an
autoassociative memory before you go on to Step 4. **Document your training results** ,
as discussed here:

```
○ You get credit for showing your preliminary test results and
discussing the number of training epochs (iterations through the
backpropagation algorithm), then explaining why you need that
many iterations.
```
**Step 4 - (8 pts) Test** your DNN on the entire dataset _X_ that you trained on in Step 3),
above -- with no noise introduced into the input dataset, using the following procedure:

```
○ Step 4a: Apply your trained DNN in autoassociativemode to the
dataset #1 X (shown above), collecting output datain a test dataset
Y
○ Step 4b: Apply your trained DNN in autoassociative mode to the
dataset #2 X ' (shown above), collecting output datain a test
dataset Y '.(Note: This has been corrected from theoriginal
"heteroassociative" - please use autoassociative mode)
```
(You will want to develop a script to do this, as well as another script to compute _Fh_ and
_Ffa_ , as defined below)

```
○ Step 4c: Compute metrics (described in ProgrammingAssignment
#1) called fraction-of-hits (Fh) and fraction-of-false-alarms(Ffa) for
(i) DNN output obtained in Step 4a (using output Y with X as the
reference dataset) -and- (ii) for DNN output obtained in Step 4b
(using output Y' with X' as the reference dataset).
```

```
■ Question to Answer in Your Report: Is there a
semantic or epistemic mismatch in Step 4b), Part (ii),
above? Should we instead use output Y' with X (instead
of X' ) as the reference dataset? Why or why not?
(Justify your answer with analysis in the report generated
in Step 8, below, and think about test, training, and
validation datasets).
■ Another Question to Answer: Would these
experiments be better if your test images were 32x
pixels instead of 16x16 pixels? Why, or why not? ( Hint :
Try it and find out viaexperiment-- that's whatscientists
do!!) Explain your results in the report generated in Step
8, below).
○ Step 4d: Graph Fh as a function of Ffa for each exemplarin each
input dataset - that is, one graph for the results of Step 4a and one
graph for Step 4b, above. Thus, each graph will look like a scatter
plot with Fh on the ordinate (vertical axis, rangingin value from 0 to
1) and Ffa on the abscissa (horizontal axis, rangingin value from 0
to 1). You can use a small triangle or small hollow circle for each
data point.
```
**What This Means in Practice:** When you use a neuralnetwork as a classifier, it is
important to develop a perfomance metric for classification accuracy that is easily
understood. This simple graph will be a precursor to a more sophisticated metric that
we will develop in Programming Assignment #3, called _Receiver Operating
Characteristic_ ( _ROC_ ) - so it is important to get thisright now. This is an important skill
for you to know in your future research & development work in Artificial Intelligence.

**Step 5 - (3 pts) Perturb** your dataset #2 (the secondset of 36 images that you
developed in Step 1), above) by adding noise, and saving the performance results, so
you can display them as described in Step 6.

```
○ Noise will be Gaussian-distributed with approximately10 percent
cross-section (e.g., 25 noise pixels out of 16x16 = 256 pixels per
image) and have zero mean, and standard deviation of (0.001,
0.002, 0.003, 0.005, 0.01, 0.02, 0.03, 0.05, and 0.1) [yes, that's
nine cases!!]. Then repeat this with noise at 20 percent, 25
percent, 30 percent, and 35 percent cross-section [yes, that's 9 x 4
= 36 more cases - so use scripts as you did in Programming
Assignment #1 !!]
○ Algorithm : (1) generate random noise with std-devas described
above, (2) add noise values to input image as you did in
```

```
Programming Assignment #1, then (3) renormalize the
noise-corrupted image so all of its pixels have values in the interval
[0,1].
```
**What This Means in Practice:** Neural networks generallydo not perform well in the
presence of noisy input, even when the noise cross-section is small (e.g., 10 percent to
35 percent, as in this assignment). So it is important to learn how to make noisy data
(real world input!!!) to test your NN by stressing it with some uncertainty. This will
compound the effect of testing your DNN trained on Dataset #1 using slightlly-different
Dataset #2 as input -- we call this _lack of generalization_.

**Step 6 - (3 pts) Display Data from your Tests in Step 5),** above, as follows:

**Step 6a:** Gather your results into a table of _Fh_ and _Ffa_ versus test-image-ID, with one
column per each value of the standard deviation, like this, where < _n_ > denotes 10, 20,
25, 30, and 35 percent noise cross section values (so you will have seven of these
tables -- one from Step 4a results, one from Step 4b results, and _five tables_ from Step 5
results -- so develop a script to automate this process!!):

**Table of Heteroassociative Deep Neural Network Response to Noisy
Input**

**Number of Inputs = 16x16 = 256
Number of Weights in an Equivalent Single-Layer Perceptron =
256x256 = 64K**

**Number of Hidden Layers in This DNN = ___
Number of Weights in Hidden Layer 1 = ___ <== YOU FILL
IN THESE VALUES**

```
Number of Weights in Hidden Layer 1 = ___
: (and so forth...)
Number of Outputs = 16x16 = 256
```
**-- Gaussian Noise Standard Deviation (<** **_n_** **> percent
cross-section) --**

**Test stdev - 0 stdev = 0.001 stdev = 0. ...
stdev = 0.**

**Image Fh Ffa Fh Ffa Fh Ffa ...
Fh Ffa**


**----- ---- ---- ----- ----- ----- -----
----- -----**

**"0"
"1"
: <** **_Fh_** **and** **_Ffa_** **values go here, should be formatted
as 0.** **_nn_** **>**

```
:
"9"
```
**Step 6b:** Make a very nice-appearing scatter-plot graphof _Fh_ versus _Ffa_ with each
noise standard deviation ( _stdev_ ) value representedon a logarithmically-scaled abscissa
whose values range from 0 to 0.1 in steps of 0.001, and with the _Fh_ and _Ffa_ values
represented on the linearly-scaled ordinate whose values range from 0 to 1 in steps of
0.1. Please label the abscissa as "Gaussian Noise Level (stdev, at< _n_ >pct xsecn)",
where you insert the various values for< _n_ >in eachinstance of the graph, and the
ordinate as " _Fh_ and _Ffa_ ". The graph should have atitle in the frame that says, "Graph
of _Fh_ and _Ffa_ vs. Noise Standard Deviation for noise-corruptedAlphanumeric Imagery
(16x16 pixels) for Heteroassociative Deep Neural Network". Make seven of these
graphs -- one from Step 4a results, one from Step 4b results, and _five tables_ from Step
5 results -- so develop a script to automate this process!!

```
Example Graph (drafted manually, from notional[i.e., fake] data):
```
```
Note : As you progress through this assignment, youmight also want to
attempt training your network on noisy input as you might have done in Programming
Assignment #1 ... but be careful: the number of imagesthat can be correctly
retrieved from your associative memory will be less than you think! So be careful of
the number of training-set images vs. the number of input nodes and the number of
hidden layers & nodes in each hidden layer.
```
**IMPORTANT:** Make sure you optimize your DNN for bestperformance before
generating and reporting your results.


**What This Means in Practice:** The purpose of this step is to report your performance
results and how your DNN performs (or does not perform well given input mismatch with
the training set and under noisy conditions (i.e., lack of generalization) in a tabular form
(for accuracy) and in a graphical form (for ease of viewing). This skill will be important
in this course, and will be key to your success as an engineer or research scientist.

**Step 7 - (3 points) -- Repeat Steps 1 through 6 for a third dataset** , which you will
construct based on 24 **_input_** images of American SignLanguage gestures, taken from
the following exemplars (with construction hints as indicated, to make your DNN
perform better with less semantic bias):

**Note:** If you assign four images from the above datasetto each of your six group
members, this step will be easer. Also, your _n_ x _n_ pixel images in this dataset will need
to be _larger_ than the 16x16-pixel images you developedfor Datasets 1 and 2, above.
How much larger? You will have to figure out the _minimum_ size needed (where, in the
above picture _n_ >32) to make your DNN perform well,but not spend too much time in
training ...

**This is Important in Practice** , as designing a datasetto achieve realistic resolution -
but with good performance - and performing the engineering tradeoffs needed to design
a DNN to avoid overfitting the data - are all important skills to learn _now_.

**Differences from Steps 1-6, above** : Your DNN for thispart of the assignment will
need to be _heteroassociative_ , as it will (a) **input** images from the sign-language image
dataset, above, then (b) **output** the correspondingimage (that is, for letter A-I, K-Y)
_from Dataset #1_. That is, if _X_ denotes the trainingset (AmerSign images, above) and _Y_
denotes the output image set (Dataset #1, in Step 1, above), then given training set _T_ =
( **x** , **y** ) you will have a sign-language image **x** takenfrom _X_ and paired with a correct
answer **y** taken from _Y_. So, your performance tableand graph will have different
entries, including but not limited to the following:

The number of inputs will be _n_ 2 (e.g., if your inputresolution is 32x32, then you will have
at least 1024 inputs and maybe one or more bias neurons)

Since the number of outputs will be 256, you will have multiple layers with more than
1024 x 256 weights -- so you will have to document your hidden layer units, as well.

**Also, some good news ...** You will have to make onefewer tables and graphs than you
did for Datasets 1 and 2, above, as you will have one noise-free mapping _X_


## →

_Y_ and five noisy results (one each for 10, 20, 25,30, and 35 percent noise
cross-sections).

**HELPFUL HINTS:** Here are some URLs that may help youorganize your approach:

```
■ https://towardsdatascience.com/american-sign-language
-hand-gesture-recognition-f1c4468fb
■ Links to an external site.
■
■ https://www.analyticsvidhya.com/blog/2021/06/sign-lang
uage-recognition-for-computer-vision-enthusiasts/
■ Links to an external site.
■
```
**Step 8 - (2 pts + 1 extra-credit point for quality of appearance) Documentyour
network parameters and results** (e.g., number of weights,number of input and output
data values, any assumptions you make about the number of layers in your DNN and
the activation function _f_ that is used for thresholdingthe network output --- _and_ the
configuration of your training set(s). Documentation should be in a PDF file with
one-inch margins and 12-point TimesNewRoman type at 1.5-line spacing, which _must_
be organized as follows:

```
● Title Block = "CAP 6615 - Neural Networks - ProgrammingAssignment 2 --
Deep Learning", followed by your group members' names and "Spring
Semester 2022" and "18 Feb 2022" (each on a separate line)
● Body of Report must contain the following information,denoted by Section
Number, as shown below:
```
1. Network parameters
2. **Discuss** your Python code for your DNNs **but put theactual code**
    **in an Appendix** to this report.
3. Training set configuration (show images in the training set in a
    nicely formatted figure)
4. SLP output results for noiseless input in terms of _Fh_ and _Ffa_ graph
    (as described in Step 4 above
5. Pseudocode and Python code (in an Appendix) for algorithms you
    used to compute _Fh_ and _Ffa_
6. SLP output results for noise-corrupted input as table and graph of
    _Fh_ and _Ffa_ (as described in Steps 4 thru 7, above)
7. Discussion (in detail) of why your DNN performed the way it did,
    and how you could improve its performance in future.


**CAUTION:** **_Do not put code in the body of your report._** **If you must include code,
then put it in an Appendix at the end of the report.** We are interested in how you got
your results, what your results are, andwhyyourresults are the way they are. That is
what researchers and engineers share, and you are all studying to be researchers and
engineers.

**Important Note:** You will need to develop Linux orWindows scripts, not only to
generate results, tables, and graphs, but also (big Helpful Hint here!) to develop entries
in your Report. If you use LaTeX for your report, then you can write scripts to make all
these things with relative ease. **This is importantin practice** as you will be doing
more of this sort of work in CAP6615, and in your research career -- so please learn
these skills _now_.

# Extra Credit (8 points = 4 pct of Final Score)

**Step 9 (3 points) - Build a Semantic Representation of Dataset #1** using a two-stage
2DNN (multiple layers per part) that (1) segments features from the letters and
numerals in Dataset #1, as follows:

```
● Example Features include, but are not limited to,Dash ("-"), Vertical Line
{"|"), Cup and Cap, Vee and Wedge, SlantLine+ ("/"), SlantLine- ("\"), LeftBow
("("), and RIghtBow (")") -and, possibly, other features.
● Example Character Representations include "A" = (Slant+,Slant+, Slant-,
Slant-, Dash) or "B" = (VerticalLine, VerticalLine, Dash, RightBow, Dash,
RightBow, Dash), and so forth...
```
then (2) functions as a heteroassociative memory, which maps features to the output
image of the correct letter or numeral in Dataset #1 or Dataset #2 and (3) displays the
correct output letter or numeral. This will work for both Datasets 1 and 2, because the
DNN will "abstract out" the relevant features, making a _font-agnostic internal
representation_ of each letter.

**Step 10 (2 points) Optimize and test your 2DNN** onDataset #1, then see how well it
generalizes to Dataset #2 -- for classifying the letters and numerals in Dataset #2 using
the semantic representation and inference steps developed in Step 9, abovce.

**Step 11 (2 points) - Test Your Optimized Two-Stage 2DNN on the Noise-Free and
Noise-Corrupted Data** per Steps 4 through 6, above)-- This will be easy, because you
will have already developed the algorithms and scripts for Fh, Ffa, tabulating, graphing,
and reporting your results.


**Step 12 (1 point) - Add an Appendix to Your Report,** in which you present and
discuss your 2DNN results, in the same way you did for the SLP in Parts 1 through 7 of
Step 8), above.


