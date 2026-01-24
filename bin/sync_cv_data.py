#!/usr/bin/env python3
"""
Sync external CV data into this al-folio Jekyll site.

Source-of-truth folder (default):
  /Users/justin/R50_Research/40-49_Admin/44_Job_Application_Material/44.01_CV/data

Outputs (in this repo):
  - _data/cv.yml
  - _data/socials.yml (subset)
  - _bibliography/papers.bib
  - _pages/publications.md (front matter: years)
"""

from __future__ import annotations

import argparse
import dataclasses
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

import yaml


DEFAULT_SOURCE_DIR = Path(
    "/Users/justin/R50_Research/40-49_Admin/44_Job_Application_Material/44.01_CV/data"
)


MONTHS = {
    1: "jan",
    2: "feb",
    3: "mar",
    4: "apr",
    5: "may",
    6: "jun",
    7: "jul",
    8: "aug",
    9: "sep",
    10: "oct",
    11: "nov",
    12: "dec",
}


CURATED_BIB_FIELDS = {
    # publication preview UI + CTA buttons in _layouts/bib.liquid
    "abbr",
    "selected",
    "preview",
    "pdf",
    "supp",
    "html",
    "code",
    "blog",
    "slides",
    "poster",
    "video",
    "website",
    # other site-specific goodies used by templates / plugins
    "award",
    "award_name",
    "additional_info",
    "annotation",
    "bibtex_show",
    # some users keep stable keys/IDs for deduplication
    "ids",
}


def _read_yaml(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(f"Missing required data file: {path}")
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _dump_yaml(obj: Any) -> str:
    return yaml.safe_dump(
        obj,
        sort_keys=False,
        allow_unicode=True,
        width=1000,
        default_flow_style=False,
    )


def _write_if_changed(path: Path, new_content: str, *, check: bool) -> bool:
    """Return True if would/does change."""
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    if old == new_content:
        return False
    if check:
        return True
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(new_content, encoding="utf-8")
    return True


def _front_matter_split(text: str) -> Tuple[Optional[str], str]:
    """
    Split Jekyll-style front matter from body.
    Returns (front_matter_text_without_delimiters_or_None, body).
    """
    if not text.startswith("---\n"):
        return None, text
    # Find the second delimiter line.
    idx = text.find("\n---\n", 4)
    if idx == -1:
        return None, text
    front = text[4:idx]
    body = text[idx + len("\n---\n") :]
    return front, body


def _update_front_matter_years(page_path: Path, years: List[int], *, check: bool) -> bool:
    raw = page_path.read_text(encoding="utf-8")
    front, body = _front_matter_split(raw)
    if front is None:
        raise ValueError(f"{page_path} has no YAML front matter to update.")
    data = yaml.safe_load(front) or {}
    data["years"] = years
    new_front = _dump_yaml(data).strip("\n") + "\n"
    new_raw = "---\n" + new_front + "---\n" + body.lstrip("\n")
    return _write_if_changed(page_path, new_raw, check=check)


def _normalize_doi(doi: str) -> str:
    return re.sub(r"\s+", "", doi).lower()


def _strip_latex(s: str) -> str:
    # Very lightweight normalization: remove braces and common latex escapes.
    s = re.sub(r"[{}]", "", s)
    s = re.sub(r"\\textbackslash\s*", "", s)
    s = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{[^}]*\})?", "", s)
    s = s.replace("\\", "")
    return s


def _normalize_title(title: str) -> str:
    t = _strip_latex(title or "")
    t = t.lower()
    t = re.sub(r"[^a-z0-9]+", "", t)
    return t


