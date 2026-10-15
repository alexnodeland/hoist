# Palette

One accent, **petrol**, and neutrals biased towards its cool hue. The accent marks what Hoist adds: its reads in a diagram, a link, the primary action. Everything else is ink on paper, or paper on ink. The values live in [`tokens.css`](tokens.css) as CSS custom properties, with light as the default and dark under `prefers-color-scheme` (or `<html data-theme="dark">`).

Every color was chosen in OKLCH and converted to sRGB inside its gamut: petrol at hue 200, the neutrals at hue 215 (light) and 220 (dark) with a chroma of 0.003–0.014, enough to read as one family with the accent and too little to read as a color.

## Tokens

| Token | Light | Dark | Use |
|---|---|---|---|
| `--hoist-bg` | `#f8fbfb` | `#0b0f11` | Page background: paper and ink |
| `--hoist-surface` | `#ffffff` | `#121719` | Cards, panels, the explainer's stage |
| `--hoist-surface-2` | `#eff3f4` | `#191f21` | Code blocks, wells, table stripes |
| `--hoist-border` | `#dae1e3` | `#272f32` | Hairlines; never the only cue |
| `--hoist-border-strong` | `#7e888b` | `#606b6f` | Outlines of controls, the baseline in charts |
| `--hoist-text` | `#141c1e` | `#eceff0` | Body text and headings |
| `--hoist-text-muted` | `#4a5557` | `#b3bcbf` | Secondary text |
| `--hoist-text-subtle` | `#646e70` | `#909a9d` | Captions, labels, scope lines |
| `--hoist-accent` | `#02767b` | `#5dd2d8` | Links and accent text |
| `--hoist-accent-hover` | `#015f63` | `#93e5e9` | Hover and pressed states |
| `--hoist-accent-graphic` | `#039298` | `#33c0c7` | Marks, bars, icons, Hoist's reads in diagrams |
| `--hoist-accent-soft` | `#e0f5f6` | `#0b292c` | Tinted wells behind accent content |
| `--hoist-accent-fill` | `#02767b` | `#33c0c7` | Buttons and badges |
| `--hoist-on-accent` | `#ffffff` | `#0b0f11` | Text on `--hoist-accent-fill` |
| `--hoist-focus` | `#02767b` | `#5dd2d8` | Focus rings |
| `--hoist-chart-baseline` | `#4a5557` | `#606b6f` | The baseline series in a chart |
| `--hoist-chart-accent` | `#039298` | `#33c0c7` | Hoist's series in a chart |

**Brand constants** do not change with the theme; the logo files use them.

| Token | Value | Use |
|---|---|---|
| `--hoist-ink` | `#141c1e` | The mark's first bar and the wordmark, on light |
| `--hoist-paper` | `#f8fbfb` | The same, on dark; the bars on the icon tile |
| `--hoist-petrol` | `#02767b` | The favicon and app-icon tile |
| `--hoist-petrol-light` | `#039298` | The mark's accent bars, on light |
| `--hoist-petrol-dark` | `#33c0c7` | The mark's accent bars, on dark |

Type tokens: `--hoist-font-sans` (Inter) and `--hoist-font-mono` (JetBrains Mono), each with system fallbacks; `--hoist-radius-sm|md|lg` are 6, 10 and 14 px.

## Using the accent

- **One job.** Petrol is Hoist's own contribution. In a diagram of an episode, the agent's LLM turns and the server are neutral; the reads Hoist made are petrol. A detour, a read the agent did not use, is a petrol outline, dashed, not a new color.
- **Charts.** A chart compares Hoist with a baseline: the baseline is `--hoist-chart-baseline`, Hoist is `--hoist-chart-accent`, and each bar carries its value as text, so no reading depends on color alone. The pair differs in lightness, not only in hue: checked with a color-vision-deficiency simulation (OKLab), the worst case is ΔE 15.9 (deuteranopia) in light and 21.8 in dark, and 18.2 and 24.2 with normal vision. A mid-gray baseline of the accent's lightness would fail that check (ΔE 2.0 under protanopia), which is why the light baseline is the darker slate.
- **No status colors.** The brand has no red or green. Where a page needs to flag an error or a warning, say so in words with an icon, and use the host's own status color if it has one.
- **Text in petrol** uses `--hoist-accent`, never `--hoist-accent-graphic`: the graphic tone reaches 3:1, not 4.5:1, on the light background.

