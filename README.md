# mlCyberAttackRFC
* Predict a connection is normal or malicious attack based on machine learning techniques: **Random Forest Classifier**
* This is a final project of the course **NTU Machine Learning 2016 Fall**.  
* For more detail, please refer to `Report.pdf` to see the whole solution concept of this project.

## `RFC.sh` Usage 
* `./RFC.sh $1`
  - `$1`: directly path containing `test.in` and `train`
  - ex. .../.../.../data/
* `RFC.sh` will execute two python files:
  - `newtrain.py`: remove the repeated training data, output `newtrain`
  - `RFC.py`: build the a random forest as trained model, and predict the testing data as `ans.csv`

## File List
* `newtrain.py`, `RFC.py`, `RFC.sh`: main program
* `Report.pdf`: report
* `class_to_vector.txt`: a transfer list of training data
* `training_attack_types.txt`: a transfer list of training data label
