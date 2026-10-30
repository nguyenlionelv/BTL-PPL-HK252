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
program: decl* EOF;
decl: structdecl | funcdecl;

structdecl: STRUCT ID LB structvarlist RB SEMI;
structvarlist: stype ID SEMI structvarlist |;

funcdecl: ftype func;
func: ID LP paramlist RP blockstmt;
paramlist: parameters |;
parameters: param CM parameters | param;
param: stype ID;

// block stmt
blockstmt: LB stmtlist RB;
stmtlist: stmt stmtlist | ;
stmt: (vardeclstmt SEMI)| ifstmt | whilestmt | forstmt | switchstmt | (controlstmt SEMI) | (exprstmt SEMI) | blockstmt;

// vardeclare
vardeclstmt: vtype var;
var: ID ASS expr | ID;

// if
ifstmt: (IF LP expr RP (blockstmt | stmt) ELSE (blockstmt | stmt)) | (IF LP expr RP (blockstmt | stmt));

// while
whilestmt: WHILE LP expr RP (blockstmt | stmt);

// for
forstmt: FOR LP init SEMI condition SEMI update RP (blockstmt | stmt);
init: vardeclstmt | assignstmt |;
condition: expr |;
update: assignstmt | prefix | postfix |;

// switch
switchstmt: SWITCH LP expr RP LB casestmt defaultstmt RB;
casestmt: caselist |;
caselist: case caselist | case;
case: CASE expr COLON stmtlist;
defaultstmt: (DEFAULT COLON stmtlist) |;

// controlstmt
controlstmt: breakstmt | continuestmt | returnstmt;
breakstmt: BREAK;
continuestmt: CONTINUE;
returnstmt: RETURN expr | RETURN;

// exprstmt
exprstmt: assignstmt | callstmt | expr;
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
multiple: multiple (MUL|DIV|MOD) unary | unary;
unary: (NOT|MINUS|PLUS) unary | prefix;
prefix: (INC|DEC) prefix | postfix;
postfix: postfix DOT ID | postfix ((LP callparam RP) | (INC|DEC)) | primary;
primary: LP expr RP | ID | INTLITERAL | FLOATLITERAL | STRINGLITERAL | LB exprlist RB;


exprlist: nonemptyexprlist|;
nonemptyexprlist: expr CM nonemptyexprlist | expr;

stype: INTEGER | FLOAT | STRING | ID;
vtype: INTEGER | FLOAT | STRING | AUTO | ID;
ftype: INTEGER | FLOAT | STRING | VOID | ID |;


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
COLON: ':';

// LITERAL
INTLITERAL: [0-9]+;
FLOATLITERAL: FLOAT_HAS_POINT | FLOAT_NON_POINT;
STRINGLITERAL: '"' STRING_CHAR* '"' {
    self.text = self.text[1:-1]
};

// FRAGMENTS
fragment DIGIT: [0-9];
// fragment FPART: (DIGIT+ '.' DIGIT*) | ('.' DIGIT+) ;
// fragment EPART: ([eE] [+-]? DIGIT+)? ;
fragment STRING_CHAR: ~["\\\r\n] | ESC_SEQ;
fragment ESC_SEQ: '\\' [bfrnt"\\];

fragment FLOAT_HAS_POINT: FLOAT_E | FLOAT_NE;
fragment FLOAT_NE: (DIGIT+ '.' DIGIT*) | ('.' DIGIT+);
fragment FLOAT_E: (DIGIT* '.' DIGIT+ [eE] [+-]? DIGIT+) | (DIGIT+ '.' [eE] [+-]? DIGIT+);
fragment FLOAT_NON_POINT: DIGIT+ [eE] [+-]? DIGIT+;


// COMMENT
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;


// WHITESPACE
WS : [ \t\f\r\n]+ -> skip ; // skip spaces, tabs

// ERROR
ILLEGAL_ESCAPE: '"' (~["\\\n\r] | ESC_SEQ)* '\\' ~[bfrnt"\\\n\r] {
    self.text = self.text[1:]
};
UNCLOSE_STRING: '"' (~["\\\r\n] | ESC_SEQ)* {
    self.text = self.text[1:]
};
ERROR_CHAR: .;

