from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from newpipeline01.config.ConfigStore import *
from newpipeline01.udfs.UDFs import *
from prophecy.utils import *
from newpipeline01.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Filter_1 = Filter_1(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/NEwPipeline01")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/NEwPipeline01", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/NEwPipeline01")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
