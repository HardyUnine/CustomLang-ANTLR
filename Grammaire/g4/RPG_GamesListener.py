# Generated from RPG_Games.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RPG_GamesParser import RPG_GamesParser
else:
    from RPG_GamesParser import RPG_GamesParser

# This class defines a complete listener for a parse tree produced by RPG_GamesParser.
class RPG_GamesListener(ParseTreeListener):

    # Enter a parse tree produced by RPG_GamesParser#program.
    def enterProgram(self, ctx:RPG_GamesParser.ProgramContext):
        pass

    # Exit a parse tree produced by RPG_GamesParser#program.
    def exitProgram(self, ctx:RPG_GamesParser.ProgramContext):
        pass


    # Enter a parse tree produced by RPG_GamesParser#statement.
    def enterStatement(self, ctx:RPG_GamesParser.StatementContext):
        pass

    # Exit a parse tree produced by RPG_GamesParser#statement.
    def exitStatement(self, ctx:RPG_GamesParser.StatementContext):
        pass


    # Enter a parse tree produced by RPG_GamesParser#playerDecl.
    def enterPlayerDecl(self, ctx:RPG_GamesParser.PlayerDeclContext):
        pass

    # Exit a parse tree produced by RPG_GamesParser#playerDecl.
    def exitPlayerDecl(self, ctx:RPG_GamesParser.PlayerDeclContext):
        pass


    # Enter a parse tree produced by RPG_GamesParser#statsUpdate.
    def enterStatsUpdate(self, ctx:RPG_GamesParser.StatsUpdateContext):
        pass

    # Exit a parse tree produced by RPG_GamesParser#statsUpdate.
    def exitStatsUpdate(self, ctx:RPG_GamesParser.StatsUpdateContext):
        pass


    # Enter a parse tree produced by RPG_GamesParser#addInventory.
    def enterAddInventory(self, ctx:RPG_GamesParser.AddInventoryContext):
        pass

    # Exit a parse tree produced by RPG_GamesParser#addInventory.
    def exitAddInventory(self, ctx:RPG_GamesParser.AddInventoryContext):
        pass


    # Enter a parse tree produced by RPG_GamesParser#removeInventory.
    def enterRemoveInventory(self, ctx:RPG_GamesParser.RemoveInventoryContext):
        pass

    # Exit a parse tree produced by RPG_GamesParser#removeInventory.
    def exitRemoveInventory(self, ctx:RPG_GamesParser.RemoveInventoryContext):
        pass


    # Enter a parse tree produced by RPG_GamesParser#inInventory.
    def enterInInventory(self, ctx:RPG_GamesParser.InInventoryContext):
        pass

    # Exit a parse tree produced by RPG_GamesParser#inInventory.
    def exitInInventory(self, ctx:RPG_GamesParser.InInventoryContext):
        pass


    # Enter a parse tree produced by RPG_GamesParser#summary.
    def enterSummary(self, ctx:RPG_GamesParser.SummaryContext):
        pass

    # Exit a parse tree produced by RPG_GamesParser#summary.
    def exitSummary(self, ctx:RPG_GamesParser.SummaryContext):
        pass


    # Enter a parse tree produced by RPG_GamesParser#poof.
    def enterPoof(self, ctx:RPG_GamesParser.PoofContext):
        pass

    # Exit a parse tree produced by RPG_GamesParser#poof.
    def exitPoof(self, ctx:RPG_GamesParser.PoofContext):
        pass


    # Enter a parse tree produced by RPG_GamesParser#weapon.
    def enterWeapon(self, ctx:RPG_GamesParser.WeaponContext):
        pass

    # Exit a parse tree produced by RPG_GamesParser#weapon.
    def exitWeapon(self, ctx:RPG_GamesParser.WeaponContext):
        pass


    # Enter a parse tree produced by RPG_GamesParser#stat.
    def enterStat(self, ctx:RPG_GamesParser.StatContext):
        pass

    # Exit a parse tree produced by RPG_GamesParser#stat.
    def exitStat(self, ctx:RPG_GamesParser.StatContext):
        pass


    # Enter a parse tree produced by RPG_GamesParser#strength.
    def enterStrength(self, ctx:RPG_GamesParser.StrengthContext):
        pass

    # Exit a parse tree produced by RPG_GamesParser#strength.
    def exitStrength(self, ctx:RPG_GamesParser.StrengthContext):
        pass


    # Enter a parse tree produced by RPG_GamesParser#agility.
    def enterAgility(self, ctx:RPG_GamesParser.AgilityContext):
        pass

    # Exit a parse tree produced by RPG_GamesParser#agility.
    def exitAgility(self, ctx:RPG_GamesParser.AgilityContext):
        pass


    # Enter a parse tree produced by RPG_GamesParser#intelligence.
    def enterIntelligence(self, ctx:RPG_GamesParser.IntelligenceContext):
        pass

    # Exit a parse tree produced by RPG_GamesParser#intelligence.
    def exitIntelligence(self, ctx:RPG_GamesParser.IntelligenceContext):
        pass


    # Enter a parse tree produced by RPG_GamesParser#hp.
    def enterHp(self, ctx:RPG_GamesParser.HpContext):
        pass

    # Exit a parse tree produced by RPG_GamesParser#hp.
    def exitHp(self, ctx:RPG_GamesParser.HpContext):
        pass



del RPG_GamesParser