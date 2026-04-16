%{
#include "booleana.tab.h"
%}

%%

"TRUE"      { return TRUE; }
"FALSE"     { return FALSE; }
"AND"       { return AND; }
"OR"        { return OR; }
"NOT"       { return NOT; }

[ \t]       ; 
\n          { return '\n'; }

.           { return yytext[0]; }

%%

int yywrap() { return 1; }