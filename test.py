# Copyright 2018 Daniel Selsam. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import math
import numpy as np
import random
import datetime
import subprocess
import pickle
import sys
import os
import argparse
from options import add_neurosat_options
from neurosat import NeuroSAT

parser = argparse.ArgumentParser()
add_neurosat_options(parser)

parser.add_argument('--test_dir', action='store', dest='test_dir', type=str, help='Directory with directories of testation data')
parser.add_argument('--restore_id', action='store', dest='restore_id', type=int)
parser.add_argument('--restore_epoch', action='store', dest='restore_epoch', type=int)
# parser.add_argument('--n_rounds', action='store', dest='n_rounds', type=int)

opts = parser.parse_args()
setattr(opts, 'run_id', None)
setattr(opts, 'n_saves_to_keep', 1)

print(opts)

g = NeuroSAT(opts)
g.restore()

results = g.test(opts.test_dir)
for (test_filename, etest_cost, accuracy_by_var, accuracy_by_problem) in results:
    print("%s %.4f (accuracy by var: %.4f | accuracy by problem: %.4f)" % (test_filename, etest_cost, accuracy_by_var, accuracy_by_problem))
