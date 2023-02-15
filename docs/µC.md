
# Programmation d'un microcontrôleur en SI et NSI

![bbc-microbit gif](../images/bbc-microbit.gif){align=left width=40%}
Les microcontroleurs, aujourd'hui on les trouve partout, ce sont les puces électroniques programmables qui rendent nos objets connectés "intelligents".

**La programmation d'une carte à microcontrôleur telle que la BBC micro:bit présentée ci-contre est donc devenue une des compétences essentielles pour un ingénieur !**

==Pour constituer votre clé d'échappement, il va vous falloir modifier le programme en langage Python implanté dans cette carte...==

***

???+ example "Expérimentation"

    ## Etape n°1

    A l'adresse [https://python.microbit.org](https://python.microbit.org/v/3){target=_blank} :

    === "Solution n°1"

        - copier/coller le code ci-dessous pour remplacer le code initial.

    === "Solution n°2"

        - cliquer sur [ce bouton](../Feu_artifice.hex){ .md-button .md-button--primary target=_blank} pour télécharger le code, puis cliquer sur le bouton `Ouvrir` et selectionner le fichier `Feu_artifice.hex` dans le dossier des téléchargements.



    ```python
    # Dépendances
    from microbit import *

    # Définitions
    a = Image("00000:00000:00900:00000:00000")
    b = Image("09090:90009:00000:90009:09090")
    c = Image("90009:00000:00000:00000:90009")
    l = Image("00900:09090:90009:09090:00900")
    s = Image("00000:00000:00000:00000:00900")
    t = Image("00000:00900:09090:00900:00000")
    v = Image("00000:00000:00000:00900:00000")

    # Boucle de répétition infinie
    while True:
        display.show(a)
        sleep(500)
        display.show(b)
        sleep(500)
        display.show(c)
        sleep(500)
        display.show(l)
        sleep(500)
        display.show(s)
        sleep(500)
        display.show(t)
        sleep(500)
        display.show(v)
        sleep(500)
        display.clear()
        sleep(1000)
            

    ```

    ## Etape n°2

    Dans la boucle de répétition infinie, réorganiser l'affichage des images désignées par les lettres a, b, c, l, s, t, v de façon à reproduire la séquence d'animation d'un feux d'artifice tel que sur la vidéo suivante :

    <center>
    <iframe title="bbc feu" width="560" height="315" src="https://tube-sciences-technologies.apps.education.fr/videos/embed/b42eccb8-0d25-4e7b-bec0-edd07eecbe4b?loop=1&amp;autoplay=1" frameborder="0" allowfullscreen="" sandbox="allow-same-origin allow-scripts allow-popups"></iframe>
    </center>

    > Essayer progressivement votre programme dans le [simulateur](https://support.microbit.org/support/solutions/articles/19000135210-python-editor-guide#simulator){target=_blank} situé à droite de l'interface.

    ## Etape n°3

    Cliquer sur le bouton `Envoyer vers micro:bit` puis suivre les instructions afin d'expérimenter le bon fonctionnement de votre programme sur une carte réelle.

???- success "Vérification"

    <iframe src="../test_µC.html?embed=true" width="1099" height="778" frameborder="0" allowfullscreen="allowfullscreen"></iframe>