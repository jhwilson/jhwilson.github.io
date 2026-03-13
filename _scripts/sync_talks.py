#!/usr/bin/env python3

from __future__ import annotations

import os
import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DEST_ROOT = REPO_ROOT / "assets" / "talks"
ENV_FILE = REPO_ROOT / ".talks-sync.env"

TALKS = [
    {
        "slug": "ttlg-quasiperiodic",
        "source_env": "TTLG_QUASIPERIODIC_SOURCE",
        "files": ["index.html"],
        "directories": ["figures", "photos"],
    }
]


def load_local_env() -> None:
    if not ENV_FILE.exists():
        return

    for raw_line in ENV_FILE.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")

        if key:
            os.environ.setdefault(key, value)


def resolve_source(talk: dict[str, object]) -> Path:
    env_var = str(talk["source_env"])
    source_value = os.environ.get(env_var)

    if not source_value:
        raise RuntimeError(
            f"Missing required environment variable {env_var}. "
            f"Set it in {ENV_FILE.name} or pass it inline, for example: "
            f"{env_var}=/absolute/path/to/talk python3 _scripts/sync_talks.py"
        )

    return Path(source_value).expanduser().resolve()


def copy_talk(talk: dict[str, object]) -> None:
    slug = talk["slug"]
    source = resolve_source(talk)
    dest = DEST_ROOT / str(slug)

    if not source.exists():
        raise FileNotFoundError(f"Talk source does not exist: {source}")

    if dest.exists():
        shutil.rmtree(dest)

    dest.mkdir(parents=True, exist_ok=True)

    for file_name in talk["files"]:
        src_file = source / str(file_name)
        if not src_file.exists():
            raise FileNotFoundError(f"Required talk file is missing: {src_file}")
        shutil.copy2(src_file, dest / src_file.name)

    for dir_name in talk["directories"]:
        src_dir = source / str(dir_name)
        if src_dir.exists():
            shutil.copytree(src_dir, dest / src_dir.name)

    print(f"Synced {source} -> {dest}")


def main() -> None:
    load_local_env()
    for talk in TALKS:
        copy_talk(talk)


if __name__ == "__main__":
    main()
