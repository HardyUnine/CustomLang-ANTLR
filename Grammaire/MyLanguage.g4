 grammar RPG_Games; // Définit nom de la grammaire

//---------------------------------------------------------------------------------------
// Parser
//---------------------------------------------------------------------------------------

// entrée dans le programme
program: 
statement* EOF; // End Of File

statement: assignement|playerDecl;

// un id(nom de variable) = une valeur entière
assignement: 
ID EQ NUMBER;

// fonction player nom joueur {hp = 12 etc }
playerDecl: 
PLAYER EQ NAME; 


// ---------------------------------------------------------------------------------------
// Lexer
// ---------------------------------------------------------------------------------------
// NOM: 'définition' ou regexp, qu'est ce que ça peut etre 
PLAYER: 'player'; //dès que antlr lit le mot player il créer un token PLAYER

ROLL : 'roll';

ARROW : '->'; //en signe d'attaque ?

NUMBER : [0-9]+;
HP: [0-9]+;

NAME: [a-zA-Z_];
ID : [a-zA-Z_][a-zA-Z_0-9]*;

EQ: '=';

CURLYL : '{';
CURLYR : '}';