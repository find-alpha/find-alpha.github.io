# FIND-A Website

FIND-A(파인드알파) 공식 홈페이지입니다. Hugo Extended, Tailwind CSS, Hugo Modules 기반의 정적 사이트이며 GitHub Pages로 배포합니다.

Live site: <https://find-alpha.github.io/>

## Stack

- Hugo Extended `0.151.0`
- Node.js `22+`
- Go `1.23+`
- Tailwind CSS `4`
- GitHub Actions + GitHub Pages

## Repository Layout

```text
.
├── hugo.toml
├── config/_default/
├── content/english/
├── data/theme.json
├── assets/
├── layouts/
├── static/
├── themes/hugoplate/
├── scripts/
└── .github/workflows/main.yml
```

Key editing paths:

- Site metadata and base URL: `hugo.toml`
- Logo, SEO metadata, search, widgets, and feature toggles: `config/_default/params.toml`
- Navigation menus: `config/_default/menus.en.toml`
- Homepage and page content: `content/english/`
- Theme colors and fonts: `data/theme.json`
- Layout overrides: `layouts/`
- Static assets: `static/`

## Local Setup

Install prerequisites first:

- Hugo Extended `0.151.0`
- Node.js `22+`
- Go `1.23+`

Then run:

```powershell
npm install
npm run dev
```

The development server runs with Hugo's default local URL, usually:

```text
http://localhost:1313/
```

## Build

```powershell
npm run build
```

The generated site is written to `public/`. Do not edit `public/` directly.

## Deployment

GitHub Pages is the canonical deployment target.

- Workflow: `.github/workflows/main.yml`
- Trigger: push to `main` or manual workflow dispatch
- Output artifact: `public/`
- Pages URL: <https://find-alpha.github.io/>

The repository may still contain template-era deployment files for other hosts. GitHub Pages is the supported path unless those files are intentionally updated later.

## Content Workflow

1. Edit Markdown content under `content/english/`.
2. Update shared site settings in `hugo.toml` or `config/_default/*.toml`.
3. Run `npm run dev` and check the page locally.
4. Run `npm run build` before pushing.
5. Commit and push to `main`.

## Notes

- This site is based on the Hugoplate theme, but the root project is already set up. Do not run `npm run project-setup` during normal development or deployment.
- Keep generated folders such as `public/`, `resources/`, `node_modules/`, and `hugo_stats.json` out of version control.
