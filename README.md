# 🧠 RAG-Powered PDF QA Bot

This repository contains a minimal Retrieval-Augmented Generation (RAG) pipeline for answering questions based on the content of a PDF file using **LangChain**, **OpenAI GPT**, **HuggingFace Embeddings**, and **FAISS**.

---

## ✨ Features

- ✅ Load and parse PDF documents
- ✅ Chunk text intelligently using LangChain
- ✅ Embed text using HuggingFace models (`thenlper/gte-small`)
- ✅ Store embeddings in a FAISS vector index
- ✅ Use GPT-3.5-Turbo to answer user queries with retrieved context
- ✅ `.env`-based secret management

---

## 📦 Tech Stack

- [LangChain](https://python.langchain.com/)
- [OpenAI GPT-3.5](https://platform.openai.com/docs/models/gpt-3-5)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Python dotenv](https://pypi.org/project/python-dotenv/)
- [PyPDF](https://pypi.org/project/pypdf/)

---

## 📁 File Structure

```
support-rag-bot/
│
├── main.py                  # Main RAG pipeline
├── support-policy.pdf       # Source document
├── .env                     # Environment variables (API keys)
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

---

## ⚙️ Setup

### 1. Clone the repo

```bash
git clone git@github.com:andrewbilous/support-rag-bot.git
cd support-rag-bot
```

### 2. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` file

Create a `.env` file in the project root with the following content:

```env
OPENAI_API_KEY=your-openai-api-key
HUGGINGFACEHUB_API_TOKEN=your-huggingface-token
```

---

## ▶️ Usage

Make sure you have a PDF file named `support-policy.pdf` in the project root.

Then run the main script:

```bash
python main.py
```

To query the document:

```python
response = qa_chain.run("What is the refund policy?")
print(response)
```

You can modify the question inside `main.py` or turn this into an interactive CLI later.

---

## 📌 Notes

- `ChatOpenAI` is used as the LLM to generate final answers.
- `FAISS` provides fast in-memory similarity search over embedded chunks.
- Embedding is done with HuggingFace’s `thenlper/gte-small` model.
- The PDF is parsed and split into overlapping chunks for better context retrieval.

---

## 📄 requirements.txt (example)

```txt
langchain
openai
python-dotenv
transformers
torch
faiss-cpu
pypdf
```

---

## 🚧 Future Improvements

- [ ] Add Gradio or Streamlit frontend
- [ ] Add support for multiple PDFs
- [ ] Cache FAISS index
- [ ] Switch to local LLM for offline use (e.g. LLaMA or Mistral)

---

## 👨‍💻 Author

**Andrii Bilous**  
[GitHub Profile](https://github.com/andrewbilous)

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).
