 grammar RPG_Games; // Définit nom de la grammaire

//---------------------------------------------------------------------------------------
// Parser
//---------------------------------------------------------------------------------------

// entrée dans le programme
program: 
statement* EOF; // End Of File

statement: assignement|
playerDecl
|statsUpdate
|removeInventory
|addInventory
|inInventory
|summary
|poof;

// un id(nom de variable) = une valeur entière
assignement: ID EQ NUMBER;

strength: NUMBER;
agility : NUMBER;
intelligence: NUMBER;
hp: NUMBER;

stat: STRENGTH|INTELLIGENCE|AGIL|HP

weapon: SWORD|BOW|STAFF;

// fonction declaration

playerDecl:  SUMMON'('NAME ',' hp ',' strength ',' intelligence ',' agility',' weapon')'; 

statsUpdate: ALTERATION '(' NAME ',' stat ',' NUMBER ')';

addInventory : AQUIRE '(' NAME ',' ITEM ')';

removeInventory : POOF '(' NAME ',' ITEM ')';

inInventory: WhatsInMyBag '(' NAME ')';

summary: SUMMAWY '(' NAME ')';

poof: POOF '(' NAME ')';
// ---------------------------------------------------------------------------------------
// Lexer
// ---------------------------------------------------------------------------------------
// NOM: 'définition' ou regexp, qu'est ce que ça peut etre 
SUMMON: 'SUMMON'; //dès que antlr lit le mot player il créer un token PLAYER

ROLL : 'roll';

SWORD : 'sword';
BOW : 'bow';
STAFF: 'staff';

STRENGTH : 'strength';
AGIL : 'agility';
INTELLIGENCE: 'intelligence';
HP : 'hp';


ITEM: [a-zA-Z_][a-zA-Z_0-9]*;

NUMBER : [0-9]+;

NAME: [a-zA-Z_]+;

// Whitespace
WS: [ \t\r\n]+ -> skip;
