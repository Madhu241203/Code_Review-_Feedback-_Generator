# Code Review Feedback Generator

## Overview

The Code Review Feedback Generator is a Generative AI-based application that analyzes code snippets and provides structured feedback without executing the code. The system helps developers identify potential issues, improve code quality, and receive actionable suggestions during the early stages of development.

This project uses:

* Python
* Streamlit (User Interface)
* Ollama
* Llama 3 Large Language Model

---

## Problem Statement

Software teams benefit from code reviews, but manual review takes time and depends heavily on reviewer availability and expertise.

The goal of this project is to build an AI-powered code review assistant that:

* Accepts a code snippet as input
* Analyzes the code without execution
* Identifies potential issues
* Suggests improvements
* Assigns a code quality rating
* Generates a concise review summary

---

## Features

* Automated code review
* Detects syntax and formatting issues
* Provides improvement suggestions
* Evaluates code quality
* Generates structured JSON output
* User-friendly web interface using Streamlit
* Works locally using Ollama (No paid API required)

---

## Technologies Used

| Technology | Purpose                  |
| ---------- | ------------------------ |
| Python     | Backend Development      |
| Streamlit  | Web Interface            |
| Ollama     | Local LLM Runtime        |
| Llama 3    | Code Review Analysis     |
| JSON       | Structured Output Format |

---

## Project Structure

```text
CodeReviewGenerator/
│
├── app.py
├── model.py
├── requirements.txt
└── README.md
```

---

## Installation

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd CodeReviewGenerator
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama from:

https://ollama.com

Verify installation:

```bash
ollama --version
```

---

## Download Llama 3 Model

```bash
ollama pull llama3
```

Verify:

```bash
ollama list
```

Expected output:

```text
NAME
llama3
```

---

## Running the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will open in your browser.

Default URL:

```text
http://localhost:8501
```

---

## Input Example

```python
for i in range(5):
print(i)
```

---

## Expected Output

```json
{
  "identified_issues": [
    "The print statement is not indented inside the loop."
  ],
  "improvement_suggestions": [
    "Indent the print statement so it becomes part of the loop body."
  ],
  "code_quality_level": "Low",
  "review_summary": "The code contains an indentation error that will cause a syntax error in Python."
}
```

---

## Output Schema

```json
{
  "identified_issues": ["string"],
  "improvement_suggestions": ["string"],
  "code_quality_level": "string",
  "review_summary": "string"
}
```

---

## Workflow

1. User enters a code snippet.
2. Streamlit sends the code to the review engine.
3. Ollama processes the prompt using Llama 3.
4. The model analyzes the code without execution.
5. Structured feedback is generated.
6. Results are displayed on the Streamlit interface.

---

## Test Cases

### Test Case 1 – Correct Code

Input:

```python
for i in range(5):
    print(i)
```

Expected:

* No major issues
* High code quality

---

### Test Case 2 – Syntax Error

Input:

```python
for i in range(5):
print(i)
```

Expected:

* Indentation issue detected
* Low code quality

---

### Test Case 3 – Poor Readability

Input:

```python
x=[1,2,3]
s=0
for a in x:
 s+=a
print(s)
```

Expected:

* Naming concerns identified
* Readability improvements suggested
* Medium code quality

---

## Advantages

* Reduces manual review effort
* Provides instant feedback
* Encourages coding best practices
* Supports learning and skill development
* No code execution required
* Runs locally without API costs

---

## Future Enhancements

* Multi-language code support
* Advanced security vulnerability detection
* Integration with GitHub repositories
* Downloadable review reports
* Support for multiple LLMs
* Code quality scoring dashboard

---

## Conclusion

The Code Review Feedback Generator demonstrates how Generative AI can assist developers by providing automated code analysis and actionable feedback. By leveraging Ollama and Llama 3, the system delivers efficient, cost-effective, and scalable code review capabilities while maintaining a simple and user-friendly interface.
