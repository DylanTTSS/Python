# # 8-1 Message
# def display_message():
#     print("In this Chapter, We'll learn something about the function")
#
#
# display_message()
#
#
# # 8-2 Favorite books
# def favorite_book(title):
#     print(f"One of my favorite book is {title.title()}")
#
#
# favorite_book('Screaming')

# from sklearn import datasets, model_selection, discriminant_analysis
#
#
# ###############################################################################
# # 用莺尾花数据集
# def load_data():
#     iris = datasets.load_iris()
#     return model_selection.train_test_split(iris.data, iris.target, test_size=0.25, random_state=0,
#                                             stratify=iris.target)
#     # 返回为: 一个元组，依次为：训练样本集、测试样本集、训练样本的标记、测试样本的标记
#
#
# ###############################################################################
# def plot_LDA(converted_X, y):
#     '''
#     绘制经过 LDA 转换后的数据
#     :param converted_X: 经过 LDA转换后的样本集
#     :param y: 样本集的标记
#     :return:  None
#     '''
#     from mpl_toolkits.mplot3d import Axes3D
#     import matplotlib.pyplot as plt
#     fig = plt.figure()
#     ax = Axes3D(fig)
#     colors = 'rgb'
#     markers = 'o*s'
#     for target, color, marker in zip([0, 1, 2], colors, markers):
#         pos = (y == target).ravel()
#         X = converted_X[pos, :]
#         ax.scatter(X[:, 0], X[:, 1], X[:, 2], color=color, marker=marker,
#                    label="Label %d" % target)
#     ax.legend(loc="best")
#     fig.suptitle("Iris After LDA")
#     plt.show()
#
#
# ###############################################################################
# import numpy as np
#
# x_train, x_test, y_train, y_test = load_data()
# X = np.vstack((x_train, x_test))  # 沿着竖直方向将矩阵堆叠起来，把训练与测试的数据放一起来看
# Y = np.vstack((y_train.reshape(y_train.size, 1), y_test.reshape(y_test.size, 1)))  # 沿着竖直方向将矩阵堆叠起来
# lda = discriminant_analysis.LinearDiscriminantAnalysis()
# lda.fit(X, Y)
# converted_X = np.dot(X, np.transpose(lda.coef_)) + lda.intercept_
# plot_LDA(converted_X, Y)


from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# 加载莺尾花数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0, stratify=y)

# 初始化并训练线性判别分析模型
lda = LinearDiscriminantAnalysis()
lda.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = lda.predict(X_test)

# 输出模型的准确度
accuracy = lda.score(X_test, y_test)
print(f'Model Accuracy: {accuracy:.2f}')

