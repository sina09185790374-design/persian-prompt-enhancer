"""Turn a raw task message (Persian or English) into a professional prompt.

Stdlib only. The user's original text — including every number, price and
name — is carried into the output verbatim, never paraphrased away.
"""
import re

TASK_KEYWORDS = {
    "content": ["اینستاگرام", "ریل", "ریلز", "کپشن", "استوری", "محتوا", "پست",
                "instagram", "reel", "caption", "story", "content", "ویدیو", "video"],
    "code": ["کد", "برنامه‌نویسی", "برنامه نویسی", "اپ", "گیت‌هاب", "گیت هاب",
             "github", "code", "coding", "app", "script", "اسکریپت", "python", "پایتون"],
    "shop": ["مغازه", "فروشگاه", "فاکتور", "اسمبل", "تعمیر", "نصب ویندوز",
             "shop", "store", "invoice"],
    "sales": ["فروش", "آگهی", "دیوار", "شیپور", "تبلیغ", "لید", "مشتری بگیر",
              "sales", "marketing", "ad ", "فریلنسر", "پروژه بگیر"],
    "research": ["تحقیق", "بررسی", "مقایسه", "تحلیل", "پیدا کن", "بگرد",
                 "research", "compare", "analysis", "find"],
}

TYPE_CHECKLISTS = {
    "content": ["Hook in the first 1–3 seconds", "Video-first format (9:16 for reels)",
                "Caption: emoji lead + number-heavy facts + 3–5 hashtags",
                "One send-to-friend / save reason + follow CTA with a reason"],
    "code": ["Working code, not a stub — runs/tests pass", "README (EN + FA section)",
             "No secrets in the repo (.env.example only)", "Clean commit message in English"],
    "shop": ["Use the shop's real name, phone, address and hours",
             "Prices exactly as given — never invent a price",
             "Printable / paste-ready output"],
    "sales": ["One clear offer + one clear price", "Ready-to-paste copy, no placeholders",
              "A free first step (audit/sample) as the hook"],
    "research": ["Live sources, checked today — no stale numbers",
                 "Compare at least 3 options with numbers", "End with one clear recommendation"],
    "general": ["Concrete deliverable, not advice only", "Numbers and dates checked",
                "Short Persian summary at the end"],
}

TYPE_LABELS = {
    "content": "Content production", "code": "Programming / build",
    "shop": "Shop operations", "sales": "Sales & marketing",
    "research": "Research", "general": "General task",
}

_NUMBER_RE = re.compile(r"[0-9۰-۹][0-9۰-۹,٬./:%-]*")
_QUOTED_RE = re.compile(r"«([^»]+)»|\"([^\"]+)\"|'([^']+)'")


def detect_type(text):
    """Return the task type whose keywords score highest (default: general)."""
    low = " " + text.lower() + " "
    best, best_score = "general", 0
    for t, words in TASK_KEYWORDS.items():
        score = sum(1 for w in words if w.lower() in low)
        if score > best_score:
            best, best_score = t, score
    return best


def extract_numbers(text):
    """All number-like tokens in the text, verbatim and in order."""
    seen, out = set(), []
    for m in _NUMBER_RE.finditer(text):
        tok = m.group(0).strip(",./-")
        if tok and tok not in seen:
            seen.add(tok)
            out.append(tok)
    return out


def extract_quoted(text):
    """Quoted names/phrases («...», "...", '...') preserved verbatim."""
    out = []
    for m in _QUOTED_RE.finditer(text):
        out.append(next(g for g in m.groups() if g))
    return out


def extract_goal(text):
    """The goal = the first non-empty sentence/line of the raw message."""
    for part in re.split(r"\n|(?<=[.!؟?])(?:\s+|$)", text):
        part = part.strip()
        if len(part) >= 4:
            return part
    return text.strip()


def enhance(text, task_type=None):
    """Build the professional prompt. Returns a Markdown string."""
    text = text.strip()
    t = task_type or detect_type(text)
    numbers = extract_numbers(text)
    quoted = extract_quoted(text)
    lines = [
        "# Professional Prompt",
        "",
        f"**Task type:** {TYPE_LABELS[t]} (`{t}`)",
        "",
        "## Goal",
        extract_goal(text),
        "",
        "## Context",
    ]
    lines.append(text if text != extract_goal(text) else "(see original below)")
    lines += ["", "## Original request (verbatim — numbers, prices and names are exact)"]
    lines.append(text)
    if numbers:
        lines += ["", "**Exact values to preserve:** " + " · ".join(numbers)]
    if quoted:
        lines += ["**Exact names/phrases to preserve:** " + " · ".join(quoted)]
    lines += ["", "## Deliverables"]
    lines += [f"- [ ] {item}" for item in TYPE_CHECKLISTS[t]]
    lines += [
        "",
        "## Constraints",
        "- Execute, don't just advise — bring back checked, ready-to-use output.",
        "- Never invent a price, date, name or number that is not in the request.",
        "- Routine work needs no approval; spending money always does.",
        "",
        "## Success criteria",
        "- The deliverable is usable as-is (paste-ready / runs / publishes).",
        "- Every number, price and name from the original request appears unchanged.",
        "- A short Persian summary reports what was done, with numbers first.",
        "",
    ]
    return "\n".join(lines)
