# Composer theming + branding on SI 26.2 (reskin recipe)

Field-verified 2026-07-21 reskinning a live 26.2 Composer to a purple "Simba
Intelligence" symphony skin with the SI logo. All via documented-ish APIs, basic
auth as admin, vendor media type `application/vnd.composer.v3+json`.

## Themes (colours / skin)

- `GET  /discovery/api/customization/themes` — list (system: composer, modern,
  dark, `__platform__`, and the D+A-branded `d+a_light` which uses `$symphony.*`
  design tokens — that token set IS "symphony").
- `GET  /discovery/api/customization/themes/active` — the active theme.
- `GET  /discovery/api/customization/themes/{id}` — a theme's full JSON.
  (GET `/name/{name}` breaks if the name has a space — use the id.)
- `POST /discovery/api/customization/themes` — create. Body `{"masterThemeId":
  "modern","name":"...","content":{...}}`; strip `id`/`system` first.
- `POST /discovery/api/customization/themes/activate` — body `{"id":"<id>"}`.

Theme colours live at `content.variables.colors.*`. The ones that move the skin:
`brandColor` (the top nav / header bar), `primary`/`primaryVariant`,
`intentPrimary`/`intentPrimaryHover`/`intentPrimaryActive`, `accentColor`,
`linkColor`. The customProperties bind `navbar.background` to `$colors.primary`
and `homePage.banner.background` to `$colors.brandColor`. Chart colours are
`content.variables.palettes.DefaultSequential` (per-N arrays) and
`DefaultCategorical`. A purple "symphony" look: brandColor `#46217C`, primary
`#7C4DFF`, purple/violet sequential + categorical palettes.

## Logo / branding

- `GET /discovery/api/branding` — config JSON. `headerLogo` is **varchar(40)** — a
  filename reference, NOT a data URI (PUTting a data URI there 409s "value too long").
- `GET /discovery/api/branding/images/{headerLogo|loginLogo|favicon}` — serves the
  image (GET only; POST/PUT there are 405).
- The header logo is rendered as `<img src="/api/branding/images/headerLogo">`.

The clean, reversible way to set a custom header logo without the image-upload
endpoint: **custom CSS override**.

- `POST /discovery/api/branding/customCss` — **NO `.css` suffix**, multipart field
  **`fileData`** (the ISW upload convention) → 200 + a new id. The `.css`-suffixed
  path and `-F file=@` and `Content-Type: text/css` all silently no-op or 4xx.
- `GET /discovery/api/branding/customCss.css` — read current CSS (has `.css`).
- POST replaces the whole CSS, so GET current, append your rule, POST combined.

Logo-swap rule (embeds the PNG as a data URI, no varchar limit):
```css
img[src*="headerLogo"] {
  content: url("data:image/png;base64,....") !important;
  height: 34px !important; width: auto !important; object-fit: contain !important;
}
```

Reversible: back up the active theme id, the branding JSON, and the current
customCss before changing; revert by re-activating the old theme and re-POSTing
the original CSS.
