# MkDocs OpenApi Markdown Plugin

This plugin generates markdown file from openapi spec file. (json or yaml)


## Configuration

Add following lines to your `mkdocs.yml` configuration file:

```
plugins:
  - openapi_markdown:
      enabled: true
      openapi_file: openapi.json
      output_file: api_doc.md
```

## Install

`pip install mkdocs-openapi-markdown-plugin`
