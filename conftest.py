import pytest
from lib.Utils import get_spark_session

## Earlier phase:
# @pytest.fixture
# def spark():
#     spark_session = get_spark_session("LOCAL")
#     return spark_session

## Now it works this way:
@pytest.fixture
def spark():
    "Creates spark session"
    spark_session = get_spark_session("LOCAL")
    yield spark_session
    # Unit Test -
    #       Cases Run --> then, next line 
    spark_session.stop()  # this line will execute


@pytest.fixture
def expected_results(spark):
    "Gives the expected results"
    results_schema = "state string, count integer"
    return spark.read \
        .format("csv") \
        .schema(results_schema) \
        .load("data/test_result/state_aggregate.csv")



# AL, 3
# AR, 12
# AZ, 213
# CA, 2012
# CO, 122
# CT, 73
# DC, 42
# DE, 23
# FL, 374
# GA, 169
# HI, 87
# IA, 5
# ID, 9
# IL, 23
# IN, 40
# KS, 29
# KY, 35
# LA, 63
# MA, 113
# MD, 164
# MI, 254
# MN, 39
# MO, 92
# MT, 7
# NC, 150
# ND, 14
# NJ, 219
# NM, 73
# NV, 103
# NY, 775
# OH, 276
# OK, 19
# OR, 119
# PA, 261
# PR, 4771
# RI, 15
# SC, 41
# TN, 104
# TX, 635
# UT, 69
# VA, 136
# WA, 72
# WI, 64
# WV, 16