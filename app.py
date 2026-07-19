import streamlit as st
import os
from datetime import datetime
from database import init_db, save_file_record, get_all_records
from embeddings import auto_tag, add_document_embedding, semantic_search
from timeline import render_timeline_html
import streamlit.components.v1 as components

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
init_db()

st.set_page_config(page_title="MemoryVerse AI", layout="wide")
st.title("📁 MemoryVerse AI — Student Digital Identity")

st.subheader("Upload your documents")

doc_type = st.selectbox("Document Type", ["Certificate", "Resume", "Project", "Internship"])
title = st.text_input("Title / Name (e.g. 'AWS Cloud Certificate')")
description = st.text_area("Short Description (optional)")
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "jpeg", "docx"])

if st.button("Upload"):
    if uploaded_file and title:
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        tags = auto_tag(f"{title} {description}")
        tags_str = ", ".join(tags)

        doc_id = save_file_record(
            doc_type=doc_type,
            title=title,
            description=description,
            file_path=file_path,
            upload_date=datetime.now().isoformat(),
            tags=tags_str
        )

        with st.spinner("Generating AI embedding..."):
            add_document_embedding(doc_id, title, description, doc_type)

        st.success(f"✅ '{title}' uploaded! Auto-tagged as: {tags_str}")
    else:
        st.error("Please add a title and select a file.")

st.divider()

# --- Semantic Search Section ---
st.subheader("🔍 Semantic Search")
search_query = st.text_input("Search (e.g. 'Show my AI projects')")
if search_query:
    results = semantic_search(search_query, n_results=5)
    if results["ids"][0]:
        for i, doc_id in enumerate(results["ids"][0]):
            meta = results["metadatas"][0][i]
            st.write(f"**{meta['title']}** ({meta['doc_type']})")
    else:
        st.info("No matching documents found.")

st.divider()
st.subheader("📋 Your Uploaded Documents")
records = get_all_records()
if records:
    for r in records:
        st.write(f"**{r[2]}** ({r[1]}) — Tags: `{r[6]}` — uploaded on {r[5][:10]}")
else:
    st.info("No documents uploaded yet.")

st.divider()
st.subheader("🕒 Your Timeline")
# records is already newest-first from get_all_records(); reverse for oldest-first chronological view
timeline_records = list(reversed(records)) if records else []
timeline_html = render_timeline_html(timeline_records)
components.html(timeline_html, height=min(200 + 180 * max(len(timeline_records), 1), 1200), scrolling=True)