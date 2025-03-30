import streamlit as st
import pandas as pd
import numpy as np
from hmmlearn import hmm
import matplotlib.pyplot as plt
import networkx as nx
import os
from PIL import Image

st.set_page_config(
    page_title="Tiger Migration Pattern Prediction",
    page_icon="🐅",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_data(file):
    try:
        xls = pd.ExcelFile(file)
        data_sheets = {sheet_name: xls.parse(sheet_name) for sheet_name in xls.sheet_names}
        return data_sheets
    except Exception as e:
        st.error(f"Error loading the dataset: {e}")
        return None

def fit_hmm_and_decode(data, n_states=3, n_iter=100):
    data = data.select_dtypes(include=[np.number]).dropna()
    if data.shape[1] == 0:
        st.warning("No numerical data available in this dataset.")
        return None

    X = data.values
    X = X.reshape(-1, 1) if X.ndim == 1 else X
    
    model = hmm.GaussianHMM(n_components=n_states, covariance_type="diag", n_iter=n_iter)
    model.fit(X)
    logprob, hidden_states = model.decode(X, algorithm="viterbi")
    
    state_labels = {
        0: "Localized Movement",
        1: "Exploratory Movement",
        2: "Migration"
    }
    labeled_states = [state_labels.get(state, "Unknown State") for state in hidden_states]
    return labeled_states

def draw_fsm(hidden_states, n_states):
    """
    Draws a finite state machine (FSM) diagram representing the transitions between states.
    """
    state_mapping = {state: idx for idx, state in enumerate(set(hidden_states))}
    hidden_states_int = [state_mapping[state] for state in hidden_states]
    
    transition_matrix = np.zeros((n_states, n_states))
    for i in range(len(hidden_states_int) - 1):
        transition_matrix[hidden_states_int[i], hidden_states_int[i + 1]] += 1
    
    transition_matrix = np.nan_to_num(
        transition_matrix / transition_matrix.sum(axis=1, keepdims=True)
    )

    G = nx.DiGraph()
    state_labels = {v: k for k, v in state_mapping.items()}
    G.add_nodes_from(state_labels.keys())

    for i in range(n_states):
        for j in range(n_states):
            if transition_matrix[i, j] > 0:
                G.add_edge(i, j, weight=transition_matrix[i, j])

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=5000)
    nx.draw_networkx_labels(G, pos, labels=state_labels, font_size=10)
    nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=20, edge_color="gray")
    edge_labels = nx.get_edge_attributes(G, "weight")
    formatted_edge_labels = {key: f"{value:.2f}" for key, value in edge_labels.items()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=formatted_edge_labels, font_size=8)
    plt.title("Finite State Machine Representation", fontsize=14)
    st.pyplot(plt.gcf())  
    plt.clf()  

def main():
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 48px;">🐅 Tiger Migration Pattern Prediction</h1>
        """, 
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('tiger.jpg'); /* Replace with a valid URL */
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )
    
    st.markdown("## About the Project")
    st.write(
        """
        This website uses advanced AI models to predict tiger migration patterns. 
        Understanding tiger movement is crucial for conservation efforts, 
        ensuring the survival of this majestic species. 
        """
    )
    st.write(
        """
        ### How It Works:
        - Upload a dataset in Excel format containing tiger movement data.
        - The model analyzes the data using a Hidden Markov Model.
        - It predicts tiger movement patterns categorized as:
          - **Localized Movement**: Restricted area, possibly resting or in home range.
          - **Exploratory Movement**: Traveling or searching for a new territory.
          - **Migration**: Moving between different regions.
        """
    )

    st.sidebar.header("Upload Data")
    uploaded_file = st.sidebar.file_uploader("Upload your migration dataset (Excel format):", type=["xlsx"])

    if uploaded_file:
        data_sheets = load_data(uploaded_file)
        
        if data_sheets is not None:
            sheet_names = list(data_sheets.keys())
            sheet_choice = st.sidebar.selectbox("Select Sheet to Analyze", sheet_names)
            data = data_sheets[sheet_choice]
            
            st.write(f"## Data from Sheet: {sheet_choice}")
            st.dataframe(data.head())
            
            if st.button("Run Migration Prediction"):
                with st.spinner("Running Hidden Markov Model..."):
                    hidden_states = fit_hmm_and_decode(data)
                    if hidden_states is not None:
                        st.write("## Predicted Migration Patterns")
                        state_count = pd.Series(hidden_states).value_counts()
                        st.bar_chart(state_count)

                        st.write("### Finite State Machine Representation")
                        draw_fsm(hidden_states, n_states=3)


if __name__ == "__main__":
    main()


