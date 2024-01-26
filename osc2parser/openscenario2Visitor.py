# Generated from openscenario2.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .openscenario2Parser import openscenario2Parser
else:
    from openscenario2Parser import openscenario2Parser

# This class defines a complete generic visitor for a parse tree produced by openscenario2Parser.

class openscenario2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by openscenario2Parser#osc_file.
    def visitOsc_file(self, ctx:openscenario2Parser.Osc_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#prelude_statement.
    def visitPrelude_statement(self, ctx:openscenario2Parser.Prelude_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#import_statement.
    def visitImport_statement(self, ctx:openscenario2Parser.Import_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#import_reference.
    def visitImport_reference(self, ctx:openscenario2Parser.Import_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#structured_identifier.
    def visitStructured_identifier(self, ctx:openscenario2Parser.Structured_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#main_statement.
    def visitMain_statement(self, ctx:openscenario2Parser.Main_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#namespace_statement.
    def visitNamespace_statement(self, ctx:openscenario2Parser.Namespace_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#namespace_list.
    def visitNamespace_list(self, ctx:openscenario2Parser.Namespace_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#namespace_name.
    def visitNamespace_name(self, ctx:openscenario2Parser.Namespace_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#global_namespace_name.
    def visitGlobal_namespace_name(self, ctx:openscenario2Parser.Global_namespace_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#export_statement.
    def visitExport_statement(self, ctx:openscenario2Parser.Export_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#export_specification.
    def visitExport_specification(self, ctx:openscenario2Parser.Export_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#export_wildcard_specification.
    def visitExport_wildcard_specification(self, ctx:openscenario2Parser.Export_wildcard_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#osc_declaration.
    def visitOsc_declaration(self, ctx:openscenario2Parser.Osc_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#type_declarator.
    def visitType_declarator(self, ctx:openscenario2Parser.Type_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#non_aggregate_type_declarator.
    def visitNon_aggregate_type_declarator(self, ctx:openscenario2Parser.Non_aggregate_type_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#declared_type_name.
    def visitDeclared_type_name(self, ctx:openscenario2Parser.Declared_type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#aggregate_type_declarator.
    def visitAggregate_type_declarator(self, ctx:openscenario2Parser.Aggregate_type_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#list_type_declarator.
    def visitList_type_declarator(self, ctx:openscenario2Parser.List_type_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#primitive_type.
    def visitPrimitive_type(self, ctx:openscenario2Parser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#physical_type_declaration.
    def visitPhysical_type_declaration(self, ctx:openscenario2Parser.Physical_type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#unit_declaration.
    def visitUnit_declaration(self, ctx:openscenario2Parser.Unit_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#base_unit_specifier.
    def visitBase_unit_specifier(self, ctx:openscenario2Parser.Base_unit_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#unit_specifier.
    def visitUnit_specifier(self, ctx:openscenario2Parser.Unit_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#si_base_unit_specifier.
    def visitSi_base_unit_specifier(self, ctx:openscenario2Parser.Si_base_unit_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#si_base_exponent_list.
    def visitSi_base_exponent_list(self, ctx:openscenario2Parser.Si_base_exponent_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#si_base_exponent.
    def visitSi_base_exponent(self, ctx:openscenario2Parser.Si_base_exponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#si_unit_specifier.
    def visitSi_unit_specifier(self, ctx:openscenario2Parser.Si_unit_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#si_factor.
    def visitSi_factor(self, ctx:openscenario2Parser.Si_factorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#si_offset.
    def visitSi_offset(self, ctx:openscenario2Parser.Si_offsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#si_base_unit_name.
    def visitSi_base_unit_name(self, ctx:openscenario2Parser.Si_base_unit_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#enum_declaration.
    def visitEnum_declaration(self, ctx:openscenario2Parser.Enum_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#enum_member_decl.
    def visitEnum_member_decl(self, ctx:openscenario2Parser.Enum_member_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#enum_name.
    def visitEnum_name(self, ctx:openscenario2Parser.Enum_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#enum_member_name.
    def visitEnum_member_name(self, ctx:openscenario2Parser.Enum_member_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#enum_member_value.
    def visitEnum_member_value(self, ctx:openscenario2Parser.Enum_member_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#enum_value_reference.
    def visitEnum_value_reference(self, ctx:openscenario2Parser.Enum_value_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#struct_declaration.
    def visitStruct_declaration(self, ctx:openscenario2Parser.Struct_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#struct_member_decl.
    def visitStruct_member_decl(self, ctx:openscenario2Parser.Struct_member_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#struct_name.
    def visitStruct_name(self, ctx:openscenario2Parser.Struct_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#field_name.
    def visitField_name(self, ctx:openscenario2Parser.Field_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#actor_declaration.
    def visitActor_declaration(self, ctx:openscenario2Parser.Actor_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#actor_member_decl.
    def visitActor_member_decl(self, ctx:openscenario2Parser.Actor_member_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#actor_name.
    def visitActor_name(self, ctx:openscenario2Parser.Actor_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#scenario_declaration.
    def visitScenario_declaration(self, ctx:openscenario2Parser.Scenario_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#scenario_member_decl.
    def visitScenario_member_decl(self, ctx:openscenario2Parser.Scenario_member_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#qualified_behavior_name.
    def visitQualified_behavior_name(self, ctx:openscenario2Parser.Qualified_behavior_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#behavior_name.
    def visitBehavior_name(self, ctx:openscenario2Parser.Behavior_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#action_declaration.
    def visitAction_declaration(self, ctx:openscenario2Parser.Action_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#modifier_declaration.
    def visitModifier_declaration(self, ctx:openscenario2Parser.Modifier_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#modifier_name.
    def visitModifier_name(self, ctx:openscenario2Parser.Modifier_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#global_parameter_declaration.
    def visitGlobal_parameter_declaration(self, ctx:openscenario2Parser.Global_parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#type_extension.
    def visitType_extension(self, ctx:openscenario2Parser.Type_extensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#enum_type_extension.
    def visitEnum_type_extension(self, ctx:openscenario2Parser.Enum_type_extensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#structured_type_extension.
    def visitStructured_type_extension(self, ctx:openscenario2Parser.Structured_type_extensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#extendable_type_name.
    def visitExtendable_type_name(self, ctx:openscenario2Parser.Extendable_type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#extension_member_decl.
    def visitExtension_member_decl(self, ctx:openscenario2Parser.Extension_member_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#event_declaration.
    def visitEvent_declaration(self, ctx:openscenario2Parser.Event_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#event_specification.
    def visitEvent_specification(self, ctx:openscenario2Parser.Event_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#event_reference.
    def visitEvent_reference(self, ctx:openscenario2Parser.Event_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#event_field_decl.
    def visitEvent_field_decl(self, ctx:openscenario2Parser.Event_field_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#event_field_name.
    def visitEvent_field_name(self, ctx:openscenario2Parser.Event_field_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#event_name.
    def visitEvent_name(self, ctx:openscenario2Parser.Event_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#event_path.
    def visitEvent_path(self, ctx:openscenario2Parser.Event_pathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#event_condition.
    def visitEvent_condition(self, ctx:openscenario2Parser.Event_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#rise_expression.
    def visitRise_expression(self, ctx:openscenario2Parser.Rise_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#fall_expression.
    def visitFall_expression(self, ctx:openscenario2Parser.Fall_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#elapsed_expression.
    def visitElapsed_expression(self, ctx:openscenario2Parser.Elapsed_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#every_expression.
    def visitEvery_expression(self, ctx:openscenario2Parser.Every_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#bool_expression.
    def visitBool_expression(self, ctx:openscenario2Parser.Bool_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#duration_expression.
    def visitDuration_expression(self, ctx:openscenario2Parser.Duration_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#field_declaration.
    def visitField_declaration(self, ctx:openscenario2Parser.Field_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#parameter_declaration.
    def visitParameter_declaration(self, ctx:openscenario2Parser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#variable_declaration.
    def visitVariable_declaration(self, ctx:openscenario2Parser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#sample_expression.
    def visitSample_expression(self, ctx:openscenario2Parser.Sample_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#default_value.
    def visitDefault_value(self, ctx:openscenario2Parser.Default_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#parameter_with_declaration.
    def visitParameter_with_declaration(self, ctx:openscenario2Parser.Parameter_with_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#parameter_with_member.
    def visitParameter_with_member(self, ctx:openscenario2Parser.Parameter_with_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#constraint_declaration.
    def visitConstraint_declaration(self, ctx:openscenario2Parser.Constraint_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#keep_constraint_declaration.
    def visitKeep_constraint_declaration(self, ctx:openscenario2Parser.Keep_constraint_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#constraint_qualifier.
    def visitConstraint_qualifier(self, ctx:openscenario2Parser.Constraint_qualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#constraint_expression.
    def visitConstraint_expression(self, ctx:openscenario2Parser.Constraint_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#remove_default_declaration.
    def visitRemove_default_declaration(self, ctx:openscenario2Parser.Remove_default_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#parameter_reference.
    def visitParameter_reference(self, ctx:openscenario2Parser.Parameter_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#method_declaration.
    def visitMethod_declaration(self, ctx:openscenario2Parser.Method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#return_type.
    def visitReturn_type(self, ctx:openscenario2Parser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#method_implementation.
    def visitMethod_implementation(self, ctx:openscenario2Parser.Method_implementationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#method_qualifier.
    def visitMethod_qualifier(self, ctx:openscenario2Parser.Method_qualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#method_name.
    def visitMethod_name(self, ctx:openscenario2Parser.Method_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#coverage_declaration.
    def visitCoverage_declaration(self, ctx:openscenario2Parser.Coverage_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#modifier_application.
    def visitModifier_application(self, ctx:openscenario2Parser.Modifier_applicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#behavior_specification.
    def visitBehavior_specification(self, ctx:openscenario2Parser.Behavior_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#on_directive.
    def visitOn_directive(self, ctx:openscenario2Parser.On_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#on_member.
    def visitOn_member(self, ctx:openscenario2Parser.On_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#do_directive.
    def visitDo_directive(self, ctx:openscenario2Parser.Do_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#do_member.
    def visitDo_member(self, ctx:openscenario2Parser.Do_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#label_name.
    def visitLabel_name(self, ctx:openscenario2Parser.Label_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#composition.
    def visitComposition(self, ctx:openscenario2Parser.CompositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#composition_operator.
    def visitComposition_operator(self, ctx:openscenario2Parser.Composition_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#behavior_invocation.
    def visitBehavior_invocation(self, ctx:openscenario2Parser.Behavior_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#behavior_with_declaration.
    def visitBehavior_with_declaration(self, ctx:openscenario2Parser.Behavior_with_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#behavior_with_member.
    def visitBehavior_with_member(self, ctx:openscenario2Parser.Behavior_with_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#actor_expression.
    def visitActor_expression(self, ctx:openscenario2Parser.Actor_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#wait_directive.
    def visitWait_directive(self, ctx:openscenario2Parser.Wait_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#emit_directive.
    def visitEmit_directive(self, ctx:openscenario2Parser.Emit_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#call_directive.
    def visitCall_directive(self, ctx:openscenario2Parser.Call_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#method_invocation.
    def visitMethod_invocation(self, ctx:openscenario2Parser.Method_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#until_directive.
    def visitUntil_directive(self, ctx:openscenario2Parser.Until_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#argument_list_specification.
    def visitArgument_list_specification(self, ctx:openscenario2Parser.Argument_list_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#argument_specification.
    def visitArgument_specification(self, ctx:openscenario2Parser.Argument_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#argument_name.
    def visitArgument_name(self, ctx:openscenario2Parser.Argument_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#argument_list.
    def visitArgument_list(self, ctx:openscenario2Parser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#positional_argument.
    def visitPositional_argument(self, ctx:openscenario2Parser.Positional_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#named_argument.
    def visitNamed_argument(self, ctx:openscenario2Parser.Named_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#unqualified_argument_list.
    def visitUnqualified_argument_list(self, ctx:openscenario2Parser.Unqualified_argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#unqualified_argument_name.
    def visitUnqualified_argument_name(self, ctx:openscenario2Parser.Unqualified_argument_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#unqualified_named_argument.
    def visitUnqualified_named_argument(self, ctx:openscenario2Parser.Unqualified_named_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#expression.
    def visitExpression(self, ctx:openscenario2Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#ternary_op_exp.
    def visitTernary_op_exp(self, ctx:openscenario2Parser.Ternary_op_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#implication.
    def visitImplication(self, ctx:openscenario2Parser.ImplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#disjunction.
    def visitDisjunction(self, ctx:openscenario2Parser.DisjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#conjunction.
    def visitConjunction(self, ctx:openscenario2Parser.ConjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#inversion.
    def visitInversion(self, ctx:openscenario2Parser.InversionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#relation.
    def visitRelation(self, ctx:openscenario2Parser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#relational_op.
    def visitRelational_op(self, ctx:openscenario2Parser.Relational_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#sum_exp.
    def visitSum_exp(self, ctx:openscenario2Parser.Sum_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#additive_op.
    def visitAdditive_op(self, ctx:openscenario2Parser.Additive_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#term.
    def visitTerm(self, ctx:openscenario2Parser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#multiplicative_op.
    def visitMultiplicative_op(self, ctx:openscenario2Parser.Multiplicative_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#factor.
    def visitFactor(self, ctx:openscenario2Parser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#type_test_exp_pe.
    def visitType_test_exp_pe(self, ctx:openscenario2Parser.Type_test_exp_peContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#cast_exp_pe.
    def visitCast_exp_pe(self, ctx:openscenario2Parser.Cast_exp_peContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#primary_exp_pe.
    def visitPrimary_exp_pe(self, ctx:openscenario2Parser.Primary_exp_peContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#field_access_pe.
    def visitField_access_pe(self, ctx:openscenario2Parser.Field_access_peContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#element_access_pe.
    def visitElement_access_pe(self, ctx:openscenario2Parser.Element_access_peContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#function_application_pe.
    def visitFunction_application_pe(self, ctx:openscenario2Parser.Function_application_peContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#field_access.
    def visitField_access(self, ctx:openscenario2Parser.Field_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#primary_exp.
    def visitPrimary_exp(self, ctx:openscenario2Parser.Primary_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#value_exp.
    def visitValue_exp(self, ctx:openscenario2Parser.Value_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#list_constructor.
    def visitList_constructor(self, ctx:openscenario2Parser.List_constructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#range_constructor.
    def visitRange_constructor(self, ctx:openscenario2Parser.Range_constructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#string_literal.
    def visitString_literal(self, ctx:openscenario2Parser.String_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#bool_literal.
    def visitBool_literal(self, ctx:openscenario2Parser.Bool_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#integer_literal.
    def visitInteger_literal(self, ctx:openscenario2Parser.Integer_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#uint_literal.
    def visitUint_literal(self, ctx:openscenario2Parser.Uint_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#hex_uint_literal.
    def visitHex_uint_literal(self, ctx:openscenario2Parser.Hex_uint_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#float_literal.
    def visitFloat_literal(self, ctx:openscenario2Parser.Float_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#identifier.
    def visitIdentifier(self, ctx:openscenario2Parser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#qualified_identifier.
    def visitQualified_identifier(self, ctx:openscenario2Parser.Qualified_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#prefixed_identifier.
    def visitPrefixed_identifier(self, ctx:openscenario2Parser.Prefixed_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#physical_literal.
    def visitPhysical_literal(self, ctx:openscenario2Parser.Physical_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by openscenario2Parser#unit_name.
    def visitUnit_name(self, ctx:openscenario2Parser.Unit_nameContext):
        return self.visitChildren(ctx)



del openscenario2Parser