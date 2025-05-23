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
        4,1,21,113,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,5,0,32,8,0,10,0,12,0,35,9,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,3,1,46,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,
        1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,
        11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,14,0,0,15,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,0,2,1,0,11,13,1,0,14,17,104,0,33,1,0,0,0,
        2,45,1,0,0,0,4,47,1,0,0,0,6,62,1,0,0,0,8,71,1,0,0,0,10,78,1,0,0,
        0,12,85,1,0,0,0,14,90,1,0,0,0,16,95,1,0,0,0,18,100,1,0,0,0,20,102,
        1,0,0,0,22,104,1,0,0,0,24,106,1,0,0,0,26,108,1,0,0,0,28,110,1,0,
        0,0,30,32,3,2,1,0,31,30,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,
        1,0,0,0,34,36,1,0,0,0,35,33,1,0,0,0,36,37,5,0,0,1,37,1,1,0,0,0,38,
        46,3,4,2,0,39,46,3,6,3,0,40,46,3,8,4,0,41,46,3,10,5,0,42,46,3,12,
        6,0,43,46,3,14,7,0,44,46,3,16,8,0,45,38,1,0,0,0,45,39,1,0,0,0,45,
        40,1,0,0,0,45,41,1,0,0,0,45,42,1,0,0,0,45,43,1,0,0,0,45,44,1,0,0,
        0,46,3,1,0,0,0,47,48,5,4,0,0,48,49,5,1,0,0,49,50,5,19,0,0,50,51,
        5,2,0,0,51,52,3,28,14,0,52,53,5,2,0,0,53,54,3,22,11,0,54,55,5,2,
        0,0,55,56,3,26,13,0,56,57,5,2,0,0,57,58,3,24,12,0,58,59,5,2,0,0,
        59,60,3,18,9,0,60,61,5,3,0,0,61,5,1,0,0,0,62,63,5,7,0,0,63,64,5,
        1,0,0,64,65,5,19,0,0,65,66,5,2,0,0,66,67,3,20,10,0,67,68,5,2,0,0,
        68,69,5,18,0,0,69,70,5,3,0,0,70,7,1,0,0,0,71,72,5,6,0,0,72,73,5,
        1,0,0,73,74,5,19,0,0,74,75,5,2,0,0,75,76,5,20,0,0,76,77,5,3,0,0,
        77,9,1,0,0,0,78,79,5,5,0,0,79,80,5,1,0,0,80,81,5,19,0,0,81,82,5,
        2,0,0,82,83,5,20,0,0,83,84,5,3,0,0,84,11,1,0,0,0,85,86,5,8,0,0,86,
        87,5,1,0,0,87,88,5,19,0,0,88,89,5,3,0,0,89,13,1,0,0,0,90,91,5,9,
        0,0,91,92,5,1,0,0,92,93,5,19,0,0,93,94,5,3,0,0,94,15,1,0,0,0,95,
        96,5,5,0,0,96,97,5,1,0,0,97,98,5,19,0,0,98,99,5,3,0,0,99,17,1,0,
        0,0,100,101,7,0,0,0,101,19,1,0,0,0,102,103,7,1,0,0,103,21,1,0,0,
        0,104,105,5,18,0,0,105,23,1,0,0,0,106,107,5,18,0,0,107,25,1,0,0,
        0,108,109,5,18,0,0,109,27,1,0,0,0,110,111,5,18,0,0,111,29,1,0,0,
        0,2,33,45
    ]

