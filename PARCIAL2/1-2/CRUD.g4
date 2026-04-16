grammar CRUD;

//GRAMATICA

s : ((sentencia ';')+ | expresion) EOF ; // Permite varias sentencias terminadas en ;

sentencia
    : insertar
    | buscar
    | actualizar
    | eliminar
    ;

insertar   : 'insertar' 'en' ID 'valores' lista ;
buscar     : 'buscar' 'en' ID cond ;
actualizar : 'actualizar' ID 'set' lista cond ;
eliminar   : 'eliminar' 'de' ID cond ;

lista : campo (',' campo)* ;
campo : ID '=' expresion ;

cond : 'donde' ID Operacion expresion
     | 
     ;

//OPERACIONES MATEAMATICAS
//en esta parte se permite que el usuario ponga operaciones como (1+1)*2

expresion
    : term (('+' | '-') term)*
    ;

term
    : factor (('*' | '/') factor)*
    ;

factor
    : VALOR
    | ID
    | '(' expresion ')'
    ;


//LEXICO 
Operacion : '==' | '!=' | '>' | '<' | '>=' | '<=' ;
ID    : [a-zA]+ ; 
VALOR : [a-zA-Z0-9]+ ;
WS    : [ \t\r\n]+ -> skip ; // se pone para poder hacer saltos de linea y que no los tome como error