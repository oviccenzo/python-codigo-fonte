import numpy as np
import pandas as pd
import os , json
import joblib
from pathlib import Path
from flask import Flask, render_template, request, jsonify

data_path = Path("data/dataset_alunos_evasao.csv")
model_dir = Path("models")
model_dir.mkdir(parents=True, exist_ok=True)
model_path = model_dir / "model_logreg.pkl"

def treinar_modelo_se_preciso():
    if model_path.exists():
        return

    df = pd.read_csv(data_path)
    df.columns = [c.strip() for c in df.columns]

    target = pd.read_csv(data_path)
    X = df.drop(columns=[target])
    y = df[target].map({"Evadiu" : 1, "Concluiu" : 0})

    numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_cols = [c for c in X.columns if c not in numeric_cols]