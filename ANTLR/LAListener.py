# Generated from LA.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LAParser import LAParser
else:
    from LAParser import LAParser

# This class defines a complete listener for a parse tree produced by LAParser.
class LAListener(ParseTreeListener):

    # Enter a parse tree produced by LAParser#programa.
    def enterPrograma(self, ctx:LAParser.ProgramaContext):
        pass

    # Exit a parse tree produced by LAParser#programa.
    def exitPrograma(self, ctx:LAParser.ProgramaContext):
        pass


    # Enter a parse tree produced by LAParser#declaracoes.
    def enterDeclaracoes(self, ctx:LAParser.DeclaracoesContext):
        pass

    # Exit a parse tree produced by LAParser#declaracoes.
    def exitDeclaracoes(self, ctx:LAParser.DeclaracoesContext):
        pass


    # Enter a parse tree produced by LAParser#decl_local_global.
    def enterDecl_local_global(self, ctx:LAParser.Decl_local_globalContext):
        pass

    # Exit a parse tree produced by LAParser#decl_local_global.
    def exitDecl_local_global(self, ctx:LAParser.Decl_local_globalContext):
        pass


    # Enter a parse tree produced by LAParser#declaracao_local.
    def enterDeclaracao_local(self, ctx:LAParser.Declaracao_localContext):
        pass

    # Exit a parse tree produced by LAParser#declaracao_local.
    def exitDeclaracao_local(self, ctx:LAParser.Declaracao_localContext):
        pass


    # Enter a parse tree produced by LAParser#variavel.
    def enterVariavel(self, ctx:LAParser.VariavelContext):
        pass

    # Exit a parse tree produced by LAParser#variavel.
    def exitVariavel(self, ctx:LAParser.VariavelContext):
        pass


    # Enter a parse tree produced by LAParser#mais_var.
    def enterMais_var(self, ctx:LAParser.Mais_varContext):
        pass

    # Exit a parse tree produced by LAParser#mais_var.
    def exitMais_var(self, ctx:LAParser.Mais_varContext):
        pass


    # Enter a parse tree produced by LAParser#identificador.
    def enterIdentificador(self, ctx:LAParser.IdentificadorContext):
        pass

    # Exit a parse tree produced by LAParser#identificador.
    def exitIdentificador(self, ctx:LAParser.IdentificadorContext):
        pass


    # Enter a parse tree produced by LAParser#ponteiros_opcionais.
    def enterPonteiros_opcionais(self, ctx:LAParser.Ponteiros_opcionaisContext):
        pass

    # Exit a parse tree produced by LAParser#ponteiros_opcionais.
    def exitPonteiros_opcionais(self, ctx:LAParser.Ponteiros_opcionaisContext):
        pass


    # Enter a parse tree produced by LAParser#outros_ident.
    def enterOutros_ident(self, ctx:LAParser.Outros_identContext):
        pass

    # Exit a parse tree produced by LAParser#outros_ident.
    def exitOutros_ident(self, ctx:LAParser.Outros_identContext):
        pass


    # Enter a parse tree produced by LAParser#dimensao.
    def enterDimensao(self, ctx:LAParser.DimensaoContext):
        pass

    # Exit a parse tree produced by LAParser#dimensao.
    def exitDimensao(self, ctx:LAParser.DimensaoContext):
        pass


    # Enter a parse tree produced by LAParser#tipo.
    def enterTipo(self, ctx:LAParser.TipoContext):
        pass

    # Exit a parse tree produced by LAParser#tipo.
    def exitTipo(self, ctx:LAParser.TipoContext):
        pass


    # Enter a parse tree produced by LAParser#mais_ident.
    def enterMais_ident(self, ctx:LAParser.Mais_identContext):
        pass

    # Exit a parse tree produced by LAParser#mais_ident.
    def exitMais_ident(self, ctx:LAParser.Mais_identContext):
        pass


    # Enter a parse tree produced by LAParser#mais_variaveis.
    def enterMais_variaveis(self, ctx:LAParser.Mais_variaveisContext):
        pass

    # Exit a parse tree produced by LAParser#mais_variaveis.
    def exitMais_variaveis(self, ctx:LAParser.Mais_variaveisContext):
        pass


    # Enter a parse tree produced by LAParser#tipo_basico.
    def enterTipo_basico(self, ctx:LAParser.Tipo_basicoContext):
        pass

    # Exit a parse tree produced by LAParser#tipo_basico.
    def exitTipo_basico(self, ctx:LAParser.Tipo_basicoContext):
        pass


    # Enter a parse tree produced by LAParser#tipo_basico_ident.
    def enterTipo_basico_ident(self, ctx:LAParser.Tipo_basico_identContext):
        pass

    # Exit a parse tree produced by LAParser#tipo_basico_ident.
    def exitTipo_basico_ident(self, ctx:LAParser.Tipo_basico_identContext):
        pass


    # Enter a parse tree produced by LAParser#tipo_estendido.
    def enterTipo_estendido(self, ctx:LAParser.Tipo_estendidoContext):
        pass

    # Exit a parse tree produced by LAParser#tipo_estendido.
    def exitTipo_estendido(self, ctx:LAParser.Tipo_estendidoContext):
        pass


    # Enter a parse tree produced by LAParser#valor_constante.
    def enterValor_constante(self, ctx:LAParser.Valor_constanteContext):
        pass

    # Exit a parse tree produced by LAParser#valor_constante.
    def exitValor_constante(self, ctx:LAParser.Valor_constanteContext):
        pass


    # Enter a parse tree produced by LAParser#registro.
    def enterRegistro(self, ctx:LAParser.RegistroContext):
        pass

    # Exit a parse tree produced by LAParser#registro.
    def exitRegistro(self, ctx:LAParser.RegistroContext):
        pass


    # Enter a parse tree produced by LAParser#declaracao_global.
    def enterDeclaracao_global(self, ctx:LAParser.Declaracao_globalContext):
        pass

    # Exit a parse tree produced by LAParser#declaracao_global.
    def exitDeclaracao_global(self, ctx:LAParser.Declaracao_globalContext):
        pass


    # Enter a parse tree produced by LAParser#parametros_opcional.
    def enterParametros_opcional(self, ctx:LAParser.Parametros_opcionalContext):
        pass

    # Exit a parse tree produced by LAParser#parametros_opcional.
    def exitParametros_opcional(self, ctx:LAParser.Parametros_opcionalContext):
        pass


    # Enter a parse tree produced by LAParser#parametro.
    def enterParametro(self, ctx:LAParser.ParametroContext):
        pass

    # Exit a parse tree produced by LAParser#parametro.
    def exitParametro(self, ctx:LAParser.ParametroContext):
        pass


    # Enter a parse tree produced by LAParser#var_opcional.
    def enterVar_opcional(self, ctx:LAParser.Var_opcionalContext):
        pass

    # Exit a parse tree produced by LAParser#var_opcional.
    def exitVar_opcional(self, ctx:LAParser.Var_opcionalContext):
        pass


    # Enter a parse tree produced by LAParser#mais_parametros.
    def enterMais_parametros(self, ctx:LAParser.Mais_parametrosContext):
        pass

    # Exit a parse tree produced by LAParser#mais_parametros.
    def exitMais_parametros(self, ctx:LAParser.Mais_parametrosContext):
        pass


    # Enter a parse tree produced by LAParser#declaracoes_locais.
    def enterDeclaracoes_locais(self, ctx:LAParser.Declaracoes_locaisContext):
        pass

    # Exit a parse tree produced by LAParser#declaracoes_locais.
    def exitDeclaracoes_locais(self, ctx:LAParser.Declaracoes_locaisContext):
        pass


    # Enter a parse tree produced by LAParser#corpo.
    def enterCorpo(self, ctx:LAParser.CorpoContext):
        pass

    # Exit a parse tree produced by LAParser#corpo.
    def exitCorpo(self, ctx:LAParser.CorpoContext):
        pass


    # Enter a parse tree produced by LAParser#comandos.
    def enterComandos(self, ctx:LAParser.ComandosContext):
        pass

    # Exit a parse tree produced by LAParser#comandos.
    def exitComandos(self, ctx:LAParser.ComandosContext):
        pass


    # Enter a parse tree produced by LAParser#cmd.
    def enterCmd(self, ctx:LAParser.CmdContext):
        pass

    # Exit a parse tree produced by LAParser#cmd.
    def exitCmd(self, ctx:LAParser.CmdContext):
        pass


    # Enter a parse tree produced by LAParser#mais_expressao.
    def enterMais_expressao(self, ctx:LAParser.Mais_expressaoContext):
        pass

    # Exit a parse tree produced by LAParser#mais_expressao.
    def exitMais_expressao(self, ctx:LAParser.Mais_expressaoContext):
        pass


    # Enter a parse tree produced by LAParser#senao_opcional.
    def enterSenao_opcional(self, ctx:LAParser.Senao_opcionalContext):
        pass

    # Exit a parse tree produced by LAParser#senao_opcional.
    def exitSenao_opcional(self, ctx:LAParser.Senao_opcionalContext):
        pass


    # Enter a parse tree produced by LAParser#chamada_atribuicao.
    def enterChamada_atribuicao(self, ctx:LAParser.Chamada_atribuicaoContext):
        pass

    # Exit a parse tree produced by LAParser#chamada_atribuicao.
    def exitChamada_atribuicao(self, ctx:LAParser.Chamada_atribuicaoContext):
        pass


    # Enter a parse tree produced by LAParser#argumentos_opcional.
    def enterArgumentos_opcional(self, ctx:LAParser.Argumentos_opcionalContext):
        pass

    # Exit a parse tree produced by LAParser#argumentos_opcional.
    def exitArgumentos_opcional(self, ctx:LAParser.Argumentos_opcionalContext):
        pass


    # Enter a parse tree produced by LAParser#selecao.
    def enterSelecao(self, ctx:LAParser.SelecaoContext):
        pass

    # Exit a parse tree produced by LAParser#selecao.
    def exitSelecao(self, ctx:LAParser.SelecaoContext):
        pass


    # Enter a parse tree produced by LAParser#mais_selecao.
    def enterMais_selecao(self, ctx:LAParser.Mais_selecaoContext):
        pass

    # Exit a parse tree produced by LAParser#mais_selecao.
    def exitMais_selecao(self, ctx:LAParser.Mais_selecaoContext):
        pass


    # Enter a parse tree produced by LAParser#constantes.
    def enterConstantes(self, ctx:LAParser.ConstantesContext):
        pass

    # Exit a parse tree produced by LAParser#constantes.
    def exitConstantes(self, ctx:LAParser.ConstantesContext):
        pass


    # Enter a parse tree produced by LAParser#mais_constantes.
    def enterMais_constantes(self, ctx:LAParser.Mais_constantesContext):
        pass

    # Exit a parse tree produced by LAParser#mais_constantes.
    def exitMais_constantes(self, ctx:LAParser.Mais_constantesContext):
        pass


    # Enter a parse tree produced by LAParser#numero_intervalo.
    def enterNumero_intervalo(self, ctx:LAParser.Numero_intervaloContext):
        pass

    # Exit a parse tree produced by LAParser#numero_intervalo.
    def exitNumero_intervalo(self, ctx:LAParser.Numero_intervaloContext):
        pass


    # Enter a parse tree produced by LAParser#intervalo_opcional.
    def enterIntervalo_opcional(self, ctx:LAParser.Intervalo_opcionalContext):
        pass

    # Exit a parse tree produced by LAParser#intervalo_opcional.
    def exitIntervalo_opcional(self, ctx:LAParser.Intervalo_opcionalContext):
        pass


    # Enter a parse tree produced by LAParser#op_unario.
    def enterOp_unario(self, ctx:LAParser.Op_unarioContext):
        pass

    # Exit a parse tree produced by LAParser#op_unario.
    def exitOp_unario(self, ctx:LAParser.Op_unarioContext):
        pass


    # Enter a parse tree produced by LAParser#exp_aritmetica.
    def enterExp_aritmetica(self, ctx:LAParser.Exp_aritmeticaContext):
        pass

    # Exit a parse tree produced by LAParser#exp_aritmetica.
    def exitExp_aritmetica(self, ctx:LAParser.Exp_aritmeticaContext):
        pass


    # Enter a parse tree produced by LAParser#op_multiplicacao.
    def enterOp_multiplicacao(self, ctx:LAParser.Op_multiplicacaoContext):
        pass

    # Exit a parse tree produced by LAParser#op_multiplicacao.
    def exitOp_multiplicacao(self, ctx:LAParser.Op_multiplicacaoContext):
        pass


    # Enter a parse tree produced by LAParser#op_adicao.
    def enterOp_adicao(self, ctx:LAParser.Op_adicaoContext):
        pass

    # Exit a parse tree produced by LAParser#op_adicao.
    def exitOp_adicao(self, ctx:LAParser.Op_adicaoContext):
        pass


    # Enter a parse tree produced by LAParser#termo.
    def enterTermo(self, ctx:LAParser.TermoContext):
        pass

    # Exit a parse tree produced by LAParser#termo.
    def exitTermo(self, ctx:LAParser.TermoContext):
        pass


    # Enter a parse tree produced by LAParser#outros_termos.
    def enterOutros_termos(self, ctx:LAParser.Outros_termosContext):
        pass

    # Exit a parse tree produced by LAParser#outros_termos.
    def exitOutros_termos(self, ctx:LAParser.Outros_termosContext):
        pass


    # Enter a parse tree produced by LAParser#fator.
    def enterFator(self, ctx:LAParser.FatorContext):
        pass

    # Exit a parse tree produced by LAParser#fator.
    def exitFator(self, ctx:LAParser.FatorContext):
        pass


    # Enter a parse tree produced by LAParser#outros_fatores.
    def enterOutros_fatores(self, ctx:LAParser.Outros_fatoresContext):
        pass

    # Exit a parse tree produced by LAParser#outros_fatores.
    def exitOutros_fatores(self, ctx:LAParser.Outros_fatoresContext):
        pass


    # Enter a parse tree produced by LAParser#parcela.
    def enterParcela(self, ctx:LAParser.ParcelaContext):
        pass

    # Exit a parse tree produced by LAParser#parcela.
    def exitParcela(self, ctx:LAParser.ParcelaContext):
        pass


    # Enter a parse tree produced by LAParser#parcela_unario.
    def enterParcela_unario(self, ctx:LAParser.Parcela_unarioContext):
        pass

    # Exit a parse tree produced by LAParser#parcela_unario.
    def exitParcela_unario(self, ctx:LAParser.Parcela_unarioContext):
        pass


    # Enter a parse tree produced by LAParser#parcela_nao_unario.
    def enterParcela_nao_unario(self, ctx:LAParser.Parcela_nao_unarioContext):
        pass

    # Exit a parse tree produced by LAParser#parcela_nao_unario.
    def exitParcela_nao_unario(self, ctx:LAParser.Parcela_nao_unarioContext):
        pass


    # Enter a parse tree produced by LAParser#outras_parcelas.
    def enterOutras_parcelas(self, ctx:LAParser.Outras_parcelasContext):
        pass

    # Exit a parse tree produced by LAParser#outras_parcelas.
    def exitOutras_parcelas(self, ctx:LAParser.Outras_parcelasContext):
        pass


    # Enter a parse tree produced by LAParser#chamada_partes.
    def enterChamada_partes(self, ctx:LAParser.Chamada_partesContext):
        pass

    # Exit a parse tree produced by LAParser#chamada_partes.
    def exitChamada_partes(self, ctx:LAParser.Chamada_partesContext):
        pass


    # Enter a parse tree produced by LAParser#exp_relacional.
    def enterExp_relacional(self, ctx:LAParser.Exp_relacionalContext):
        pass

    # Exit a parse tree produced by LAParser#exp_relacional.
    def exitExp_relacional(self, ctx:LAParser.Exp_relacionalContext):
        pass


    # Enter a parse tree produced by LAParser#op_opcional.
    def enterOp_opcional(self, ctx:LAParser.Op_opcionalContext):
        pass

    # Exit a parse tree produced by LAParser#op_opcional.
    def exitOp_opcional(self, ctx:LAParser.Op_opcionalContext):
        pass


    # Enter a parse tree produced by LAParser#op_relacional.
    def enterOp_relacional(self, ctx:LAParser.Op_relacionalContext):
        pass

    # Exit a parse tree produced by LAParser#op_relacional.
    def exitOp_relacional(self, ctx:LAParser.Op_relacionalContext):
        pass


    # Enter a parse tree produced by LAParser#expressao.
    def enterExpressao(self, ctx:LAParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by LAParser#expressao.
    def exitExpressao(self, ctx:LAParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by LAParser#op_nao.
    def enterOp_nao(self, ctx:LAParser.Op_naoContext):
        pass

    # Exit a parse tree produced by LAParser#op_nao.
    def exitOp_nao(self, ctx:LAParser.Op_naoContext):
        pass


    # Enter a parse tree produced by LAParser#termo_logico.
    def enterTermo_logico(self, ctx:LAParser.Termo_logicoContext):
        pass

    # Exit a parse tree produced by LAParser#termo_logico.
    def exitTermo_logico(self, ctx:LAParser.Termo_logicoContext):
        pass


    # Enter a parse tree produced by LAParser#outros_termos_logicos.
    def enterOutros_termos_logicos(self, ctx:LAParser.Outros_termos_logicosContext):
        pass

    # Exit a parse tree produced by LAParser#outros_termos_logicos.
    def exitOutros_termos_logicos(self, ctx:LAParser.Outros_termos_logicosContext):
        pass


    # Enter a parse tree produced by LAParser#outros_fatores_logicos.
    def enterOutros_fatores_logicos(self, ctx:LAParser.Outros_fatores_logicosContext):
        pass

    # Exit a parse tree produced by LAParser#outros_fatores_logicos.
    def exitOutros_fatores_logicos(self, ctx:LAParser.Outros_fatores_logicosContext):
        pass


    # Enter a parse tree produced by LAParser#fator_logico.
    def enterFator_logico(self, ctx:LAParser.Fator_logicoContext):
        pass

    # Exit a parse tree produced by LAParser#fator_logico.
    def exitFator_logico(self, ctx:LAParser.Fator_logicoContext):
        pass


    # Enter a parse tree produced by LAParser#parcela_logica.
    def enterParcela_logica(self, ctx:LAParser.Parcela_logicaContext):
        pass

    # Exit a parse tree produced by LAParser#parcela_logica.
    def exitParcela_logica(self, ctx:LAParser.Parcela_logicaContext):
        pass


