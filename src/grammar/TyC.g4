grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

// TODO: Define grammar rules here
program: decl+ EOF;
decl: structdecl | funcdecl;

structdecl: STRUCT ID LB structvarlist RB SEMI;
structvarlist: stype ID SEMI structvarlist |;

funcdecl: (ftype func) | func;
func: ID LP paramlist RP blockstmt;
paramlist: parameters |;
parameters: param CM parameters | param;
param: stype ID;

blockstmt: LB stmtlist RB;
stmtlist: stmt stmtlist | stmt;
stmt: (vardeclstmt SEMI)| ifstmt | whilestmt | forstmt | switchstmt | (controlstmt SEMI) | (exprstmt SEMI);

// vardeclare
vardeclstmt: vtype vardecl ;
vardecl: var CM vardecl | var ;
var: ID ASS expr | ID;

// if
ifstmt: (IF LP expr RP (blockstmt | stmt) ELSE (blockstmt | stmt)) | (IF LP expr RP (blockstmt | stmt));

// while
whilestmt: WHILE LP expr RP (blockstmt | stmt);

// for
forstmt: FOR LP init SEMI condition SEMI update RP (blockstmt | stmt);
init: (vardeclstmt | assignstmt) CM init | (vardeclstmt | assignstmt) |;
condition: expr |;
update: expr |;

// switch
switchstmt: SWITCH LP expr RP LB casestmt defaultstmt RB;
casestmt: caselist |;
caselist: case caselist | case;
case: CASE expr ':' stmtlist;
defaultstmt: (DEFAULT ':' stmtlist) |;

// controlstmt
controlstmt: breakstmt | continuestmt | returnstmt;
breakstmt: BREAK;
continuestmt: CONTINUE;
returnstmt: RETURN expr | RETURN;

// exprstmt
exprstmt: assignstmt | callstmt | prefixstmt;
assignstmt: assignvar ASS expr;
assignvar: ID DOT assignvar | ID;
callstmt: ID LP callparam RP;
callparam: callparameter |;
callparameter: expr CM callparameter | expr;

// expression
expr: logicOR ASS expr| logicOR;
logicOR: logicOR OR logicAND | logicAND;
logicAND: logicAND AND eqcompare | eqcompare;
eqcompare: eqcompare (EQ|NEQ) relop | relop;
relop: relop (LETH|GRTH|LTE|GTE) additive | additive;
additive: additive (PLUS|MINUS) multiple | multiple;
multiple: multiple (MUL|DIV|MOD) prefixstmt | prefixstmt;
prefixstmt: (INC | DEC | NOT | MINUS | PLUS) prefixstmt | postfix;
postfix: postfix (INC|DEC) | memberaccess;
memberaccess: memberaccess DOT ID | primary;
primary: LP expr RP | ID | INTLITERAL | FLOATLITERAL | STRINGLITERAL | LB exprlist RB | callstmt;


exprlist: nonemptyexprlist|;
nonemptyexprlist: expr CM nonemptyexprlist | expr;

stype: INTEGER | FLOAT | STRING | ID;
vtype: INTEGER | FLOAT | STRING | AUTO | ID;
ftype: INTEGER | FLOAT | STRING | VOID | ID;


// KEYWORDS
// Type
AUTO: 'auto';
FLOAT: 'float';
INTEGER: 'int';
STRING: 'string';
VOID: 'void';

// Structure
STRUCT: 'struct';
WHILE : 'while';
FOR: 'for';
IF: 'if';
ELSE: 'else';
SWITCH : 'switch';
CASE: 'case';
DEFAULT: 'default';

// Control flow
BREAK: 'break';
CONTINUE: 'continue';
RETURN : 'return';

// IDENTIFIER
ID: [a-zA-Z_][a-zA-Z0-9_]*;


// OPERATOR
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';

EQ: '==';
NEQ: '!=';
LETH: '<';
GRTH: '>';
LTE: '<=';
GTE: '>=';

OR: '||';
AND: '&&';
NOT: '!';

INC: '++';
DEC: '--';
ASS: '=';
DOT: '.';

// SEPARATOR
LB: '{';
RB: '}';
LP: '(';
RP: ')';
SEMI: ';';
CM: ',';

// LITERAL
INTLITERAL: '0' | [1-9][0-9]*;
FLOATLITERAL: FPART EPART;
STRINGLITERAL: '"' STRING_CHAR* '"' {
    self.text = self.text.replace('"', '')
};

// FRAGMENTS
fragment DIGIT: [0-9];
fragment FPART: (DIGIT+ '.' DIGIT*) | ('.' DIGIT+) ;
fragment EPART: ([eE] [+-]? DIGIT+)? ;
fragment STRING_CHAR: ~["\\] | ESC_SEQ;
fragment ESC_SEQ: '\\' [bfrnt"\\];


// COMMENT
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;


// WHITESPACE
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs

// ERROR
ERROR_CHAR: .;
ILLEGAL_ESCAPE: '"' (~["\\] | '\\' [bfrnt"\\])* '\\' ~[bfrnt"\\];
UNCLOSE_STRING: '"' (~["\\\r\n] | ESC_SEQ)* ([\r\n] | EOF);

