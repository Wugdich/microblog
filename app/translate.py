from flask_babel import _
import translators as ts


def translate(text: str, source_language: str, dest_language: str) -> str:
    try:
        return ts.google(text, from_language=source_language,
                         to_language=dest_language)
    except:
        return _('Error: the translations service failed.')

