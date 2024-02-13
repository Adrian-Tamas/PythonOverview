import argparse


def using_keyword_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--name', type=str,
                        required=True,
                        help='A name')
    parser.add_argument('--id', type=str,
                        required=True,
                        help='the id of the user')
    parser.add_argument('--age', type=str,
                        help='the age of the user')
    parser.add_argument('--email', type=str,
                        default="user@email.com",
                        help='A name')
    args = parser.parse_args()

    using_keyword_args(name=args.name,
                       id=args.id,
                       age=args.age,
                       email=args.email)
