# Bienvenu

## Les spécialités scientifiques et technologiques au lycée

- [Numérique et Science Informatique](http://si.lycee.ecmorlaix.fr/nsi/){target=_blank} ;

- [Sciences de l'Ingénieur](http://si.lycee.ecmorlaix.fr/){target=_blank} ;

## Exemple d'activité de programmation d'un BBC micro:bit :

### Mise en situation

![](./images/bbc-microbit.gif){ .center}

???+ info "Kesako ? ..."
    ![](./images/bbc-microbit-revue.png){ align=left width=70% }
    <br>

    BBC micro:bit est un mini-ordinateur programmable de poche (une carte à microcontrôleur) conçu pour développer votre créativité avec la technologie.

    <br>

    Ce petit appareil intègre beaucoup de fonctionnalités : il a 25 LED rouges qui peuvent afficher des messages, et deux boutons programmables pouvant être utilisés pour contrôler des jeux, ou, par exemple, faire une pause et sauter des chansons sur une liste de lecture ;

    Le BBC micro:bit peut détecter le mouvement, la température, la  luminosité, et vous dire dans quelle direction vous vous dirigez ;
    
    Il peut aussi utiliser une connexion Bluetooth à faible énergie pour interagir avec d'autres appareils et Internet.

    ![](./images/bbc-breadbit.png){ align=right width=70%}
    
    <br>
    Ce petit ordinateur possède la dernière technologie qui équipe les appareils modernes : téléphones mobiles, réfrigérateurs, montres intelligentes, alarmes antivol, robots, etc...

    Ainsi, il s'apparente à ce que l'on nomme l'Internet des objets : Internet of Things, abrégé IoT.

    Grâce à la connexion à l'IoT, nous pouvons interagir avec un large éventail de capteurs à travers le monde entier en temps réel et nous pouvons maintenant prendre des décisions intelligentes en utilisant nos appareils.

    <br>
    
    Un micro:bit est à la fois autonome et extensible. En plus d'utiliser ses LED intégrées, boutons et capteurs, nous pouvons élargir sa gamme de fonctions en l'insérant dans un connecteur comme ci-contre.

    Donc finalement, micro:bit est tout ce que vous pouvez imaginer. Vous pouvez le transformer en votre dispositif de messagerie, console de jeu, vêtement intelligent, alarme antivol, contrôleur de maison intelligente...  
    A peu près tout ce que votre imagination peut créer en utilisant des capteurs supplémentaires, en réalisant un boitier ou un support pour la carte, et en programmant son microcontroleur.


???+ info "Historique ..."

    La BBC a initié en 2015 le projet Micro:bit, qui se veut être un nano-ordinateur à carte unique à processeur ARM destiné à l’éducation.  
    L’objectif de cette dernière : fournir à chaque écolier de 12 ans (« year 7 ») un support amusant et facile à utiliser.

    Au début des années 80, le groupe de chaînes publiques au Royaume-Uni, la « British Broadcasting Corporation », dite BBC, lança un appel à projet pour créer un ordinateur éducatif à destination des écoliers et des écoles. Une jeune entreprise de Cambridge « Acorn » (« gland » en anglais) fut retenue pour créer cette plateforme. Le « BBC Micro » était né. Dans la même période, ici en France, nous avons connu une initiative comparable avec le Plan Informatique pour Tous basé sur des micro-ordinateurs Thomson MO5 et TO7.

    Plus récemment, quand les membres fondateurs du Raspberry Pi commencèrent à concrétiser leurs rêves d’un nano-ordinateur éducatif, ils voulurent y inscrire en guise de clin d’œil le label « BBC ». Ce droit ne leur fut pas octroyé ; néanmoins un journaliste high-tech de la célèbre « Corporation » sur son blog et sur la chaîne YouTube leur donna un coup de projecteur qui lancera le mouvement autour du Raspberry Pi.
    
    L’histoire se répète, en 2012, trente ans plus tard, la BBC s’est « remis dans le bain » en lançant un objectif très ambitieux : envisager un « ordinateur de poche programmable permettant aux enfants d’explorer la créativité technologique ». Elle voulait formuler une réponse à la fracture numérique et aux lacunes perçues des compétences informatiques des citoyens. Dans l’environnement fertile des startups technologiques du Royaume Uni et inspiré par l’énergie des « makers » et « programmeurs » autour des cartes « hackables » comme l’Arduino, le Raspberry Pi, Beaglebone et bien d’autres, la BBC a de nouveau monté une initiative d’éducation numérique dans la continuité du projet « Make It Digital » (créer le numérique). Ils ont su rapidement rassembler une trentaine de partenaires et des industriels. Aujourd’hui, ces partenaires sont réunis dans la Fondation Micro:bit.

## WorkFlow d'expérimentation

Il existe différentes façon de programmer la carte BBC micro:bit, ici, nous allons utiliser l'éditeur en ligne [edublocks](https://app.edublocks.org/){target=_blank}

<figure>
<iframe width='1080' height='720' allowfullscreen frameborder='0' style='border:1px #d6d6d6 solid;' src="https://app.edublocks.org/"></iframe>
</figure>

Le principe consiste à glisser/déposer des blocs d'instructions du menu de gauche dans la zone graphique pour obtenir le code Python correspondant.

Pour tester son programme :

- soit on raccorde une carte BBC micro:bit avec un cordon USB au PC et on clique sur le bouton `Connect` puis sur le bouton `Flash` ;
- soit on copie/colle le code en Python dans le simulateur de [create.withcode.uk](https://create.withcode.uk/){target=_blank} et puis on appuye sur la combinaison de touches `Ctrl+Entrée` pour l'exécuter...

<figure>
<iframe width='1080' height='720' allowfullscreen frameborder='0' style='border:1px #d6d6d6 solid;' src="https://create.withcode.uk/"></iframe>
</figure>

> **Autres solutions :**
>
> - [microsoft makecode](https://makecode.microbit.org/){target=_blank}
> - [vittascience](https://fr.vittascience.com/microbit/?mode=mixed&console=bottom&toolbox=vittascience&simu=1){target=_blank}
> - [editeur python microbit](https://python.microbit.org/v/2){target=_blank}


## Défis à relever


### Smiley

S'inscrire sur [edublocks](https://app.edublocks.org/){target=_blank} et faire afficher un Smiley sur la matrice des 25 Leds...

![](./images/bbc-Smiley.gif){ .center}

### Coeur clignotant

Modifier le programme pour qu'après la phase de démarrage du BBC micro:bit la matrice de 25 LEDs affiche alternativement les 2 images de coeur suivantes :

![](./images/bbc-coeur.png){ .center}

> La fonction `sleep(t)` met en pause l’exécution pendant `t` millisecondes.  
> Exemple : `sleep(1000)` suspend l’exécution pendant 1 seconde.


### Feux d'artifice

Créer une autre séquence animée simulant un feux d'artifice comme par exemple :

<figure>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/uueiyRfRk7k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>

### Pluie

- Représenter une goutte d’eau qui tombe dans la 1ère colonne.

![](./images/bbc-D2-A1_pluieLong.gif){ .center}

> La fonction `display.set_pixel(x,y,i)` permet d’allumer la LED de la colonne `x` (nombre entre 0 et 4) et de la ligne `y` (nombre entre 0 et 4) avec une intensité `i` (nombre entre 0 et 9).  
> Exemple : `display.set_pixel(1,2,9)` allume la LED située à la colonne 1 de la ligne 2 avec l’intensité 9.

- Faire tomber dix gouttes de suite dans la 1ère colonne.

- Faire tomber une goutte une fois dans chaque colonne.

![](./images/bbc-D2-A3_pluieLong.gif){ .center}

- Faire tomber dix fois une goutte de pluie dans des colonnes choisies aléatoirement.

> La fonction `randint(x,y)` retourne un nombre entier aléatoire compris entre les nombres entiers x et y inclus. Pour pourvoir utiliser cette fonction, il faut ajouter from random import * au début du programme.  
> Exemple: `randint(0,10)` retourne un nombre aléatoire compris entre 0 et 10.

### Pierre, feuille, ciseau

Développer un programme pour qu'après avoir été secoué la carte BBC micro:bit affiche de façon aléatoire l'un des trois symboles suivants correspondant respectivement à une feuille, une pierre, ou des ciseaux.

![](./images/bbc-feuille.png){ .center}
![](./images/bbc-pierre.png){ .center}
![](./images/bbc-ciseaux.png){ .center}

### Hacker un haut-parleur

  Développer un programme pour qu'après un appui sur le bouton A de la face avant, le BBC micro:bit joue une de ses mélodies préprogrammées, tandis qu'après un appui sur le bouton B ce soit votre propre musique qui résonne.
  
  Pour que la carte produise du son une fois programmée, il faut la connecter avec des fils à pinces crocodiles à une prise jack d'un casque ou d'un haut parleur comme suggéré par le schéma :
  
  ![](./images/jack.png){ .center width="40%"}
     
  > Pensez à utiliser des boucles et à définir des fonctions.
  
  En manque d'inspiration ? Voici un exemple de partition à coder :
  
  ![](./images/StarWars.jpg){ .center width="80%"}
  

### Autres défis

Essayer d'autres choses en vous inspirant par exemple de :

<ul>
    <li>
      <a href="https://projects.raspberrypi.org/fr-FR/projects/interactive-badge">Badge Interactif</a>
    </li>
    <li>
      <a href="https://projects.raspberrypi.org/fr-FR/projects/frustration">Frustration</a>
    </li>
    <li>
      <a href="https://projects.raspberrypi.org/fr-FR/projects/fortune-teller">Diseuse de bonne aventure</a>
    </li>
    <li>
      <a href="https://projects.raspberrypi.org/fr-FR/projects/against-the-clock">Contre la montre</a>
    </li>
    <li>
      <a href="https://projects.raspberrypi.org/fr-FR/projects/rate-your-mates">Note tes potes</a>
    </li>
    <li>
      <a href="https://projects.raspberrypi.org/fr-FR/projects/reaction">Réflexes</a>
    </li>
  </ul>  

### Prolongements

Pour aller plus loins en programmation Python avec la carte BBC micro:bit :

- <https://matthieu-branthome.github.io/activite/#d%C3%A9fi-1-le-smiley>


<!-- 
http://2si.si.lycee.ecmorlaix.fr/Robotique/BBCmicrobit.html
 -->
