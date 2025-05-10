%{
#include <iostream>
#include <string>
#include <map>
static std::map<std::string, int> vars;
inline void yyerror(const char *str) { std::cout << str << std::endl; }
int yylex();
%}

%union { int num; std::string *str; }

%token<num> NUMBER
%token<str> ID
%token print
%type<num> expression
%type<num> assignment

%right '='
%left '+' '-'
%left '*' '/'



%%

program: statement_list
        ;

statement_list: statement
    | statement_list statement
    ;

statement: assignment
    | expression ':'          { std::cout << $1 << std::endl; }
    ;

assignment: ID '=' expression ':'
    { 
        printf("Assign %s = %d\n", $1->c_str(), $3); 
        $$ = vars[*$1] = $3; 
        delete $1;
    }
    ;

expression:
    NUMBER                  { printf("NUM(%d)\n", $1); $$ = $1; }
    | ID                    { $$ = vars[*$1]; printf("VAR(%s = %d)\n", $1->c_str(), $$); delete $1; }
    | expression '+' expression  { printf("(+ %d %d)\n", $1, $3); $$ = $1 + $3; }
    | expression '-' expression  { printf("(- %d %d)\n", $1, $3); $$ = $1 - $3; }
    | expression '*' expression  { printf("(* %d %d)\n", $1, $3); $$ = $1 * $3; }
    | expression '/' expression  { 
        if ($3 == 0) {
            yyerror("Error: División por cero");
            $$ = 0;
        } else {
            printf("(/ %d %d)\n", $1, $3);
            $$ = $1 / $3;
        }
    }
    ;
%%

int main() {
    yyparse();
    return 0;
}
