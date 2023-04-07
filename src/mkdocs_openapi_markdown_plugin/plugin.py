from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
from openapi_markdown.generator import to_markdown


class GenApiPlugin(BasePlugin):
    config_scheme = (
        ('enabled', config_options.Type(bool, default=True)),
        ('openapi_file', config_options.Type(str, default='openapi.json')),
        ('output_file', config_options.Type(str, default='api-doc.md')),
    )

    def on_config(self, config, **kwargs):
        enabled = self.config['enabled']
        if not enabled:
            return

        api_file = self.config['openapi_file']
        output_file = self.config['output_file']

        to_markdown(api_file, output_file)
        return config

