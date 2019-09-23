from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

# Django contains a registry of installed applications that stores configuration and
# provides introspection. It also maintains a list of available models.
# This registry is simply called apps and it’s available in django.apps:
