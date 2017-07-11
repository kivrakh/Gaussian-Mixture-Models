from GMM_GMR import GMM_GMR
from matplotlib import pyplot as plt
import numpy as np

if __name__ == "__main__":
    data = np.loadtxt("data.txt", delimiter=',')
    data = data[:, 0:2].T
    gmm = GMM_GMR(4, 100)
    gmm.fit(data)
    fig = plt.figure()

    ax1 = fig.add_subplot(221)
    plt.title("Data")
    gmm.plot(ax=ax1, plotType="Data")

    ax2 = fig.add_subplot(222)
    plt.title("Gaussian States")
    gmm.plot(ax=ax2, plotType="Clusters")

    ax3 = fig.add_subplot(223)
    plt.title("Regression")
    gmm.plot(ax=ax3, plotType="Regression")

    ax4 = fig.add_subplot(224)
    plt.title("Clusters + Regression")
    gmm.plot(ax=ax4, plotType="Clusters")
    gmm.plot(ax=ax4, plotType="Regression")
    plt.show()