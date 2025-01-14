class ProfilerTypeMapping:
    """Useful backend type mapping for building profilers."""

    INT_TYPE_NAMES = [
        "BIGINT",
        "BYTEINT",
        "ByteType()",
        "INT",
        "INT64",
        "INTEGER",
        "Int16Dtype",
        "Int32Dtype",
        "Int64Dtype",
        "Int8Dtype",
        "IntegerType",
        "IntegerType()",
        "LongType",
        "LongType()",
        "SMALLINT",
        "ShortType()",
        "TINYINT",
        "UInt16Dtype",
        "UInt32Dtype",
        "UInt64Dtype",
        "UInt8Dtype",
        "int",
        "int16",
        "int32",
        "int64",
        "int8",
        "int_",
        "integer",
        "uint16",
        "uint32",
        "uint64",
        "uint8",
    ]
    FLOAT_TYPE_NAMES = [
        "DECIMAL",
        "DOUBLE",
        "DOUBLE_PRECISION",
        "DecimalType()",
        "DoubleType",
        "DoubleType()",
        "FLOAT",
        "FLOAT4",
        "FLOAT64",
        "FLOAT8",
        "FloatType",
        "FloatType()",
        "NUMERIC",
        "REAL",
        "float",
        "float16",
        "float32",
        "float64",
        "float_",
        "number",
    ]
    STRING_TYPE_NAMES = [
        "CHAR",
        "NCHAR",
        "NTEXT",
        "NVARCHAR",
        "STRING",
        "StringType",
        "StringType()",
        "TEXT",
        "VARCHAR",
        "dtype('O')",
        "object",
        "str",
        "string",
    ]
    BOOLEAN_TYPE_NAMES = [
        "BIT",
        "BOOL",
        "BOOLEAN",
        "BooleanType",
        "BooleanType()",
        "TINYINT",
        "bool",
        "boolean",
    ]
    DATETIME_TYPE_NAMES = [
        "DATE",
        "TIME",
        "DATETIME",
        "DATETIME2",
        "DATETIME64",
        "SMALLDATETIME",
        "DATETIMEOFFSET",
        "TIMESTAMP",
        "Timestamp",
        "TimestampType",
        "TimestampType()",
        "DateType",
        "DateType()",
        "datetime64",
        "datetime64[ns]",
        "timedelta[ns]",
        "<M8[ns]",
    ]
    BINARY_TYPE_NAMES = [
        "BINARY",
        "BinaryType()",
        "IMAGE",
        "VARBINARY",
        "binary",
        "image",
        "varbinary",
    ]
    CURRENCY_TYPE_NAMES = [
        "MONEY",
        "SMALLMONEY",
        "money",
        "smallmoney",
    ]
    IDENTIFIER_TYPE_NAMES = [
        "UNIQUEIDENTIFIER",
        "uniqueidentifier",
    ]
    MISCELLANEOUS_TYPE_NAMES = [
        "SQL_VARIANT",
        "sql_variant",
    ]
    RECORD_TYPE_NAMES = [
        "JSON",
        "json",
    ]
