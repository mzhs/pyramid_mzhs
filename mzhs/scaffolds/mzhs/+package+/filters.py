import re

from markdown import markdown as md

from html import escape


def markdown(value):
    return md(value)

def strip_html(value):
    return re.sub('<.*?>', '', value)

def nl2br(value):
    return escape(value).replace('\n', '<br>\n')

