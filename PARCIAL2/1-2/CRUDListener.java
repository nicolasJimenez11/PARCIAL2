// Generated from CRUD.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CRUDParser}.
 */
public interface CRUDListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CRUDParser#s}.
	 * @param ctx the parse tree
	 */
	void enterS(CRUDParser.SContext ctx);
	/**
	 * Exit a parse tree produced by {@link CRUDParser#s}.
	 * @param ctx the parse tree
	 */
	void exitS(CRUDParser.SContext ctx);
	/**
	 * Enter a parse tree produced by {@link CRUDParser#sentencia}.
	 * @param ctx the parse tree
	 */
	void enterSentencia(CRUDParser.SentenciaContext ctx);
	/**
	 * Exit a parse tree produced by {@link CRUDParser#sentencia}.
	 * @param ctx the parse tree
	 */
	void exitSentencia(CRUDParser.SentenciaContext ctx);
	/**
	 * Enter a parse tree produced by {@link CRUDParser#insertar}.
	 * @param ctx the parse tree
	 */
	void enterInsertar(CRUDParser.InsertarContext ctx);
	/**
	 * Exit a parse tree produced by {@link CRUDParser#insertar}.
	 * @param ctx the parse tree
	 */
	void exitInsertar(CRUDParser.InsertarContext ctx);
	/**
	 * Enter a parse tree produced by {@link CRUDParser#buscar}.
	 * @param ctx the parse tree
	 */
	void enterBuscar(CRUDParser.BuscarContext ctx);
	/**
	 * Exit a parse tree produced by {@link CRUDParser#buscar}.
	 * @param ctx the parse tree
	 */
	void exitBuscar(CRUDParser.BuscarContext ctx);
	/**
	 * Enter a parse tree produced by {@link CRUDParser#actualizar}.
	 * @param ctx the parse tree
	 */
	void enterActualizar(CRUDParser.ActualizarContext ctx);
	/**
	 * Exit a parse tree produced by {@link CRUDParser#actualizar}.
	 * @param ctx the parse tree
	 */
	void exitActualizar(CRUDParser.ActualizarContext ctx);
	/**
	 * Enter a parse tree produced by {@link CRUDParser#eliminar}.
	 * @param ctx the parse tree
	 */
	void enterEliminar(CRUDParser.EliminarContext ctx);
	/**
	 * Exit a parse tree produced by {@link CRUDParser#eliminar}.
	 * @param ctx the parse tree
	 */
	void exitEliminar(CRUDParser.EliminarContext ctx);
	/**
	 * Enter a parse tree produced by {@link CRUDParser#lista}.
	 * @param ctx the parse tree
	 */
	void enterLista(CRUDParser.ListaContext ctx);
	/**
	 * Exit a parse tree produced by {@link CRUDParser#lista}.
	 * @param ctx the parse tree
	 */
	void exitLista(CRUDParser.ListaContext ctx);
	/**
	 * Enter a parse tree produced by {@link CRUDParser#campo}.
	 * @param ctx the parse tree
	 */
	void enterCampo(CRUDParser.CampoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CRUDParser#campo}.
	 * @param ctx the parse tree
	 */
	void exitCampo(CRUDParser.CampoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CRUDParser#cond}.
	 * @param ctx the parse tree
	 */
	void enterCond(CRUDParser.CondContext ctx);
	/**
	 * Exit a parse tree produced by {@link CRUDParser#cond}.
	 * @param ctx the parse tree
	 */
	void exitCond(CRUDParser.CondContext ctx);
	/**
	 * Enter a parse tree produced by {@link CRUDParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterExpresion(CRUDParser.ExpresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CRUDParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitExpresion(CRUDParser.ExpresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CRUDParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(CRUDParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link CRUDParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(CRUDParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link CRUDParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(CRUDParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CRUDParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(CRUDParser.FactorContext ctx);
}