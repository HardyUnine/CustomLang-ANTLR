import sys
import os
from antlr4 import *
from g4.RPG_GamesLexer import RPG_GamesLexer
from g4.RPG_GamesParser import RPG_GamesParser
from g4.RPG_GamesVisitor import RPG_GamesVisitor

class RPGInterpreter(RPG_GamesVisitor):
    def __init__(self):
        self.player = {
            'Igor' : {'hp': 0,
                      'strength': 2}
        }

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
        weapon = self.visit(ctx.weapon())

        self.player[name] = {'hp': hp,
                             'strength': strength,
                             'intelligence': intel,
                             'agility': agi,
                             'weapon': weapon,
                             'inventory': {}
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
    
    def visitWeapon(self, ctx: RPG_GamesParser.WeaponContext):
        return ctx.getChild(0).getText()

    def visitStatsUpdate(self, ctx: RPG_GamesParser.StatsUpdateContext):
        name = ctx.NAME().getText()
        if name not in self.player:
            raise NameError(f"{name} is not a listed player")
        stat = ctx.stat().getText()
        value = int(ctx.NUMBER.getText())
        self.player[name][stat] = value
        return self.player
    
    def visitAddInventory(self, ctx: RPG_GamesParser.AddInventoryContext):
        name = ctx.NAME().getText()
        if name not in self.player:
            raise NameError(f"{name} is not a listed player")
        item = ctx.ITEM().getText()
        if item in self.player[name]['inventory']:
            self.player[name]['inventory'][item]+= 1
        self.player[name]['inventory'][item] = 1
        return self.player
    
    def visitRemoveInventory(self, ctx: RPG_GamesParser.RemoveInventoryContext):
        name = ctx.NAME().getText()
        if name not in self.player:
            raise ValueError(f"{name} is not a listed player")
        item = ctx.ITEM().getText()
        if item not in self.player[name]['inventory']:
            raise ValueError(f"{name} never had {item}")
        self.player[name]['inventory'][item]-= 1
        if self.player[name]['inventory'][item] == 0:
            self.player[name]['inventory'].pop(item)
        return self.player
    
    def visitInInventory(self, ctx: RPG_GamesParser.InInventoryContext):
        name = ctx.NAME().getText()
        if name not in self.player:
            raise ValueError(f"{name} is not a listed player")
        inv = ""
        for key, val in self.player[name]['inventory'].items():
            inv+= f'{key}: {val}\n'
        print(f"{name} has:\n{inv if inv != "" else "Nothing!"}")
        # whattoreturn??
        
    
    def visitSummary(self, ctx: RPG_GamesParser.SummaryContext):
        name = ctx.NAME().getText()
        if name not in self.player:
            raise ValueError(f"{name} is not a listed player")
        inv = ""
        for key, val in self.player[name].items():
            if key == 'inventory':
                continue
            inv+= f'{key}: {val}\n'
        print(f"{name} stats:\n{inv}")
        # whattoreturnthesequel
        

    def visitPoof(self, ctx: RPG_GamesParser.PoofContext):
        name = ctx.NAME().getText()
        if name not in self.player:
            raise ValueError(f"{name} is not poofable")
        self.player.pop(name)
        return self.player

    