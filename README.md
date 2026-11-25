# parmet.com-jeffrey

Jekyll site built by GitHub Pages. Live at https://jeffrey-parmet.github.io/parmet.com-jeffrey/ — every push to `main` rebuilds and republishes.

## Add a post

Create `writing/_posts/YYYY-MM-DD-slug.md`:

```markdown
---
title: Post title
---

Body in Markdown.
```

Push. It appears at `/writing/slug.html`, on the Writing page, and in "Recent writing" on the homepage (newest three).

## Preview locally

```sh
docker run --rm -p 4000:4000 -v "$PWD":/srv/jekyll jekyll/jekyll:4 jekyll serve
```

Then open http://localhost:4000/parmet.com-jeffrey/.

## Layout

- `_layouts/default.html`: sidebar and page shell, shared by every page.
- `_layouts/post.html`: post title and date.
- `style.css`: all styling.

## Images

- Photo: `img/me.jpeg`, shown as a circle on the homepage.
- Icons: `img/icon-<size>`. The favicon is `icon-32.jpg`; drop in a replacement with the same name.
