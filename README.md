# pyghlight -- a simple wrapper for pygments to generate a pdf file

## Requirements

lualatex needs to be installed and placed in your command path.

## Install

    python setup.py install

## Install & Uninstall
For unix

    python setup.py install --record files.txt
    cat files.txt | xargs rm -rf

For Windows

    python setup.py install --record files.txt
    Get-Content files.txt | ForEach-Object {Remove-Item $_ -Recurse -Force}

How to use

    pyghlight sample.py

