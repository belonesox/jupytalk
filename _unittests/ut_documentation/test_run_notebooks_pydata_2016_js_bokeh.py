# -*- coding: utf-8 -*-
"""
@brief      test log(time=53s)
"""

import sys
import os
import unittest
import shutil
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, skipif_travis
from pyquickhelper.ipythonhelper import execute_notebook_list, execute_notebook_list_finalize_ut
import jupytalk


class TestRunNotebooksPyData2016_js_bokeh(unittest.TestCase):

    @skipif_travis("travis gets stuck can do not move to the next unit test")
    def test_run_notebook_js_bokeh(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from sklearn.datasets import load_iris
        self.assertTrue(load_iris is not None)
        temp = get_temp_folder(__file__, "temp_run_notebooks_js_bokeh")

        # selection of notebooks
        fnb = os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "..", "_doc", "notebooks", "2016", "pydata"))
        keepnote = []
        for f in os.listdir(fnb):
            if os.path.splitext(f)[-1] == ".ipynb" and "js_" in f and "pyjs_" not in f and \
                    "bokeh" in f:
                keepnote.append(os.path.join(fnb, f))

        # function to tell that a can be run
        def valid(cell):
            if 'bar.render(path="render.png")' in cell:
                return False
            return True

        # file to copy
        for cop in ["pydy.svg"]:
            fsrc = os.path.join(fnb, cop)
            if os.path.exists(fsrc):
                dest = temp
                shutil.copy(fsrc, dest)

        # additionnal path to add
        addpaths = [os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "..", "src")),
            os.path.normpath(os.path.join(
                os.path.abspath(os.path.dirname(__file__)), "..", "..", "..", "pyquickhelper", "src")),
            os.path.normpath(os.path.join(
                os.path.abspath(os.path.dirname(__file__)), "..", "..", "..", "jyquickhelper", "src"))
        ]

        keepnote = [_ for _ in keepnote if 'mpld3' not in _]

        # run the notebooks
        res = execute_notebook_list(
            temp, keepnote, fLOG=fLOG, valid=valid, additional_path=addpaths)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=jupytalk)


if __name__ == "__main__":
    unittest.main()
