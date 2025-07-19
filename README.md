# 🤖 AI Interview Preparation Assistant

This project is an AI-powered assistant that generates interview questions and model answers based on selected topics and difficulty levels.

## 🧠 Tech Stack

- **Python**
- **OpenAI GPT API**
- **Streamlit** – for the user interface
- **Google Colab** – for experimentation and development

---

## 🚀 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-interview-prep.git
cd ai-interview-prep
```

### 2. Create & Activate a Virtual Environment

#### On **Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

#### On **macOS/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Using `requirements.txt`:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install streamlit openai
```

### 4. Run the Streamlit App
```bash
streamlit run app.py
```

---

## 📌 Notes

- Make sure you have a valid **OpenAI API key**. You can enter it in the sidebar of the Streamlit app.
- It's recommended to use a **virtual environment** to avoid package conflicts.
- To stop the app, press `Ctrl + C` in the terminal.

---

## 🧪 Optional: Run in Google Colab

You can also experiment in a [Google Colab notebook](https://colab.research.google.com/) for quick testing. Just ensure your OpenAI API key is safely handled using environment variables or notebook secrets.

---

## 📄 License

MIT License – feel free to use, modify, and share!
