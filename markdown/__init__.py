"""
Python Markdown

A Python implementation of John Gruber's Markdown.

Documentation: https://python-markdown.github.io/
GitHub: https://github.com/Python-Markdown/markdown/
PyPI: https://pypi.org/project/Markdown/

Started by Manfred Stienstra (http://www.dwerg.net/).
Maintained for a few years by Yuri Takhteyev (http://www.freewisdom.org).
Currently maintained by Waylan Limberg (https://github.com/waylan),
Dmitry Shachnev (https://github.com/mitya57) and Isaac Muse (https://github.com/facelessuser).

Copyright 2007-2018 The Python Markdown Project (v. 1.7 and later)
Copyright 2004, 2005, 2006 Yuri Takhteyev (v. 0.2-1.6b)
Copyright 2004 Manfred Stienstra (the original version)

License: BSD (see LICENSE.md for details).
"""

import sys

# TODO: Remove this check at some point in the future.
# (also remove flake8's 'ignore E402' comments below)
if sys.version_info[0] < 3:  # pragma: no cover
    raise ImportError('A recent version of Python 3 is required.')

from .core import Markdown, markdown, markdownFromFile  # noqa: E402
from .__meta__ import __version__, __version_info__     # noqa: E402
import warnings                                         # noqa: E402

# For backward compatibility as some extensions expect it...
from .extensions import Extension  # noqa

__all__ = ['Markdown', 'markdown', 'markdownFromFile']

__deprecated__ = {
    "version": ("__version__", __version__),
    "version_info": ("__version_info__", __version_info__)
}


def __getattr__(name):
    """Get attribute."""

    deprecated = __deprecated__.get(name)
    if deprecated:
        warnings.warn(
            "'{}' is deprecated. Use '{}' instead.".format(name, deprecated[0]),
            category=DeprecationWarning,
            stacklevel=(3 if (3, 7) <= sys.version_info else 4)
        )
        return deprecated[1]
    raise AttributeError("module '{}' has no attribute '{}'".format(__name__, name))
