## K Mean Clustering
We have use the **Iris Dataset** which can be easily loaded using:
```python
from sklearn import datasets
iris = datasets.load_iris()
```
That's it the dataset is loaded.

Lets have a brief look about **K Mean Clustering**:

- K Means Clustering is a machine learning algorithm used to partition or cluster data points by calculating squared Euclidean distance between the points and cluster centers.
- Firstly the cluster centers are initialized random and later the distance is calculated and the centers moves based on the distance from the data points.
- This can be observed in the animation from wikipedia below:

![Animation](K-means_convergence.gif)

**The big question is how to determine the optimal number of cluster :**
### Elbow Method
The basic intution is to calculate the sum of mean square errors and plot the graph as below:

