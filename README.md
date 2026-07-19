<<<<<<< HEAD
# 📁 MemoryVerse AI — Student Digital Identity System

> An AI-powered digital identity platform that lets students upload, organize, and semantically search their academic and professional achievements — certificates, resumes, projects, and internships — all in one place.

---

## 🎯 Problem Statement

Students accumulate certificates, project work, resumes, and internship records across multiple platforms (Coursera, GitHub, email, local drives). There is no single, intelligent system to consolidate this into a searchable, chronological "digital identity." MemoryVerse AI solves this by combining structured storage with AI-powered semantic understanding.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📤 **Document Upload** | Upload certificates, resumes, projects, and internship records with title & description |
| 🏷️ **AI Auto-Categorization** | Automatically tags documents (AI/ML, Cloud, Web Dev, Data Science, etc.) based on content |
| 🔍 **Semantic Search** | Search using natural language (e.g. *"Show my AI projects"*) — powered by sentence embeddings, not just keyword matching |
| 🕒 **Visual Timeline** | Chronological, color-coded timeline view of a student's entire achievement journey |
| 💾 **Persistent Storage** | SQLite for structured metadata + ChromaDB (vector database) for embeddings |

---

## 🧠 AI / NLP Components (Judging Criteria Alignment)

- **Embeddings**: Documents are converted into dense vector representations using `all-MiniLM-L6-v2` (Sentence Transformers).
- **Vector Database**: ChromaDB stores and indexes embeddings for fast similarity search.
- **Semantic Search**: User queries are embedded and matched against document embeddings using cosine similarity — enabling meaning-based retrieval instead of exact keyword matches.
- **NLP-based Auto-tagging**: Lightweight keyword/context analysis classifies documents into skill categories automatically at upload time.

---

## 🏗️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Structured Database**: SQLite
- **Vector Database**: ChromaDB
- **Embeddings Model**: Sentence Transformers (`all-MiniLM-L6-v2`)
- **Search**: Semantic (cosine similarity) search over embeddings

---

## 📂 Project Structure

```
memoryverse-ai/
│
├── app.py              # Main Streamlit application (UI + routing)
├── database.py         # SQLite schema & CRUD operations
├── embeddings.py        # Embedding generation, auto-tagging, semantic search
├── timeline.py          # Visual HTML/CSS timeline renderer
├── uploads/              # Uploaded document files (gitignored)
├── chroma_db/            # ChromaDB persistent vector store (gitignored)
├── memoryverse.db        # SQLite database (gitignored)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Architecture Overview

```
┌─────────────────┐
│   Streamlit UI    │  ← Upload form, search box, timeline view
└────────┬─────────┘
         │
         ▼
┌─────────────────┐        ┌──────────────────────┐
│   database.py      │◄──────►│   memoryverse.db (SQLite) │
│  (metadata storage) │        │  id, type, title, tags...  │
└────────┬─────────┘        └──────────────────────┘
         │
         ▼
┌─────────────────┐        ┌──────────────────────┐
│  embeddings.py      │◄──────►│   ChromaDB (chroma_db/)    │
│ - auto_tag()          │        │  vector embeddings          │
│ - add_document_       │        │  + metadata                  │
│   embedding()          │        └──────────────────────┘
│ - semantic_search()    │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   timeline.py       │  ← Renders chronological HTML/CSS timeline
└─────────────────┘
```

**Flow:**
1. User uploads a document with title/description via Streamlit UI.
2. File is saved locally; metadata + auto-generated tags are stored in SQLite.
3. Title + description text is encoded into a vector embedding and stored in ChromaDB.
4. On search, the query is embedded the same way and compared against stored embeddings using cosine similarity to retrieve the most semantically relevant documents.
5. All documents are rendered chronologically in an interactive timeline view.

---

## 🚀 Setup & Installation

### Prerequisites
- Python 3.10+
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/rithishkumar-07/memoryverse-ai.git
cd memoryverse-ai

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`.

> **Note:** On first run, the `all-MiniLM-L6-v2` embedding model (~90MB) will download automatically via Hugging Face. This requires an internet connection for the initial setup only — after that, it runs fully offline.

---

## 🎬 Demo Walkthrough

1. Select a document type (Certificate / Resume / Project / Internship).
2. Enter a title and short description, then upload the file.
3. The system auto-tags the document and generates its AI embedding.
4. Use the **Semantic Search** box to query in plain English, e.g. *"cloud computing skills"* or *"AI certifications"*.
5. Scroll down to view the **Timeline** — a visual, color-coded history of all uploaded achievements.

---

## 🔮 Future Enhancements

- RAG-based conversational Q&A over uploaded documents (retrieve + generate natural-language answers)
- OCR support for scanned certificate images
- Export digital identity as a shareable public profile / PDF portfolio
- Multi-user authentication and cloud deployment

---

## 📄 License

=======
# 📁 MemoryVerse AI — Student Digital Identity System

