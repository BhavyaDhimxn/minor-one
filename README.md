# 🐅 **Tiger Migration Pattern Prediction**

## 🚀 **Overview**
This is a **Streamlit-based web application** that uses **Hidden Markov Models (HMM)** to predict and visualize tiger migration patterns. The app helps conservationists and researchers analyze tiger movement data, aiding in better conservation strategies by identifying migration behaviors.

---

## 🔥 **Features**

✅ **Data Upload:**  
- Upload Excel files containing tiger movement data.  
- Automatically detects and processes numerical data.

🤖 **HMM Prediction:**  
- Classifies tiger movement into three states:  
    - 🟡 **Localized Movement:** Restricted area movement (resting or home range).  
    - 🔵 **Exploratory Movement:** Traveling or searching for new territory.  
    - 🔴 **Migration:** Long-distance movement between regions.  

📊 **Visualization:**  
- **Bar Chart:** Displays the frequency of each movement state.  
- **Finite State Machine (FSM):** Visualizes transitions between states with probabilities.  

🌄 **Aesthetic Design:**  
- Tiger image background for visual appeal.  

---

## ⚙️ **How It Works**

1. **Upload Dataset:**  
    - Upload an Excel file (`.xlsx`) containing tiger movement data.  
    - The app automatically detects numerical columns.  

2. **Run HMM Prediction:**  
    - Classifies movements into **three states** using HMM.  
    - Displays the state frequency and transition probabilities.  

3. **Data Visualization:**  
    - **Bar Chart:** Shows the distribution of movement states.  
    - **FSM:** Visualizes transitions between states.

---

## 💻 **Tech Stack**

- **Frontend:** Streamlit  
- **Backend:** Python (`hmmlearn` for HMM)  
- **Data Visualization:** `matplotlib`, `networkx`, `pandas`  
- **Image Processing:** `Pillow (PIL)`  

---

## 📦 **Project Structure**


```

📁 Tiger-Migration-Prediction

 ├── Dockerfile              # Docker configuration

 ├── requirements.txt        # Python dependencies

 ├── tiger.jpg               # Background image

 ├── app.py                  # Main Streamlit application script

 ├── README.md               # Documentation

 └── data/                   # Directory for sample Excel data

```

---

## 🐳 **Run with Docker**

1\. **Build the Docker Image**

```bash

docker build -t tiger-migration-app .

```

2\. **Run the Docker Container**

```bash

docker run -p 8501:8501 tiger-migration-app

```

3\. **Access the App**

Open your browser and navigate to:

```

http://localhost:8501

```

---

## ⚡ **Installation and Running Locally**

1\. **Clone the Repository**

```bash

git clone <repository_url>

cd Tiger-Migration-Prediction

```

2\. **Create a Virtual Environment**

```bash

python3 -m venv venv

source venv/bin/activate  # For Windows: venv\Scripts\activate

```

3\. **Install Dependencies**

```bash

pip install -r requirements.txt

```

4\. **Run the Streamlit App**

```bash

streamlit run app.py

```

---

## 📊 **Usage Instructions**

1\. Upload a dataset in Excel format.

2\. Select the desired sheet containing tiger movement data.

3\. Click on **"Run Migration Prediction"**.

4\. View the predicted movement patterns and visualize them through:

    - **Bar chart**

    - **Finite State Machine (FSM)**

---

## 🔥 **Sample Dataset**

- You can test the application using sample Excel files in the `data/` directory.

---

## 🛠️ **Dependencies**

- `streamlit`

- `pandas`

- `numpy`

- `hmmlearn`

- `matplotlib`

- `networkx`

- `pillow`

---

## 🐛 **Troubleshooting**

- **Blank Screen Issue:** Ensure the Docker container exposes the app on `0.0.0.0` and the port is mapped correctly.

- **Image Not Loading:** Verify the path to `tiger.jpg` in the `Dockerfile` and `app.py`.

- **Missing Libraries:** Install missing dependencies using:

```bash

pip install -r requirements.txt

```

---

## 📝 **Contributing**

- Feel free to fork the repository and submit pull requests.

- For major changes, open an issue first to discuss the changes.

---

## 💡 **Acknowledgments**

- Inspired by conservation efforts to track and protect endangered tigers.

- Developed using Streamlit and HMM algorithms.

```

✅ This `README.md` covers:

- Project overview

- Features

- Installation steps (both locally and with Docker)

- Usage instructions

- Troubleshooting tips

- License and acknowledgments