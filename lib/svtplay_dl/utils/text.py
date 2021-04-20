import html
import re


def ensure_unicode(s):
    """
    Ensure string is a unicode string. If it isn't it assumed it is
    utf-8 and decodes it to a unicode string.
    """
    if isinstance(s, bytes):
        s = s.decode("utf-8", "replace")
    return s


def decode_html_entities(s):
    """
    Replaces html entities with the character they represent.

        >>> print(decode_html_entities("&lt;3 &amp;"))
        <3 &
    """

    def unesc(m):
        return html.unescape(m.group())

    return re.sub(r"(&[^;]+;)", unesc, ensure_unicode(s))


def filenamify(title):
    """
    Convert a string to something suitable as a file name. E.g.

     Matlagning del 1 av 10 - Räksmörgås | SVT Play
       ->  matlagning.del.1.av.10.-.raksmorgas.svt.play
    """
    # ensure it is unicode
    title = ensure_unicode(title)

    # Drop any leading/trailing whitespace that may have appeared
    title = title.strip()

    # Replace multiple whitespace with single space
    title = re.sub(r"\s+", " ", title)

    return title


def exclude(config, name):
    if config.get("exclude"):
        excludes = config.get("exclude").split(",")
        for exclude in excludes:
            if exclude in name:
                return True
    return False
