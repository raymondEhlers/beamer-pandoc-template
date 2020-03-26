
""" Convert time for proper display.

Note:
    It's okay to import arrow, as this filter is to be used in conjunction with
    cookiecutter, which installs jinja2-time, which depends on arrow. So it should
    always be available anywhere this filter will be useful.

.. codeauthor:: Raymond Ehlers <raymond.ehlers@cern.ch>, ORNL
"""

import arrow
import jinja2
from jinja2.ext import Extension


def format_time(input_time: str, format: str = "YYYY-MM-DD") -> str:
    t = arrow.get(input_time)
    # Use the arrow format when we think is appropriate (YYYY is meaningful for arrow and unlikely to show up otherwise)
    if "YYYY" in format:
        #print(t.format(format))
        return t.format(format)
    # And if not arrow, use the standard strftime.
    #print(t.strftime(format))
    return t.strftime(format)


class FormatTime(Extension):

    def __init__(self, environment: jinja2.Environment):
        super(Extension, self).__init__()
        environment.filters["format_time"] = format_time

__all__ = ["FormatTime"]
