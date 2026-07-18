# Aether Seismic — Seismic Intelligence OS

An interactive, presentation-grade UI for a subsurface intelligence platform:
analytics, live fault inference, prospect intelligence, and geological reporting.
Built with Google Stitch (Tailwind + three.js). Fully static — open in any browser.

## Screens
- **`index.html`** — launcher (start here)
- `seismic_analytics_dashboard/code.html` — Analytics Dashboard
- `live_inference_aether_seismic/code.html` — Live Inference
- `prospect_intelligence_ai/code.html` — Prospect Intelligence AI
- `geological_report_viewer/code.html` — Geological Report Viewer
- `three.js/code.html`, `shader/code.html` — WebGL / shader experiments
- `DESIGN.md` — the "Aether Seismic" design system

## Run locally
Open `index.html` in a browser, or serve the folder:
```bash
python -m http.server 8000   # then visit http://localhost:8000
```

## Deploy (free, static)
- **GitHub Pages:** repo → Settings → Pages → Source: `main` / root. Your app goes live at
  `https://<user>.github.io/seismic-intelligence-os/`.
- The pages load Tailwind, Google Fonts, and three.js from CDNs, so they need internet at runtime.
