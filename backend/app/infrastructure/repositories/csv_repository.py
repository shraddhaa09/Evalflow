import csv
import os
from typing import List
from app.domain.interfaces.repository import ISubmissionRepository
from app.domain.models.plagiarism import Submission
from app.core.config import settings
from app.core.logger import logger
from app.domain.exceptions import CorpusUnavailableException

class CSVSubmissionRepository(ISubmissionRepository):
    def __init__(self):
        self._corpus = {}
        self.loaded = False

    def _load_corpus(self):
        if self.loaded:
            return

        if not os.path.exists(settings.submissions_csv_path) or not os.path.exists(settings.telemetry_csv_path):
            logger.error("Corpus files not found. Check settings.submissions_csv_path.")
            raise CorpusUnavailableException("Submissions or Telemetry CSV files are missing.")

        try:
            subs = {}
            with open(settings.submissions_csv_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    subs[row["submission_id"]] = row
                    
            with open(settings.telemetry_csv_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    sid = row["submission_id"]
                    if sid in subs:
                        subs[sid]["typing_speed_wpm"] = float(row.get("typing_speed_wpm", 0))
                        subs[sid]["idle_ratio"] = float(row.get("idle_ratio", 0))
                        subs[sid]["paste_ratio"] = float(row.get("paste_ratio", 0))
                        subs[sid]["tab_switches"] = int(row.get("tab_switches", 0))
                        subs[sid]["suspicion_score"] = float(row.get("suspicion_score", 0))
                        subs[sid]["label"] = int(row.get("label", 0)) if "label" in row else 0

            for sid, record in subs.items():
                aid = record["assignment_id"]
                if aid not in self._corpus:
                    self._corpus[aid] = []
                    
                file_path = record.get("file_path", "")
                full_path = os.path.normpath(os.path.join(settings.dataset_dir, file_path))
                
                code = ""
                try:
                    with open(full_path, "r", encoding="utf-8") as cf:
                        code = cf.read()
                except Exception as e:
                    logger.warning(f"Failed to read submission file at {full_path}: {e}")
                
                submission = Submission(
                    submission_id=sid,
                    assignment_id=aid,
                    file_path=full_path,
                    code=code,
                    label=record.get("label", 0),
                    typing_speed_wpm=record.get("typing_speed_wpm", 0.0),
                    idle_ratio=record.get("idle_ratio", 0.0),
                    paste_ratio=record.get("paste_ratio", 0.0),
                    tab_switches=record.get("tab_switches", 0),
                    suspicion_score=record.get("suspicion_score", 0.0)
                )
                self._corpus[aid].append(submission)
            
            self.loaded = True
            logger.info(f"Loaded {len(subs)} submissions into CSV repository.")
        except Exception as e:
            logger.error(f"Failed to load CSV corpus: {e}")
            raise CorpusUnavailableException(f"Corpus parse error: {e}")

    def get_by_assignment(self, assignment_id: str) -> List[Submission]:
        if not self.loaded:
            self._load_corpus()
        return self._corpus.get(str(assignment_id), [])

    def get_all_submissions(self) -> List[Submission]:
        if not self.loaded:
            self._load_corpus()
        all_subs = []
        for subs in self._corpus.values():
            all_subs.extend(subs)
        return all_subs