def _parse_date_to_year_month(date_str: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Accepts YYYY, YYYY-MM, YYYY-MM-DD, or other ISO-ish forms.
    Returns (year, month_abbrev_lower) (month may be None).
    """
    if not date_str:
        return None, None
    date_str = str(date_str).strip()
    m = re.match(r"^(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?$", date_str)
    if not m:
        # Fallback: try parsing as date.
        try:
            dt = datetime.fromisoformat(date_str)
            return str(dt.year), MONTHS.get(dt.month)
        except Exception:
            return None, None
    year = m.group(1)
    month = m.group(2)
    if month:
        try:
            month_int = int(month)
            return year, MONTHS.get(month_int)
        except Exception:
            return year, None
    return year, None


def _format_range(start: Any, end: Any) -> str:
    s = str(start).strip() if start is not None else ""
    e = str(end).strip() if end is not None else ""
    if not s and not e:
        return ""
    if not e:
        return s
    return f"{s} - {e}"


def _cv_section(title: str, type_: str, contents: Any) -> Dict[str, Any]:
    return {"title": title, "type": type_, "contents": contents}


def build_cv_data(source_dir: Path) -> List[Dict[str, Any]]:
    personal = _read_yaml(source_dir / "personal.yaml") or {}
    education = _read_yaml(source_dir / "education.yaml") or {}
    appointments = _read_yaml(source_dir / "appointments.yaml") or {}
    awards = _read_yaml(source_dir / "awards.yaml") or {}
    grants = _read_yaml(source_dir / "grants.yaml") or {}
    service = _read_yaml(source_dir / "service.yaml") or {}
    teaching = _read_yaml(source_dir / "teaching.yaml") or {}
    talks = _read_yaml(source_dir / "talks.yaml") or {}
    mentoring = _read_yaml(source_dir / "mentoring.yaml") or {}

    p = personal.get("personal", {}) if isinstance(personal, dict) else {}

    # General information (map)
    gi: List[Dict[str, Any]] = []
    if p.get("name"):
        gi.append({"name": "Full Name", "value": p["name"]})
    if p.get("current_title"):
        gi.append({"name": "Title", "value": p["current_title"]})
    if p.get("institution"):
        gi.append({"name": "Institution", "value": p["institution"]})
    if p.get("department"):
        gi.append({"name": "Department", "value": p["department"]})
    if p.get("location"):
        gi.append({"name": "Location", "value": p["location"]})
    contact = p.get("contact", {}) if isinstance(p.get("contact"), dict) else {}
    if contact.get("email"):
        gi.append({"name": "Email", "value": contact["email"]})
    if contact.get("website"):
        gi.append(
            {
                "name": "Website",
                "value": contact["website"],
                "links": [{"name": "link", "link": contact["website"]}],
            }
        )
    if contact.get("orcid"):
        gi.append({"name": "ORCID", "value": contact["orcid"]})
    if contact.get("github"):
        gi.append({"name": "GitHub", "value": contact["github"]})
    metrics = p.get("academic_metrics", {}) if isinstance(p.get("academic_metrics"), dict) else {}
    if metrics.get("h_index"):
        src = metrics.get("h_index_source")
        dt = metrics.get("h_index_date")
        suffix = f" ({src}" + (f", {dt}" if dt else "") + ")" if src else ""
        gi.append({"name": "h-index", "value": f"{metrics['h_index']}{suffix}"})

    cv: List[Dict[str, Any]] = []
    cv.append(_cv_section("General Information", "map", gi))

    # Research interests (list)
    interests = p.get("research_interests", [])
    if isinstance(interests, list) and interests:
        cv.append(_cv_section("Research Interests", "list", interests))

    # Personal statement (free text)
    if p.get("personal_statement"):
        cv.append(_cv_section("Personal Statement", "list", [p["personal_statement"]]))

    # Appointments (time_table)
    appts: List[Dict[str, Any]] = []
    for a in (appointments.get("appointments") or []):
        year = _format_range(a.get("start_date"), a.get("end_date"))
        appts.append(
            {
                "title": a.get("title"),
                "institution": a.get("institution"),
                "department": a.get("department"),
                "location": a.get("location"),
                "year": year,
                "description": [x for x in [a.get("description")] if x],
            }
        )
    if appts:
        cv.append(_cv_section("Appointments", "time_table", appts))

    # Education (time_table)
    edus: List[Dict[str, Any]] = []
    for e in (education.get("education") or []):
        year = _format_range(e.get("start_date"), e.get("end_date"))
        desc: List[Any] = []
        if e.get("field"):
            desc.append(f"Field: {e['field']}")
        if e.get("thesis_title"):
            desc.append(f"Thesis: {e['thesis_title']}")
        if e.get("advisor"):
            desc.append(f"Advisor: {e['advisor']}")
        if e.get("advisors"):
            desc.append(f"Advisors: {e['advisors']}")
        if e.get("honors"):
            desc.append(f"Honors: {e['honors']}")
        if e.get("description"):
            desc.append(e["description"])
        if e.get("thesis_description"):
            desc.append(e["thesis_description"])
        edus.append(
            {
                "title": e.get("degree"),
                "institution": e.get("institution"),
                "department": e.get("department"),
                "location": e.get("location"),
                "year": year,
                "description": desc,
            }
        )
    if edus:
        cv.append(_cv_section("Education", "time_table", edus))

    # Grants (time_table)
    grant_rows: List[Dict[str, Any]] = []
    for g in (grants.get("grants") or []):
        desc: List[str] = []
        if g.get("title"):
            desc.append(g["title"])
        if g.get("grant_number"):
            desc.append(f"Grant number: {g['grant_number']}")
        if g.get("pi"):
            desc.append(f"PI: {g['pi']}")
        if g.get("status"):
            desc.append(f"Status: {g['status']}")
        if g.get("duration"):
            desc.append(f"Duration: {g['duration']}")
        if g.get("amount"):
            desc.append(f"Amount: {g['amount']}")
        grant_rows.append(
            {
                "title": g.get("name"),
                "institution": g.get("institution"),
                "location": None,
                "year": g.get("year"),
                "description": desc,
            }
        )
    if grant_rows:
        cv.append(_cv_section("Grants", "time_table", grant_rows))

    # Awards (time_table + list)
    award_rows: List[Dict[str, Any]] = []
    for aw in (awards.get("awards") or []):
        items: List[str] = [aw.get("name")] if aw.get("name") else []
        if aw.get("amount"):
            items.append(str(aw["amount"]))
        if aw.get("description"):
            items.append(str(aw["description"]))
        award_rows.append({"year": aw.get("year"), "items": items})
    if award_rows:
        cv.append(_cv_section("Honors and Awards", "time_table", award_rows))

    student_awards = awards.get("student_awards") or []
    if isinstance(student_awards, list) and student_awards:
        rows: List[Dict[str, Any]] = []
        for sa in student_awards:
            title = sa.get("name")
            year = sa.get("year")
            desc: List[str] = []
            if sa.get("stage"):
                desc.append(f"Stage: {sa['stage']}")
            if sa.get("institution"):
                desc.append(f"Institution: {sa['institution']}")
            if sa.get("amount"):
                desc.append(f"Amount: {sa['amount']}")
            if sa.get("description"):
                desc.append(sa["description"])
            rows.append({"year": year, "title": title, "description": desc})
        cv.append(_cv_section("Student Awards", "time_table", rows))

    honor_societies = awards.get("honor_societies") or []
    if isinstance(honor_societies, list) and honor_societies:
        cv.append(_cv_section("Honor Societies", "list", [h.get("name", str(h)) for h in honor_societies]))

    # Teaching (time_table)
    teach_rows: List[Dict[str, Any]] = []
    tdata = teaching.get("teaching") if isinstance(teaching, dict) else None
    if isinstance(tdata, dict):
        for c in (tdata.get("courses_taught") or []):
            year = c.get("semester")
            title = f"{c.get('course', '')} — {c.get('title', '')}".strip(" —")
            desc: List[str] = []
            if c.get("role"):
                desc.append(f"Role: {c['role']}")
            if c.get("course_evaluation"):
                desc.append(f"Course evaluation: {c['course_evaluation']}")
            if c.get("description"):
                desc.append(c["description"])
            if c.get("student_quote"):
                desc.append(f"Student quote: {c['student_quote']}")
            linkitems = []
            if c.get("url"):
                linkitems.append({"link": c["url"], "linkname": "course"})
            teach_rows.append(
                {
                    "year": year,
                    "title": title,
                    "institution": c.get("institution"),
                    "location": None,
                    "description": desc,
                    "linkitems": linkitems,
                }
            )
        for c in (tdata.get("teaching_assistantships") or []):
            year = c.get("semester")
            title = f"{c.get('course', '')} — {c.get('title', '')}".strip(" —")
            desc = []
            if c.get("role"):
                desc.append(f"Role: {c['role']}")
            if c.get("description"):
                desc.append(c["description"])
            teach_rows.append(
                {
                    "year": year,
                    "title": title,
                    "institution": c.get("institution"),
                    "location": None,
                    "description": desc,
                }
            )
    if teach_rows:
        cv.append(_cv_section("Teaching", "time_table", teach_rows))

    # Service (nested_list)
    svc = service if isinstance(service, dict) else {}
    svc_items: List[Dict[str, Any]] = []
    for key, label in [
        ("noteable_service", "Notable service"),
        ("grant_reviewing", "Grant reviewing"),
        ("refereeing", "Refereeing"),
        ("committees", "Committees"),
        ("graduate_exam_committees", "Graduate exam committees"),
        ("conferences_organized", "Conferences organized"),
        ("other_service", "Other service"),
    ]:
        data = svc.get(key) or []
        if not data:
            continue
        lines: List[str] = []
        for item in data:
            if isinstance(item, str):
                lines.append(item)
                continue
            title = item.get("title") or item.get("committee") or item.get("organization") or item.get("journals")
            dates = item.get("dates") or _format_range(item.get("start_date"), item.get("status"))
            where = item.get("location") or item.get("level") or item.get("department")
            bits = [b for b in [dates, title, where] if b]
            line = " — ".join(bits)
            if item.get("description"):
                line += f": {item['description']}"
            if item.get("url"):
                line += f" ({item['url']})"
            lines.append(line)
        svc_items.append({"title": label, "items": lines})
    if svc_items:
        cv.append(_cv_section("Service", "nested_list", svc_items))

    # Mentoring (nested_list)
    men = mentoring.get("mentoring") if isinstance(mentoring, dict) else {}
    ment_items: List[Dict[str, Any]] = []
    if isinstance(men, dict):
        # Flatten a few known structures.
        for group_key, group_label in [
            ("postdocs", "Postdocs"),
            ("phd_students", "PhD students"),
            ("reu_students", "REU students"),
        ]:
            grp = men.get(group_key)
            if not isinstance(grp, dict):
                continue
            for subkey in ["current", "past"]:
                arr = grp.get(subkey) or []
                if not arr:
                    continue
                lines: List[str] = []
                for x in arr:
                    if isinstance(x, str):
                        lines.append(x)
                        continue
                    dates = _format_range(x.get("start_date") or x.get("year"), x.get("status"))
                    title = x.get("name")
                    inst = x.get("institution")
                    bits = [b for b in [dates, title, inst] if b]
                    line = " — ".join(bits)
                    if x.get("description"):
                        line += f": {x['description']}"
                    lines.append(line)
                ment_items.append({"title": f"{group_label} ({subkey})", "items": lines})
        # Junior mentoring (already flat list)
        jm = men.get("junior_mentoring") or []
        if jm:
            lines = []
            for x in jm:
                dates = _format_range(x.get("start_date"), x.get("end_date"))
                bits = [b for b in [dates, x.get("name"), x.get("type"), x.get("institution")] if b]
                line = " — ".join(bits)
                if x.get("description"):
                    line += f": {x['description']}"
                lines.append(line)
            ment_items.append({"title": "Junior mentoring", "items": lines})
    if ment_items:
        cv.append(_cv_section("Mentoring", "nested_list", ment_items))

    # Talks (nested_list)
    talks_root = talks.get("talks") if isinstance(talks, dict) else {}
    talk_items: List[Dict[str, Any]] = []
    if isinstance(talks_root, dict):
        invited = talks_root.get("invited") if isinstance(talks_root.get("invited"), dict) else {}
        # Walk a couple layers deep but keep output simple.
        def _flatten_talks(obj: Any, prefix: str) -> None:
            if isinstance(obj, list):
                lines: List[str] = []
                for t in obj:
                    if isinstance(t, str):
                        lines.append(t)
                        continue
                    date = t.get("date")
                    title = t.get("title")
                    venue = t.get("venue")
                    loc = t.get("location")
                    bits = [b for b in [date, title, venue, loc] if b]
                    line = " — ".join(bits)
                    talk_items.append({"title": prefix, "items": [line]})
                return
            if isinstance(obj, dict):
                for k, v in obj.items():
                    _flatten_talks(v, f"{prefix}: {k.replace('_', ' ')}")

        # Invited is structured; we flatten to a reasonable set of titles.
        if isinstance(invited, dict):
            for k, v in invited.items():
                if isinstance(v, list):
                    lines: List[str] = []
                    for t in v:
                        date = t.get("date")
                        title = t.get("title")
                        venue = t.get("venue")
                        loc = t.get("location")
                        bits = [b for b in [date, title, venue, loc] if b]
                        line = " — ".join(bits)
                        lines.append(line)
                    if lines:
                        talk_items.append({"title": f"Invited: {k.replace('_', ' ')}", "items": lines})
                elif isinstance(v, dict):
                    for kk, vv in v.items():
                        if isinstance(vv, list):
                            lines = []
                            for t in vv:
                                date = t.get("date")
                                title = t.get("title")
                                venue = t.get("venue")
                                loc = t.get("location")
                                bits = [b for b in [date, title, venue, loc] if b]
                                lines.append(" — ".join(bits))
                            if lines:
                                talk_items.append(
                                    {
                                        "title": f"Invited: {k.replace('_', ' ')} / {kk.replace('_', ' ')}",
                                        "items": lines,
                                    }
                                )
        # If there are other top-level talk categories in future, keep them via generic flatten.
        for k, v in talks_root.items():
            if k == "invited":
                continue
            _flatten_talks(v, k.replace("_", " ").capitalize())
    if talk_items:
        cv.append(_cv_section("Talks", "nested_list", talk_items))

    return cv


def update_socials(source_dir: Path, repo_socials_path: Path, *, check: bool) -> bool:
    personal = _read_yaml(source_dir / "personal.yaml") or {}
    p = personal.get("personal", {}) if isinstance(personal, dict) else {}
    contact = p.get("contact", {}) if isinstance(p.get("contact"), dict) else {}

    existing = yaml.safe_load(repo_socials_path.read_text(encoding="utf-8")) if repo_socials_path.exists() else {}
    if not isinstance(existing, dict):
        existing = {}

    # Sync a safe subset; do not stomp user-managed handles unless present.
    if contact.get("email"):
        existing["email"] = contact["email"]
    if contact.get("github"):
        existing["github_username"] = contact["github"]
    if contact.get("orcid"):
        existing["orcid_id"] = contact["orcid"]

    # Optional: secondary email (only if already in file or present in data)
    if contact.get("alt_email") and "alt_email" in existing:
        existing["alt_email"] = contact["alt_email"]

    return _write_if_changed(repo_socials_path, _dump_yaml(existing), check=check)


@dataclasses.dataclass(frozen=True)
class BibEntry:
    entry_type: str
    key: str
    fields: Dict[str, str]


def _bibtex_import_or_die() -> Tuple[Any, Any, Any, Any]:
    try:
        from bibtexparser.bparser import BibTexParser  # type: ignore
        from bibtexparser.bwriter import BibTexWriter  # type: ignore
        from bibtexparser.bibdatabase import BibDatabase  # type: ignore
        import bibtexparser  # type: ignore

        return bibtexparser, BibTexParser, BibTexWriter, BibDatabase
    except Exception as e:  # pragma: no cover
        print(
            "Missing dependency 'bibtexparser'. Install it with:\n"
            "  pip install -r requirements.txt\n\n"
            f"Import error: {e}",
            file=sys.stderr,
        )
        sys.exit(2)


def _load_bib_entries(bib_path: Path) -> List[BibEntry]:
    bibtexparser, BibTexParser, _, _ = _bibtex_import_or_die()
    parser = BibTexParser(common_strings=True)
    # External CV bib uses biblatex-ish/nonstandard entry types (e.g. @online, @patent).
    # We still want to ingest and normalize them rather than silently dropping them.
    if hasattr(parser, "ignore_nonstandard_types"):
        parser.ignore_nonstandard_types = False
    # Preserve LaTeX as-is; we only normalize for matching.
    with bib_path.open("r", encoding="utf-8") as bibtex_file:
        db = bibtexparser.load(bibtex_file, parser=parser)
    entries: List[BibEntry] = []
    for e in db.entries:
        entry_type = (e.get("ENTRYTYPE") or "").strip().lower()
        key = (e.get("ID") or "").strip()
        fields = {k: str(v) for k, v in e.items() if k not in {"ENTRYTYPE", "ID"} and v is not None}
        if not entry_type or not key:
            continue
        entries.append(BibEntry(entry_type=entry_type, key=key, fields=fields))
    return entries


def _entry_match_key(entry: BibEntry) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    doi = entry.fields.get("doi")
    title = entry.fields.get("title")
    eprint = entry.fields.get("eprint")
    eprinttype = (entry.fields.get("eprinttype") or "").lower()
    arxiv_id = None
    if eprint and ("arxiv" in eprinttype):
        arxiv_id = eprint.strip()
    if doi:
        return _normalize_doi(doi), None, None
    if arxiv_id:
        return None, arxiv_id, None
    if title:
        return None, None, _normalize_title(title)
    return None, None, None


def _convert_external_bib_entry(entry: BibEntry) -> BibEntry:
    fields = dict(entry.fields)

    # Convert biblatex-ish to bibtex-ish field names used by the site templates.
    if "journaltitle" in fields and "journal" not in fields:
        fields["journal"] = fields.pop("journaltitle")

    if "date" in fields:
        year, month = _parse_date_to_year_month(fields.get("date", ""))
        if year and "year" not in fields:
            fields["year"] = year
        if month and "month" not in fields:
            fields["month"] = month
        fields.pop("date", None)

    # Ensure arXiv links/buttons work in _layouts/bib.liquid.
    eprint = fields.get("eprint")
    eprinttype = (fields.get("eprinttype") or "").lower()
    if eprint and "arxiv" in eprinttype and "arxiv" not in fields:
        fields["arxiv"] = eprint.strip()
    doi = fields.get("doi", "")
    if doi.lower().startswith("10.48550/arxiv.") and "arxiv" not in fields:
        fields["arxiv"] = doi.split(".", 2)[-1]

    # Normalize type for arXiv preprints that are stored as @online in the CV bib.
    entry_type = entry.entry_type
    if entry_type == "online" and ("arxiv" in eprinttype or "arxiv" in (fields.get("url", "").lower())):
        entry_type = "article"
        if "journal" not in fields:
            fields["journal"] = "arXiv preprint"

    return BibEntry(entry_type=entry_type, key=entry.key, fields=fields)


def _merge_curated_fields(
    new_entry: BibEntry, existing_match: Optional[BibEntry]
) -> BibEntry:
    if existing_match is None:
        return new_entry
    fields = dict(new_entry.fields)
    for k in CURATED_BIB_FIELDS:
        if k in existing_match.fields and k not in fields:
            fields[k] = existing_match.fields[k]
    return BibEntry(entry_type=new_entry.entry_type, key=new_entry.key, fields=fields)


def _choose_output_key(new_entry: BibEntry, existing_match: Optional[BibEntry]) -> str:
    # Prefer keeping stable existing keys to preserve /bibliography/<key>/ URLs.
    if existing_match is not None and existing_match.key:
        return existing_match.key
    return new_entry.key


def build_papers_bib(
    *,
    external_bib: Path,
    existing_site_bib: Path,
) -> Tuple[List[BibEntry], List[int]]:
    external_entries_raw = _load_bib_entries(external_bib)
    external_entries = [_convert_external_bib_entry(e) for e in external_entries_raw]

    existing_entries = _load_bib_entries(existing_site_bib) if existing_site_bib.exists() else []
    existing_by_doi: Dict[str, BibEntry] = {}
    existing_by_arxiv: Dict[str, BibEntry] = {}
    existing_by_title: Dict[str, BibEntry] = {}
    for e in existing_entries:
        doi, arxiv_id, title = _entry_match_key(e)
        if doi:
            existing_by_doi[doi] = e
        if arxiv_id:
            existing_by_arxiv[arxiv_id] = e
        if title:
            existing_by_title[title] = e

    out_entries: List[BibEntry] = []
    years: List[int] = []
    for e in external_entries:
        doi, arxiv_id, title = _entry_match_key(e)
        match = None
        if doi and doi in existing_by_doi:
            match = existing_by_doi[doi]
        elif arxiv_id and arxiv_id in existing_by_arxiv:
            match = existing_by_arxiv[arxiv_id]
        elif title and title in existing_by_title:
            match = existing_by_title[title]

        merged = _merge_curated_fields(e, match)
        key = _choose_output_key(merged, match)
        year_val = merged.fields.get("year")
        if year_val:
            try:
                years.append(int(str(year_val).strip()))
            except Exception:
                pass
        out_entries.append(BibEntry(entry_type=merged.entry_type, key=key, fields=merged.fields))

    years_sorted = sorted({y for y in years if y > 0}, reverse=True)
    return out_entries, years_sorted


def _write_bib_file(entries: List[BibEntry], dest_path: Path, *, check: bool) -> bool:
    _, _, BibTexWriter, BibDatabase = _bibtex_import_or_die()
    db = BibDatabase()
    db.entries = []
    for e in entries:
        d = {"ENTRYTYPE": e.entry_type, "ID": e.key}
        d.update(e.fields)
        db.entries.append(d)
    writer = BibTexWriter()
    writer.indent = "  "
    writer.order_entries_by = None  # preserve input ordering
    bib_text = writer.write(db)
    return _write_if_changed(dest_path, bib_text, check=check)


def main(argv: Optional[Sequence[str]] = None) -> int:
    repo_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description="Sync external CV data into this site repo.")
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(os.environ.get("CV_DATA_DIR", str(DEFAULT_SOURCE_DIR))),
        help="Path to external CV data folder (contains *.yaml + publications.bib).",
    )
    parser.add_argument("--check", action="store_true", help="Do not write; exit nonzero if changes needed.")
    args = parser.parse_args(argv)

    source_dir: Path = args.source
    check: bool = bool(args.check)

    changed = False

    # 1) CV YAML
    cv_path = repo_root / "_data" / "cv.yml"
    cv_data = build_cv_data(source_dir)
    changed |= _write_if_changed(cv_path, _dump_yaml(cv_data), check=check)

    # 2) Socials subset
    socials_path = repo_root / "_data" / "socials.yml"
    changed |= update_socials(source_dir, socials_path, check=check)

    # 3) Publications bib
    existing_site_bib = repo_root / "_bibliography" / "papers.bib"
    external_bib = source_dir / "publications.bib"
    out_entries, years = build_papers_bib(external_bib=external_bib, existing_site_bib=existing_site_bib)
    changed |= _write_bib_file(out_entries, existing_site_bib, check=check)

    # 4) Update publications page year list
    pubs_page = repo_root / "_pages" / "publications.md"
    if pubs_page.exists() and years:
        changed |= _update_front_matter_years(pubs_page, years, check=check)

    if check and changed:
        print("Sync would update one or more files.", file=sys.stderr)
        return 1

    print("Sync complete." + (" (no changes)" if not changed else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

