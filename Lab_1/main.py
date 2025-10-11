import findspark

from core import session
from task_1 import count_words
from task_2 import inverted_index

findspark.init()


def main():
    spark_session = session.build()
    spark_context = spark_session.sparkContext

    text1 = spark_context.textFile("*.txt")
    count_words(text1)

    text2 = spark_context.wholeTextFiles("*.txt")
    inverted_index(text2)


if __name__ == "__main__":
    main()
