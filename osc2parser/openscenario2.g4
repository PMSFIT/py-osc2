/*
 * PMSF py-osc2 Framework
 *
 * (C) 2021 -- 2022 PMSF IT Consulting Pierre R. Mai
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

grammar openscenario2;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from .openscenario2Parser import openscenario2Parser
}
@lexer::members {
class openscenario2Denter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: openscenario2Lexer = lexer

    def pull_token(self):
        return super(openscenario2Lexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.openscenario2Denter(self, self.NEWLINE, openscenario2Parser.INDENT, openscenario2Parser.DEDENT, False)
    return self.denter.next_token()

}

osc_file : prelude_statement* osc_declaration*  EOF;

prelude_statement : import_statement  ;

import_statement : 'import' import_reference NEWLINE  ;
import_reference : string_literal | structured_identifier  ;

structured_identifier : (identifier '.')* identifier  ;

osc_declaration :   physical_type_declaration
                    | unit_declaration
                    | enum_declaration
                    | struct_declaration
                    | actor_declaration
                    | action_declaration
                    | scenario_declaration
                    | modifier_declaration  ;

type_declarator : non_aggregate_type_declarator | aggregate_type_declarator  ;

non_aggregate_type_declarator : primitive_type | declared_type_name ;
declared_type_name : identifier ;

aggregate_type_declarator : list_type_declarator  ;
list_type_declarator : 'list' 'of' non_aggregate_type_declarator  ;

primitive_type : 'int' | 'uint' | 'float' | 'bool' | 'string'  ;

physical_type_declaration : 'type' declared_type_name 'is' base_unit_specifier NEWLINE  ;

unit_declaration : 'unit' unit_name 'of' declared_type_name 'is' unit_specifier NEWLINE  ;

base_unit_specifier : si_base_unit_specifier  ;
unit_specifier : si_unit_specifier  ;

si_base_unit_specifier : 'SI' '(' si_base_exponent_list ')'  ;
si_base_exponent_list : si_base_exponent (',' si_base_exponent)*  ;
si_base_exponent : si_base_unit_name ':' integer_literal  ;

si_unit_specifier : 'SI' '(' si_base_exponent_list (',' si_factor)? (',' si_offset)? ')'  ;
si_factor : 'factor' ':' ( float_literal | integer_literal ) ;
si_offset : 'offset' ':' ( float_literal | integer_literal ) ;
si_base_unit_name : 'kg' | 'm' | 's' | 'A' | 'K' | 'mol' | 'cd' | 'rad'  ;

enum_declaration : 'enum' enum_name ':' '[' enum_member_decl (',' enum_member_decl)* ']' NEWLINE  ;
enum_member_decl : enum_member_name ( '=' enum_member_value )?  ;
enum_name : identifier  ;
enum_member_name : identifier  ;
enum_member_value : uint_literal | hex_uint_literal  ;

enum_value_reference : (enum_name '.')? enum_member_name  ;

struct_declaration : 'struct' struct_name ('inherits' struct_name ('(' field_name '=='  (enum_value_reference | bool_literal) ')')?)? (':' INDENT struct_member_decl+ DEDENT)?  ;

struct_member_decl : event_declaration|field_declaration|constraint_declaration|method_declaration|coverage_declaration  ;
struct_name : identifier  ;
field_name : identifier  ;

actor_declaration : 'actor' actor_name ('inherits' actor_name ('(' field_name '==' (enum_value_reference | bool_literal) ')')?)? (':' INDENT actor_member_decl+)?  ;

actor_member_decl : event_declaration|field_declaration|constraint_declaration|method_declaration|coverage_declaration  ;
actor_name : identifier  ;

scenario_declaration : 'scenario' qualified_behavior_name ('inherits' qualified_behavior_name ('(' field_name '==' (enum_value_reference | bool_literal) ')')?)? (':' INDENT (scenario_member_decl | behavior_specification)+ DEDENT)?  ;

scenario_member_decl : event_declaration|field_declaration|constraint_declaration|method_declaration|coverage_declaration|modifier_application  ;

qualified_behavior_name : (actor_name '.')? behavior_name  ;
behavior_name : identifier  ;

action_declaration : 'action' qualified_behavior_name ('inherits' qualified_behavior_name ('(' field_name '==' (enum_value_reference | bool_literal) ')')?)? (':' INDENT (scenario_member_decl | behavior_specification)+ DEDENT)?  ;

modifier_declaration : 'modifier' (actor_name '.')? modifier_name ('of' qualified_behavior_name)? (':' INDENT (scenario_member_decl | on_directive)+ DEDENT)?  ;

modifier_name : identifier  ;

type_extension : enum_type_extension | structured_type_extension  ;

enum_type_extension : 'extend' enum_name ':' INDENT (enum_member_decl NEWLINE)+ DEDENT  ;

structured_type_extension : 'extend' extendable_type_name ':' INDENT extension_member_decl+ DEDENT  ;

extendable_type_name : struct_name | actor_name | qualified_behavior_name  ;
extension_member_decl : struct_member_decl | actor_member_decl | scenario_member_decl | behavior_specification  ;

event_declaration : 'event' event_name ('(' argument_list_specification ')')? ('is' event_specification)? NEWLINE  ;
event_specification : event_reference ( (event_field_decl)? 'if' event_condition )?
                       | event_condition  ;

event_reference : '@' event_path  ;
event_field_decl : 'as' event_field_name  ;
event_field_name : identifier  ;
event_name : identifier  ;
event_path : (expression '.')? event_name  ;

event_condition : bool_expression | rise_expression | fall_expression | elapsed_expression | every_expression  ;
rise_expression : 'rise' '(' bool_expression ')'  ;
fall_expression : 'fall' '(' bool_expression ')'  ;
elapsed_expression : 'elapsed' '(' duration_expression ')'  ;
every_expression : 'every' '(' duration_expression (',' 'offset' ':' duration_expression)? ')'  ;

bool_expression : expression  ;
duration_expression : expression  ;

field_declaration :  parameter_declaration | variable_declaration  ;
parameter_declaration : field_name (',' field_name)* ':' type_declarator ('=' default_value)? (parameter_with_declaration | NEWLINE)  ;
variable_declaration : 'var' field_name (',' field_name)* ':' type_declarator ('=' default_value | sample_expression )? NEWLINE  ;

sample_expression : 'sample' '(' expression ',' event_specification (',' default_value)? ')'  ;
default_value : value_exp  ;

parameter_with_declaration : 'with' ':' INDENT parameter_with_member+ DEDENT  ;
parameter_with_member : constraint_declaration  ;

constraint_declaration : keep_constraint_declaration | remove_default_declaration  ;

keep_constraint_declaration : 'keep' '(' (constraint_qualifier)? constraint_expression ')' NEWLINE  ;
constraint_qualifier : 'default' | 'hard'  ;

constraint_expression : expression  ;

remove_default_declaration : 'remove_default' '(' parameter_reference ')' NEWLINE  ;

parameter_reference : field_name | field_access  ;

method_declaration : 'def' method_name '(' (argument_list_specification)? ')' ('->' return_type)? method_implementation NEWLINE  ;

return_type : type_declarator  ;

method_implementation : 'is' (method_qualifier)? ('expression' expression | 'undefined' | 'external' structured_identifier '(' (argument_list)? ')')  ;

method_qualifier : 'only'  ;
method_name : identifier  ;

coverage_declaration : ('cover' | 'record') '(' argument_list ')' NEWLINE  ;

modifier_application : (actor_expression '.')? modifier_name '(' (argument_list)? ')' NEWLINE  ;

behavior_specification : on_directive | do_directive  ;

on_directive : 'on' event_specification ':' INDENT on_member+ DEDENT  ;

on_member : call_directive | emit_directive  ;

do_directive : 'do' do_member  ;

do_member : (label_name ':')? ( composition | behavior_invocation | wait_directive | emit_directive | call_directive )  ;

label_name : identifier  ;

composition : composition_operator ('(' argument_list ')')?':' INDENT      do_member+ DEDENT (behavior_with_declaration)?  ;

composition_operator : 'serial' | 'one_of' | 'parallel'  ;

behavior_invocation : (actor_expression '.')? behavior_name '(' (argument_list)? ')' (behavior_with_declaration | NEWLINE)  ;

behavior_with_declaration : 'with' ':' INDENT behavior_with_member+ DEDENT  ;
behavior_with_member : constraint_declaration
                       | modifier_application
                       | until_directive  ;

actor_expression : expression  ;

wait_directive : 'wait' event_specification NEWLINE  ;

emit_directive : 'emit' event_name ('(' argument_list ')')? NEWLINE  ;

call_directive : 'call' method_invocation NEWLINE  ;

method_invocation : postfix_exp '(' (argument_list)? ')'  ;

until_directive : 'until' event_specification NEWLINE  ;

argument_list_specification : argument_specification (',' argument_specification)*  ;

argument_specification : argument_name ':' type_declarator ('=' default_value)?  ;

argument_name : identifier  ;

argument_list : positional_argument (',' positional_argument)* (',' named_argument)*
                | named_argument (',' named_argument)*  ;

positional_argument : expression  ;
named_argument : argument_name ':' expression  ;

expression : implication | ternary_op_exp  ;

ternary_op_exp : implication '?' expression ':' expression  ;

implication : disjunction ('=>' disjunction)*  ;
disjunction : conjunction ('or' conjunction)*  ;
conjunction : inversion ('and' inversion)*  ;
inversion : 'not' inversion | relation  ;

relation : sum_exp | relation relational_op sum_exp  ;
relational_op : '==' | '!=' | '<' | '<=' | '>' | '>=' | 'in'  ;

sum_exp : term | sum_exp additive_op term  ;
additive_op : '+' | '-'  ;

term : factor | term multiplicative_op factor  ;
multiplicative_op : '*' | '/' | '%'  ;

factor : postfix_exp | '-' factor  ;


postfix_exp : primary_exp #primary_exp_pe
              | postfix_exp '.' 'as' '(' type_declarator ')' #cast_exp_pe
              | postfix_exp '.' 'is' '(' type_declarator ')' #type_test_exp_pe
              | postfix_exp '(' expression ')?' #element_access_pe
              | postfix_exp '(' (argument_list)? ')' #function_application_pe
              | postfix_exp '.' field_name #field_access_pe
              ;

field_access : postfix_exp '.' field_name  ;

primary_exp : value_exp | 'it' | identifier | '(' expression ')'  ;

value_exp : integer_literal
            | float_literal
            | physical_literal
            | bool_literal
            | string_literal
            | list_constructor
            | range_constructor  ;

list_constructor : '[' expression (',' expression)* ']'  ;
range_constructor : 'range' '(' expression ',' expression ')' | '[' expression '..' expression ']'  ;

string_literal : STRING_LITERAL;
STRING_LITERAL : SHORTSTRING | LONGSTRING ;
SHORTSTRING : ('"' (~[\\'"\r\n] | '\\' ~[\r\n])* '"') | ('\'' (~[\\'"\r\n] | '\\' ~[\r\n])* '\'') ;
LONGSTRING : ('"""' (~[\\'"] | '\\' ~[\r\n])* '"""') | ('\'\'\'' (~[\\'"] | '\\' ~[\r\n])* '\'\'\'') ;

bool_literal : BOOL_LITERAL;
BOOL_LITERAL : 'true' | 'false' ;

integer_literal : INTEGER_LITERAL;
INTEGER_LITERAL : UINT_LITERAL | HEX_UINT_LITERAL | INT_LITERAL  ;
uint_literal : UINT_LITERAL;
UINT_LITERAL : DIGIT+  ;
hex_uint_literal : HEX_UINT_LITERAL;
HEX_UINT_LITERAL : '0x' HEX_DIGIT+  ;
INT_LITERAL : '-' DIGIT+  ;
fragment DIGIT : '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'  ;
fragment HEX_DIGIT : DIGIT | 'A' | 'a' | 'B' | 'b' | 'C' | 'c' | 'D' | 'd' | 'E' | 'e' | 'F' | 'f'  ;

float_literal : FLOAT_LITERAL;
FLOAT_LITERAL : ('+' | '-')? DIGIT* '.' DIGIT+ (('e' | 'E') ('+'|'-')? DIGIT+)?  ;

identifier : IDENTIFIER | 'expression' | 'unit' | 'import' ;
IDENTIFIER : ( [A-Za-z] [A-Za-z0-9_]* ) | ( '|' (~[|])+ '|' )  ;

physical_literal : PHYSICAL_LITERAL;
PHYSICAL_LITERAL : (FLOAT_LITERAL | INTEGER_LITERAL) UNIT_NAME  ;
unit_name : UNIT_NAME ;
UNIT_NAME : IDENTIFIER ;

LINEJOINER : '\\' '\r'? '\n' -> skip ;

NEWLINE: ('\r'? '\n' ' '*);

WS : [ \t]+ -> skip ;
COMMENT : '#' ~[\r\n]* -> skip ;
