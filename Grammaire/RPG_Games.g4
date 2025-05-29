grammar RPG_Games; // Définit nom de la grammaire

// TO UPDATE INTERPRETER 
// (Assuming your are pointing to Grammaire):
// antlr4 -Dlanguage=Python3 -visitor -o ..\Interpreter\g4 RPG_Games.g4 
// to run on linux:
// /var/data/python/bin/antlr4 -Dlanguage=Python3 -visitor -o ../Interpreter/g4 RPG_Games.g4


//---------------------------------------------------------------------------------------
// Parser
//---------------------------------------------------------------------------------------

// entrée dans le programme
program: statement* EOF; // End Of File

statement: playerDecl
| statsUpdate
| addInventory
| removeInventory
| inInventory
| listplayer
| summary
| poof
| diceRoll 
| save
| load;


playerDecl:  CREATE '(' NAME ',' race ',' classes ')'; 

statsUpdate: UPDATE '(' NAME ',' stat ',' NUMBER ')';

addInventory : GET '(' NAME ',' item ')';

removeInventory : DEL '(' NAME ',' item ')';

item: NAME | ITEM;

inInventory: PRINTINV '(' NAME ')';

listplayer: PRINTCAR;

summary: PRINTCAR '(' NAME ')';

poof: DEL '(' NAME ')';

diceRoll
    : DICEROLL '(' NAME ',' NUMBER ')'     # RollWithName
    | DICEROLL '(' NUMBER ')'              # RollWithoutName
    ;

stat: STRENGTH | INTELLIGENCE | AGILITY | HP;

race: DWARF | HUMAN | ELF;

classes: PALADIN | WIZARD | RANGER;

save: 'SAVE' '(' STRING ')';

load: 'LOAD' '(' STRING ')';

// weapon: SWORD | BOW | STAFF;
// strength: NUMBER;
// agility : NUMBER;
// intelligence: NUMBER;
// hp: NUMBER;

// ---------------------------------------------------------------------------------------
// Lexer
// ---------------------------------------------------------------------------------------
// NOM: 'définition' ou regexp, qu'est ce que ça peut etre 
CREATE: 'SUMMON'; //dès que antlr lit le mot player il créer un token PLAYER
DEL: 'POOF';
GET: 'AQUIRE';
UPDATE: 'ALTERATE';
PRINTINV: 'WhatsInMyBag';
PRINTCAR: 'SUMMAWY';
DICEROLL: 'ROLL';

SWORD : 'sword';
BOW : 'bow';
STAFF: 'staff';

STRENGTH : 'strength';
AGILITY : 'agility';
INTELLIGENCE: 'intelligence';
HP : 'hp';

DWARF: 'Dwarf';
HUMAN: 'Human';
ELF: 'Elf';

PALADIN: 'Paladin';
WIZARD: 'Wizard';
RANGER: 'Ranger';

NAME: [a-zA-Z_]+;

ITEM: [a-zA-Z_][a-zA-Z_0-9]*;

NUMBER : [0-9]+;

STRING: '"' (~["\r\n])* '"';

// Whitespace
WS: [ \t\r\n]+ -> skip;
