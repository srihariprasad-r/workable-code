from behave import *
from pyspark.sql import types as T

def typeMapping(input):
    type = {'String': T.StringType(),
            'Int' : T.IntegerType(),
            'Float': T.FloatType(),
            'Long': T.LongType() }

    return type[input]

def table_to_spark(spark, table):
    cols = [h.split(':') for h in table.headings]

    schema = T.StructType(
        [T.StructField(name, T.StringType(), False) for (name, type) in cols])
    rows = [row.cells for row in table]
    df = spark.createDataFrame(rows, schema=schema)
    print(df)
    for (name, field_type) in cols:
        df = (
            df
            .withColumn(name, df[name].cast(typeMapping(field_type)))
            .drop(name + "_str")
        )

    return df


@when(u'I do the join business logic')
def step_impl(context):
    df = context.spark.sql("""
        select s.id, s.name as student_name, c.name as subject_name
        from students s
        join subjects c on (s.sid == c.id)
    """)
    df.createOrReplaceTempView("results")


@when(u'I find maximum score in "{table_name}"')
def step_impl(context, table_name):
    df = context.spark.sql(
        "select * from {0}".format(table_name))
    x = df.groupBy().max().collect()[0]


@given(u'a table called "{table_name}" containing')
def step_impl(context, table_name):
    df = table_to_spark(context.spark, context.table)
    df.createOrReplaceTempView(table_name)

@then(u'the table "{table_name}" contains')
def step_impl(context, table_name):
    expected_df = table_to_spark(context.spark, context.table)
    actual_df = context.spark.sql("select * from {0}".format(table_name))

    assert (expected_df.schema == actual_df.schema)
    assert (expected_df.subtract(actual_df).count() == 0)
    assert (actual_df.subtract(expected_df).count() == 0)
