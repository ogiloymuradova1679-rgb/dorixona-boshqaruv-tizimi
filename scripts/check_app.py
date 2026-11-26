#!/usr/bin/env python3
"""DoriMed bitta faylli ilovasi uchun yengil sifat nazorati."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parent.parent
APP = ROOT / "index.html"
BUILD = ROOT / "build"
REPORT = BUILD / "check-report.txt"

REQUIRED_IDS = {
    "page-dashboard", "page-medicines", "page-manufacturers",
    "page-transactions", "page-reports", "page-settings",
    "medicineTableBody", "txTableBody", "reportStats",
    "transactionForm", "modalOverlay", "globalSearch",
}
REQUIRED_JS = {
    "localStorage", "statusOf", "renderDashboard", "addTransaction",
    "exportMedicinesCSV", "downloadBackup", "escapeHtml",
}

errors: list[str] = []
warnings: list[str] = []
checks: list[str] = []


class StructureParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.errors: list[str] = []
        self.ids: list[str] = []
        self.scripts: list[tuple[str, str]] = []
        self.in_script = False
        self.script_attrs: dict[str, str | None] = {}
        self.script_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if "id" in data:
            self.ids.append(str(data["id"]))
        if tag in {"meta", "link", "br", "hr", "img", "input", "source", "area", "base", "col", "embed", "param", "track", "wbr"}:
            return
        self.stack.append(tag)
        if tag == "script":
            self.in_script = True
            self.script_attrs = data
            self.script_parts = []

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if "id" in data:
            self.ids.append(str(data["id"]))

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self.in_script:
            self.scripts.append((self.script_attrs.get("src") or "", "".join(self.script_parts)))
            self.in_script = False
            self.script_attrs = {}
            self.script_parts = []
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            self.errors.append(f"Teg tartibi buzilgan: </{tag}>")
            while self.stack and self.stack[-1] != tag:
                self.stack.pop()
            if self.stack:
                self.stack.pop()

    def handle_data(self, data: str) -> None:
        if self.in_script:
            self.script_parts.append(data)


def check(condition: bool, success: str, failure: str) -> None:
    if condition:
        checks.append(f"PASS  {success}")
    else:
        errors.append(failure)


def main() -> int:
    if not APP.exists():
        print("FAIL  index.html topilmadi")
        return 1

    text = APP.read_text(encoding="utf-8")
    parser = StructureParser()
    parser.feed(text)
    parser.close()

    check(APP.stat().st_size > 40_000, f"Fayl hajmi: {APP.stat().st_size / 1024:.1f} KB", "Fayl kutilganidan juda kichik")
    check('<html lang="uz">' in text, "HTML tili uz", "html lang='uz' topilmadi")
    check("<title>" in text and "DoriMed" in text, "Sarlavha mavjud", "Sarlavha topilmadi")
    check('name="viewport"' in text, "Mobil viewport mavjud", "Viewport meta teg yo'q")
    check(not parser.errors, "HTML asosiy tuzilmasi yopilgan", "; ".join(parser.errors) or "HTML tuzilmasi xato")
    check(not parser.stack, f"Barcha asosiy teglar yopilgan ({len(parser.stack)} ochiq)", f"Yopilmagan teglar: {parser.stack[:8]}")

    duplicates = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
    check(not duplicates, f"{len(parser.ids)} ta unikal ID", f"Takrorlangan ID: {duplicates[:8]}")
    missing = sorted(REQUIRED_IDS - set(parser.ids))
    check(not missing, "Kerakli interfeys elementlari mavjud", f"Yetishmayotgan ID: {missing}")

    external_scripts = [src for src, _ in parser.scripts if src.strip()]
    inline_scripts = [body for src, body in parser.scripts if not src.strip() and body.strip()]
    check(not external_scripts, "Tashqi JavaScript fayllari yo'q", f"Tashqi skriptlar: {external_scripts}")
    check(not re.search(r'<link[^>]+rel=["\']stylesheet', text, re.I), "Tashqi CSS fayli yo'q", "Tashqi stylesheet topildi")
    check(len(inline_scripts) == 1, "Bitta inline JavaScript bloki", f"Inline skriptlar soni: {len(inline_scripts)}")
    check("cdn." not in text.lower(), "CDN ishlatilmagan", "CDN havolasi topildi")
    check("eval(" not in text and "document.write(" not in text, "Xavfsiz bo'lmagan eval/document.write yo'q", "eval yoki document.write topildi")

    js = inline_scripts[0] if inline_scripts else ""
    missing_js = sorted(item for item in REQUIRED_JS if item not in js)
    check(not missing_js, "Asosiy JavaScript funksiyalari mavjud", f"Yetishmayotgan funksiyalar: {missing_js}")

    BUILD.mkdir(exist_ok=True)
    (BUILD / "app.js").write_text(js, encoding="utf-8")
    report = {
        "app": "DoriMed",
        "checkedAt": datetime.now(timezone.utc).isoformat(),
        "fileSizeBytes": APP.stat().st_size,
        "lines": text.count("\n") + 1,
        "ids": len(parser.ids),
        "inlineScripts": len(inline_scripts),
        "errors": errors,
        "warnings": warnings,
        "checks": checks,
    }
    (BUILD / "check-report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    lines = [
        "DoriMed — HTML sifat nazorati",
        "=" * 34,
        *checks,
        "",
    ]
    if warnings:
        lines.extend([f"WARN  {w}" for w in warnings])
    if errors:
        lines.extend([f"FAIL  {e}" for e in errors])
        REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print("\n".join(lines))
        return 1

    lines.append(f"Natija: {len(checks)} ta tekshiruv muvaffaqiyatli o'tdi.")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
