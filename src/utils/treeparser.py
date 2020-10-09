import re
import argparse
import os


def parse_tree(lines, indentation):
    stack = []
    for i, line in enumerate(lines):
        if line.strip().startswith("#"):
            continue
        elif line.strip().startswith("echo"):
            continue
        elif line.strip().startswith("exit"):
            continue
        elif not line.strip():
            continue
        line = line.rstrip()
        indent = len(line) - len(line.strip())
        pattern = "^(?P<indent>(?: {%s})*)(?P<name>\S.*)" % indent
        regex = re.compile(r"{}".format(pattern))
        match = regex.match(line)
        if not match:
            raise ValueError(
                f'Indentation is not right on line number {i}: "{line}"'
            )

        level = len(match.group("indent")) // indentation

        if level > len(stack):
            raise ValueError(
                f'Indentation too deep on line number {i}: "{line}"'
            )
        stack[level:] = [match.group("name")]
        yield stack


def treeparser(file_input, file_output, indentation=4):
    with open(file_input) as fin:
        with open(file_output, "w") as fout:
            for stack in parse_tree(fin, indentation):
                fout.write(("/{}{}".format(" ".join(stack), "\n")))
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--indentation",
        type=int,
        help="Type indentation space count (Default=4)",
    )
    parser.add_argument(
        "-fin",
        "--file_input",
        help="Type path to file input (original configuration from CMG)",
    )
    parser.add_argument(
        "-fout",
        "--file_output",
        help="Type path to file output (Configuration in tree format)",
    )

    args = parser.parse_args()

    file_input = os.path.abspath(args.file_input)
    file_output = os.path.abspath(args.file_output)
    indentation = int(args.indentation) if args.indentation else 4

    treeparser(file_input, file_output, indentation)
