# PyData Sri Lanka - UniConnect 2024  

## **Project Overview**  
This repository contains my work for the **PyData Sri Lanka - UniConnect 2024** competition. The project involved data analysis, visualization, natural language processing, and dashboard creation, showcasing a comprehensive application of data science skills.  

The case study, titled *"From Grapes to Glass - The Story of Wine"*, focuses on analyzing wine data from multiple countries. The tasks span data preparation, NLP using HuggingFace, and creating an interactive dashboard.  

---

## **Repository Structure**  
The repository is structured as follows:  

- **data/**  
  Contains the provided datasets, including 8 CSV files for wine data and a separate file for wine reviews.  

- **notebooks/**  
  - `data_preparation.ipynb`: Jupyter notebook for data cleaning, exploration, and merging.  
  - `huggingface_nlp.ipynb`: Notebook for deploying a zero-shot classification model on wine reviews.  

- **dashboard/**  
  - `dashboard.py`: Code for creating an interactive dashboard using Plotly Dash.  
  - `dashboard_video.mp4`: A screen recording of the final dashboard presentation.  

- **presentation/**  
  - `presentation.pdf`: A concise 5-slide presentation summarizing the project workflow and insights.  

- **README.md**  
  This file provides a detailed overview of the project and its structure.  

---

## **Tasks and Deliverables**  

### **1. Data Preparation**  
- Combined 8 CSV files into a single DataFrame (`wine_df`).  
- Cleaned the data by handling duplicates, null values, and outliers.  
- Extracted new features like `Country` and `Country_Region` from the `Region` column.  
- Expanded the `Food Pairings` column into 21 new binary columns for better analysis.  

### **2. Natural Language Processing (NLP)**  
- Deployed a zero-shot classification model from HuggingFace to classify wine reviews into 4 categories:  
  - Talks about food combinations.  
  - Talks about taste.  
  - Talks about value for money.  
  - Other.  
- Added the predicted labels to the dataset and visualized category distributions.  

### **3. Interactive Dashboard**  
- Designed an engaging and interactive dashboard using **Plotly Dash**.  
- Visualized key insights about wine ratings, prices, food pairings, and regions.  
- Included multiple interactive charts, such as bar charts, scatter plots, and filters.  

### **4. Version Control**  
- Followed best practices with Git and GitHub:  
  - Maintained branches for each task.  
  - Used meaningful commit messages and pull requests.  
  - Ensured a conflict-free main branch.  

---

## **Technologies Used**  
- **Programming Languages**: Python  
- **Libraries**: Pandas, NumPy, Plotly Dash, HuggingFace Transformers, Matplotlib, Seaborn  
- **Tools**: Jupyter Notebook, Git, GitHub  

---

## **How to Run**  

### **1. Data Preparation**  
1. Open `Group13-Assignment/Task_02/task_02.ipynb` in Jupyter Notebook.  
2. Execute the cells sequentially to load, clean, and prepare the dataset.  

### **2. NLP Task**  
1. Open `Group13-Assignment/Task_03/task_03_Combined.ipynb`.  
2. Ensure the HuggingFace Transformers library is installed.  
3. Run the notebook to classify the reviews and visualize the results.  

### **3. Dashboard**  
1. Navigate to the `Group13-Assignment/Task_04/task04.ipynb` folder.  
2. Run `dashboard.py` using the command:  
   ```bash  
   python dashboard.py  
   ```  
3. Open the provided localhost link to interact with the dashboard.  

## **Deliverables**  
- GitHub Repository: Includes all Python scripts, notebooks, and data.  
- Video Clip: Demonstrates the interactive dashboard functionality.  
- Presentation: Summarizes the project and its insights.  

---
