"""
@brief      test log(time=0s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import check_pep8, ExtTestCase


def _run_cmd_filter(name):
    print("#", name)
    return True


class TestCodeStyle(ExtTestCase):
    """Test style."""

    def test_style_src(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        src_ = os.path.normpath(os.path.join(thi, "..", "..", "src"))
        check_pep8(src_, fLOG=fLOG, run_cmd_filter=_run_cmd_filter,
                   pylint_ignore=('C0103', 'C1801', 'R1705', 'W0108', 'W0613',
                                  'R0911', 'W0201', 'W0622', 'R1702',
                                  'C0111', 'W0703', 'C0200', 'C0415', 'C0209',
                                  'R1735'),
                   neg_pattern='.*MokadiGrammar_((frParser)|(frListener)|(frLexer))[.]py$',
                   skip=["Unable to import 'ensae_teaching_cs.pythonnet'",
                         "treant_wrapper.py:38: W0603",
                         "No name 'imwrite' in module 'cv2'",
                         "No name 'VideoCapture' in module 'cv2'",
                         "pydata2016.py:77: W0612",
                         "mokadi_mails.py:42: W0612",
                         "Unable to import 'pymmails.grabber'",
                         "mokadi_action_slides.py:84: W0612",
                         "gui_mokadi_process.py:13: W0612",
                         "Redefining name 'fLOG' from outer scope",
                         "Access to member 'thread_listen' before its definition",
                         "Instance of 'Exception' has no 'strerror'",
                         "Instance of 'Exception' has no 'errno'",
                         "gui_mokadi.py:129",
                         "gui_mokadi.py:78: W0612",
                         "Unused variable 'ensae_teaching_cs'",
                         "Unable to import 'ensae_teaching_cs'",
                         "Unable to import 'pygame'",
                         "Unable to import 'pygame.camera'",
                         "Unable to import 'cv2'",
                         "Unable to import 'keyring'",
                         "Unable to import 'pyaudio'",
                         ])

    def test_style_test(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        test = os.path.normpath(os.path.join(thi, "..", ))
        check_pep8(test, fLOG=fLOG, neg_pattern="temp_.*", run_cmd_filter=_run_cmd_filter,
                   pylint_ignore=('C0103', 'C1801', 'R1705', 'W0108', 'W0613',
                                  'C0111', 'W0703', 'W0101', 'R1707',
                                  'W0611', 'C0415', 'C0209', 'R1735'),
                   skip=["Unable to import 'ensae_teaching_cs.pythonnet'",
                         "Redefining name 'path' from outer scope",
                         "Unable to import 'keyring'",
                         "W0143: Comparing against a callable",
                         ])


if __name__ == "__main__":
    unittest.main()
