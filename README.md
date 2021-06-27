# Pair Artists

To set expectations:

1. Assume none of the artist names (see below) contain commas, newlines or malicious constructs
2. We recommend that candidates use their strongest language
3. We care more about readability (variable names, formatting, complexity, etc.), good practices and correctness than performance within reason
4. Tests aren't required but submissions that come with unit tests are much more likely to be correct
5. Comments in code aren't required but should indicate intent; we frown on things like "import libs" or "set value to 1"

The attached text file contains the favorite musical artists of 1000 users from Some Popular Music Review Website. 

Each line is a list of up to 50 comma-separated artist names. For example:

Radiohead,Pulp,Morrissey,Delays,Stereophonics,Blur,Suede,Sleeper,The La's,Super Furry Animals,Iggy Pop
Band of Horses,Smashing Pumpkins,The Velvet Underground,Radiohead,The Decemberists,Morrissey,Television
etc.

Write a program that, using this file as input, produces an output file containing a list of pairs of artists which appear TOGETHER in at least fifty different lists. It should be able to be run from the command line. For example, in the above sample, Radiohead and Morrissey appear together twice, but every other pair appears only once. Your solution should be a CSV, with each row being a pair. For example:

Morrissey,Radiohead

Your solution MAY return a best guess, i.e. pairs which appear at least 50 times with high probability, as long as you explain how your approach affects accuracy and why this tradeoff improves the performance of the algorithm. Please include, either in comments or in a separate file, a brief one-paragraph description of any optimizations you made and how they impact the run-time of the algorithm.

Please provide written instructions for how to build, compile and run your code. Please no Jupyter notebooks.

## Instructions:
1. Run `python artist_pairs.py artist_lists_small artist_tuple 50` where :
- artist_lists_small is the name of the txt file given, and 
- artist_tuple is the name of the csv output, and
- 50 is the positive integer number of pairs we want to display in the output
(Optional: activate a python virtual environment beforehand: i.e. conda activate base or create one that is specific to the project)

2. the python files, the input file, and the output file should all be in the same directory.

3. to run the tests, run `pytest` in that same directory. This test suite could be expanded to test more pairs and be more extensive and robust as it's really lightweight at the moment. It could also be built to take in the parameters at command line. However the expected output would need to determined ahead of time in order to make assertions. Steps here: https://docs.pytest.org/en/6.2.x/example/simple.html#pass-different-values-to-a-test-function-depending-on-command-line-options