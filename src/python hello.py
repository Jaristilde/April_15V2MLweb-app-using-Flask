import pickle
from flask import Flask, jsonify, request
import pandas as pd
model_path = '/workspaces/April_15MLweb-app-using-Flask/src/decision_tree_classifier_default_42.sav'
model = pickle.load(open(model_path, 'rb'))


