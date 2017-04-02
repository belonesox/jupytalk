# -*- coding: utf-8 -*-
"""
@file
@brief Make Mokadi's engine.
"""
import os
import random
from pyquickhelper.loghelper import CustomLog
from .mokadi_message import MokadiMessage
from .mokadi_info import MokadiInfo
from .mokadi_exceptions import MokadiException


class MokadiEngine:
    """
    Defines results for mokadi.
    """

    _messages = {"dontunderstand": ["Je n'ai pas compris.", "Parlez vous mokadi?"],
                 "failure": ["Un imprévu s'est produit.", "Grosse tuile"]}

    @staticmethod
    def peak_random(mes: list):
        """
        Pick a random message

        @param      mes     list of strings
        @return             one string
        """
        i = random.randint(0, len(mes) - 1)
        return mes[i]

    def __init__(self, root, clog: CustomLog, actions):
        """
        Constructor

        @param      root        root folder
        @param      clog        custom log
        @param      actions     list of actions
        """
        self._clog = clog
        self._root = root
        self._actions = actions

        if not os.path.exists(root):
            raise FileNotFoundError(root)

    def fLOG(self, *l, **p):
        """
        message to string
        """
        self._clog(*l, **p)

    def process(self, message: MokadiMessage, exc=False):
        """
        Process one message and returns an iterator on @see cl MokadiInfo.

        @param      message     @see cl MokadiMessage
        @param      exc         raises an exception if an error happens
        @return                 iterator on @see cl MokadiInfo
        """
        self.fLOG("[MokadiEngine.process]", message)
        res = message.interpret(exc=False)
        if isinstance(res, Exception):
            info = MokadiInfo("error", MokadiEngine.peak_random(
                MokadiEngine._messages["dontunderstand"]), str(res), None)
            self.fLOG("[MokadiEngine.process]", info)
            yield info
        else:
            if exc:
                for info in self.process_interpreted_message(res, message):
                    self.fLOG("[MokadiEngine.process]", info)
                    yield info
            else:
                try:
                    for info in self.process_interpreted_message(res, message):
                        self.fLOG("[MokadiEngine.process]", info)
                        yield info
                except Exception as e:
                    info = MokadiInfo("error", MokadiEngine.peak_random(
                        MokadiEngine._messages["failure"]), str(e), None)
                    self.fLOG("[MokadiEngine.process]", info)
                    yield info

    def process_interpreted_message(self, interpretation, message):
        """
        Process the interpreted message.

        @param      interpretation      interpretation
        @param      message             original message
        @return                         iterator on Info
        """
        done = False
        for act in self._actions:
            if act.can_do(interpretation, message):
                for info in act.process_interpreted_message(interpretation, message):
                    yield info
                done = True
        if not done:
            raise MokadiException(
                "Unable to process '{0}' - '{1}'.".format(interpretation, message))