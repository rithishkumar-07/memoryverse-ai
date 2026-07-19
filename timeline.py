from datetime import datetime

# Icons per document type
TYPE_ICONS = {
    "Certificate": "🏆",
    "Resume": "📄",
    "Project": "💻",
    "Internship": "🏢",
}

# Colors per document type (for the timeline dot/card accent)
TYPE_COLORS = {
    "Certificate": "#F5A623",
    "Resume": "#4A90D9",
    "Project": "#7ED321",
    "Internship": "#BD10E0",
}


def format_date(iso_date: str) -> str:
    try:
        dt = datetime.fromisoformat(iso_date)
        return dt.strftime("%d %b %Y")
    except Exception:
        return iso_date[:10]


def render_timeline_html(records) -> str:
    """
    records: list of tuples from database.get_all_records()
    Schema: (id, doc_type, title, description, file_path, upload_date, tags)
    Expects records already sorted (e.g., newest first or oldest first).
    """
    if not records:
        return "<p style='color:#888;'>No documents yet. Upload something to build your timeline!</p>"

    items_html = ""
    for r in records:
        doc_id, doc_type, title, description, file_path, upload_date, tags = r
        icon = TYPE_ICONS.get(doc_type, "📌")
        color = TYPE_COLORS.get(doc_type, "#999999")
        date_str = format_date(upload_date)
        desc_short = (description[:120] + "…") if description and len(description) > 120 else (description or "")

        items_html += f"""
        <div class="tl-item">
          <div class="tl-dot" style="background:{color};">{icon}</div>
          <div class="tl-card" style="border-left: 4px solid {color};">
            <div class="tl-date">{date_str}</div>
            <div class="tl-title">{title}</div>
            <div class="tl-type" style="color:{color};">{doc_type}</div>
            <div class="tl-desc">{desc_short}</div>
            <div class="tl-tags">{tags}</div>
          </div>
        </div>
        """

    html = f"""
    <style>
      .tl-container {{
        position: relative;
        margin: 20px 0;
        padding-left: 40px;
      }}
      .tl-container::before {{
        content: '';
        position: absolute;
        left: 15px;
        top: 0;
        bottom: 0;
        width: 3px;
        background: linear-gradient(to bottom, #F5A623, #4A90D9, #7ED321, #BD10E0);
        border-radius: 2px;
      }}
      .tl-item {{
        position: relative;
        margin-bottom: 28px;
      }}
      .tl-dot {{
        position: absolute;
        left: -40px;
        top: 0;
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
        box-shadow: 0 0 0 4px #ffffff, 0 0 0 5px #ddd;
      }}
      .tl-card {{
        background: #fff;
        border-radius: 8px;
        padding: 12px 16px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.12);
        margin-left: 10px;
      }}
      .tl-date {{
        font-size: 12px;
        color: #888;
        font-weight: 600;
      }}
      .tl-title {{
        font-size: 16px;
        font-weight: 700;
        color: #222;
        margin: 2px 0;
      }}
      .tl-type {{
        font-size: 12px;
        font-weight: 600;
        margin-bottom: 6px;
      }}
      .tl-desc {{
        font-size: 13px;
        color: #555;
        margin-bottom: 6px;
      }}
      .tl-tags {{
        font-size: 11px;
        color: #999;
        font-style: italic;
      }}
    </style>
    <div class="tl-container">
      {items_html}
    </div>
    """
    return html