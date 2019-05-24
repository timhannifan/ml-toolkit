# Constructed from https://github.com/rayidghani/magicloops
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import ParameterGrid
import grids

clfs = {
    'RF': RandomForestClassifier(n_estimators=50, n_jobs=-1),
    'ET': ExtraTreesClassifier(n_estimators=10, n_jobs=-1, criterion='entropy'),
    'AB': AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), algorithm="SAMME", n_estimators=200),
    'LR': LogisticRegression(penalty='l1', C=1e5),
    'SVM': svm.SVC(kernel='linear', probability=True, random_state=0),
    'GB': GradientBoostingClassifier(learning_rate=0.05, subsample=0.5, max_depth=6, n_estimators=10),
    'NB': GaussianNB(),
    'DT': DecisionTreeClassifier(),
    'SGD': SGDClassifier(loss="hinge", penalty="l2"),
    'KNN': KNeighborsClassifier(n_neighbors=3) 
}

def define_clfs_params(grid_size):
    """Define defaults for different classifiers.
    Define four types of grids:
    Tiny: bare minimum
    Test: larger than tiny, more models.
    Small: small grid
    Large: Larger grid that has a lot more parameter sweeps
    """
    if (grid_size == 'large'):
        return clfs, grids.LARGE
    elif (grid_size == 'small'):
        return clfs, grids.SMALL
    elif (grid_size == 'test'):
        return clfs, grids.TEST
    elif (grid_size == 'tiny'):
        return clfs, grids.TINY
    else:
        return 0, 0