class RPG_GamesParser ( Parser ):

    grammarFileName = "RPG_Games.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'SUMMON'", "'POOF'", 
                     "'AQUIRE'", "'ALTERATE'", "'WhatsInMyBag'", "'SUMMAWY'", 
                     "'roll'", "'sword'", "'bow'", "'staff'", "'strength'", 
                     "'agility'", "'intelligence'", "'hp'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "CREATE", "DEL", "GET", "UPDATE", "PRINTINV", "PRINTCAR", 
                      "ROLL", "SWORD", "BOW", "STAFF", "STRENGTH", "AGILITY", 
                      "INTELLIGENCE", "HP", "NUMBER", "NAME", "ITEM", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_playerDecl = 2
    RULE_statsUpdate = 3
    RULE_addInventory = 4
    RULE_removeInventory = 5
    RULE_inInventory = 6
    RULE_summary = 7
    RULE_poof = 8
    RULE_weapon = 9
    RULE_stat = 10
    RULE_strength = 11
    RULE_agility = 12
    RULE_intelligence = 13
    RULE_hp = 14

    ruleNames =  [ "program", "statement", "playerDecl", "statsUpdate", 
                   "addInventory", "removeInventory", "inInventory", "summary", 
                   "poof", "weapon", "stat", "strength", "agility", "intelligence", 
                   "hp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    CREATE=4
    DEL=5
    GET=6
    UPDATE=7
    PRINTINV=8
    PRINTCAR=9
    ROLL=10
    SWORD=11
    BOW=12
    STAFF=13
    STRENGTH=14
    AGILITY=15
    INTELLIGENCE=16
    HP=17
    NUMBER=18
    NAME=19
    ITEM=20
    WS=21

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
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1008) != 0):
                self.state = 30
                self.statement()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 36
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
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.playerDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.statsUpdate()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.addInventory()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 41
                self.removeInventory()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 42
                self.inInventory()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 43
                self.summary()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 44
                self.poof()
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

        def hp(self):
            return self.getTypedRuleContext(RPG_GamesParser.HpContext,0)


        def strength(self):
            return self.getTypedRuleContext(RPG_GamesParser.StrengthContext,0)


        def intelligence(self):
            return self.getTypedRuleContext(RPG_GamesParser.IntelligenceContext,0)


        def agility(self):
            return self.getTypedRuleContext(RPG_GamesParser.AgilityContext,0)


        def weapon(self):
            return self.getTypedRuleContext(RPG_GamesParser.WeaponContext,0)


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
            self.state = 47
            self.match(RPG_GamesParser.CREATE)
            self.state = 48
            self.match(RPG_GamesParser.T__0)
            self.state = 49
            self.match(RPG_GamesParser.NAME)
            self.state = 50
            self.match(RPG_GamesParser.T__1)
            self.state = 51
            self.hp()
            self.state = 52
            self.match(RPG_GamesParser.T__1)
            self.state = 53
            self.strength()
            self.state = 54
            self.match(RPG_GamesParser.T__1)
            self.state = 55
            self.intelligence()
            self.state = 56
            self.match(RPG_GamesParser.T__1)
            self.state = 57
            self.agility()
            self.state = 58
            self.match(RPG_GamesParser.T__1)
            self.state = 59
            self.weapon()
            self.state = 60
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
            self.state = 62
            self.match(RPG_GamesParser.UPDATE)
            self.state = 63
            self.match(RPG_GamesParser.T__0)
            self.state = 64
            self.match(RPG_GamesParser.NAME)
            self.state = 65
            self.match(RPG_GamesParser.T__1)
            self.state = 66
            self.stat()
            self.state = 67
            self.match(RPG_GamesParser.T__1)
            self.state = 68
            self.match(RPG_GamesParser.NUMBER)
            self.state = 69
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

        def ITEM(self):
            return self.getToken(RPG_GamesParser.ITEM, 0)

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
            self.state = 71
            self.match(RPG_GamesParser.GET)
            self.state = 72
            self.match(RPG_GamesParser.T__0)
            self.state = 73
            self.match(RPG_GamesParser.NAME)
            self.state = 74
            self.match(RPG_GamesParser.T__1)
            self.state = 75
            self.match(RPG_GamesParser.ITEM)
            self.state = 76
            self.match(RPG_GamesParser.T__2)
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
        self.enterRule(localctx, 10, self.RULE_removeInventory)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(RPG_GamesParser.DEL)
            self.state = 79
            self.match(RPG_GamesParser.T__0)
            self.state = 80
            self.match(RPG_GamesParser.NAME)
            self.state = 81
            self.match(RPG_GamesParser.T__1)
            self.state = 82
            self.match(RPG_GamesParser.ITEM)
            self.state = 83
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
        self.enterRule(localctx, 12, self.RULE_inInventory)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(RPG_GamesParser.PRINTINV)
            self.state = 86
            self.match(RPG_GamesParser.T__0)
            self.state = 87
            self.match(RPG_GamesParser.NAME)
            self.state = 88
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
        self.enterRule(localctx, 14, self.RULE_summary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(RPG_GamesParser.PRINTCAR)
            self.state = 91
            self.match(RPG_GamesParser.T__0)
            self.state = 92
            self.match(RPG_GamesParser.NAME)
            self.state = 93
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
        self.enterRule(localctx, 16, self.RULE_poof)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(RPG_GamesParser.DEL)
            self.state = 96
            self.match(RPG_GamesParser.T__0)
            self.state = 97
            self.match(RPG_GamesParser.NAME)
            self.state = 98
            self.match(RPG_GamesParser.T__2)
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
        self.enterRule(localctx, 18, self.RULE_weapon)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
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
        self.enterRule(localctx, 20, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0)):
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


    class StrengthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(RPG_GamesParser.NUMBER, 0)

        def getRuleIndex(self):
            return RPG_GamesParser.RULE_strength

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrength" ):
                listener.enterStrength(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrength" ):
                listener.exitStrength(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrength" ):
                return visitor.visitStrength(self)
            else:
                return visitor.visitChildren(self)




    def strength(self):

        localctx = RPG_GamesParser.StrengthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_strength)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(RPG_GamesParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgilityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(RPG_GamesParser.NUMBER, 0)

        def getRuleIndex(self):
            return RPG_GamesParser.RULE_agility

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgility" ):
                listener.enterAgility(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgility" ):
                listener.exitAgility(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgility" ):
                return visitor.visitAgility(self)
            else:
                return visitor.visitChildren(self)




    def agility(self):

        localctx = RPG_GamesParser.AgilityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_agility)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(RPG_GamesParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntelligenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(RPG_GamesParser.NUMBER, 0)

        def getRuleIndex(self):
            return RPG_GamesParser.RULE_intelligence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntelligence" ):
                listener.enterIntelligence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntelligence" ):
                listener.exitIntelligence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntelligence" ):
                return visitor.visitIntelligence(self)
            else:
                return visitor.visitChildren(self)




    def intelligence(self):

        localctx = RPG_GamesParser.IntelligenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_intelligence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(RPG_GamesParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(RPG_GamesParser.NUMBER, 0)

        def getRuleIndex(self):
            return RPG_GamesParser.RULE_hp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHp" ):
                listener.enterHp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHp" ):
                listener.exitHp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHp" ):
                return visitor.visitHp(self)
            else:
                return visitor.visitChildren(self)




    def hp(self):

        localctx = RPG_GamesParser.HpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_hp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(RPG_GamesParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





