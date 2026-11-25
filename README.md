# parmet.com-jeffrey

Jekyll site built by GitHub Pages. Live at parmet.com/jeffrey

## Add a post

Create `writing/_posts/YYYY-MM-DD-slug.md`:

```markdown
---
title: Post title
---

Body in Markdown.
```

Push.

## Preview locally

```sh
docker run --rm -p 4000:4000 -v "$PWD":/srv/jekyll jekyll/jekyll:4 jekyll serve
```

Then open http://localhost:4000/.