> An AI-powered digital identity platform that lets students upload, organize, and semantically search their academic and professional achievements — certificates, resumes, projects, and internships — all in one place.

---

## 🎯 Problem Statement

Students accumulate certificates, project work, resumes, and internship records across multiple platforms (Coursera, GitHub, email, local drives). There is no single, intelligent system to consolidate this into a searchable, chronological "digital identity." MemoryVerse AI solves this by combining structured storage with AI-powered semantic understanding.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📤 **Document Upload** | Upload certificates, resumes, projects, and internship records with title & description |
| 🏷️ **AI Auto-Categorization** | Automatically tags documents (AI/ML, Cloud, Web Dev, Data Science, etc.) based on content |
| 🔍 **Semantic Search** | Search using natural language (e.g. *"Show my AI projects"*) — powered by sentence embeddings, not just keyword matching |
| 🕒 **Visual Timeline** | Chronological, color-coded timeline view of a student's entire achievement journey |
| 💾 **Persistent Storage** | SQLite for structured metadata + ChromaDB (vector database) for embeddings |

---

## 🧠 AI / NLP Components (Judging Criteria Alignment)

- **Embeddings**: Documents are converted into dense vector representations using `all-MiniLM-L6-v2` (Sentence Transformers).
- **Vector Database**: ChromaDB stores and indexes embeddings for fast similarity search.
- **Semantic Search**: User queries are embedded and matched against document embeddings using cosine similarity — enabling meaning-based retrieval instead of exact keyword matches.
- **NLP-based Auto-tagging**: Lightweight keyword/context analysis classifies documents into skill categories automatically at upload time.

---

## 🏗️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Structured Database**: SQLite
- **Vector Database**: ChromaDB
- **Embeddings Model**: Sentence Transformers (`all-MiniLM-L6-v2`)
- **Search**: Semantic (cosine similarity) search over embeddings

---

## 📂 Project Structure

```
memoryverse-ai/
│
├── app.py              # Main Streamlit application (UI + routing)
├── database.py         # SQLite schema & CRUD operations
├── embeddings.py        # Embedding generation, auto-tagging, semantic search
├── timeline.py          # Visual HTML/CSS timeline renderer
├── uploads/              # Uploaded document files (gitignored)
├── chroma_db/            # ChromaDB persistent vector store (gitignored)
├── memoryverse.db        # SQLite database (gitignored)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Architecture Overview

```
┌─────────────────┐
│   Streamlit UI    │  ← Upload form, search box, timeline view
└────────┬─────────┘
         │
         ▼
┌─────────────────┐        ┌──────────────────────┐
│   database.py      │◄──────►│   memoryverse.db (SQLite) │
│  (metadata storage) │        │  id, type, title, tags...  │
└────────┬─────────┘        └──────────────────────┘
         │
         ▼
┌─────────────────┐        ┌──────────────────────┐
│  embeddings.py      │◄──────►│   ChromaDB (chroma_db/)    │
│ - auto_tag()          │        │  vector embeddings          │
│ - add_document_       │        │  + metadata                  │
│   embedding()          │        └──────────────────────┘
│ - semantic_search()    │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   timeline.py       │  ← Renders chronological HTML/CSS timeline
└─────────────────┘
```

**Flow:**
1. User uploads a document with title/description via Streamlit UI.
2. File is saved locally; metadata + auto-generated tags are stored in SQLite.
3. Title + description text is encoded into a vector embedding and stored in ChromaDB.
4. On search, the query is embedded the same way and compared against stored embeddings using cosine similarity to retrieve the most semantically relevant documents.
5. All documents are rendered chronologically in an interactive timeline view.

---

## 🚀 Setup & Installation

### Prerequisites
- Python 3.10+
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/rithishkumar-07/memoryverse-ai.git
cd memoryverse-ai

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`.

> **Note:** On first run, the `all-MiniLM-L6-v2` embedding model (~90MB) will download automatically via Hugging Face. This requires an internet connection for the initial setup only — after that, it runs fully offline.

---

## 🎬 Demo Walkthrough

1. Select a document type (Certificate / Resume / Project / Internship).
2. Enter a title and short description, then upload the file.
3. The system auto-tags the document and generates its AI embedding.
4. Use the **Semantic Search** box to query in plain English, e.g. *"cloud computing skills"* or *"AI certifications"*.
5. Scroll down to view the **Timeline** — a visual, color-coded history of all uploaded achievements.

---

## 🔮 Future Enhancements

- RAG-based conversational Q&A over uploaded documents (retrieve + generate natural-language answers)
- OCR support for scanned certificate images
- Export digital identity as a shareable public profile / PDF portfolio
- Multi-user authentication and cloud deployment

---

## 📄 License

>>>>>>> eee80de5179337e4aebdc1a752cb3ba7289daac6
This project is built for educational and hackathon demonstration purposes.