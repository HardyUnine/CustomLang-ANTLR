# Generated from RPG_Games.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RPG_GamesParser import RPG_GamesParser
else:
    from RPG_GamesParser import RPG_GamesParser

# This class defines a complete generic visitor for a parse tree produced by RPG_GamesParser.

class RPG_GamesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RPG_GamesParser#program.
    def visitProgram(self, ctx:RPG_GamesParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPG_GamesParser#statement.
    def visitStatement(self, ctx:RPG_GamesParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPG_GamesParser#playerDecl.
    def visitPlayerDecl(self, ctx:RPG_GamesParser.PlayerDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPG_GamesParser#statsUpdate.
    def visitStatsUpdate(self, ctx:RPG_GamesParser.StatsUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPG_GamesParser#addInventory.
    def visitAddInventory(self, ctx:RPG_GamesParser.AddInventoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPG_GamesParser#removeInventory.
    def visitRemoveInventory(self, ctx:RPG_GamesParser.RemoveInventoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPG_GamesParser#item.
    def visitItem(self, ctx:RPG_GamesParser.ItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPG_GamesParser#inInventory.
    def visitInInventory(self, ctx:RPG_GamesParser.InInventoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPG_GamesParser#listplayer.
    def visitListplayer(self, ctx:RPG_GamesParser.ListplayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPG_GamesParser#summary.
    def visitSummary(self, ctx:RPG_GamesParser.SummaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPG_GamesParser#poof.
    def visitPoof(self, ctx:RPG_GamesParser.PoofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPG_GamesParser#RollWithName.
    def visitRollWithName(self, ctx:RPG_GamesParser.RollWithNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPG_GamesParser#RollWithoutName.
    def visitRollWithoutName(self, ctx:RPG_GamesParser.RollWithoutNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPG_GamesParser#stat.
    def visitStat(self, ctx:RPG_GamesParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPG_GamesParser#race.
    def visitRace(self, ctx:RPG_GamesParser.RaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPG_GamesParser#classes.
    def visitClasses(self, ctx:RPG_GamesParser.ClassesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPG_GamesParser#save.
    def visitSave(self, ctx:RPG_GamesParser.SaveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPG_GamesParser#load.
    def visitLoad(self, ctx:RPG_GamesParser.LoadContext):
        return self.visitChildren(ctx)



del RPG_GamesParser