# ML_CyberAttack_RFC
This is a final project of the course **NTU Machine Learning 2016 Fall.**
Please refer to `Report.pdf` to see the whole solution concept of this project.

## `RFC.sh` Usage 
* `./RFC.sh $1`
* $1: directly path containing `test.in` and `train`
  - ex. .../.../.../data/
* `RFC.sh` will execute two python files:
  - `newtrain.py`: remove the repeated training data, output `newtrain`
  - `RFC.py`: build the a random forest as trained model, and predict the testing data as `ans.csv`

## File List
* `newtrain.py`
* `Report.pdf`
* `RFC.py`
* `RFC.sh`
