Bonjour,

Lorsque j'exécute `app.py`, une erreur apparaît :

    NameError: name 'c' is not defined

La fonction `addition(a, b)` utilise `c` alors que cette variable n'existe pas.  
La ligne suivante pose problème :

    return a + c

Solution attendue : remplacer `c` par `b`.

Merci !
