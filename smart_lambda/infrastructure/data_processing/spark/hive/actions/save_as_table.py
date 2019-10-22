def action(collection, tabela):
    (collection.write
                .option("compression", "zlib")
                .option("encoding", "UTF-8")
                .mode("overwrite")
                .format("orc")
                .saveAsTable(tabela))