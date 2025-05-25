# Generated from RPG_Games.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,30,134,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,5,0,36,8,0,10,0,12,0,39,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,53,8,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,114,8,10,1,11,
        1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,16,
        1,16,1,16,1,16,1,16,1,16,0,0,17,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,0,5,1,0,26,27,1,0,13,15,1,0,16,19,1,0,20,22,1,0,23,25,
        127,0,37,1,0,0,0,2,52,1,0,0,0,4,54,1,0,0,0,6,63,1,0,0,0,8,72,1,0,
        0,0,10,79,1,0,0,0,12,81,1,0,0,0,14,88,1,0,0,0,16,93,1,0,0,0,18,98,
        1,0,0,0,20,113,1,0,0,0,22,115,1,0,0,0,24,117,1,0,0,0,26,119,1,0,
        0,0,28,121,1,0,0,0,30,123,1,0,0,0,32,128,1,0,0,0,34,36,3,2,1,0,35,
        34,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,
        0,39,37,1,0,0,0,40,41,5,0,0,1,41,1,1,0,0,0,42,53,3,4,2,0,43,53,3,
        6,3,0,44,53,3,8,4,0,45,53,3,12,6,0,46,53,3,14,7,0,47,53,3,16,8,0,
        48,53,3,18,9,0,49,53,3,20,10,0,50,53,3,30,15,0,51,53,3,32,16,0,52,
        42,1,0,0,0,52,43,1,0,0,0,52,44,1,0,0,0,52,45,1,0,0,0,52,46,1,0,0,
        0,52,47,1,0,0,0,52,48,1,0,0,0,52,49,1,0,0,0,52,50,1,0,0,0,52,51,
        1,0,0,0,53,3,1,0,0,0,54,55,5,6,0,0,55,56,5,1,0,0,56,57,5,26,0,0,
        57,58,5,2,0,0,58,59,3,26,13,0,59,60,5,2,0,0,60,61,3,28,14,0,61,62,
        5,3,0,0,62,5,1,0,0,0,63,64,5,9,0,0,64,65,5,1,0,0,65,66,5,26,0,0,
        66,67,5,2,0,0,67,68,3,24,12,0,68,69,5,2,0,0,69,70,5,28,0,0,70,71,
        5,3,0,0,71,7,1,0,0,0,72,73,5,8,0,0,73,74,5,1,0,0,74,75,5,26,0,0,
        75,76,5,2,0,0,76,77,3,10,5,0,77,78,5,3,0,0,78,9,1,0,0,0,79,80,7,
        0,0,0,80,11,1,0,0,0,81,82,5,7,0,0,82,83,5,1,0,0,83,84,5,26,0,0,84,
        85,5,2,0,0,85,86,5,27,0,0,86,87,5,3,0,0,87,13,1,0,0,0,88,89,5,10,
        0,0,89,90,5,1,0,0,90,91,5,26,0,0,91,92,5,3,0,0,92,15,1,0,0,0,93,
        94,5,11,0,0,94,95,5,1,0,0,95,96,5,26,0,0,96,97,5,3,0,0,97,17,1,0,
        0,0,98,99,5,7,0,0,99,100,5,1,0,0,100,101,5,26,0,0,101,102,5,3,0,
        0,102,19,1,0,0,0,103,104,5,12,0,0,104,105,5,1,0,0,105,106,5,26,0,
        0,106,107,5,2,0,0,107,108,5,28,0,0,108,114,5,3,0,0,109,110,5,12,
        0,0,110,111,5,1,0,0,111,112,5,28,0,0,112,114,5,3,0,0,113,103,1,0,
        0,0,113,109,1,0,0,0,114,21,1,0,0,0,115,116,7,1,0,0,116,23,1,0,0,
        0,117,118,7,2,0,0,118,25,1,0,0,0,119,120,7,3,0,0,120,27,1,0,0,0,
        121,122,7,4,0,0,122,29,1,0,0,0,123,124,5,4,0,0,124,125,5,1,0,0,125,
        126,5,29,0,0,126,127,5,3,0,0,127,31,1,0,0,0,128,129,5,5,0,0,129,
        130,5,1,0,0,130,131,5,29,0,0,131,132,5,3,0,0,132,33,1,0,0,0,3,37,
        52,113
    ]

