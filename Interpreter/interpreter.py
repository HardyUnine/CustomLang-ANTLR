import sys
import os
from antlr4 import *
from g4.RPG_GamesLexer import RPG_GamesLexer
from g4.RPG_GamesParser import RPG_GamesParser
from g4.RPG_GamesVisitor import RPG_GamesVisitor

class RPGInterpreter(RPG_GamesVisitor):
    def __init__(self):
        self.player = {}

    def visitProgram(self, ctx: RPG_GamesParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return self.player
    
    def visitPlayerDecl(self, ctx: RPG_GamesParser.PlayerDeclContext):
        name = ctx.NAME().getText()
        hp = self.visit(ctx.hp())
        strength = self.visit(ctx.strength())
        intel = self.visit(ctx.intelligence())
        agi = self.visit(ctx.agility())
        weapon = ctx.weapon().getText()

        self.player[name] = {'hp': hp,
                             'strength': strength,
                             'intelligence': intel,
                             'agility': agi,
                             'weapon': weapon
                             }
        
        return self.player
    
    def visitHp(self, ctx: RPG_GamesParser.HpContext):
        return int(ctx.NUMBER().getText())
    
    def visitStrength(self, ctx: RPG_GamesParser.StrengthContext):
        return int(ctx.NUMBER().getText())
    
    def visitIntelligence(self, ctx: RPG_GamesParser.IntelligenceContext):
        return int(ctx.NUMBER().getText())

    def visitAgility(self, ctx: RPG_GamesParser.AgilityContext):
        return int(ctx.NUMBER().getText())

    def visitStatsUpdate(self, ctx: RPG_GamesParser.StatsUpdateContext):
        return super().visitStatsUpdate(ctx)
    
    def visitAddInventory(self, ctx: RPG_GamesParser.AddInventoryContext):
        return super().visitAddInventory(ctx)
    
    def visitRemoveInventory(self, ctx: RPG_GamesParser.RemoveInventoryContext):
        return super().visitRemoveInventory(ctx)
    
    def visitInInventory(self, ctx: RPG_GamesParser.InInventoryContext):
        return super().visitInInventory(ctx)
    
    def visitSummary(self, ctx: RPG_GamesParser.SummaryContext):
        return super().visitSummary(ctx)
    
    def visitPoof(self, ctx: RPG_GamesParser.PoofContext):
        return super().visitPoof(ctx)

    