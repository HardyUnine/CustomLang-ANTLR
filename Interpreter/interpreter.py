import sys
import os
import random
from antlr4 import *
from g4.RPG_GamesLexer import RPG_GamesLexer
from g4.RPG_GamesParser import RPG_GamesParser
from g4.RPG_GamesVisitor import RPG_GamesVisitor

class RPGInterpreter(RPG_GamesVisitor):
    def __init__(self):
        self.player = {
            'Igor' : {'hp': 0,
                      'strength': 2,
                      'intelligence': 3,
                      'agility': 5,
                      'weapon': "bow",
                      'inventory': {}
                      }
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
        weapon = ctx.weapon().getText()

        self.player[name] = {'hp': hp,
                             'strength': strength,
                             'intelligence': intel,
                             'agility': agi,
                             'weapon': weapon,
                             'inventory': {}
                             }
        
        return self.player
    
    def visitWeapon(self, ctx: RPG_GamesParser.WeaponContext):
        return ctx.getChild(0).getText()

    def visitStatsUpdate(self, ctx: RPG_GamesParser.StatsUpdateContext):
        name = ctx.NAME().getText()
        # if name not in self.player.keys():
        #     raise NameError(f"{name} is not a listed player")
        stat = ctx.stat().getText()
        value = int(ctx.NUMBER().getText())
        self.player[name][stat] = value
        return self.player
    
    def visitAddInventory(self, ctx: RPG_GamesParser.AddInventoryContext):
        name = ctx.NAME().getText()
        if name not in self.player.keys():
            raise ValueError(f"{name} is not a listed player")
        item = ctx.ITEM().getText()
        if item in self.player[name]['inventory']:
            self.player[name]['inventory'][item]+= 1
        self.player[name]['inventory'][item] = 1
        return self.player
    
    def visitRemoveInventory(self, ctx: RPG_GamesParser.RemoveInventoryContext):
        name = ctx.NAME().getText()
        if name not in self.player.keys():
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
        if name not in self.player.keys():
            raise ValueError(f"{name} is not a listed player")
        inv = ""
        for key, val in self.player[name]['inventory'].items():
            inv+= f'{key}: {val}\n'
        # print(f"{name} has:\n{inv if inv != "" else "Nothing!"}")
        return f"{name} has:\n{inv if inv != "" else "Nothing!"}"
        
    
    def visitSummary(self, ctx: RPG_GamesParser.SummaryContext):
        name = ctx.NAME().getText()
        for keys, val in self.player.items():
            print(keys, val)
        # if name not in self.player.keys():
        #     raise ValueError(f"{name} is not a listed player")
        inv = ""
        for key, val in self.player[name].items():
            if key == 'inventory':
                continue
            inv+= f'{key}: {val}\n'
        # print(f"{name} stats:\n{inv}")
        return f"{name} stats:\n{inv}"
        

    def visitPoof(self, ctx: RPG_GamesParser.PoofContext):
        name = ctx.NAME().getText()
        if name not in self.player.keys():
            raise ValueError(f"{name} is not poofable")
        self.player.pop(name)
        return self.player
    
    
    def visitRollWithName(self, ctx: RPG_GamesParser.RollWithNameContext):
        name = ctx.NAME().getText()
        if name not in self.player:
            raise ValueError(f"{name} is not a listed player")
        dice_sides = int(ctx.NUMBER().getText())
        roll = random.randint(1, dice_sides)
        if roll == 1:
            return f"{name} rolled a {roll} and got a critical fail!"
        elif roll == dice_sides:
            return f"{name} rolled a {roll} and got a critical success!"
        else:
            return f"{name} rolled a {roll}"
    

    def visitRollWithoutName(self, ctx: RPG_GamesParser.RollWithoutNameContext):
        dice_sides = int(ctx.NUMBER().getText())
        roll = random.randint(1, dice_sides)
        return f"You rolled a d{dice_sides} and got {roll}"


# Main entry point of the program
if __name__ == "__main__":
    # Infinite loop to continuously accept user input
    calc = RPGInterpreter()
    while True:
        try:
            # Prompt the user for input
            text = input("> ")
            # Initialize the lexer with the input text
            lexer = RPG_GamesLexer(InputStream(text))
            # Create a token stream from the lexer
            stream = CommonTokenStream(lexer)
            # Initialize the parser with the token stream
            parser = RPG_GamesParser(stream)
            # Parse the expression to generate the parse tree
            tree = parser.statement()
            # Visit the parse tree and print the evaluation result
            print(calc.visit(tree))
        # Handle end of file (EOF) or keyboard interrupt (Ctrl + C) to exit the loop
        except (EOFError, KeyboardInterrupt):
            break
