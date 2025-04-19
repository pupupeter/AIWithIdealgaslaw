# AIWithIdealgaslaw
AIWithIdealgaslaw use


# Ideal Gas Law AI Simulator

## 1. Project Overview

This project is an AI simulator built using Gradio, designed to handle questions related to the ideal gas law equation PV = nRT. It performs the corresponding calculations and visualizes the P-V curve. Users can input questions, and the AI assistant will compute the answer and provide an explanation from the AI professor.

## 2. Key Components

### 2.1 Gradio
- **Web Interface**: A simple and intuitive web interface that allows users to interact with the AI simulator.
- **Real-Time Feedback**: Users can directly input questions and view the AI simulator's computation results and explanations.

### 2.2 AI Agents
- **Assistant AI**: Calculates the answer based on the input question.
- **Professor AI**: Provides theoretical explanations and reasoning on how the problem is solved.

### 2.3 Visualization
- **P-V Curve Plotting**: Plots the P-V curve based on user input, showing the relationship between pressure and volume.

## 3. Quickstart

### 3.1 System Requirements

Make sure your development environment meets the following requirements:

- Python 3.8 or later
- pip package manager installed

### 3.2 Install Dependencies

Run the following command to install the required dependencies in your project folder:

```
pip install smolagents
pip install gradio
pip install flask
pip install plotly

```

### 3.3 Run the Application

```
python app.py or agents.py
```


app.py :

https://github.com/pupupeter/AIWithIdealgaslaw/blob/main/app.py

agents.py :

https://github.com/pupupeter/AIWithIdealgaslaw/blob/main/agents.py

#### Once started, Gradio or flask will automatically launch a web interface at the following URL:

and enter your questions and interact with the AI assistant and professor.


### 4. System Architecture

```

+--------------------------+
|      User Input UI       |
| (Gradio Web Interface)   |
+------------+-------------+
             |
             v
  +-----------------------------+
  |     Multi-Agent Controller |
  | (Route to TA / Teacher AI) |
  +-------------+---------------+
                | 
    +-----------+------------+
    |                        |
    v                        v
[Assistant AI]         [Professor AI]
(Computation / Solving)   (Theory / Explanation)
    |                        |
    +-----------+------------+
                |
                v
        +----------------+
        | Answer Merger  |
        | (Markdown Form) |
        +--------+--------+
                 |
                 v
     +----------------------------+
     | Visualization Generator   |
     | (Matplotlib P-V Curve)    |
     +----------------------------+
                 |
                 v
       +-----------------------------+
       | Gradio or flaskOutput Panel |
       +-----------------------------+

```
