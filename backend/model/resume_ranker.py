import os
import re
from typing import List, Dict

class ResumeRanker:
    def __init__(self, upload_dir="backend/data/uploads"):
        self.upload_dir = upload_dir

    def _read_file(self, file_path: str) -> str:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().lower()

    def _extract_keywords(self, text: str) -> List[str]:
        return re.findall(r'\b[a-zA-Z]{4,}\b', text)

    def rank_resumes(self, job_description: str, min_score: float = 0.3, max_results: int = 10) -> List[Dict]:
        jd_keywords = set(self._extract_keywords(job_description.lower()))
        results = []

        for fname in os.listdir(self.upload_dir):
            fpath = os.path.join(self.upload_dir, fname)
            if os.path.isfile(fpath) and fname.endswith('.txt'):
                resume_text = self._read_file(fpath)
                resume_keywords = set(self._extract_keywords(resume_text))
                matched_keywords = jd_keywords & resume_keywords
                score = len(matched_keywords) / len(jd_keywords) if jd_keywords else 0.0

                if score >= min_score:
                    results.append({
                        "file": fname,
                        "score": round(score, 3),
                        "keywords": list(matched_keywords),
                        "summary": f"{len(matched_keywords)} keywords matched"
                    })

        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:max_results]
