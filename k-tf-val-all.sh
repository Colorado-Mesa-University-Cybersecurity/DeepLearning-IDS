#! /bin/sh
# I included this file because I kinda messed up previously by not changing/updating the output write stuff in keras-tensorflow.py so it never actually ends up writing to the results files
# I also figured since I messed that up I'd create these couple of files to fix the issue. All you have to do is include the path to your keras-tf models and it will run the validation process on all of the models and print out a bunch of stuff.

#path may have to change person to person
for file in $(ls results_keras_tensorflow/models) ; do
	python k-tf-validation.py $file
done
