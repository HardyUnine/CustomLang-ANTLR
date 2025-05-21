 grammar RPG_Games; // Définit nom de la grammaire

//---------------------------------------------------------------------------------------
// Parser
//---------------------------------------------------------------------------------------

// entrée dans le programme
program: 
statement* EOF; // End Of File

statement: assignement|playerDecl;

// un id(nom de variable) = une valeur entière
assignement: ID EQ NUMBER;


strength: NUMBER;
agility : NUMBER;
intelligence: NUMBER

weapon: SWORD|BOW|STAFF;

// fonction declaration
playerDecl: SUMMON '('NAME ',' strength ',' intelligence ',' agility ',' weapon')'; 



// ---------------------------------------------------------------------------------------
// Lexer
// ---------------------------------------------------------------------------------------
// NOM: 'définition' ou regexp, qu'est ce que ça peut etre 
PLAYER: 'SUMMON'; //dès que antlr lit le mot player il créer un token PLAYER

ASSIGN: '';

ROLL : 'roll';

SWORD : 'sword';
BOW : 'bow';
STAFF: 'staff';


NUMBER : [0-9]+;
HP: [0-9]+;

NAME: [a-zA-Z_];
ID : [a-zA-Z_][a-zA-Z_0-9]*;

EQ: '=';

CURLYL : '{';
CURLYR : '}';

PARL : '(';
PARR : ')';

