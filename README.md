<h1 align="center">🧱 Going ACF-free</h1>

<p align="center">
  <strong>Replacing a plugin dependency with core WordPress. A talk for WP Suomi 2026.</strong>
</p>

<p align="center">
  <img style="height:28px;width:auto;" src="https://github.com/user-attachments/assets/86155721-5148-4ca1-b2f1-9731af65bf27" alt="Keynote" />
  <img src="https://img.shields.io/badge/Google%20Slides-FBBC04?style=for-the-badge&logo=googleslides&logoColor=white" alt="Google Slides" />
  <img src="https://img.shields.io/badge/PDF-b21c20?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTYgMmg4bDYgNnYxMmEyIDIgMCAwIDEtMiAySDZhMiAyIDAgMCAxLTItMlY0YTIgMiAwIDAgMSAyLTJ6bTcgMnY1aDVsLTUtNXpNNy41IDEzSDljMS4xIDAgMS45LjcgMS45IDEuN1MxMC4xIDE2LjUgOSAxNi41aC0uNlYxOGgtLjl2LTV6bS45Ljh2MS45SDljLjYgMCAxLS40IDEtLjk1UzkuNiAxMy44IDkgMTMuOGgtLjZ6TTEyIDEzaDEuNWMxLjQgMCAyLjMgMSAyLjMgMi41UzE0LjkgMTggMTMuNSAxOEgxMnYtNXptLjkuOHYzLjRoLjVjLjkgMCAxLjQtLjYgMS40LTEuN3MtLjUtMS43LTEuNC0xLjdoLS41ek0xNi44IDEzaDIuOHYuOGgtMS45djEuM2gxLjh2LjhoLTEuOFYxOGgtLjl2LTV6Ii8+PC9zdmc+&logoColor=white" alt="PDF" />
  <img src="https://img.shields.io/badge/WordPress-21759B?style=for-the-badge&logo=wordpress&logoColor=white" alt="WordPress" />
  <img src="https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white" alt="macOS" />
</p>

---

<img width="1920" height="1080" alt="Going ACF-free cover slide" src="cover.png" />

> [!IMPORTANT]  
> These slides are a work in progress and subject to change until the talk has been given.

## The talk

| | |
| -- | -- |
| Event | [WP Suomi 2026](https://wpsuomi.fi/), Hotel Lasaretti, Oulu |
| Slot | Thursday 16.10.2026, 14:10-14:55, main stage, 35 minutes plus Q&A |
| Complexity | Hard |
| Audience | Theme developers and agencies maintaining ACF-dependent WordPress sites |

Advanced Custom Fields has been a default in WordPress work for over a decade, to the point where a lot of sites cannot be maintained without it. Core has caught up considerably since then, particularly in how native Gutenberg blocks handle custom data and how blocks can be registered. Rolle goes through what core offers in place of the features developers lean on most, what changes in how you build once the plugin is gone, and where ACF is still the more sensible choice.

## Structure

| Path | What it is |
| -- | -- |
| `Going ACF-free.key` | The deck used for presenting, and the source of truth |
| `export/` | Exports for the organisers: `.pptx` for Google Slides and a `.pdf` |
| `keyassets/` | Images used on the slides: stamps, logos, GIFs, screenshots, code panels, diagrams and their HTML sources |
| `photos/` | Photos used on the About slide |
| `minutes.json` | Estimated minutes per slide, used by the footer timing bars |
| `tools/` | The AppleScript helpers that edit the open deck in Keynote |
| `talk.py` | The source of the first version of the deck, kept for reference |
| `speaker-notes.md`, `OUTLINE.md` | Early notes, and the running order with speaker notes exported from the deck |

## Working on the deck

The first version of the deck was generated with [keynote-base](https://github.com/rollecode/keynote-base). Since then it has been edited in Keynote, and it is not generated again. Changes are made to the `.key` file in Keynote, by hand or with `tools/newsection.py`.

The timing bar in each slide footer shows how many minutes into the talk you should be on that slide. After adding or moving slides, update `minutes.json` and run this in the keynote-base root:

```bash
python3 scripts/refresh-progress.py talks/wpsuomi-2026 --minutes=minutes.json
```
