# data-science-training
Training exercises

How to commit & push changes from Jupyter Notebooks to GitHub:
  1. Make changes in the file saved in the folder where I cloned the repositoy: C:\Users\franz\Documents\Git Repository\data-science-training
  2. Open Git Bash
  3. Navigate to the above folder using command "cd"
  4. Enter "git add "workbook name.ipynb" to track the file
  5. Enter "git commit -m "Add a note of the changes made"" to create a version - I can revert from this version any time
  6. Enter "git push" to push the file to Github


How to extract data from Kaggle?
1. Open Command Prompt
2. Navigate to the folder on the drive where this code is saved
3. Install kaggle (pip install kaggle)
4. Download API token from kaggle website (under profile -> settings)
5. Move downloaded token to the folder C:\User.kaggle
6. In the command prompt, enter kaggle competitions download -c [name of dataset]
