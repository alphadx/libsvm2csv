
# libsvm2csv
libsvm to csv weka make nominal classes

The way to use is:

$python libsvm2csv.py fileName.withExtention.libsvm

the ouptut will be a csv file with same name as original file, with all features numbers as cols and a las col called "Class".
Each row will contains the value of each feature and the class value (from 1 to n) in libsvm will have a upper case alphabet letter.
Only accept 24 classes (by 24 alphabet letter... of course it is expansible line 46)
