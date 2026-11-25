# parmet.com-jeffrey

Plain HTML + one CSS file. No build step. Live at https://jeffrey-parmet.github.io/parmet.com-jeffrey/ — every push to `main` republishes via GitHub Pages.

## Preview

```sh
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Add a post

1. Copy `writing/_template.html` to `writing/<slug>.html` and fill in the title, date, and body.
2. Add a `<li>` to the top of the list in `writing/index.html`.
3. Add it to "Recent writing" on `index.html` (keep three or fewer so the homepage fits one screen).

## Images

- Photo: `img/me.jpeg`, shown as a circle on the homepage.
- Icons: `img/icon-<size>`. The favicon is `icon-32.jpg`; drop in a replacement with the same name.
