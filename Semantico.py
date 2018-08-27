from ANTLR.LAVisitor import *
from ANTLR.LAParser import *


class Semantico(LAVisitor):

    def visitPrograma(self, ctx: LAParser.ProgramaContext):
        print(ctx.getText())
