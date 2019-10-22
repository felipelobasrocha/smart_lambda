class Hive():

    def __init__(self, command):
        self._command = command

    def create(self, collection, table, type_pattern, partition, location, callback):
        return callback(self._create(self._command.CREATE_TABLE, collection, table, type_pattern, partition, location))

    def _create(self, query, collection, table, type_pattern, partition, location):
        query = query.replace("REPLACETABLE", table)
        query = query.replace("REPLACECOLUMN", self._get_fields(collection, type_pattern))
        query = query.replace("REPLACEPARTITION", partition)
        return query.replace("REPLACELOCATION", location)

    def _get_fields(self, collection, type_pattern):
        fields = "("
        for item in collection.schema().fields():
            fields += item.name() + " " + self._get_type(item) + ","
        fields = ")"
        return fields.replace(",)", ")")

    def _get_type(self, field, type_pattern):
        return type_pattern(field.dataType().typeName())