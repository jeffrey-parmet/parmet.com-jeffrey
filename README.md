# parmet.com-jeffrey

Jekyll site built by GitHub Pages. Live at parmet.com/jeffrey

## Add a post

Create `_posts/YYYY-MM-DD-slug.md`:

```markdown
---
title: Post title
---

Body in Markdown.
```

Push.

## Preview locally

```sh
docker run --rm -p 4000:4000 -v "$PWD":/srv/jekyll jekyll/jekyll:4 jekyll serve --host 0.0.0.0
```

Then open http://localhost:4000/.

## Add a work case

Put the thumbnail in `img/projects/`, then create `_projects/NN-slug.md`. Cards sort by filename:

```markdown
---
title: Case title
image: thumb.jpg
link: https://github.com/you/repo
---

Short text under the thumbnail.
```
