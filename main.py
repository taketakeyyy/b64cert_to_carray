# -*- coding:utf-8 -*-
import base64

def read_input():
    with open("input.txt", encoding="utf-8") as f:
        s = f.read()
    return s


def decode(s):
    return base64.b64decode(s)


def make_str(byts):
    NUM = 12  # 1行あたりの数
    ans = "unsigned char cert[] = {\n"

    line = ""
    for i, b in enumerate(byts):
        if (i+1)%NUM==1:
            line += "  "
        else:
            line += " "

        line += format(b, "#04x") + ","

        if (i+1)%NUM==0:
            ans += line + "\n"
            line = ""
    ans += line[:-1]
    ans += "\n"
    ans += "};\n"
    ans += f"unsigned int cert_len = {i+1};\n"

    return ans

def write_output(s):
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(s)


if __name__ == "__main__":
    s = read_input()

    byts = decode(s)

    s = make_str(byts)

    write_output(s)