class RPG_GamesParser ( Parser ):

    grammarFileName = "RPG_Games.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'SAVE'", "'LOAD'", 
                     "'SUMMON'", "'POOF'", "'AQUIRE'", "'ALTERATE'", "'WhatsInMyBag'", 
                     "'SUMMAWY'", "'ROLL'", "'sword'", "'bow'", "'staff'", 
                     "'strength'", "'agility'", "'intelligence'", "'hp'", 
                     "'Dwarf'", "'Human'", "'Elf'", "'Paladin'", "'Wizard'", 
                     "'Ranger'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "CREATE", "DEL", "GET", 
                      "UPDATE", "PRINTINV", "PRINTCAR", "DICEROLL", "SWORD", 
                      "BOW", "STAFF", "STRENGTH", "AGILITY", "INTELLIGENCE", 
                      "HP", "DWARF", "HUMAN", "ELF", "PALADIN", "WIZARD", 
                      "RANGER", "NAME", "ITEM", "NUMBER", "STRING", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_playerDecl = 2
    RULE_statsUpdate = 3
    RULE_addInventory = 4
    RULE_item = 5
    RULE_removeInventory = 6
    RULE_inInventory = 7
    RULE_summary = 8
    RULE_poof = 9
    RULE_diceRoll = 10
    RULE_weapon = 11
    RULE_stat = 12
    RULE_race = 13
    RULE_classes = 14
    RULE_save = 15
    RULE_load = 16

    ruleNames =  [ "program", "statement", "playerDecl", "statsUpdate", 
                   "addInventory", "item", "removeInventory", "inInventory", 
                   "summary", "poof", "diceRoll", "weapon", "stat", "race", 
                   "classes", "save", "load" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    CREATE=6
    DEL=7
    GET=8
    UPDATE=9
    PRINTINV=10
    PRINTCAR=11
    DICEROLL=12
    SWORD=13
    BOW=14
    STAFF=15
    STRENGTH=16
    AGILITY=17
    INTELLIGENCE=18
    HP=19
    DWARF=20
    HUMAN=21
    ELF=22
    PALADIN=23
    WIZARD=24
    RANGER=25
    NAME=26
    ITEM=27
    NUMBER=28
    STRING=29
    WS=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(RPG_GamesParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RPG_GamesParser.StatementContext)
            else:
                return self.getTypedRuleContext(RPG_GamesParser.StatementContext,i)


        def getRuleIndex(self):
            return RPG_GamesParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = RPG_GamesParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8176) != 0):
                self.state = 34
                self.statement()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(RPG_GamesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def playerDecl(self):
            return self.getTypedRuleContext(RPG_GamesParser.PlayerDeclContext,0)


        def statsUpdate(self):
            return self.getTypedRuleContext(RPG_GamesParser.StatsUpdateContext,0)


        def addInventory(self):
            return self.getTypedRuleContext(RPG_GamesParser.AddInventoryContext,0)


        def removeInventory(self):
            return self.getTypedRuleContext(RPG_GamesParser.RemoveInventoryContext,0)


        def inInventory(self):
            return self.getTypedRuleContext(RPG_GamesParser.InInventoryContext,0)


        def summary(self):
            return self.getTypedRuleContext(RPG_GamesParser.SummaryContext,0)


        def poof(self):
            return self.getTypedRuleContext(RPG_GamesParser.PoofContext,0)


        def diceRoll(self):
            return self.getTypedRuleContext(RPG_GamesParser.DiceRollContext,0)


        def save(self):
            return self.getTypedRuleContext(RPG_GamesParser.SaveContext,0)


        def load(self):
            return self.getTypedRuleContext(RPG_GamesParser.LoadContext,0)


        def getRuleIndex(self):
            return RPG_GamesParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = RPG_GamesParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.playerDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.statsUpdate()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.addInventory()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.removeInventory()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 46
                self.inInventory()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 47
                self.summary()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 48
                self.poof()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 49
                self.diceRoll()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 50
                self.save()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 51
                self.load()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlayerDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREATE(self):
            return self.getToken(RPG_GamesParser.CREATE, 0)

        def NAME(self):
            return self.getToken(RPG_GamesParser.NAME, 0)

        def race(self):
            return self.getTypedRuleContext(RPG_GamesParser.RaceContext,0)


        def classes(self):
            return self.getTypedRuleContext(RPG_GamesParser.ClassesContext,0)


        def getRuleIndex(self):
            return RPG_GamesParser.RULE_playerDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlayerDecl" ):
                listener.enterPlayerDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlayerDecl" ):
                listener.exitPlayerDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlayerDecl" ):
                return visitor.visitPlayerDecl(self)
            else:
                return visitor.visitChildren(self)




    def playerDecl(self):

        localctx = RPG_GamesParser.PlayerDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_playerDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(RPG_GamesParser.CREATE)
            self.state = 55
            self.match(RPG_GamesParser.T__0)
            self.state = 56
            self.match(RPG_GamesParser.NAME)
            self.state = 57
            self.match(RPG_GamesParser.T__1)
            self.state = 58
            self.race()
            self.state = 59
            self.match(RPG_GamesParser.T__1)
            self.state = 60
            self.classes()
            self.state = 61
            self.match(RPG_GamesParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatsUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPDATE(self):
            return self.getToken(RPG_GamesParser.UPDATE, 0)

        def NAME(self):
            return self.getToken(RPG_GamesParser.NAME, 0)

        def stat(self):
            return self.getTypedRuleContext(RPG_GamesParser.StatContext,0)


        def NUMBER(self):
            return self.getToken(RPG_GamesParser.NUMBER, 0)

        def getRuleIndex(self):
            return RPG_GamesParser.RULE_statsUpdate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatsUpdate" ):
                listener.enterStatsUpdate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatsUpdate" ):
                listener.exitStatsUpdate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatsUpdate" ):
                return visitor.visitStatsUpdate(self)
            else:
                return visitor.visitChildren(self)




    def statsUpdate(self):

        localctx = RPG_GamesParser.StatsUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statsUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(RPG_GamesParser.UPDATE)
            self.state = 64
            self.match(RPG_GamesParser.T__0)
            self.state = 65
            self.match(RPG_GamesParser.NAME)
            self.state = 66
            self.match(RPG_GamesParser.T__1)
            self.state = 67
            self.stat()
            self.state = 68
            self.match(RPG_GamesParser.T__1)
            self.state = 69
            self.match(RPG_GamesParser.NUMBER)
            self.state = 70
            self.match(RPG_GamesParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddInventoryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GET(self):
            return self.getToken(RPG_GamesParser.GET, 0)

        def NAME(self):
            return self.getToken(RPG_GamesParser.NAME, 0)

        def item(self):
            return self.getTypedRuleContext(RPG_GamesParser.ItemContext,0)


        def getRuleIndex(self):
            return RPG_GamesParser.RULE_addInventory

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddInventory" ):
                listener.enterAddInventory(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddInventory" ):
                listener.exitAddInventory(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddInventory" ):
                return visitor.visitAddInventory(self)
            else:
                return visitor.visitChildren(self)




    def addInventory(self):

        localctx = RPG_GamesParser.AddInventoryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_addInventory)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(RPG_GamesParser.GET)
            self.state = 73
            self.match(RPG_GamesParser.T__0)
            self.state = 74
            self.match(RPG_GamesParser.NAME)
            self.state = 75
            self.match(RPG_GamesParser.T__1)
            self.state = 76
            self.item()
            self.state = 77
            self.match(RPG_GamesParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(RPG_GamesParser.NAME, 0)

        def ITEM(self):
            return self.getToken(RPG_GamesParser.ITEM, 0)

        def getRuleIndex(self):
            return RPG_GamesParser.RULE_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem" ):
                listener.enterItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem" ):
                listener.exitItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = RPG_GamesParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RemoveInventoryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEL(self):
            return self.getToken(RPG_GamesParser.DEL, 0)

        def NAME(self):
            return self.getToken(RPG_GamesParser.NAME, 0)

        def ITEM(self):
            return self.getToken(RPG_GamesParser.ITEM, 0)

        def getRuleIndex(self):
            return RPG_GamesParser.RULE_removeInventory

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRemoveInventory" ):
                listener.enterRemoveInventory(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRemoveInventory" ):
                listener.exitRemoveInventory(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRemoveInventory" ):
                return visitor.visitRemoveInventory(self)
            else:
                return visitor.visitChildren(self)




    def removeInventory(self):

        localctx = RPG_GamesParser.RemoveInventoryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_removeInventory)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(RPG_GamesParser.DEL)
            self.state = 82
            self.match(RPG_GamesParser.T__0)
            self.state = 83
            self.match(RPG_GamesParser.NAME)
            self.state = 84
            self.match(RPG_GamesParser.T__1)
            self.state = 85
            self.match(RPG_GamesParser.ITEM)
            self.state = 86
            self.match(RPG_GamesParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InInventoryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINTINV(self):
            return self.getToken(RPG_GamesParser.PRINTINV, 0)

        def NAME(self):
            return self.getToken(RPG_GamesParser.NAME, 0)

        def getRuleIndex(self):
            return RPG_GamesParser.RULE_inInventory

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInInventory" ):
                listener.enterInInventory(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInInventory" ):
                listener.exitInInventory(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInInventory" ):
                return visitor.visitInInventory(self)
            else:
                return visitor.visitChildren(self)




    def inInventory(self):

        localctx = RPG_GamesParser.InInventoryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_inInventory)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(RPG_GamesParser.PRINTINV)
            self.state = 89
            self.match(RPG_GamesParser.T__0)
            self.state = 90
            self.match(RPG_GamesParser.NAME)
            self.state = 91
            self.match(RPG_GamesParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SummaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINTCAR(self):
            return self.getToken(RPG_GamesParser.PRINTCAR, 0)

        def NAME(self):
            return self.getToken(RPG_GamesParser.NAME, 0)

        def getRuleIndex(self):
            return RPG_GamesParser.RULE_summary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSummary" ):
                listener.enterSummary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSummary" ):
                listener.exitSummary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSummary" ):
                return visitor.visitSummary(self)
            else:
                return visitor.visitChildren(self)




    def summary(self):

        localctx = RPG_GamesParser.SummaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_summary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(RPG_GamesParser.PRINTCAR)
            self.state = 94
            self.match(RPG_GamesParser.T__0)
            self.state = 95
            self.match(RPG_GamesParser.NAME)
            self.state = 96
            self.match(RPG_GamesParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PoofContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEL(self):
            return self.getToken(RPG_GamesParser.DEL, 0)

        def NAME(self):
            return self.getToken(RPG_GamesParser.NAME, 0)

        def getRuleIndex(self):
            return RPG_GamesParser.RULE_poof

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPoof" ):
                listener.enterPoof(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPoof" ):
                listener.exitPoof(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPoof" ):
                return visitor.visitPoof(self)
            else:
                return visitor.visitChildren(self)




    def poof(self):

        localctx = RPG_GamesParser.PoofContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_poof)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(RPG_GamesParser.DEL)
            self.state = 99
            self.match(RPG_GamesParser.T__0)
            self.state = 100
            self.match(RPG_GamesParser.NAME)
            self.state = 101
            self.match(RPG_GamesParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DiceRollContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RPG_GamesParser.RULE_diceRoll

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RollWithoutNameContext(DiceRollContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RPG_GamesParser.DiceRollContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DICEROLL(self):
            return self.getToken(RPG_GamesParser.DICEROLL, 0)
        def NUMBER(self):
            return self.getToken(RPG_GamesParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRollWithoutName" ):
                listener.enterRollWithoutName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRollWithoutName" ):
                listener.exitRollWithoutName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRollWithoutName" ):
                return visitor.visitRollWithoutName(self)
            else:
                return visitor.visitChildren(self)


    class RollWithNameContext(DiceRollContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RPG_GamesParser.DiceRollContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DICEROLL(self):
            return self.getToken(RPG_GamesParser.DICEROLL, 0)
        def NAME(self):
            return self.getToken(RPG_GamesParser.NAME, 0)
        def NUMBER(self):
            return self.getToken(RPG_GamesParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRollWithName" ):
                listener.enterRollWithName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRollWithName" ):
                listener.exitRollWithName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRollWithName" ):
                return visitor.visitRollWithName(self)
            else:
                return visitor.visitChildren(self)



    def diceRoll(self):

        localctx = RPG_GamesParser.DiceRollContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_diceRoll)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = RPG_GamesParser.RollWithNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.match(RPG_GamesParser.DICEROLL)
                self.state = 104
                self.match(RPG_GamesParser.T__0)
                self.state = 105
                self.match(RPG_GamesParser.NAME)
                self.state = 106
                self.match(RPG_GamesParser.T__1)
                self.state = 107
                self.match(RPG_GamesParser.NUMBER)
                self.state = 108
                self.match(RPG_GamesParser.T__2)
                pass

            elif la_ == 2:
                localctx = RPG_GamesParser.RollWithoutNameContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.match(RPG_GamesParser.DICEROLL)
                self.state = 110
                self.match(RPG_GamesParser.T__0)
                self.state = 111
                self.match(RPG_GamesParser.NUMBER)
                self.state = 112
                self.match(RPG_GamesParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WeaponContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWORD(self):
            return self.getToken(RPG_GamesParser.SWORD, 0)

        def BOW(self):
            return self.getToken(RPG_GamesParser.BOW, 0)

        def STAFF(self):
            return self.getToken(RPG_GamesParser.STAFF, 0)

        def getRuleIndex(self):
            return RPG_GamesParser.RULE_weapon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWeapon" ):
                listener.enterWeapon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWeapon" ):
                listener.exitWeapon(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWeapon" ):
                return visitor.visitWeapon(self)
            else:
                return visitor.visitChildren(self)




    def weapon(self):

        localctx = RPG_GamesParser.WeaponContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_weapon)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRENGTH(self):
            return self.getToken(RPG_GamesParser.STRENGTH, 0)

        def INTELLIGENCE(self):
            return self.getToken(RPG_GamesParser.INTELLIGENCE, 0)

        def AGILITY(self):
            return self.getToken(RPG_GamesParser.AGILITY, 0)

        def HP(self):
            return self.getToken(RPG_GamesParser.HP, 0)

        def getRuleIndex(self):
            return RPG_GamesParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = RPG_GamesParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 983040) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DWARF(self):
            return self.getToken(RPG_GamesParser.DWARF, 0)

        def HUMAN(self):
            return self.getToken(RPG_GamesParser.HUMAN, 0)

        def ELF(self):
            return self.getToken(RPG_GamesParser.ELF, 0)

        def getRuleIndex(self):
            return RPG_GamesParser.RULE_race

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRace" ):
                listener.enterRace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRace" ):
                listener.exitRace(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRace" ):
                return visitor.visitRace(self)
            else:
                return visitor.visitChildren(self)




    def race(self):

        localctx = RPG_GamesParser.RaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_race)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PALADIN(self):
            return self.getToken(RPG_GamesParser.PALADIN, 0)

        def WIZARD(self):
            return self.getToken(RPG_GamesParser.WIZARD, 0)

        def RANGER(self):
            return self.getToken(RPG_GamesParser.RANGER, 0)

        def getRuleIndex(self):
            return RPG_GamesParser.RULE_classes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClasses" ):
                listener.enterClasses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClasses" ):
                listener.exitClasses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClasses" ):
                return visitor.visitClasses(self)
            else:
                return visitor.visitChildren(self)




    def classes(self):

        localctx = RPG_GamesParser.ClassesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_classes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SaveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(RPG_GamesParser.STRING, 0)

        def getRuleIndex(self):
            return RPG_GamesParser.RULE_save

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSave" ):
                listener.enterSave(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSave" ):
                listener.exitSave(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSave" ):
                return visitor.visitSave(self)
            else:
                return visitor.visitChildren(self)




    def save(self):

        localctx = RPG_GamesParser.SaveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_save)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(RPG_GamesParser.T__3)
            self.state = 124
            self.match(RPG_GamesParser.T__0)
            self.state = 125
            self.match(RPG_GamesParser.STRING)
            self.state = 126
            self.match(RPG_GamesParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(RPG_GamesParser.STRING, 0)

        def getRuleIndex(self):
            return RPG_GamesParser.RULE_load

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoad" ):
                listener.enterLoad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoad" ):
                listener.exitLoad(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoad" ):
                return visitor.visitLoad(self)
            else:
                return visitor.visitChildren(self)




    def load(self):

        localctx = RPG_GamesParser.LoadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_load)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(RPG_GamesParser.T__4)
            self.state = 129
            self.match(RPG_GamesParser.T__0)
            self.state = 130
            self.match(RPG_GamesParser.STRING)
            self.state = 131
            self.match(RPG_GamesParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





