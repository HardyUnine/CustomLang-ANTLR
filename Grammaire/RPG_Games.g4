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
| summary
| poof
| diceRoll; //assignement

// un id(nom de variable) = une valeur entière
// assignement: ID EQ NUMBER;

// fonction declaration

//playerDecl:  CREATE '(' NAME ',' hp ',' strength ',' intelligence ',' agility',' weapon')'; 
playerDecl:  CREATE '(' NAME ',' race ',' classes ')'; 

statsUpdate: UPDATE '(' NAME ',' stat ',' NUMBER ')';

addInventory : GET '(' NAME ',' ITEM ')';

removeInventory : DEL '(' NAME ',' ITEM ')';

inInventory: PRINTINV '(' NAME ')';

summary: PRINTCAR '(' NAME ')';

poof: DEL '(' NAME ')';

diceRoll
    : 'ROLL' '(' NAME ',' NUMBER ')'     # RollWithName
    | 'ROLL' '(' NUMBER ')'              # RollWithoutName
    ;

weapon: SWORD | BOW | STAFF;

stat: STRENGTH | INTELLIGENCE | AGILITY | HP;

race: DWARF | HUMAN | ELF;

classes: PALADIN | WIZARD | RANGER;

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



// Whitespace
WS: [ \t\r\n]+ -> skip;
