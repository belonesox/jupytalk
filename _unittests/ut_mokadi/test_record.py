#-*- coding: utf-8 -*-
"""
@brief      test log(time=10s)
"""

import sys
import os
import unittest


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

try:
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper as skip_

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor
from src.jupytalk.mokadi import record_speech, play_speech


class TestRestApiSpeech(unittest.TestCase):

    def test_record(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            # no keys
            return

        fLOG("record")
        record = record_speech(3, fLOG=fLOG)
        fLOG("play")
        play_speech(record)
        fLOG("end")


if __name__ == "__main__":
    unittest.main()