Documentacion de LinkaForm


Para hacer el build
```
sphinx-build -c /srv/docs/ content/ static/
```


```
docker run --rm -v ${PWD}:/srv/docs linkaform/documentation:latest sphinx-build -c /srv/docs/ content/ build/
```

https://www.sphinx-doc.org/en/master/