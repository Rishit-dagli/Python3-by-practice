# Decision Trees and Random Forests in Python

We are using the [Kyphosis-dataset](https://www.kaggle.com/abbasit/kyphosis-dataset) provided by [Abdul Basit](https://www.kaggle.com/abbasit). The same is provided in the repository along with notebook.

A brief introduction to Decision Trees and Random Forests:
- Decision trees use machine learning to identify key differentiating factors between the different classes of our data. By doing so, decision trees can take some input data and predict a class by running the data through a set of differentiating questions that it forms using machine learning.
- The most widely used algorithm when actually constructing decision trees is known as ID3. The ID3 algorithm makes use of two concepts known as ‘entropy’ and ‘information gain’ to design the decision tree.
- Despite all the merits of the decision tree model, there is a limit to how accurately one individual decision tree can perform classification. Thus, rather than using just one decision tree, very often, we tend to create a set of decision trees that perform classification. Such a model is known as a ‘Random Forest Classifier’ and it yields a significantly higher accuracy than that of an individual decision tree.
- One of the main reasons Random Forest Classifiers are so effective is because each tree in the forest is unrelated to the other trees in the forest to a great extent, a condition achieved due to the random sampling of data for the training of each individual tree (bagging).

Main applications: Classification and Regression

**Additional Reading**
- https://medium.com/analytics-vidhya/machine-learning-decision-trees-and-random-forest-classifiers-81422887a544
- https://towardsdatascience.com/decision-trees-and-random-forests-df0c3123f991 