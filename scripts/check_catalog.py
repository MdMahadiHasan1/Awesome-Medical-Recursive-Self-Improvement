"""Check canonical paper entries and local links in the catalog documentation."""

import re
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "docs/papers.md"
LINK = re.compile(r"!?\[[^\]]*\]\(([^\s)]+)\)")
ENTRY = re.compile(
    r'^- (?:<a name="[^"]+"></a>)?\[([^\]]+)\]\((https://[^)]+)\)'
    r" · [^·]+, \d{4} · \*\*(?:Inference|Persistent|Meta-update|Resource)\*\*\. \S"
)


def markdown_lines(path):
    fence = None
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if marker:
            delimiter, rest = marker.groups()
            if fence is None:
                fence = delimiter
                continue
            if delimiter[0] == fence[0] and len(delimiter) >= len(fence) and not rest.strip():
                fence = None
                continue
        if fence is None:
            yield line_number, line


def anchors(path):
    result = set()
    for _, line in markdown_lines(path):
        heading = re.match(r"^#{1,6} (.+)$", line)
        if heading:
            plain = re.sub(r"[^\w -]", "", heading[1].lower())
            slug = plain.replace(" ", "-")
            suffix = 0
            candidate = slug
            while candidate in result:
                suffix += 1
                candidate = f"{slug}-{suffix}"
            result.add(candidate)
        result.update(re.findall(r'<a (?:name|id)="([^"]+)">', line))
    return result


def source_key(url):
    parsed = urlsplit(url)
    host = (parsed.hostname or "").lower().removeprefix("www.")
    path = unquote(parsed.path).rstrip("/").lower()
    if host in {"arxiv.org", "doi.org"}:
        arxiv = re.fullmatch(
            r"/(?:abs/|pdf/|10\.48550/arxiv\.)(\d{4}\.\d{4,5})(?:v\d+)?(?:\.pdf)?",
            path,
        )
        if arxiv:
            return f"arxiv:{arxiv[1]}"
    if host == "openreview.net":
        paper_ids = parse_qs(parsed.query).get("id")
        if paper_ids:
            return f"openreview:{paper_ids[0]}"
    if host == "nature.com" and path.startswith("/articles/"):
        return f"doi.org/10.1038/{path.removeprefix('/articles/')}"
    return host + path


def check_papers():
    sources = {}
    titles = {}
    errors = []
    for line_number, line in markdown_lines(PAPERS):
        if not line.startswith(("- [", "- <a")) or "](https://" not in line:
            continue
        entry = ENTRY.match(line)
        if entry is None:
            errors.append(f"docs/papers.md:{line_number}: invalid paper entry")
            continue
        title, url = entry.groups()
        title_key = re.sub(r"[^\w]", "", title.casefold())
        url_key = source_key(url)
        if url_key in sources or title_key in titles:
            first = sources.get(url_key) or titles[title_key]
            errors.append(f"docs/papers.md:{line_number}: duplicate paper from line {first}")
        sources[url_key] = line_number
        titles[title_key] = line_number
    if not sources:
        errors.append("docs/papers.md: expected at least one paper entry")
    return len(sources), errors


def check_links(pages):
    errors = []
    for page in pages:
        for line_number, line in markdown_lines(page):
            for link in LINK.findall(line):
                parsed = urlsplit(link)
                if parsed.scheme or parsed.netloc:
                    continue
                target = (page.parent / unquote(parsed.path)).resolve() if parsed.path else page
                prefix = f"{page.relative_to(ROOT)}:{line_number}"
                if not target.is_relative_to(ROOT) or not target.is_file():
                    errors.append(f"{prefix}: missing local file {link}")
                elif parsed.fragment and target.suffix == ".md" and unquote(parsed.fragment) not in anchors(target):
                    errors.append(f"{prefix}: missing anchor {link}")
    return errors


def main():
    pages = sorted(ROOT.glob("*.md")) + sorted((ROOT / "docs").rglob("*.md"))
    pages.extend(sorted((ROOT / ".github").glob("*.md")))
    paper_count, errors = check_papers()
    errors.extend(check_links(pages))
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Validated {paper_count} unique papers and local links in {len(pages)} Markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
