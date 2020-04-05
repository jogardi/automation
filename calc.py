import clipboard as cb
from math import *
from math import log
from collections import defaultdict
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import itertools
import random
import pint
import glob
import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
from bash import *
import os, sys


ureg = pint.UnitRegistry()


def clean(line):
    if len(line) == 0 or not line[0].isdigit():
        return line
    else:
        return " ".join(line.split(" ")[1:])


def rm_nums():
    cb.copy("\n".join([clean(x) for x in cb.paste().split("\n")]))


default_domain = np.linspace(1 / 1000, 10, 10 * 100)


def plot_func(function, domain=default_domain, yscale="linear", xscale="linear"):
    plt.figure()
    vfunc = np.vectorize(function)
    plt.scatter(domain, vfunc(domain))
    plt.yscale(yscale)
    plt.xscale(xscale)
    plt.show(block=False)


def entropy(*probs):
    if len(probs) == 1:
        p = probs[0]
        return stats.entropy([p, 1 - p], base=2)
    else:
        return stats.entropy(probs, base=2)


lg = lambda x: log(x, 2)

arr = np.array([[1, 2], [3, 4]])
