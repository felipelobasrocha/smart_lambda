def action(colecao, tabela):
    colecao.write \
            .option("compression", "zlib") \
            .option("encoding", "UTF-8") \
            .mode("overwrite") \
            .format("orc") \
            .option("header", "false") \
            .insertInto(tabela, overwrite='False')