import json
import os
import time
import threading
from typing import Any

_PLUGIN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_DATA_DIR = os.path.join(_PLUGIN_DIR, "data")
_ARCHIVE_FILE = os.path.join(_DATA_DIR, "archive.json")
_lock = threading.Lock()


def _ensure_data_dir() -> None:
    os.makedirs(_DATA_DIR, exist_ok=True)


def _read_json(path: str) -> Any:
    """Read JSON from disk. Caller must hold _lock."""
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None


def _write_json(path: str, data: Any) -> None:
    """Atomically write JSON to disk. Caller must hold _lock."""
    _ensure_data_dir()
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp_path, path)


# ── Archive operations ────────────────────────────────────────────


def get_archived() -> dict[str, dict[str, Any]]:
    """Return dict of {chat_id: {archived_at: float, name: str}}."""
    with _lock:
        raw = _read_json(_ARCHIVE_FILE)
        if not isinstance(raw, dict):
            return {}
        return raw


def archive_chat(chat_id: str, name: str = "") -> float:
    """Archive a chat. Returns the archived_at timestamp."""
    with _lock:
        raw = _read_json(_ARCHIVE_FILE)
        if not isinstance(raw, dict):
            raw = {}
        ts = time.time()
        raw[chat_id] = {"archived_at": ts, "name": name}
        _write_json(_ARCHIVE_FILE, raw)
        return ts


def unarchive_chat(chat_id: str) -> bool:
    """Remove a chat from the archive. Returns True if it was archived."""
    with _lock:
        raw = _read_json(_ARCHIVE_FILE)
        if not isinstance(raw, dict):
            return False
        if chat_id not in raw:
            return False
        del raw[chat_id]
        _write_json(_ARCHIVE_FILE, raw)
        return True


def is_archived(chat_id: str) -> bool:
    """Check if a chat is archived."""
    return chat_id in get_archived()


def delete_archived(chat_id: str) -> bool:
    """Permanently remove a chat from archive records. Returns True if found."""
    return unarchive_chat(chat_id)
