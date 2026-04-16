%{
#include <stdio.h>
#include <stdlib.h>

void yyerror(const char *s);
int yylex();
extern FILE *yyin; // Referencia al archivo de entrada de Flex
%}

%token TRUE FALSE AND OR NOT
%left OR
%left AND
%right NOT

%%
input:
    | input line
    ;

line:
    exp '\n' { printf("RESULTADO: %s\n", $1 ? "VERDADERO" : "FALSO"); }
    | '\n'
    ;

exp:
    TRUE          { $$ = 1; }
    | FALSE       { $$ = 0; }
    | exp AND exp { $$ = $1 && $3; }
    | exp OR exp  { $$ = $1 || $3; }
    | NOT exp     { $$ = !$2; }
    | '(' exp ')' { $$ = $2; }
    ;
%%

void yyerror(const char *s) {
    fprintf(stderr, "Error sintactico: %s\n", s);
}

int main(int argc, char **argv) {
    if (argc > 1) {
        FILE *file = fopen(argv[1], "r");
        if (!file) {
            fprintf(stderr, "No se pudo abrir el archivo %s\n", argv[1]);
            return 1;
        }
        yyin = file; // Indicamos a Flex que lea del archivo
    } else {
        printf("Ingresa expresiones booleanas (o pasa un .txt como argumento)");
    }
    
    return yyparse();
}