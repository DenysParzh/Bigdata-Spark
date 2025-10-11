import findspark

from core import session
from task_1 import count_words

findspark.init()


def main():
    spark_session = session.build()
    spark_context = spark_session.sparkContext

    text_resources = spark_context.textFile("*.txt")

    count_words(text_resources)


if __name__ == "__main__":
    main()
