python -m pip install PEP517 PIP SetUpTools Wheel --upgrade

python -m pip install -e ".[build, dev, doc, gpu, lint, publish, test, viz]" --upgrade --user
