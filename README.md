# Still & Clay

Two reading themes for the [Markdown Viewer](https://github.com/simov/markdown-viewer) browser extension. Made for notes, code and mathematical writing, with automatic light and dark appearance.

## Still

Quiet monochrome colors, focused typography and soft code blocks. Inspired by the reading experience of ChatGPT and Codex; an independent, unofficial theme.

| Light | Dark |
| :---: | :---: |
| ![Still light preview](screenshots/still/light.webp) | ![Still dark preview](screenshots/still/dark.webp) |

[Download Still CSS](themes/still/still.css) · [Installation and design guide](themes/still/README.md) · [Offline HTML preview](themes/still/preview.html) · [Sample Markdown](themes/still/sample.md)

These are actual Chrome Markdown Viewer captures. The dark screenshot uses browser media emulation. Download the HTML preview to switch between light, dark and system appearance locally.

## Clay

A warm, paper-like theme with soft off-white and warm gray backgrounds. The original theme, sample and screenshots are preserved.

| Light | Dark |
| :---: | :---: |
| ![Clay light preview](screenshots/light.png) | ![Clay dark preview](screenshots/dark.png) |

[Download Clay CSS](clay.css) · [Original guide](themes/clay/README.md) · [Sample Markdown](sample.md)

## Install

1. Install [Markdown Viewer for Chrome](https://chromewebstore.google.com/detail/markdown-viewer/ckkdlimhmcjmikdlpkmbgfkaikojcbjk).
2. Download the CSS for your chosen theme (open its GitHub page and use the raw-file download button).
3. Open **Advanced Options → Settings**, select **Content Theme → CUSTOM**, then **ADD / UPDATE** and choose the CSS file.
4. Set **Color Scheme → AUTO** and **Content Width → AUTO**, then reload the Markdown tab.
5. For local notes, enable **Allow access to file URLs** in Chrome → Extensions → Markdown Viewer → Details.

Only one custom theme is active at a time. Switch between Still and Clay by uploading the other CSS. Upload again after updating a file; the extension stores its own copy.

Themes style the rendered Markdown document, not the extension settings screen. Open a `.md` file to see the result.

### Recommended settings

| Section | Options | Value |
| --- | --- | --- |
| Theme | Content Width / Color Scheme | AUTO / AUTO |
| Content | `mathjax`, `toc`, `autoreload`, `syntax` | on |
| Compiler (markdown-it) | `cjk`, `footnote`, `mark`, `tasklists` | on |

## Project layout

```text
clay.css                  Original Clay theme (compatible path)
sample.md                 Original Clay sample
screenshots/              Original Clay screenshots
themes/clay/README.md     Original Clay guide and creation notes
themes/still/still.css    Still theme
themes/still/preview.html Standalone appearance preview
themes/still/sample.md    Extension rendering sample
scripts/sync_preview.py   Refresh preview CSS after edits
```

## Development

The CSS files are self-contained; no build tools or downloaded fonts are needed. After editing Still, run `python3 scripts/sync_preview.py`. Keep the uploaded CSS below the extension's 8KB limit. Check light and dark appearance, narrow windows, long code lines, tables, formulas and the ToC before release.

Local working directory: `/Users/hejunyi/Documents/codexspace/markdown-viewer-themes`.

## License

[MIT](LICENSE). Original Clay theme and license retained. See the [Clay guide](themes/clay/README.md) for the original creation notes.
