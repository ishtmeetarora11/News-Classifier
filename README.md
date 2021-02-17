# News-Classifier

The script takes in a news text as an input and predicts top 3 categories as an output. It also appends the predicted news in the training set.
Once the file is executed it will run indefinitely until it gets a char ‘n’ as an input before the news text is given.

If the csv file exceeds a limit of 1184 a new file is created. And hence we get a cluster of csv file instead of a single file. 

We will get all the files using the directory command of OS and will only use the csv files to train the model.

 When the file is executed again the model (Naive Byes) is trained by greater and improved training data.

Python script can be executed once in 24 hrs when the traffic is low.

