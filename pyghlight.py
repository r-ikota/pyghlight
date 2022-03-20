#!/usr/bin/env python
# coding: utf-8

import os, subprocess, shutil, argparse
from pygments.lexers import get_lexer_for_filename
from pygments.formatters import LatexFormatter
from pygments import highlight
from tempfile import TemporaryDirectory

#%%
preamble = r"""
\usepackage[
    paperwidth=210truemm,
    paperheight=297truemm,
    top=30truemm,
    bottom=30truemm,
    left=25truemm,
    right=25truemm
]{{geometry}}
"""

#%%

#%%
def build(input_file, output_file=None):

    cwd = os.getcwd()

    input_file_basename = os.path.basename(input_file)
    input_file_root, input_file_ext = os.path.splitext(input_file_basename)

    pdf_file_basename = input_file_root + ".pdf"
    pdf_fpath_to = output_file if output_file else os.path.join(cwd, pdf_file_basename)

    latex_file_basename = input_file_root + ".tex"

    lexer = get_lexer_for_filename(input_file_basename)

    with open(input_file, "r") as f:
        code = f.read()

    latex = highlight(code, lexer, LatexFormatter(preamble=preamble, full=True))

    with TemporaryDirectory() as tmpdir:
        latex_fpath = os.path.join(tmpdir, latex_file_basename)
        pdf_fpath_from = os.path.join(tmpdir, pdf_file_basename)

        with open(latex_fpath, "w") as f:
            f.write(latex)
        subprocess.run(
            [
                "/usr/bin/env",
                "lualatex",
                latex_file_basename,
                "--output-format=pdf",
                "--interaction=batchmode",
            ],
            cwd=tmpdir,
            capture_output=False,
        )
        shutil.move(pdf_fpath_from, pdf_fpath_to)

def main():
    parser = argparse.ArgumentParser(
        description="highlite a given code file and save the result in a pdf file"
    )
    parser.add_argument("input_file", help="a file containing code")
    parser.add_argument("-o", "--out", help="an output file name, optional")
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.out
    build(input_file, output_file)

if __name__ == "__main__":
    main()
