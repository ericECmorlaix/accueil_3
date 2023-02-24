
# Cryptographie en NSI

![jull](../images/jull.png){width=33% align=left}
## Le chiffre de César

Le chiffre de César est une méthode de chiffrement consistant à décaler les lettres de l'alphabet de quelques rangs. On nomme ce nombre la clé de déchiffrement.

Ici le message secret est :

```markdown
oqlan rkqo wrav pnkqra ha xkj ykza
```

==Pour vous échapper, vous devez le décoder...==

***

???- example "Expérimentation"

    Le plus simple serait de connaitre la clé du décalage utilisé ici.

    Mais, pour éviter qu'une personne malveillante ne vole notre code de sécurité, nous vous donnons plutôt 2 indices de décryptage :


    === "**Indice n°1 :**"

        - Quelle est la lettre la plus fréquente dans la langue française ? 

    === "**Indice n°2 :**"
        
        - Les œufs sont pourris.

    **Deviner** la clé de décalage pour **déchiffrer** chaque lettre du message secret...

???- success "Vérification"

    <iframe src="../test_crypto.html?embed=true" width="1100" height="400" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

--8<-- "sorties.md"