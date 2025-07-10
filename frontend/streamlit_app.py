import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="SmartHire Pro", layout="wide")

st.title("📄 SmartHire Pro - Resume Ranking AI")

api_url = "http://127.0.0.1:8000"

# --- Resume Upload ---
st.header("📄 Upload Resume")
uploaded_file = st.file_uploader("Upload Resume (.txt only)", type=["txt"])

if uploaded_file and st.button("🚀 Upload"):
    try:
        files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
        res = requests.post(f"{api_url}/upload", files=files)
        if res.status_code == 200:
            st.success("Resume uploaded successfully!")
        else:
            st.error(f"Upload failed! Code: {res.status_code}")
    except Exception as e:
        st.error(f"Error: {e}")

# --- Job Description Matching ---
st.header("🧠 Job Description")
jd = st.text_area("Paste Job Description", height=200)

min_score = 0.3
max_results = 10

if jd and st.button("🎯 Rank Resumes"):
    try:
        data = {
            "job_description": jd,
            "min_score": min_score,
            "max_results": max_results
        }
        res = requests.post(f"{api_url}/rank", json=data)
        if res.status_code == 200:
            results = res.json().get("matches", [])
            if results:
                st.success(f"Found {len(results)} resumes above score {min_score}")
                for i, r in enumerate(results, 1):
                    st.write(f"**{i}. {r['file']}** — Score: {r['score']:.2f}")
                    if 'summary' in r:
                        st.caption(r['summary'])
                    if 'keywords' in r:
                        st.write(f"Keywords: {', '.join(r['keywords'])}")

                # --- HR Email Notification ---
                st.subheader("📩 Notify HR")
                hr_email = st.text_input("Enter HR Email")
                if hr_email and st.button("📧 Send Notification"):
                    try:
                        notify_payload = {
                            "email": hr_email,
                            "matches": results[:3]  # top 3
                        }
                        notify = requests.post(f"{api_url}/notify", json=notify_payload)
                        if notify.status_code == 200:
                            st.success("HR has been notified about top matching resumes.")
                        else:
                            st.error(f"Notification failed. Code: {notify.status_code}")
                    except Exception as e:
                        st.error(f"Notification error: {e}")

            else:
                st.warning("No resumes matched.")
        else:
            st.error(f"Error: {res.status_code}")
    except Exception as e:
        st.error(f"Error: {e}")
