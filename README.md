# Beamer Pandoc template

Template to write a presentation in markdown, which is then converted to beamer via `pandoc`.

As of March 2020, it relies on external files - it's still a bit of a work in progress.

## Use

```bash
$ cookiecutter https://github.com/raymondEhlers/beamer-pandoc-template.git
```

Note: It depends on [cookiecutter PR #994](https://github.com/cookiecutter/cookiecutter/pull/944) (or similar)
to allow a jinja2 filter to be defined within the template. It is merged in my fork (which I think installed
locally).