## Contrast

Computed by [`tools/contrast.mjs`](tools/contrast.mjs) from `tokens.css`, with the WCAG 2.2 formula. Text needs 4.5:1 (AA for normal text); marks, bars, icons, control outlines and focus rings need 3:1 (AA, non-text contrast). Every pair passes. The tightest are subtle text on the tinted well in light (4.63:1), petrol bars on the light code background (3.38:1) and control outlines on the dark code background (3.04:1).

Run `node brand/tools/contrast.mjs --check` after changing a token; it exits with 1 if a pair fails, or if the two copies of the dark theme in `tokens.css` differ.

<details>
<summary>Every pair (80)</summary>

| Theme | Foreground | Background | Kind | Ratio | Needs | Result |
|---|---|---|---|---|---|---|
| light | `--hoist-text` #141c1e | `--hoist-bg` #f8fbfb | text | 16.62:1 | 4.5:1 | pass |
| light | `--hoist-text` #141c1e | `--hoist-surface` #ffffff | text | 17.29:1 | 4.5:1 | pass |
| light | `--hoist-text` #141c1e | `--hoist-surface-2` #eff3f4 | text | 15.48:1 | 4.5:1 | pass |
| light | `--hoist-text` #141c1e | `--hoist-accent-soft` #e0f5f6 | text | 15.28:1 | 4.5:1 | pass |
| light | `--hoist-text-muted` #4a5557 | `--hoist-bg` #f8fbfb | text | 7.40:1 | 4.5:1 | pass |
| light | `--hoist-text-muted` #4a5557 | `--hoist-surface` #ffffff | text | 7.70:1 | 4.5:1 | pass |
| light | `--hoist-text-muted` #4a5557 | `--hoist-surface-2` #eff3f4 | text | 6.89:1 | 4.5:1 | pass |
| light | `--hoist-text-muted` #4a5557 | `--hoist-accent-soft` #e0f5f6 | text | 6.80:1 | 4.5:1 | pass |
| light | `--hoist-text-subtle` #646e70 | `--hoist-bg` #f8fbfb | text | 5.04:1 | 4.5:1 | pass |
| light | `--hoist-text-subtle` #646e70 | `--hoist-surface` #ffffff | text | 5.24:1 | 4.5:1 | pass |
| light | `--hoist-text-subtle` #646e70 | `--hoist-surface-2` #eff3f4 | text | 4.69:1 | 4.5:1 | pass |
| light | `--hoist-text-subtle` #646e70 | `--hoist-accent-soft` #e0f5f6 | text | 4.63:1 | 4.5:1 | pass |
| light | `--hoist-accent` #02767b | `--hoist-bg` #f8fbfb | text | 5.20:1 | 4.5:1 | pass |
| light | `--hoist-accent` #02767b | `--hoist-surface` #ffffff | text | 5.41:1 | 4.5:1 | pass |
| light | `--hoist-accent` #02767b | `--hoist-surface-2` #eff3f4 | text | 4.84:1 | 4.5:1 | pass |
| light | `--hoist-accent` #02767b | `--hoist-accent-soft` #e0f5f6 | text | 4.78:1 | 4.5:1 | pass |
| light | `--hoist-accent-hover` #015f63 | `--hoist-bg` #f8fbfb | text | 7.16:1 | 4.5:1 | pass |
| light | `--hoist-accent-hover` #015f63 | `--hoist-surface` #ffffff | text | 7.45:1 | 4.5:1 | pass |
| light | `--hoist-accent-hover` #015f63 | `--hoist-surface-2` #eff3f4 | text | 6.67:1 | 4.5:1 | pass |
| light | `--hoist-accent-hover` #015f63 | `--hoist-accent-soft` #e0f5f6 | text | 6.59:1 | 4.5:1 | pass |
| light | `--hoist-on-accent` #ffffff | `--hoist-accent-fill` #02767b | text | 5.41:1 | 4.5:1 | pass |
| light | `--hoist-accent-graphic` #039298 | `--hoist-bg` #f8fbfb | graphic | 3.62:1 | 3:1 | pass |
| light | `--hoist-accent-graphic` #039298 | `--hoist-surface` #ffffff | graphic | 3.77:1 | 3:1 | pass |
| light | `--hoist-accent-graphic` #039298 | `--hoist-surface-2` #eff3f4 | graphic | 3.38:1 | 3:1 | pass |
| light | `--hoist-border-strong` #7e888b | `--hoist-bg` #f8fbfb | graphic | 3.49:1 | 3:1 | pass |
| light | `--hoist-border-strong` #7e888b | `--hoist-surface` #ffffff | graphic | 3.63:1 | 3:1 | pass |
| light | `--hoist-border-strong` #7e888b | `--hoist-surface-2` #eff3f4 | graphic | 3.25:1 | 3:1 | pass |
| light | `--hoist-focus` #02767b | `--hoist-bg` #f8fbfb | graphic | 5.20:1 | 3:1 | pass |
| light | `--hoist-focus` #02767b | `--hoist-surface` #ffffff | graphic | 5.41:1 | 3:1 | pass |
| light | `--hoist-focus` #02767b | `--hoist-surface-2` #eff3f4 | graphic | 4.84:1 | 3:1 | pass |
| light | `--hoist-chart-baseline` #4a5557 | `--hoist-bg` #f8fbfb | graphic | 7.40:1 | 3:1 | pass |
| light | `--hoist-chart-baseline` #4a5557 | `--hoist-surface` #ffffff | graphic | 7.70:1 | 3:1 | pass |
| light | `--hoist-chart-baseline` #4a5557 | `--hoist-surface-2` #eff3f4 | graphic | 6.89:1 | 3:1 | pass |
| light | `--hoist-chart-accent` #039298 | `--hoist-bg` #f8fbfb | graphic | 3.62:1 | 3:1 | pass |
| light | `--hoist-chart-accent` #039298 | `--hoist-surface` #ffffff | graphic | 3.77:1 | 3:1 | pass |
| light | `--hoist-chart-accent` #039298 | `--hoist-surface-2` #eff3f4 | graphic | 3.38:1 | 3:1 | pass |
| dark | `--hoist-text` #eceff0 | `--hoist-bg` #0b0f11 | text | 16.66:1 | 4.5:1 | pass |
| dark | `--hoist-text` #eceff0 | `--hoist-surface` #121719 | text | 15.63:1 | 4.5:1 | pass |
| dark | `--hoist-text` #eceff0 | `--hoist-surface-2` #191f21 | text | 14.43:1 | 4.5:1 | pass |
| dark | `--hoist-text` #eceff0 | `--hoist-accent-soft` #0b292c | text | 13.29:1 | 4.5:1 | pass |
| dark | `--hoist-text-muted` #b3bcbf | `--hoist-bg` #0b0f11 | text | 9.96:1 | 4.5:1 | pass |
| dark | `--hoist-text-muted` #b3bcbf | `--hoist-surface` #121719 | text | 9.35:1 | 4.5:1 | pass |
| dark | `--hoist-text-muted` #b3bcbf | `--hoist-surface-2` #191f21 | text | 8.63:1 | 4.5:1 | pass |
| dark | `--hoist-text-muted` #b3bcbf | `--hoist-accent-soft` #0b292c | text | 7.94:1 | 4.5:1 | pass |
| dark | `--hoist-text-subtle` #909a9d | `--hoist-bg` #0b0f11 | text | 6.69:1 | 4.5:1 | pass |
| dark | `--hoist-text-subtle` #909a9d | `--hoist-surface` #121719 | text | 6.28:1 | 4.5:1 | pass |
| dark | `--hoist-text-subtle` #909a9d | `--hoist-surface-2` #191f21 | text | 5.79:1 | 4.5:1 | pass |
| dark | `--hoist-text-subtle` #909a9d | `--hoist-accent-soft` #0b292c | text | 5.33:1 | 4.5:1 | pass |
| dark | `--hoist-accent` #5dd2d8 | `--hoist-bg` #0b0f11 | text | 10.71:1 | 4.5:1 | pass |
| dark | `--hoist-accent` #5dd2d8 | `--hoist-surface` #121719 | text | 10.05:1 | 4.5:1 | pass |
| dark | `--hoist-accent` #5dd2d8 | `--hoist-surface-2` #191f21 | text | 9.27:1 | 4.5:1 | pass |
| dark | `--hoist-accent` #5dd2d8 | `--hoist-accent-soft` #0b292c | text | 8.54:1 | 4.5:1 | pass |
| dark | `--hoist-accent-hover` #93e5e9 | `--hoist-bg` #0b0f11 | text | 13.41:1 | 4.5:1 | pass |
| dark | `--hoist-accent-hover` #93e5e9 | `--hoist-surface` #121719 | text | 12.58:1 | 4.5:1 | pass |
| dark | `--hoist-accent-hover` #93e5e9 | `--hoist-surface-2` #191f21 | text | 11.61:1 | 4.5:1 | pass |
| dark | `--hoist-accent-hover` #93e5e9 | `--hoist-accent-soft` #0b292c | text | 10.69:1 | 4.5:1 | pass |
| dark | `--hoist-on-accent` #0b0f11 | `--hoist-accent-fill` #33c0c7 | text | 8.72:1 | 4.5:1 | pass |
| dark | `--hoist-accent-graphic` #33c0c7 | `--hoist-bg` #0b0f11 | graphic | 8.72:1 | 3:1 | pass |
| dark | `--hoist-accent-graphic` #33c0c7 | `--hoist-surface` #121719 | graphic | 8.18:1 | 3:1 | pass |
| dark | `--hoist-accent-graphic` #33c0c7 | `--hoist-surface-2` #191f21 | graphic | 7.55:1 | 3:1 | pass |
| dark | `--hoist-border-strong` #606b6f | `--hoist-bg` #0b0f11 | graphic | 3.51:1 | 3:1 | pass |
| dark | `--hoist-border-strong` #606b6f | `--hoist-surface` #121719 | graphic | 3.30:1 | 3:1 | pass |
| dark | `--hoist-border-strong` #606b6f | `--hoist-surface-2` #191f21 | graphic | 3.04:1 | 3:1 | pass |
| dark | `--hoist-focus` #5dd2d8 | `--hoist-bg` #0b0f11 | graphic | 10.71:1 | 3:1 | pass |
| dark | `--hoist-focus` #5dd2d8 | `--hoist-surface` #121719 | graphic | 10.05:1 | 3:1 | pass |
| dark | `--hoist-focus` #5dd2d8 | `--hoist-surface-2` #191f21 | graphic | 9.27:1 | 3:1 | pass |
| dark | `--hoist-chart-baseline` #606b6f | `--hoist-bg` #0b0f11 | graphic | 3.51:1 | 3:1 | pass |
| dark | `--hoist-chart-baseline` #606b6f | `--hoist-surface` #121719 | graphic | 3.30:1 | 3:1 | pass |
| dark | `--hoist-chart-baseline` #606b6f | `--hoist-surface-2` #191f21 | graphic | 3.04:1 | 3:1 | pass |
| dark | `--hoist-chart-accent` #33c0c7 | `--hoist-bg` #0b0f11 | graphic | 8.72:1 | 3:1 | pass |
| dark | `--hoist-chart-accent` #33c0c7 | `--hoist-surface` #121719 | graphic | 8.18:1 | 3:1 | pass |
| dark | `--hoist-chart-accent` #33c0c7 | `--hoist-surface-2` #191f21 | graphic | 7.55:1 | 3:1 | pass |
| brand | logo on light: ink bar #141c1e | #f8fbfb | graphic | 16.62:1 | 3:1 | pass |
| brand | logo on light: petrol bars #039298 | #f8fbfb | graphic | 3.62:1 | 3:1 | pass |
| brand | logo on light: petrol bars on white #039298 | #ffffff | graphic | 3.77:1 | 3:1 | pass |
| brand | logo on dark: paper bar #f8fbfb | #0b0f11 | graphic | 18.51:1 | 3:1 | pass |
| brand | logo on dark: petrol bars #33c0c7 | #0b0f11 | graphic | 8.72:1 | 3:1 | pass |
| brand | icon tile: paper bars on petrol #f8fbfb | #02767b | graphic | 5.20:1 | 3:1 | pass |
| brand | wordmark: ink on paper #141c1e | #f8fbfb | text | 16.62:1 | 4.5:1 | pass |
| brand | wordmark: paper on dark bg #f8fbfb | #0b0f11 | text | 18.51:1 | 4.5:1 | pass |

</details>
