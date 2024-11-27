Here's a step-by-step guide to set up and run the Pointing Poker project on your machine:

---

### **1. Install Required Tools**

#### **a. Install Python**
Ensure Python 3.7 or later is installed on your machine.

- Check Python version:
  ```bash
  python --version
  ```
  or
  ```bash
  python3 --version
  ```
- If not installed, download and install Python from [python.org](https://www.python.org/downloads/).

---

#### **b. Install Pip**
Pip (Python's package manager) usually comes with Python installations. Verify with:
```bash
pip --version
```
If not installed, follow [pip installation instructions](https://pip.pypa.io/en/stable/installation/).

---

#### **c. Install Streamlit**
Streamlit is the framework we'll use. Install it using pip:
```bash
pip install streamlit
```

---

### **2. Set Up the Project**

#### **a. Create a Project Directory**
Create a folder for your project:
```bash
mkdir pointing-poker
cd pointing-poker
```

#### **b. Create a Python File**
Create a file named `app.py` in the project directory:
```bash
touch app.py
```
Paste the provided code into `app.py`.

#### **c. Install Additional Dependencies**
If your app uses external libraries like `pandas`, install them:
```bash
pip install pandas
```

You can create a `requirements.txt` file for dependency management:
```bash
streamlit
pandas
```

Install dependencies from the file:
```bash
pip install -r requirements.txt
```

---

### **3. Run the Streamlit App**

Run the app using the Streamlit CLI:
```bash
streamlit run app.py
```

This will open the app in your default web browser at `http://localhost:8501`.

---

### **4. Optional: Use Virtual Environment**

To avoid conflicts with other Python projects, use a virtual environment:

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate it:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. Install dependencies inside the virtual environment:
   ```bash
   pip install -r requirements.txt
   ```

---

### **5. Testing and Debugging**

- Use the browser to navigate between pages and test functionality.
- Open the terminal running Streamlit to see error messages or logs.
- Modify the code in `app.py` to add features or fix bugs. Refresh the browser to apply changes.

---

### **6. Deployment (Optional)**

When ready, deploy the app to a cloud platform. Popular options include:

- **Streamlit Community Cloud** (Free and easy):
  1. Push your project to GitHub.
  2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud).
  3. Connect your GitHub repo and deploy.

- **Other Hosting Platforms**: 
  - Dockerize your app for deployment on AWS, GCP, or Azure.

---

If you encounter any issues during setup or running the project, feel free to ask for help!