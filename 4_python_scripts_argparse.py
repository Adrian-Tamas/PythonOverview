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
                        help='the email of the user')
    args = parser.parse_args()

    using_keyword_args(name=args.name,
                       id=args.id,
                       age=args.age,
                       email=args.email)


# run from command line
#  python 4_python_scripts_argparse.py --help
#  python 4_python_scripts_argparse.py --name Adrian --id 32
# python 4_python_scripts_argparse.py --name Adrian --id 32 --age 39 --email adi@email.com
