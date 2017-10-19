import sys

sys.path.append('.\eeg_model\mach_learning_dir\classifier')
from function_classifier import RegularizedDiscriminantAnalysis
import numpy as np


# Function required for matlab file which checks consistency
def test_rda(x, y, z):
    rda = RegularizedDiscriminantAnalysis()
    rda.fit(x, y)

    prb = rda.get_proba(z)

    return [np.array(rda.cov), np.array(rda.reg_inverse_cov), np.array(
        rda.means), prb]


# dim_x = 2
# num_x_p = 2000
# num_x_n = 500
#
# x_p = 2 * np.random.randn(num_x_p, dim_x)
# x_n = 4 + np.random.randn(num_x_n, dim_x)
# y_p = [1] * num_x_p
# y_n = [0] * num_x_n
#
# x = np.concatenate(np.asarray([x_p, x_n]), 0)
# y = np.concatenate(np.asarray([y_p, y_n]), 0)
#
# # out = test_rda(x, y)
#
# rda = RegularizedDiscriminantAnalysis()
#
# z = rda.fit_transform(x, y)
# rda.fit(x, y)
# z_2 = rda.transform(x)
