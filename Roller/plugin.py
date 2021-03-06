# ##
# Copyright (c) 2014, David Rickman
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import random


class Roller(callbacks.Plugin):
    """rolls dice for Vampire the Masquerade"""
    threaded = False

    def __init__(self, irc):
        #pass
        self.__parent = super(Roller, self)
        self.__parent.__init__(irc)

    def roll(self, irc, msg, args, num, difficulty, texty):
        """
        !roll <number of dice> <difficulty> (optional action text)"""

        #VARIABLES
        success = ones = spec = 0
        difficulty = int(difficulty)
        fancy_outcome = []

        # CALCULATIONS
        #compare outcome list with successes, 1s and 10s rolled and calc accordingly
        for s in range(num):
            die = random.randint(1, 10)

            if die >= difficulty:  #success evaluation
                success += 1
                if die == 10:
                    spec += 1
                    fancy_outcome.append(ircutils.mircColor(die, 10))
                else:
                    fancy_outcome.append(ircutils.mircColor(die, 12))

            elif die == 1:  #math for ones
                ones += 1
                fancy_outcome.append(ircutils.mircColor(die, 4))

            else:
                fancy_outcome.append(ircutils.mircColor(die, 6))

        #the aftermath
        total = success - ones
        if spec > ones:
            spec = spec - ones + total
        else:
            spec = total

        # OUTPUT, bottom up approach: from botch, failure, success, specialty success.
        if success == 0 and ones > 0:
            total = "BOTCH  >:D"
            dicepool = 'rolled: %s (%s)@diff %s' % (" ".join(fancy_outcome), total, str(difficulty))
            irc.reply(dicepool)
        elif 0 <= success <= ones:
            total = "Failure"
            dicepool = 'rolled: %s (%s)@diff %s' % (" ".join(fancy_outcome), total, str(difficulty))
            irc.reply(dicepool)
        elif 0 < total == spec:
            dicepool = 'rolled: %s (%s successes)@diff %s' % (" ".join(fancy_outcome), total, str(difficulty))
            irc.reply(dicepool)
        elif 0 < total < spec:
            dicepool = 'rolled: %s (%s successes (spec: %s))@diff %s' % (
                " ".join(fancy_outcome), total, spec, str(difficulty))
            irc.reply(dicepool)

    roll = wrap(roll, ['int', 'int', optional('text')])


Class = Roller
