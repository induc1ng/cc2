grammar TileMap;

ID :      ('a'..'z' | 'A'..'Z' | '_') ('a'..'z' | 'A'..'Z' | '0'..'9' | '_')*;
NUM_INT :    ('0'..'9')+;
NUM_REAL :   ('0'..'9')+ '.' ('0'..'9')+;
CADEIA :     '"' ~('\n' | '\r' | '"')* '"';
WS : 		 [ \n\t\r]+ -> skip;

/* Bloco principal */

mapa:
	'map' '(' size ')' 'quantity' '(' size ')' 'import' '{' tile? '}' 'commands' '{'commands?'}' EOF;

/* Comandos para se utilizar para preencher / alterar o mapa */

commands:
  (add) recur_commands ;

recur_commands:  commands | ;

add:
    'add' tipoTyle NUM_INT;

tile:
    ID '{' path 'type' ':' tipoTyle '}' recur_tiles;

recur_tiles:
    tile | ;

tipoTyle: 
  ID;

size:
  'size' ':' NUM_INT;
  
path:
  'path' ':' CADEIA;