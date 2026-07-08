import numpy as np
import sklearn

# You are allowed to import any submodules of numpy or sklearn e.g. sklearn.metrics.accuracy_score to calculate accuracy of a learnt model
# You are not allowed to use other libraries such as scipy, keras, tensorflow etc

# SUBMIT YOUR CODE AS A SINGLE PYTHON (.PY) FILE INSIDE A ZIP ARCHIVE
# THE NAME OF THE PYTHON FILE MUST BE submit.py

# DO NOT CHANGE THE NAME OF THE METHODS my_map, my_params etc BELOW
# THESE WILL BE INVOKED BY THE EVALUATION SCRIPT. CHANGING THESE NAMES WILL CAUSE EVALUATION FAILURE

# You may define any new functions, variables, classes here

################################
# Non Editable Region Starting #
################################
def my_map( X ):
################################
#  Non Editable Region Ending  #
################################

	# Use this method to map raw features to proper embeddings
	# Your embeddings will be used to train a linear SVM model
	
	return X_map

################################
# Non Editable Region Starting #
################################
def my_params( X_map, X_raw, y ):
################################
#  Non Editable Region Ending  #
################################

	# Use this method to return your preferred hyperparameters
	# The original and mapped train features and train labels have been supplied in case you wish to perform hyperparameter turning via validation.
	# You may ignore the inputs and provide fixed values of the hyperparameters that you found to work well on the public train/test set.
	# You need not set every single hyperparameter. The ones you do not set will be set to their default value. Please refer to the API for sklearn.svm.LinearSVC for the default values.
	
	return my_params

