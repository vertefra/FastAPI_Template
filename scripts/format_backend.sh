set +x

echo "Isort formatting..."
isort backend/**/*.py 
echo "autopep8 formatting..."
autopep8 --in-place --aggressive --aggressive backend/**/*.py