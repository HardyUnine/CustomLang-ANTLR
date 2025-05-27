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
        race = ctx.race().getText()
        classe = ctx.classes().getText()

        stats = self.calculateStatsFromRaceAndClass(race, classe)

        self.player[name] = {
            'hp': stats['hp'],
            'strength': stats['strength'],
            'intelligence': stats['intelligence'],
            'agility': stats['agility'],
            'weapon': stats['weapon'],
            'inventory': {}
        }

        return self.player

    
    def calculateStatsFromRaceAndClass(self, race, classe):
    # Base stats by race
        race_stats = {
            'Dwarf': {'hp': 10, 'strength': 4, 'intelligence': 2, 'agility': 2},
            'Human': {'hp': 8,  'strength': 3, 'intelligence': 3, 'agility': 3},
            'Elf':   {'hp': 6,  'strength': 2, 'intelligence': 4, 'agility': 4},
        }

        # Class bonuses and default weapons
        class_bonus = {
            'Paladin': {'hp': 4, 'strength': 2, 'intelligence': 0, 'agility': 0, 'weapon': 'sword'},
            'Wizard':  {'hp': 2, 'strength': 0, 'intelligence': 3, 'agility': 0, 'weapon': 'staff'},
            'Ranger':  {'hp': 1, 'strength': 0, 'intelligence': 0, 'agility': 3, 'weapon': 'bow'},
        }

        if race not in race_stats or classe not in class_bonus:
            raise ValueError(f"Invalid race or class: {race}, {classe}")

        base = race_stats[race]
        bonus = class_bonus[classe]

        return {
            'hp': base['hp'] + bonus['hp'],
            'strength': base['strength'] + bonus['strength'],
            'intelligence': base['intelligence'] + bonus['intelligence'],
            'agility': base['agility'] + bonus['agility'],
            'weapon': bonus['weapon']
        }

    
    def visitWeapon(self, ctx: RPG_GamesParser.WeaponContext):
        return ctx.getChild(0).getText()

    def visitStatsUpdate(self, ctx: RPG_GamesParser.StatsUpdateContext):
        name = ctx.NAME().getText()
        # if name not in self.player:
        #     raise NameError(f"{name} is not a listed player")
        stat = ctx.stat().getText()
        value = int(ctx.NUMBER().getText())
        self.player[name][stat] = value
        return self.player
    
    def visitAddInventory(self, ctx: RPG_GamesParser.AddInventoryContext):
        name = ctx.NAME().getText()
        if name not in self.player:
            raise ValueError(f"{name} is not a listed player")
        item_token = ctx.item()
        if not item_token:
            raise ValueError("Invalid item name")
        item = item_token.getText()
        if item in self.player[name]['inventory']:
            self.player[name]['inventory'][item] += 1
        else:
            self.player[name]['inventory'][item] = 1
        return self.player
    
    def visitRemoveInventory(self, ctx: RPG_GamesParser.RemoveInventoryContext):
        name = ctx.NAME().getText()
        if name not in self.player:
            raise ValueError(f"{name} is not a listed player")
        item = ctx.item().getText()
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
        # print(f"{name} has:\n{inv if inv != "" else "Nothing!"}")
        return f"{name} has:\n{inv if inv != "" else "Nothing!"}"
        
    
    def visitSummary(self, ctx: RPG_GamesParser.SummaryContext):
        name = ctx.NAME().getText()
        for keys, val in self.player.items():
            print(keys, val)
        # if name not in self.player:
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
        if name not in self.player:
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
    
    def visitSave(self, ctx: RPG_GamesParser.SaveContext):
        filename = ctx.STRING().getText().strip('"')
        with open(filename, 'w') as f:
            for name, info in self.player.items():
                f.write(f"PLAYER:{name}\n")
                for key, val in info.items():
                    if key == 'inventory':
                        f.write("INVENTORY:\n")
                        for item, qty in val.items():
                            f.write(f"- {item}:{qty}\n")
                    else:
                        f.write(f"{key.upper()}:{val}\n")
                f.write("END\n")
        return f"Game saved to {filename}"

    def visitLoad(self, ctx: RPG_GamesParser.LoadContext):
        filename = ctx.STRING().getText().strip('"')
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
            self.player = {}
            current_player = None
            for line in lines:
                line = line.strip()
                if line.startswith("PLAYER:"):
                    current_player = line.split(":", 1)[1]
                    self.player[current_player] = {'inventory': {}}
                elif line.startswith("INVENTORY:"):
                    continue
                elif line.startswith("-"):
                    item, qty = line[1:].split(":")
                    self.player[current_player]['inventory'][item] = int(qty)
                elif ":" in line:
                    key, val = line.split(":", 1)
                    self.player[current_player][key.lower()] = int(val) if val.isdigit() else val
        except FileNotFoundError:
            return f"File '{filename}' not found."
        return f"Game loaded from {filename}"



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
