#!/usr/bin/env python
import sys
from django.template.loader import add_to_builtins
from django.template import Template, Context
from django.conf import settings

settings.configure()
settings.TEMPLATE_DIRS = ['.']

add_to_builtins('django.template.loader_tags')

def render(filename):
    with open(filename) as f:
        html = f.read()
        template = Template(html)
        context = Context()
        return template.render(context)

def main():
    try:
        filename = sys.argv[1]
    except IndexError:
        sys.exit('Please provide template fil path as argument, usage:\n\n\t$ firedj index.html\n')

    print render(filename)


if __name__ == '__main__':
    main()
