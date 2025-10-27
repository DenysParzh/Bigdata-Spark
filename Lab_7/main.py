from core.utils import load_vocabulary
from infrastructure import build_dataloader


def base_test(fulltext):
    dataloader = build_dataloader(fulltext,
                                  batch_size=1,
                                  stride=1,
                                  max_length=4,
                                  shuffle=False)

    data_iter = iter(dataloader)

    input_01, target_01 = next(data_iter)
    input_02, target_02 = next(data_iter)

    print("First batch: ")
    print(input_01)
    print(target_01)

    print("\nSecond batch: ")
    print(input_02)
    print(target_02)


def test01(fulltext):
    dataloader = build_dataloader(fulltext,
                                  batch_size=2,
                                  stride=2,
                                  max_length=2,
                                  shuffle=False)

    data_iter = iter(dataloader)

    input_01, target_01 = next(data_iter)
    input_02, target_02 = next(data_iter)

    print("\nFirst batch: ")
    print(input_01)
    print(target_01)

    print("\nSecond batch: ")
    print(input_02)
    print(target_02)


def test02(fulltext):
    dataloader = build_dataloader(fulltext,
                                  batch_size=4,
                                  stride=4,
                                  max_length=8,
                                  shuffle=False)

    data_iter = iter(dataloader)

    input_01, target_01 = next(data_iter)
    input_02, target_02 = next(data_iter)

    print("\nFirst batch: ")
    print(input_01)
    print(target_01)

    print("\nSecond batch: ")
    print(input_02)
    print(target_02)


def main():
    fulltext = load_vocabulary("../Lab_5/the-verdict.txt")
    base_test(fulltext)
    test01(fulltext)
    test02(fulltext)


if __name__ == "__main__":
    main()
