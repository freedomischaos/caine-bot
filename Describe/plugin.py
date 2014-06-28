###
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
import supybot.conf as conf
import supybot.world as world
import supybot.irclib as irclib
import supybot.ircmsgs as ircmsgs
import supybot.ircutils as ircutils
import supybot.registry as registry
import supybot.callbacks as callbacks

import MySQLdb


class Describe(callbacks.Plugin):
    """This plugin will register a character and then allow the player to set a description and associated URL."""
    threaded = True

    def __init__(self, irc):
        self.__parent = super(Describe, self)
        self.__parent.__init__(irc)

    #private function for ops(aka storytellers) this will initialize a arg which is the character's IRC nick.
    # this inserts the default record into the database
    # autosets the description to "no description set"
    def newchar(self, irc, msg, args, nick):
        nick = nick
        irc.reply("has registered a new player.", action=True)

    newchar = wrap(newchar, ['admin', 'text'])

    #associate a description to the the irc.nick
    def setdesc(self, irc, msg, args, text):
        pass
    setdesc = wrap(wrap(setdesc, ['text']))


    #set the irc.nick's link association. Generally used to set links to character wiki page or image link
    def setlink(self, irc, msg, args, text):
        pass
    setlink = wrap(setlink, ['text'])

    #!describe <character> -- returns results by querying mysqldb
    # for irc.nick and it's associated description set by !setdesc
    # it should also return it's associated URL (still text area) if one exists
    # this will also verify if a character is registered and inform the character if they need to contact an ST
    # for assistance in registering their nick
    def describe(self, irc, msg, args, text):
        pass
    describe = wrap(describe, ['text'])

Class = Describe
