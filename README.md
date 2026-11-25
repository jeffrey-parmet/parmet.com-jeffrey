# parmet-com

Plain HTML + one CSS file. No build step.

## Preview

```sh
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Add a post

1. Copy `writing/_template.html` to `writing/<slug>.html` and fill in the title, date, and body.
2. Add a `<li>` to the top of the list in `writing/index.html`.
3. Optionally add it to "Recent writing" on `index.html`.

## Photo

Replace `img/me.svg` with a real photo and update the `src` in `index.html`.
