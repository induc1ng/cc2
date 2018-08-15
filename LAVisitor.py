# Generated from LA.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LAParser import LAParser
else:
    from LAParser import LAParser

# This class defines a complete generic visitor for a parse tree produced by LAParser.

class LAVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LAParser#programa.
    def visitPrograma(self, ctx:LAParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#declaracoes.
    def visitDeclaracoes(self, ctx:LAParser.DeclaracoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#decl_local_global.
    def visitDecl_local_global(self, ctx:LAParser.Decl_local_globalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#declaracao_local.
    def visitDeclaracao_local(self, ctx:LAParser.Declaracao_localContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#variavel.
    def visitVariavel(self, ctx:LAParser.VariavelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#mais_var.
    def visitMais_var(self, ctx:LAParser.Mais_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#identificador.
    def visitIdentificador(self, ctx:LAParser.IdentificadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#ponteiros_opcionais.
    def visitPonteiros_opcionais(self, ctx:LAParser.Ponteiros_opcionaisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#outros_ident.
    def visitOutros_ident(self, ctx:LAParser.Outros_identContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#dimensao.
    def visitDimensao(self, ctx:LAParser.DimensaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#tipo.
    def visitTipo(self, ctx:LAParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#mais_ident.
    def visitMais_ident(self, ctx:LAParser.Mais_identContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#mais_variaveis.
    def visitMais_variaveis(self, ctx:LAParser.Mais_variaveisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#tipo_basico.
    def visitTipo_basico(self, ctx:LAParser.Tipo_basicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#tipo_basico_ident.
    def visitTipo_basico_ident(self, ctx:LAParser.Tipo_basico_identContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#tipo_estendido.
    def visitTipo_estendido(self, ctx:LAParser.Tipo_estendidoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#valor_constante.
    def visitValor_constante(self, ctx:LAParser.Valor_constanteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#registro.
    def visitRegistro(self, ctx:LAParser.RegistroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#declaracao_global.
    def visitDeclaracao_global(self, ctx:LAParser.Declaracao_globalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#parametros_opcional.
    def visitParametros_opcional(self, ctx:LAParser.Parametros_opcionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#parametro.
    def visitParametro(self, ctx:LAParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#var_opcional.
    def visitVar_opcional(self, ctx:LAParser.Var_opcionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#mais_parametros.
    def visitMais_parametros(self, ctx:LAParser.Mais_parametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#declaracoes_locais.
    def visitDeclaracoes_locais(self, ctx:LAParser.Declaracoes_locaisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#corpo.
    def visitCorpo(self, ctx:LAParser.CorpoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#comandos.
    def visitComandos(self, ctx:LAParser.ComandosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#cmd.
    def visitCmd(self, ctx:LAParser.CmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#mais_expressao.
    def visitMais_expressao(self, ctx:LAParser.Mais_expressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#senao_opcional.
    def visitSenao_opcional(self, ctx:LAParser.Senao_opcionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#chamada_atribuicao.
    def visitChamada_atribuicao(self, ctx:LAParser.Chamada_atribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#argumentos_opcional.
    def visitArgumentos_opcional(self, ctx:LAParser.Argumentos_opcionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#selecao.
    def visitSelecao(self, ctx:LAParser.SelecaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#mais_selecao.
    def visitMais_selecao(self, ctx:LAParser.Mais_selecaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#constantes.
    def visitConstantes(self, ctx:LAParser.ConstantesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#mais_constantes.
    def visitMais_constantes(self, ctx:LAParser.Mais_constantesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#numero_intervalo.
    def visitNumero_intervalo(self, ctx:LAParser.Numero_intervaloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#intervalo_opcional.
    def visitIntervalo_opcional(self, ctx:LAParser.Intervalo_opcionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#op_unario.
    def visitOp_unario(self, ctx:LAParser.Op_unarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#exp_aritmetica.
    def visitExp_aritmetica(self, ctx:LAParser.Exp_aritmeticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#op_multiplicacao.
    def visitOp_multiplicacao(self, ctx:LAParser.Op_multiplicacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#op_adicao.
    def visitOp_adicao(self, ctx:LAParser.Op_adicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#termo.
    def visitTermo(self, ctx:LAParser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#outros_termos.
    def visitOutros_termos(self, ctx:LAParser.Outros_termosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#fator.
    def visitFator(self, ctx:LAParser.FatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#outros_fatores.
    def visitOutros_fatores(self, ctx:LAParser.Outros_fatoresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#parcela.
    def visitParcela(self, ctx:LAParser.ParcelaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#parcela_unario.
    def visitParcela_unario(self, ctx:LAParser.Parcela_unarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#parcela_nao_unario.
    def visitParcela_nao_unario(self, ctx:LAParser.Parcela_nao_unarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#outras_parcelas.
    def visitOutras_parcelas(self, ctx:LAParser.Outras_parcelasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#chamada_partes.
    def visitChamada_partes(self, ctx:LAParser.Chamada_partesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#exp_relacional.
    def visitExp_relacional(self, ctx:LAParser.Exp_relacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#op_opcional.
    def visitOp_opcional(self, ctx:LAParser.Op_opcionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#op_relacional.
    def visitOp_relacional(self, ctx:LAParser.Op_relacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#expressao.
    def visitExpressao(self, ctx:LAParser.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#op_nao.
    def visitOp_nao(self, ctx:LAParser.Op_naoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#termo_logico.
    def visitTermo_logico(self, ctx:LAParser.Termo_logicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#outros_termos_logicos.
    def visitOutros_termos_logicos(self, ctx:LAParser.Outros_termos_logicosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#outros_fatores_logicos.
    def visitOutros_fatores_logicos(self, ctx:LAParser.Outros_fatores_logicosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#fator_logico.
    def visitFator_logico(self, ctx:LAParser.Fator_logicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LAParser#parcela_logica.
    def visitParcela_logica(self, ctx:LAParser.Parcela_logicaContext):
        return self.visitChildren(ctx)



del LAParser