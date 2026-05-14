import streamlit as st
import joblib
from huggingface_hub import hf_hub_download

REPO_ID = "mankadevansh/carebot-model"

@st.cache_resource
def load_model():
    path = hf_hub_download(
    repo_id=REPO_ID,
    filename="model.pkl"
    )
    return joblib.load(path)

@st.cache_resource
def load_encoder():
    path = hf_hub_download(
    repo_id=REPO_ID,
    filename="encoder.pkl"
    )
    return joblib.load(path)

@st.cache_resource
def load_features():
    path = hf_hub_download(
    repo_id=REPO_ID,
    filename="features.pkl"
    )
    return joblib.load(path)
