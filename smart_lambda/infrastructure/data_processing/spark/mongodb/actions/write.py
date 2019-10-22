def action(colecao, config):
      colecao.write \
      .option("compression", "zlib") \
      .option("encoding", "UTF-8") \
      .option("header", "false") \
      .option(config.connection) \
      .format("com.mongodb.spark.sql.DefaultSource") \
      .mode(config.savemode) \
      .save()