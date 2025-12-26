# [Leçon inaugurale] Yann Le Cun - Apprentissage profond et au-delà : les nouveaux défis de l'IA

Unknown Speaker:
Merci Anthony. Aujourd'hui, nous avons le plaisir d'accueillir Yann Le Cun. qui est chief AI scientist chez Meta et qui est professeur à NYU. Yann, merci beaucoup d'être là.

Yann est aussi membre de notre conseil scientifique et un certain nombre de chercheurs,  dont certains sont là d'ailleurs,

 travaillent avec Meta sur des sujets d'IA et on va signer d'ailleurs un partenariat tout à l'heure de cinq ans avec Meta sur un certain nombre de sujets de thèse. Donc, Yann a fait ses études pas très loin d'ici, au départ, à l'ESIE.

Et ensuite, il a fait une thèse de doctorat à l'université à Paris. Et puis, il est parti pour les Etats-Unis, où il a travaillé pour les laboratoires AT&T Bell Labs. C'est là, d'ailleurs, qu'on s'est croisés il y a quelques années.

Et en fait,  il a beaucoup travaillé au moment où les sujets des réseaux de neurones,  on n'appelait pas,  le mot intelligence artificielle n'était pas très très populaire à cette époque là.

C'était des réseaux de neurones qui avaient été en vogue dans les années 70-80 et qui étaient retombés de mode. Yann a été très persévérant avec un certain nombre de ses collègues comme Yoshua Bengio et Geoffrey Hinton.

Ils ont continué de travailler et ont trouvé des nouvelles méthodes d'apprentissage,  donc il vous en parlera,  en particulier ce qu'on appelle le Deep Learning,  qui ont complètement,  à partir des années 2010,  revivifié le domaine.

Il a rejoint Facebook en 2013, si mes notes sont bonnes. Il a fondé le FAIR, Facebook AI Research Lab, qu'il a dirigé pendant plusieurs années. Et puis,  il a reçu en 2018,  avec ses deux collègues que j'ai cités,  le Prix Turing,

 qui est en gros l'équivalent du prix Nobel pour les gens du computer science. Ce qui est intéressant aussi,  je pense,  d'écouter chez Yann,  Il y a une partie technique mais aussi une partie de réflexion sur le développement de l'IA,

 pourquoi,  quels en sont les problèmes de transparence,  de collaboration,  la compréhension des limites actuelles. Et puis, je pense qu'il est convaincu que c'est un outil qui doit être mis au service du bien commun.

Ça, il le dit en particulier dans un certain nombre de publications que vous pouvez retrouver. Il y a deux livres, je peux les citer et ensuite je te laisse la parole. Donc en 2018,  la plus belle histoire de l'intelligence,

 des origines aux neurones artificiels vers une nouvelle étape de l'évolution avec Stanislas Dehenne qui donc a Un professeur au Collège de France spécialiste de neurobiologie.

Et le deuxième, c'est quand la machine apprend, la révolution des neurones artificiels et de l'apprentissage profond. Donc ce n'est pas seulement un sujet technique, c'est un sujet de société.

Et Yann, on te laisse la parole pour nous en parler.

Speaker 1:
Merci. Merci Jérôme. Oui, on se connaît depuis très longtemps. On ne va pas avouer depuis combien de temps. Alors j'ai un beau speech tout préparé. Mais en fait,

 je crois que je ne vais pas vous donner ce speech-là parce que c'est une audience un petit peu spéciale.

Donc je vais vous faire des petits dessins au tableau pour expliquer un petit peu comment fonctionne l'IA pour ceux d'entre vous qui ne vous êtes pas déjà plongé dans le sujet.

Et puis poser un petit peu les questions de quelles sont les limites des approches actuelles de l'IA.

Je suis sûr que la plupart d'entre vous ont joué avec des systèmes d'IA ou les ont utilisés sans peut-être s'en rendre compte aussi parce que l'IA est utilisé un peu partout.

Mais bon, il y a des grosses limitations aux approches actuelles et il y a un futur. Il y a un futur à l'IA. Il y a une révolution qui va se passer Dans l'IA, dans les années qui viennent.

Et quand vous commencez vos études, vous allez faire partie de ça. Donc ce serait peut-être intéressant pour vous de savoir quelle va être cette révolution. On a l'impression que l'IA actuelle va nous amener à des systèmes intelligents,

 peut-être au niveau de l'intelligence humaine,  peut-être super intelligents,  qu'elle va être en relation avec eux,  etc.

Donc j'ai essayé de parler pendant pas trop longtemps pour qu'on puisse ensuite avoir une session de questions et de réponses. Je suis sûr que vous avez beaucoup d'interrogations. Alors,  on a besoin de,  on va avoir besoin de,

 on ne s'en rend pas encore compte,  mais on va avoir besoin de systèmes intelligents qui atteignent en fait l'intelligence humaine ou qui même la surpassent.

L'histoire de l'informatique, c'est qu'on a fait des systèmes informatiques dont les capacités, en fait, surpassent les capacités humaines. C'est un peu le principe d'utiliser des outils,

 c'est qu'on augmente la puissance humaine avec des outils,  qu'ils soient mécaniques ou informatiques,  logiques,  etc.,  mathématiques.

Donc il y a Il doit être vu comme un moyen d'amplifier l'intelligence humaine et ça ne peut avoir que de bons effets au total. Bien sûr on peut faire ça correctement,

 il y a aussi des risques mais il ne faut pas non plus les magnifier ou en être prisonnier disons. Mais le but c'est d'amplifier l'intelligence humaine.

Alors si on sort place quelques siècles en arrière sur quel a été un événement dans l'histoire qui a eu un effet un petit peu similaire d'amplifier l'intelligence humaine,

 probablement ce qui s'en rapproche le plus c'est l'invention de l'imprimerie au 15e siècle,  dans l'ouest en tout cas,  qui a permis d'abord de dissaminer le savoir beaucoup plus largement qu'il ne l'était à l'époque.

De motiver les gens d'apprendre à lire,  ce qui n'était pas forcément une bonne chose avant parce que ça ne servait pas à grand chose si on n'avait pas accès aux livres. Et puis de disséminer le savoir.

Alors le premier savoir qui a été disséminé par l'imprimerie, c'est La Bible. C'est les premières choses qu'on a imprimées avec l'imprimerie. Et qu'est-ce que ça a causé ?

Ça a causé que les gens ont pu lire la Bible même au lieu d'avoir le message religieux à travers les prêtres. Et ça a créé le mouvement protestant. Et ça a causé 200 ans de conflits religieux en Europe. Donc,

 personne aujourd'hui ne se permettrait de dire que l'imprimerie,  l'invention de l'imprimerie a été mauvaise pour l'humanité,  mais ça a quand même créé des effets délétères et qui,  dont il faut se prévenir,  se méfier,

 il y a toujours des effets qu'on a du mal à prédire. On peut comparer ça par exemple avec l'effet de l'imprimerie sur Sur,  par exemple,  le Moyen-Orient,  le monde arabe à l'époque,  qui dominait complètement la science au Moyen-Âge.

La raison pour laquelle toutes les étoiles dans le ciel ont des noms arabes,  c'est parce que les astronomes arabes leur ont donné des noms. Alors qu'au Moyen-Âge, dans l'Ouest, on était un peu sous le coup du... De l'obscurantisme.

Et puis l'imprimerie a tout changé. L'Ouest a commencé à s'éveiller avec le siècle des lumières. Et au contraire, le monde musulman s'est refermé, interdit l'imprimerie, en tout cas pour l'arabe.

Et ça a probablement contribué au déclin progressif du monde musulman à l'époque. Il y a deux leçons à apprendre là-dedans. La première leçon, c'est disséminer le savoir.

C'est toujours bien au total, mais il y a quand même des dangers qu'il faut prévenir. On s'en aperçoit aussi aujourd'hui avec des excès des réseaux sociaux, etc.

Mais il faut aussi faire attention à ne pas se mettre dans une position de ne pas accepter les progrès technologiques,  surtout quand ces progrès technologiques permettent la dissémination du savoir et de la science,

 parce que c'est vraiment le moteur du progrès humain. L'IA, si elle est bien utilisée, permettra une amplification de l'intelligence humaine.

Ça permettra à tout un chacun de prendre des décisions qui sont peut-être plus rationnelles qu'elles le sont normalement. Ça va accélérer le progrès de la science.

L'IA appliquée à la science On imagine des promesses dans des choses qui intéressent les étudiants de cette école,  comme par exemple la science des matériaux,  des choses comme ça,

 qui vont faire des progrès probablement assez rapides grâce à l'IA. On va assister à quelques décennies vraiment très différentes de celles qui se sont passées précédemment. Il ne faut pas en avoir peur.

Vous serez partie prenante de ça, je trouve. Alors, quelles relations allons-nous avoir avec les systèmes intelligents, surtout s'ils sont plus intelligents que nous ? Il ne faut pas en avoir peur non plus. C'est-à-dire qu'on sera leur boss.

Tout un chacun,  vous,  quand vous aurez fini vos études,  vous aurez des assistants d'IA avec vous qui seront plus ou moins intelligents. D'ici trois ans, ils ne seront pas très intelligents encore. D'ici cinq ans, en plus.

D'ici dix ans, encore plus. Et peut-être plus intelligents que vous. Il ne faut pas avoir peur de travailler avec des entités qui sont plus intelligents que vous. En fait, c'est la meilleure chose qui peut vous arriver.

C'est d'avoir des gens ou des choses qui travaillent avec vous, qui sont plus intelligents que vous. C'est l'histoire de ma carrière. J'ai toujours collaboré avec des gens qui étaient plus intelligents que moi.

Et je garantis, c'est vraiment la meilleure chose qui puisse vous arriver. Donc, il ne faut pas avoir peur non plus. Mais notre relation avec l'IA du futur,

 c'est que les systèmes d'IA seront comme une équipe de gens virtuels qui nous accompagneront dans notre vie de tous les jours et qui nous aideront. En fait, j'ai un assistant d'IA dans mes lunettes là.

Alors, je peux faire des choses comme prendre des photos, souriez. Voilà, vous avez vu le petit flash. Mais je peux aussi lui demander de prendre une photo. Alors je ne vais pas le faire parce que c'est un peu compliqué,

 mais je peux aussi lui demander n'importe quelle question. C'est comme un LLM classique, quoi, qui s'appelle Meta AI, qui est fait par mes collègues.

Speaker 2:
OK.

Speaker 1:
Je vais aussi prendre un selfie. Sauriez encore.

Unknown Speaker:
Voilà.

Speaker 1:
Alors c'est quoi l'IA ? C'est quoi le machine learning ? Devons un petit peu plus technique là. Et pourquoi ça s'appelle apprentissage profond ? Si on veut faire faire à une machine quelque chose, on peut écrire un programme.

Mais il y a des tas de tâches pour lesquelles on ne sait pas écrire le programme qui permet d'accomplir ces tâches. Par exemple,  si on veut écrire un programme qui prend une image,  une image c'est un tableau de nombre,

 c'est des valeurs de pixels,  qui interprète une image pour nous dire s'il y a une personne,  un piéton,  une voiture,  etc. Par exemple,

 si on veut faire une Un système d'assistance à la conduite qui fait en sorte que la voiture freine automatiquement quand il y a un piéton qui traverse devant ou un obstacle quelconque ou qui se conduit toute seule sur l'autoroute ou même ailleurs.

Il faut des systèmes de vision qui puissent interpréter les signaux qui viennent d'une caméra,  par exemple,  ou peut-être d'autres types de capteurs,  mais essentiellement d'une caméra.

Et on ne sait pas vraiment écrire un programme qui va interpréter dans tous les cas de figure si cette image,  par exemple,  a un piéton dedans,  ou un cycliste,  ou quelque chose comme ça,

 parce que la variabilité est tellement énorme qu'on ne sait pas le faire. Par contre, ce qu'on sait faire, c'est entraîner la machine à le faire. Qu'est-ce que ça veut dire, entraîner une machine ? Ça veut dire écrire un programme,

 et ce programme prend une entrée,  que je vais appeler X,  et par exemple,  qui est une image. C'est un tableau de nombre, avec la valeur des pixels.

En fait, si c'est une image couleur, il y a trois tableaux de nombre pour les trois composantes RGB. On va écrire un programme très simple qui peut tenir en une page de code ou même une demi-page.

Ce que fait ce programme, c'est des calculs numériques, des additions, des multiplications, des comparaisons. Mais des multiplications avec des coefficients et ces coefficients vont être appris. Alors qu'est-ce que ça veut dire ?

Prenons un cas vraiment très simple. Un cas très simple dans lequel je vais représenter tous ces pixels comme un vecteur. Chaque composante du vecteur, c'est la valeur de pixels. Je veux savoir si dans ce vecteur,  il y a,  disons,

 pas un visage ou pas un visage,  mais disons,  est-ce qu'il y a la lettre... Il y a beaucoup de pixels ici, mais je peux reprendre ça comme une image. Est-ce que c'est une lettre C ou une lettre D ?

Je peux faire quelque chose de très simple que des gens ont découvert ou inventé dans les années 50,  qui consiste à calculer une espèce de combinaison linéaire de ces valeurs avec des coefficients que je vais appeler un W,

 donc c'est un vecteur,  et la combinaison linéaire des coefficients dans ce vecteur par ce vecteur X,  Je peux écrire ça,  W transpose X,  c'est à dire la somme de Wixi.

Et puis si cette somme pondérée est supérieure à un seuil, je dis que c'est la catégorie C, d'accord ? Et si elle est inférieure à un seuil, ce n'est pas un C.

Et je peux bien sûr mettre plusieurs de ces unités pour reconnaître toutes les lettres de l'alphabet, etc. Donc la grosse question qu'on peut se poser,  c'est quelle valeur donner à ces poids,  à ces coefficients,

 pour que quand je montre un C,  cette unité-là a une grande somme pondérée et toutes les autres ont des sommes pondérées plus basses.

Et ça, c'est la base de l'apprentissage machine ou de ce qu'on a appelé aussi la reconnaissance des formes statistiques. Et l'idée pour entraîner ça est vraiment super simple.

Donc, par exemple, on peut décider que si cette somme pondérée est supérieure à un certain seuil, c'est... La lettre C, et si c'est inférieur à la seuil, ce n'est pas la lettre C.

Pour entraîner un système comme ça, je peux faire une sorte de régression. Beaucoup d'entre vous ont probablement entendu parler de régression linéaire.

Je peux dire par exemple, pour un exemple particulier, Qui serait, par exemple, une lettre C ? Je voudrais que cette somme pronérée soit,  disons,  égale à plus 1.  Et puis,  si je monte n'importe quoi d'autre,  une lettre A,

 B ou D ou n'importe quoi,  je voudrais que ce soit moins 1.  D'accord ? Est-ce que je peux trouver une combinaison de poids qui va faire en sorte que ça va être le cas ? Alors,  si j'ai une série d'exemples,  que j'aurais appelé comme ça,  OK,

 j'ai une série d'exemples,  donc c'est une image et une étiquette qui est plus 1,  moins 1.  Disons,  si je veux juste classifier deux catégories possibles. Ce que je vais faire, c'est calculer la somme sur tous ces exemples.

Peut-être diviser par le nombre d'exemples. De l'étiquette moins la... Le produit scalaire, pardon, je l'ai appelé, j'ai mis le I en haut et c'est un K.

Speaker 2:
Voilà.

Speaker 1:
Je mets ça au carré. Donc ça, c'est l'erreur que fait le système.

Speaker 2:
D'accord ?

Speaker 1:
Si je lui donne un Y particulier,  il calcule sa somme pondérée et je voudrais que la différence entre la sortie que je veux et la sortie qui produit soit la plus petite possible.

Une procédure, un problème de moindre carré, c'est la régression linéaire. On apprend ça en statistiques élémentaires. Je suis sûr que vous avez tous vu ça à la maternelle. Ou peut-être au lycée, ou peut-être en prépa.

Speaker 2:
OK.

Speaker 1:
Mais je suis sûr que vous avez vu ça quelque part. Donc on appelle ça une fonction de coût. Et c'est une fonction du vecteur de paramètre W. Donc qu'est-ce qu'on a ici ? En fait,

 c'est qu'on a une machine dont la fonction entrée-sortie est déterminée par un vecteur de paramètre et qui va nous sortir une prédiction pour un Y. Et puis,

 on va calculer une fonction de coût qui va être la différence entre le Y qu'on veut et le Y que produit la machine. Et le problème qu'on a à résoudre est un problème d'optimisation de mathématiques appliquées.

On est fort en mathématiques appliquées en France. Comment on fait pour minimiser ça ? On minimise ça par une méthode de gradient. C'est vraiment très simple.

On calcule simplement le gradient de cette fonction par rapport au vecteur de paramètres sur notre ensemble d'apprentissage. On calcule la moyenne de ça sur l'ensemble d'apprentissage. Et pour un exemple d'apprentissage particulier,

 si je prends simplement un terme là-dedans,  le gradient de ça par rapport à W C'est simplement deux fois yk,  il y a un moins devant,  pour un k particulier,  xk.

Speaker 2:
D'accord ?

Speaker 1:
Donc ça c'est un scalaire, ça c'est un vecteur. Techniquement, ça devrait y avoir une transposée quelque part parce que la dérivée d'un... Le gradient d'une fonction, c'est en fait un vecteur ligne, mais oublions ça.

Donc voilà, j'ai un truc très simple. Et la méthode d'apprentissage qui est la méthode de descente de gradient,  c'est simplement,  je vais prendre ma valeur W,

 je vais la remplacer par elle-même moins un coefficient qu'on appelle un taux d'apprentissage. fois le gradient de L par rapport à W.

Alors évidemment il faut calculer la moyenne de ça sur tout l'ensemble d'apprentissage mais bon la moyenne,  la dérivée de la moyenne c'est la moyenne de la dérivée. Et donc je me retrouve avec un truc vraiment super simple qui est,

 pour un exemple Wk particulier,  xk,  yk particulier,  je fais simplement Donc je modifie mon paramètre de poids par un coefficient fois le terme d'erreur multiplié par le vecteur d'entrée. C'est super simple.

C'est la méthode la plus simple pour faire Pour faire la régression linéaire en fait, tout simple. Mais c'est l'algorithme d'apprentissage le plus simple qu'on puisse imaginer,  qui a été proposé dans les années 50,  60 et autres,

 indépendamment par des statisticiens,  par des gens qui étaient intéressés par ce qu'on appelait à l'époque la cybernétique,  par le traitement de signal adaptatif,  etc.

Et puis c'est devenu tout un domaine qu'on appelait la reconnaissance des formes statistiques et autres. Voilà, alors ça c'est l'apprentissage élémentaire. Mais le problème de ça,  c'est qu'évidemment,  calculer des combinaisons linéaires,

 ça ne va pas nous permettre d'entraîner une machine à reconnaître des images ou prédire le mot qui suit une séquence de mots comme le font les chatbots et les LLM. Donc pour ça, il faut du deep learning.

Qu'est-ce que c'est le deep learning ? C'est une petite modification de ça dans laquelle on a toujours une entrée X.

Mais au lieu d'avoir une machine qui est relativement simple avec des paramètres qui calcule une combinaison linéaire ou quelque chose comme ça,  on va en empiler plusieurs.

On va avoir peut-être une matrice de poids ici et puis ensuite une espèce de fonction non linéaire. Je vais expliquer ce qu'elle fait. Et puis une autre matrice de poids ici et puis une autre fonction non linéaire.

Et puis peut-être une autre. Et puis là,  on va avoir la fonction de coût qui va nous dire,  je prédis un Y,  mais le Y que je veux,  c'est celui-là pour ce X là.

Et donc, il va falloir que j'ajuste tous ces paramètres qui sont des matrices maintenant. Je vais vous dire pourquoi dans une minute. De manière à minimiser l'erreur entre le Y qu'on veut et le Y qu'on a, que le système produit.

Pourquoi ça s'appelle le Deep Learning ? Parce qu'il y a plusieurs étages. C'est tout. C'est pas plus profond que ça. Ça,  ça fait appel,  et c'est ça la révolution du deep learning,  vous allez voir que c'est pas vraiment compliqué,

 ça fait appel à un concept mathématique ultra compliqué que vous avez peut-être pas appris à l'école maternelle mais à l'école élémentaire qui s'appelle la règle de dérivation des fonctions composées. D'accord ?

On a plusieurs fonctions qu'on applique les unes après les autres. Comment calculer le gradient ? Une fonction de coût par rapport à tous ces paramètres.

Et ça semble très très bizarre parce qu'on reconnaît la règle de dérivation des fonctions composées depuis Newton et Euler,  la Gnitz.

Mais on a eu l'idée d'utiliser ça pour l'apprentissage machine que relativement récemment dans les années 80. Il y a des gens qui avaient eu l'idée dans les années 70,  mais ils n'avaient pas réussi à la faire marcher. Et puis,

 c'est vraiment devenu un petit peu commun au milieu des années 80.  Et puis,  il y a eu une dizaine d'années où il y a eu des progrès dans la question.

Et puis, au milieu des années 90, pour une raison mystérieuse, la communauté de la recherche s'est désintéressée de ces méthodes.

Et elles sont revenues en force au début des années 2010 et c'est la révolution de l'IA qu'on connaît aujourd'hui et grâce à ce renouveau d'intérêt pour ces méthodes. Alors c'est en fait hyper simple. Vous savez,

 si on veut calculer la dérivée d'une fonction,  la dérivée d'une fonction composée et de deux fonctions qu'on applique successivement,

 c'est le produit de la dérivée de la première fonction fois la dérivée de la deuxième fonction aux beaux endroits. Mais on peut écrire ça très simplement. Par exemple,  si j'appelle cette variable-là S1 et puis celle-là S2,

 si je veux calculer,  par exemple,  D2L sur DS1,  ça va être D2L sur DS2 fois DS2 sur DS1. Règle de dérivation des fonctions composées, c'est vraiment simple. Alors, S est un vecteur. Cette dérivée, c'est un vecteur.

S2 est aussi un vecteur de taille différente. Ça, c'est aussi un vecteur. Ça, c'est une matrice. D'accord ? Ça, c'est une matrice qui comporte les dérivées de toutes les sorties. Alors, qu'est-ce que c'est ?

Ce qui produit S2 à partir de S1, c'est ce bloc-là. Ok, c'est une fonction. Et ce qu'il va falloir calculer ici,  c'est une matrice qui contient toutes les dérivées partielles de toutes les sorties par rapport à toutes les entrées. D'accord ?

Donc une composante IJ de cette matrice, c'est la dérivée de la sortie I par rapport à l'entrée J. D'accord ? Si vous perturbez l'entrée J d'un petit peu, de combien est perturbée la sortie numéro I ? C'est cette matrice-là. Et si...

Si la fonction qui produit S2 par rapport à S1 est une fonction linéaire,  c'est-à-dire simplement une matrice,  multiplication par une matrice,  à ce moment-là,  ce truc-là,  c'est simplement la transposée de la matrice. C'est vachement simple.

Donc ce que ça veut dire,  c'est que si on a le gradient de nos fonctions de coût par rapport à Y,  on multiplie par la matrice,  ça,  ça s'appelle la matrice Jacobienne.

On multiplie ce gradient qui est un vecteur par la matrice jacobienne de ce bloc. La matrice elle-même est transposée. On obtient le gradient par rapport à ici. Cette fonction non linéaire que je ne vais pas détailler,

 elle applique une fonction non linéaire à chaque composante du vecteur. C'est très simple. On peut rétro-propager les gradients à travers ça aussi. Ensuite, multiplier par la transpose de cette matrice, etc., de proche en proche.

Par une itération de proche en proche à l'envers, Un algorithme qui s'appelle la rétropropagation de gradient. On peut calculer le gradient de la fonction de coût par rapport à tous les paramètres internes du système,

 les mettre à jour avec cette règle,  qui est une règle de descente de gradient,  simplement. Et c'est ça le Deep Learning. Vous pouvez écrire ça en deux pages de Python, trois peut-être.

Certainement, si vous n'utilisez pas Itorch, ça va prendre quatre lignes. Parce que dans les systèmes modernes de l'IA et de programmation comme PyTorch,

 donc c'est une bibliothèque au-dessus du piton qui permet de faciliter l'écriture de ce genre de choses,  vous n'avez pas besoin en fait d'écrire comment rétropropager ces gradients,

 vous écrivez simplement une fonction qui calcule la sortie par rapport à l'entrée et automatiquement PyTorch va produire une fonction qui permet de rétropropager les gradients À travers ces structures,  vous n'avez pas besoin d'occuper.

Ça s'appelle la différenciation automatique et c'est hyper puissant pour tout un tas de choses,  pas seulement pour le machine learning,  mais pour tout un tas de choses. Donc voilà, un peu démystifié.

Maintenant, comment marchent les systèmes d'IA actuels ? Ceux que tout le monde utilise. Il y en a plusieurs sortes. Donc il y a ceux qui servent à piloter nos voitures plus ou moins automatiquement,  ou en tout cas éviter les obstacles,

 ou freiner automatiquement s'il y a un obstacle qui se présente. Et ceux-là sont basés sur quelque chose qui est un peu mon invention,  qui s'appelle réseau convolutif,

 qui est une manière particulière de structurer ces matrices dans un réseau profond. Ces matrices,  au lieu d'être des matrices pleines,

 elles sont creuses et ça correspond à une espèce d'architecture qui est un petit peu inspirée de l'architecture du cortex visuel. Je ne vais pas rentrer dans les détails, mais ça s'appelle un réseau convolutif.

Pratiquement tous les systèmes de vision en temps réel sont à base de réseaux convolutifs. Si ce n'est pas en temps réel,  on peut utiliser d'autres architectures mais si on veut que ça aille vite,  on est obligé d'utiliser ça.

Tous les systèmes qu'il y a dans les voitures d'assistance à la conduite,  Tous les systèmes d'analyse d'images médicales,  de détection de tumeurs dans les mammographies,  des choses comme ça. Tous les systèmes de reconnaissance de visage.

Quand on passe à la frontière, il y a un système qui reconnaît les visages. C'est basé là-dessus. Ça sert à certains pays pour espionner leur population. Ces utilisations ne sont pas toujours très bonnes. C'est utilisé aussi de manière plus...

disons de plus en plus importante dans des drones autonomes,  c'est à dire le conflit entre la Russie et l'Ukraine par exemple,

 les Ukrainiens construisent des drones qui ont des capacités de reconnaissance automatique de cibles parce que Les systèmes ne peuvent pas être toujours pilotés à distance à cause du brouillage radio,

 donc il faut leur donner un petit peu d'autonomie. C'est utilisé pour tout un tas de choses, bonnes ou mauvaises, mais c'est absolument partout. Maintenant, il y a un autre type d'architecture qui s'appelle les transformers.

C'est pas un bon nom parce que ça dit pas grand chose ce que ça fait,  mais le réseau convolutif est basé sur des opérations mathématiques qui s'appellent les convolutions dont certains d'entre vous ont probablement entendu parler.

Les transformeurs transforment d'une certaine manière mais les réseaux convolutifs ont la propriété que si on leur donne une image en entrée et on translate l'image,  la sortie du réseau convolutif est aussi translatée mais pas changée.

Ça permet de faire en sorte que quand on applique un réseau convolutif à une image et qu'il y a tout un tas d'objets dedans,  le système va détecter les objets où qu'ils soient dans l'image et on peut faire bouger les objets dans l'image,

 la détection va bouger aussi,  etc. Ceux-là sont équivariants par translation. Les transformeurs ont une propriété amusante, c'est qu'ils sont équivariants aussi, par permutation. C'est-à-dire qu'on leur donne une série de vecteurs en entrée,

 et si on permute ces vecteurs,  la sortie est aussi permutée,  mais inchangée par ailleurs. Et ça c'est intéressant si l'entrée qu'on fournit au réseau neurone,  la position des objets dans l'entrée n'est pas si importante.

Si c'est important, ce qui est important c'est leur relation. Les transformers sont des architectures qui sont utilisées principalement pour le traitement de la langue,  dans les LLM,  les chatbots,  etc.

Je ne vais pas expliquer comment c'est fait. Il y a plein de tutoriels sur le web si vous voulez. En gros,  c'est un réseau de deep learning avec des paramètres,  avec des couches qu'on empile et qu'on entraîne par des centres de gradients,

 etc. Comment on entraîne un transformeur ? Il y a un type particulier d'architecture pour organiser les transformeurs qu'on appelle GPT. ChatGPT vient de ça. Ça veut dire Ça veut dire General Pre-trained Transformer en anglais.

Le P c'est Pre-trained. Qu'est-ce que ça veut dire Pre-trained ? Ça veut dire qu'on ne l'entraîne pas pour une tâche particulière à résoudre comme répondre à des questions ou traduire d'une langue à une autre,  etc.

On l'entraîne simplement par ce qu'on appelle apprentissage auto-supervisé, à prédire le mot qui suit une séquence de mots. Alors ce qu'on peut faire c'est prendre une séquence de mots, Chaque mot est encodé comme un vecteur, simplement.

On associe un vecteur à chaque mot du dictionnaire. En fait, ce n'est pas des mots qu'on utilise, c'est des sous mots qu'on appelle les tokens, mais peu importe. On prend une séquence de mots,  on la fait passer dans un gros réseau neurone,

 qui est une sorte de transformeur,  qui nous produit une sortie. Et ce qu'on va faire, c'est qu'on va comparer cette sortie avec le mot qui suit. Notre fonction de coup,  c'est une sorte de divergence entre le vecteur du mot qu'on veut,

 qui suit cette séquence de mots,  et la prédiction du réseau neurone. C'est un énorme réseau neurone avec Des millions,  des centaines de millions,  des milliards,  des centaines de milliards,

 ça peut aller jusqu'au mille milliards de paramètres. Ces systèmes peuvent stocker une quantité d'informations absolument gigantesque et accumuler la totalité de la connaissance humaine. Pas exactement, mais un peu.

La manière dont on s'est entraîné, c'est un peu plus futé que ça. On prend une longue séquence de mots,  Et on n'entraîne pas une seule copie de ce réseau,  mais autant de copies qu'on a de fenêtres sur l'entrée.

On fait tourner un grand nombre de copies de ce réseau. Chacun est appliqué à une fenêtre différente et chacun est entraîné à reproduire son entrée sur sa sortie. En fait, on peut voir ça comme ce qu'on appelle un auto-encodeur.

C'est-à-dire qu'on a la séquence d'entrée ici,  la même séquence ici en haut,  et on entraîne simplement ce réseau à apprendre la fonction identité. Ça paraît stupide.

Pourquoi entraîner un réseau avec des centaines de milliards de paramètres Apprendre simplement la fonction d'identité. Mais en fait, on l'entraîne à calculer la fonction d'identité. Simplement,

 il ne peut regarder qu'une fenêtre de mots particulière pour calculer la sortie suivante et il ne peut pas regarder l'entrée correspondante.

Donc il ne peut pas Trouver une solution triviale qui consisterait simplement à copier son entrée sur sa sortie,  il est obligé en fait de prédire. Alors pourquoi ça marche ces trucs-là ? Pourquoi on arrive à faire des ChatGPT avec ?

Pour deux raisons. La première c'est qu'on peut entraîner,

 on peut mettre beaucoup beaucoup de paramètres là-dedans et entraîner ces systèmes à À prédire le mot suivant appartient une très grande quantité de données d'apprentissage ou aussi la fenêtre de contexte que peut regarder le système peut correspondre à 100 000 mots ou peut-être un million si on arrive à le faire.

Et on entraîne avec typiquement de l'ordre de 3 10 à la puissance 12.

Speaker 2:
Mots ou tokens, c'est comme des mots. D'accord ?

Speaker 1:
Donc ça commence à faire beaucoup. En fait,  c'est même 30 10 à la puissance 12.  Je ne sais pas comment on appelle 10 à la puissance 12.  Chaque token est représenté sur 3 octets environ. Donc à la fin, ça fait 09 10 à la puissance 14 octets.

de données d'apprentissage. Ça, ça correspond à la totalité du texte disponible sur Internet publiquement, et puis plus d'autres données.

Ça nous prendrait, tout un chacun ici, de l'ordre de 400 000 ans à lire, en lisant plus de 12 heures par jour. D'accord ? Alors c'est énorme. Et ce que fait le système,  c'est qu'il apprend une espèce de version compressée d'un peu tout ça,

 si vous voulez. Alors il y a quand même un problème essentiel avec ça,  c'est qu'il n'y a pas vraiment de capacité de raisonnement dans un système comme ça.

Il ne fait que prédire le mot suivant et puis il y a des problèmes d'hallucination comme on en a beaucoup parlé. Maintenant on compare ça. Alors maintenant je vais en venir aux limitations des systèmes actuels.

Ces systèmes-là ne comprennent pas le monde physique. n'ont pas de mémoire persistante, n'ont pas vraiment de capacité de raisonnement. Les gens essaient de corriger ça, mais ça ne marche pas très bien.

Et certainement pas de capacité de planification, à moins de les entraîner systématiquement, en fait, avec des tas d'exemples. Donc, tout l'argent qui est dépensé en ce moment en IA, c'est pour deux choses.

Un, l'infrastructure de calcul nécessaire à entraîner et surtout à faire tourner ces trucs-là. Mais aussi la phase de ce qu'on appelle le post-training,

 c'est-à-dire affiner le système pour le faire accomplir des tâches comme répondre à des questions fréquentes,  aller rechercher l'information par un moteur de recherche pour l'intégrer dans la réponse,  etc.

Et faire en sorte qu'il ne soit pas complètement toxique, etc. Donc, il y a tout un tas d'efforts qui sont dédiés à ça là-dedans. Mais maintenant, comparons ça avec un enfant de 4 ans.

Un enfant de 4 ans a été éveillé à un total d'environ 16 000 heures. L'information qui arrive à notre cortex visuel dans ces 16 000 heures Il y a énormément d'informations qui arrivent sur la rétine.

On a 60 millions de récepteurs, 60 millions de pixels par œil, si vous voulez. Mais en fait, tout ça est compressé pour passer dans le neuroptique. Le neuroptique n'a qu'un million de fibres nerveuses qui arrivent au cerveau par œil.

Et chaque fibre nerveuse peut faire transiter environ un mégaoctet par seconde. Elle arrive à notre cerveau environ 2 mégaoctets par seconde.

Multipliez ça par 16 000 heures, 3600 secondes par heure et on arrive environ à 10 puissance 14 octets.

Un enfant de 4 ans a vu autant de données à travers la vision que le plus gros des LLM actuels entraînés sur la totalité de tout le texte disponible sur internet publiquement. Donc ça, ça vous dit deux choses.

On ne va pas arriver à un système au niveau de l'intelligence humain ou surhumain simplement en entraînant sur du texte. Ça ne peut pas arriver. Il y a des gens qui vont vous dire que si,  l'année prochaine,

 on aura des systèmes super intelligents,  aussi bons qu'un doctorant,  etc. C'est faux. C'est faux.

Speaker 2:
D'accord ?

Speaker 1:
Alors comment faire ça ? C'est le sujet de la prochaine révolution de l'IA. C'est sur quoi je travaille depuis assez longtemps. On fait beaucoup de progrès et la manière dont on fait les progrès,

 c'est sur des systèmes qu'on appelle des modèles du monde. J'ai des tas de jolies vidéos à vous montrer de robots qui sont contrôlés par des trucs comme ça,

 mais je pense que c'est plus intéressant pour vous de comprendre un petit peu ce qui est sous-jacent là-dedans. Qu'est-ce que c'est un modèle du monde ? Un modèle du monde,  c'est si vous avez une idée de l'état du monde à l'instant T,

 Et si vous imaginez prendre une action à l'instant T,  ce qu'il faut pouvoir faire,  c'est prédire quelle va être la conséquence de cette action sur l'état du monde. Comment le monde va être changé si je prends cette action à l'instant T ?

C'est-à-dire que si je prends ce téléphone et que je le mets ici,  ça change un petit peu l'état du monde,  pas beaucoup. Pas autant que si, je ne sais pas, le Premier ministre démissionne par exemple.

Mais bon, ça change un petit peu l'état du monde. Donc là,  ce qu'il nous faut,  c'est un réseau de neurones qui,  étant donné une idée de l'état du monde à l'instant t,

 peut nous prédire l'état du monde à l'instant t plus 1 en fonction d'une action qu'il imagine prendre. Bon, maintenant, comment calculer l'état du monde ?

L'état du monde sépare Une représentation de tout l'état du monde parce que si je voulais représenter l'état du monde,  l'état de la pièce en ce moment,

 je pourrais descendre au niveau de la théorie des champs quantiques ou quelque chose comme ça,  avoir la fonction d'onde complète de toute cette pièce et en principe je peux tout calculer,

 ce qui va se passer dans cette pièce à partir de l'information de la fonction d'onde et puis je vais tourner la mécanique quantique.

Évidemment, c'est complètement impossible parce qu'on ne peut pas mesurer la fonction d'onde d'un système macroscopique d'abord. Et puis,  surtout,  on n'a pas des ordinateurs assez puissants pour faire ce genre de calcul,

 même avec des ordinateurs quantiques qui n'existent pas encore. Donc, ce n'est pas vraiment possible. Qu'est-ce qu'on fait en tant qu'humains ? Les animaux font les mêmes choses.

Et certainement, dans la science, les sciences d'ingénieurs ont fait ça de manière très systématique. C'est qu'on trouve une représentation abstraite De l'état du monde qui nous permet de faire des prédictions.

Donc au lieu de prédire tout ce qui se passe dans le monde comme je ne sais pas dans le monde de la politique en termes de théorie quantique des champs. On invente des abstractions comme par exemple les atomes, les molécules.

Dans le monde vivant, les protéines, les organelles, les cellules, les organismes, les organes, les organismes, etc. jusqu'aux sociétés, individus, sociétés, écosystèmes.

Donc on a toute cette hiérarchie de représentations abstraites du monde dans lesquelles les détails de la couche en dessous sont un petit peu oubliés. Éliminer.

Et on ne maintient que l'information qui nous permet de faire des prédictions à relativement long terme. Alors j'ai cité toute cette hiérarchie.

Vous pouvez remarquer que chaque niveau dans cette hiérarchie est un champ différent de la science.

Speaker 2:
OK ?

Speaker 1:
Il y a la physique élémentaire, la physique des particules, la physique nucléaire, la chimie, la biochimie, la biologie, etc. Biologie moléculaire, etc. Et puis jusqu'à psychologie, sociologie, écologie, etc.

Donc ce qu'il nous faut, c'est inventer une architecture qui permet de construire ces abstractions. Et donc à partir d'une observation du monde,  Xt,  Entraîner une sorte de réseau neurone,  de deep learning,

 à produire cette représentation abstraite de l'état du monde. On n'aura probablement pas un seul niveau, on aura plusieurs niveaux hiérarchiques. Et pour l'entraîner, c'est très simple. Il suffit d'observer ce que va faire le monde,

 ce que fait le monde au temps T plus 1.  Rentrer ça dans le même encodeur. On appelle ça un encodeur. On appelle ça un prédicteur. Et puis comparer la prédiction de... Alors ça,  ce n'est pas le vrai ST plus 1,

 c'est la prédiction de ST plus 1 et ça,  c'est le vrai ST plus 1 qui est observé. On compare les deux et puis on entraîne tout le système à réduire cette erreur de prédiction.

Alors il y a des problèmes techniques là-dedans dont je ne vais pas rentrer dans les détails. Mais cette architecture s'appelle Joint Embedding.

Speaker 2:
Predictive architecture. Okay, GPAT.

Speaker 1:
Donc c'est une architecture que j'ai proposée relativement récemment,  mais il y a beaucoup d'engouement pour ça dans la recherche en IA en ce moment.

Donc si vous tapez dans Google Scholar, scholar.google.com, Gentlemanic Predictive Architecture entre... Entre guillemets, vous aurez entre 700 et 800 papiers sur ce sujet. Et je pense que c'est le futur de l'IA. Donc,

 la prochaine révolution de l'IA,  à mon avis,  passe par les JAPA,  par les World Models,  donc les modèles du monde,  et puis par des systèmes qui,  à partir du moment où ils ont ce genre de modèles du monde,

 ils pourront planifier une séquence d'action pour arriver à un objectif particulier. C'est-à-dire,  sur l'ordre d'un objectif,  L'état du monde soit dans une configuration particulière,  par exemple,

 que mon téléphone soit de l'autre côté du laptop. On donne ce but et ensuite,  le système peut imaginer,  peut prédire,  en fait,

 le résultat d'une séquence d'action et donc peut essayer d'imaginer une séquence d'action qui va satisfaire ce but,  c'est-à-dire qui va amener l'état du monde à une configuration particulière. Ça s'appelle la planification.

Et c'est quelque chose dont les LLM ne sont pas vraiment capables,  mais que ces architectures JEPA en fait sont capables. Donc je mets beaucoup d'espoir dans ce genre de choses et c'est peut-être une idée du futur de l'IA.

Voilà, je vais arrêter là et ouvrir si vous avez des questions.

Unknown Speaker:
Je voulais revenir sur les modèles du monde que vous évoquiez. De manière générale, par exemple, si on continue l'analogie avec un humain, les modèles du monde changent. En fait, on arrive à l'adapter en fonction de la situation.

Alors qu'en général, les modèles d'IA, il y a une phase d'entraînement, une phase d'inférence. Est-ce que vous ne pensez pas qu'entraînement devrait être continu,

 c'est-à-dire qu'il devrait être capable de dater les poids du modèle de manière communément ?

Speaker 1:
Oui absolument. Très clairement l'apprentissage devrait être continu. Bien sûr quand on a un modèle du monde en tant qu'humain et qu'on imagine qu'une action qu'on va prendre va avoir un résultat particulier,

 Il s'avère qu'on a fait une erreur,  c'est-à-dire que nos prédictions étaient fausses. En général, on corrige notre modèle du monde immédiatement. Et ça, ça nous arrive absolument tout le temps.

Par exemple, on prend un objet, il est plus lourd que prévu. On ajuste très rapidement tous les petits coefficients qu'il faut dans notre cervelet pour pouvoir adapter. C'est une méthode d'adaptation extrêmement rapide.

Il y en a, bien sûr, qui sont beaucoup plus lentes. Les modèles qui nous permettent de prédire le comportement d'une personne,  ou d'un groupe de personnes,  ou de la société,  ou d'un marché,  ou d'un système physique compliqué,

 l'intuition qu'on construit,  on l'ajuste constamment. On devrait faire ça avec nos systèmes. Ce n'est pas un problème conceptuel particulièrement compliqué, il suffit de ne pas arrêter l'apprentissage.

Speaker 2:
Bonjour. Bonjour.

Unknown Speaker:
Est-ce que vous pensez que l'IA va pouvoir être capable de s'améliorer elle-même bientôt ?

Speaker 2:
Oui.

Speaker 1:
En fait,  ce genre de système,  à la base,  il y a une série de théories en psychologie,  popularisée par un certain Daniel Kahneman,  qui est un psychologue,  mais aussi,  enfin,  qui était,  parce qu'il est mort récemment.

Mais qui est aussi prix Nobel d'économie. Et lui,  il a proposé ce qu'il appelle le système 1 et le système 2.  Alors système 1,  c'est le type de comportement,  en tant qu'humain,  qu'on fait sans avoir à réfléchir.

On est tellement habitué à accomplir la tâche qu'on la fait sans avoir à réfléchir et planifier. Puis système 2,

 c'est plutôt le type de comportement qui nécessite justement d'utiliser notre modèle du monde et de réfléchir à quelles séquences d'action prendre pour pouvoir accomplir la tâche qu'on a décidé d'accomplir.

On peut voir, par exemple, les LLM comme une sorte de système 1. Ils sont réactifs. C'est-à-dire qu'on donne une entrée,  on propage dans,  je ne sais pas combien de couches dans les réseaux neurones,  ça produit une sortie. Alors que ça,

 c'est plus système 2.  Par optimisation et par recherche,  on essaie de trouver une séquence d'action qui remplit la tâche qu'on donne au système. Et si on a un système comme ça, système 2, il peut trouver des solutions à un problème.

dont il n'avait aucune idée au départ. C'est-à-dire par recherche d'une séquence d'action qui arrive à un résultat particulier,  par exemple,  recherche d'une séquence de dérivation qui démontre un résultat de maths,

 on apprend de nouvelles choses en faisant ça. Toutes les tâches qu'on fait,  qu'on accomplit,  je sais pas,  on construit quelque chose avec du bois ou on joue aux échecs ou quoi que ce soit,

 en fait on s'entraîne soi-même en faisant la tâche et puis en cherchant des solutions. Donc à terme, je pense, les systèmes qui vont s'améliorer eux-mêmes vont utiliser ce genre de principe.

Unknown Speaker:
Autre question ?

Speaker 1:
Merci pour votre présentation.

Unknown Speaker:
J'ai une double question pour vous. Est-ce que vous pensez que l'art de l'intelligence artificielle générale est atteignable ? Et si oui, est-ce que c'est souhaitable ?

Speaker 1:
Alors il y a deux réponses à ces questions. La première réponse est absolument pas et la deuxième réponse est oui. En fait ça dépend de ce qu'on veut dire par l'intelligence artificielle générale, en anglais AGI.

Alors c'est une très très mauvaise dénomination pour vouloir en fait parler de l'intelligence de niveau humain. D'accord. Mais ça, ça présuppose que l'intelligence humaine est générale. Or l'intelligence humaine n'est absolument pas générale.

On est très très très spécialisé. Et c'est un peu difficile de s'imaginer qu'on est spécialisé, on a l'impression qu'on peut résoudre tous les problèmes etc. Mais c'est pas vrai, on est super spécialisé.

D'ailleurs la meilleure preuve c'est que vous pouvez acheter un gadget dans un magasin de jouets qui va jouer aux échecs et vous battre à plate couture. Ce système là est plus intelligent que vous pour jouer aux échecs. Vous allez sur,

 je ne sais pas quel site web,  vous rentrez une expression pour une intégrale et le truc va vous calculer l'intégrale symboliquement bien mieux,  bien plus rapidement que vous,  que moi certainement.

Donc il y a beaucoup de systèmes informatiques qui sont plus intelligents que nous dans plein de domaines et ça veut dire qu'on n'est pas général. En tout cas, on n'est pas général avec un certain niveau d'efficacité. Mathématiser ça.

Comme j'ai dit tout à l'heure, on a un million de fibres dans le nerf optique. Imaginons que ce qui transite dans le nerf optique, c'est binaire. Donc on a un million de bits qui arrivent au contexte visuel, qui est à l'arrière du cerveau.

Combien y a-t-il de fonctions ? C'est une question intéressante pour n'importe qui. Une fonction de classification,  comme je décrivais précédemment,  sur ce million de bits,

 c'est une fonction qui prend un million de bits et qui produit un bit en sortie,  1 ou 0 si c'est classe 1,  0 si c'est classe 2.  Combien de fonctions de ce type là existent-il ? Combien de fonctions de un million de bits ?

Une fonction Boolean de un million de bits ?

Speaker 2:
Quelqu'un connaît la réponse ?

Speaker 1:
Deux puissances un million.

Speaker 2:
Autre réponse ?

Speaker 1:
Pas d'autres propositions ?

Speaker 2:
Non ?

Speaker 1:
Allez, ne soyez pas timide. OK, j'ai deux symboles sur les trois corrects. Il y a effectivement deux à la million dedans. Vous allez avoir la réponse ? C'est 2 à la puissance 2 à la puissance 1 million.

Unknown Speaker:
D'accord ?

Speaker 1:
Parce que, il y a effectivement 2 à la puissance 1 million configurations possibles de 1 million de bits. D'accord ? Donc ça veut dire que la fonction est caractérisée par une séquence de 2 à la puissance 1 million de bits.

Et le nombre de configurations de ça,  qui est le nombre de fonctions,  c'est 2 à la puissance 2 à la puissance 1 million.

Unknown Speaker:
D'accord ?

Speaker 1:
Voilà donc, 2 symboles sur 3, correct, c'est bien. Combien, parmi ces fonctions, combien de fonctions de ce type là est-ce que notre contexte visuel est capable de réaliser ?

Speaker 2:
A la louche ?

Speaker 1:
Ok, je vous donne un petit élément de réponse. Dans le cerveau complet,  pas seulement dans le contexte visuel,  on a environ 10 à la puissance 14 synapses,  c'est-à-dire connexions entre neurones.

C'est ces connexions qui sont ajustables par l'apprentissage. Donc la capacité totale de notre mémoire, c'est 10 à la puissance 14 octets, disons.

Speaker 2:
Peut-être plus, peut-être moins, mais à peu près.

Speaker 1:
Mais le nombre de fonctions réalisables en changeant toutes ces valeurs est tout petit par rapport à ça. C'est même minuscule. C'est infinitésimal en fait. Donc dire qu'on a l'intelligence générale, c'est un contresens total.

Ok, donc j'ai toujours pas répondu à votre question. Donc la première chose,  c'est qu'il ne fait absolument aucun doute que dans un futur peut-être pas si éloigné,  on aura des machines qui sont plus intelligentes que les humains,

 dans tous les domaines où les humains sont intelligents. Alors les plus optimistes disent 5 ans, Les optimistes disent 10 ans, les moins optimistes disent peut-être 20 ans. Et puis,  il y en a qui disent qu'on n'y arrivera jamais,

 mais ils n'ont pas de bons arguments pour ça. Pour moi,  ça ne fait aucun doute qu'on va y arriver,  mais ce n'est pas clair combien de temps ça va prendre.

Mais je pense qu'on aura probablement de bonnes idées ou des idées qui vont s'en rapprocher,  peut-être basées sur les JAPA,  d'ici 3-5 ans. Et puis là,

 on va rencontrer des obstacles qu'on n'avait pas vus et donc ça va prendre plus de temps que prévu parce que c'est toujours comme ça dans l'histoire de l'IA. Mais ça ne fait aucun doute qu'on va y arriver.

Mais par contre, ces systèmes-là n'auront pas l'intelligence générale.

Speaker 2:
Bonjour.

Speaker 1:
Vous avez parlé des nouvelles architectures comme par exemple les GEPA qui restent à construire. Et si nous,  par exemple,  les ingénieurs des ponts,  on veut travailler dans l'IA,  comment est-ce qu'on peut faire pour être pertinent ?

Est-ce que par exemple on est obligé de faire des doctorats pour Pour être personnellement dans ce domaine,  est-ce qu'il faut être brillant en maths ? Et si oui,

 qu'est-ce que vous nous conseillez de faire pour rester compétitif face à d'autres étudiants comme ceux de l'ENS,  ULM ou de l'ICSE,  par exemple,  pour entrer dans une entreprise comme Meta ? Attendez, vous n'avez pas de complexe à avoir.

Moi, j'ai fait l'essai. Je n'ai pas fait TOP, je n'ai pas fait CPSP. Conseiller d'orientation. Conseiller d'orientation. Je vais faire un doctorat après, effectivement. Non,  si vous voulez faire de la recherche,  et ce qui est marrant dans l'IA,

 c'est de faire de la recherche,  effectivement,  il vaut mieux faire un doctorat. Et il y a une vérité qui était,  enfin un fait qui était vrai dans le passé et qui ne l'est plus,  c'est qu'il y a encore 15 ans,

 vous sortiez d'une grande école à la française,  quoi. Entre autres, ENS, X, Centrale, Pont, Mine, machin, Télécom. Votre voie était toute tracée et en fait,  l'intérêt de faire une thèse n'était pas évident,

 sauf si vous vouliez vous lancer dans la recherche académique ou publique. C'est plus vrai. En ce sens que maintenant,  si vous voulez vraiment avoir une carrière déjà qui commence par une carrière technique et puis qui innove,

 Il faut faire un doctorat. Il y a une revalorisation assez importante du doctorat en France qui n'existait pas jusqu'à il y a une quinzaine d'années,  mais qui est très,

 très claire maintenant et qui rattrape un petit peu le concept du doctorat qu'on a aux Etats-Unis,  par exemple,  ou même en Allemagne,  où le doctorat était traditionnellement beaucoup plus valorisé qu'en France. Donc,

 il y a une valorisation très claire du doctorat et ça mène à des métiers qui sont pour moi plus intéressants. Je me vois comme un chercheur, ingénieur et chercheur, mais ce n'est pas pour tout le monde.

Maintenant, qu'est-ce que ça veut dire ? Ça veut dire que la technologie va évoluer extrêmement rapidement. Ce qu'il faut apprendre, c'est apprendre à apprendre.

Parce que quand la technologie évolue, il faut apprendre de nouvelles choses de manière continue. Donc apprendre à apprendre, ça veut dire avoir des bases solides.

Et ça, c'est un avantage qu'on a en France, c'est qu'on a des bases de maths, de physique, etc. assez solides. Qui n'est pas le cas forcément de vos collègues américains ou dans d'autres pays.

Donc ça c'est un avantage sur lequel il faut construire. Mais ce que ça veut dire au niveau des cours à prendre par exemple,  c'est que si vous avez le choix entre Un cours pour apprendre à servir d'une nouvelle technologie,

 à programmer une application mobile sur iPhone ou autre. Si vous voulez le choix entre ça ou un cours de mécanique quantique, prenez mécanique quantique.

Vous avez l'impression que vous n'allez jamais vous servir la mécanique quantique si vous faites du génie civil. Mais en fait,  si,  parce que les méthodes qui ont été inventées dans le contexte de la mécanique quantique,  en fait,

 sont utilisées absolument partout. Par exemple,  je ne vais pas entrer dans ce genre de détails,  mais si on veut faire de l'inférence probabiliste dans ces systèmes comme ça,

 avec des variables latentes où il faut Essayer de trouver une distribution sur ces variables attentes ou alors gérer les incertitudes dans cette prédiction avec ce qu'on appelle les modèles de diffusion dont je n'ai pas parlé.

C'est ça qu'on utilise pour faire générer des images.

Les maths de ça sont des maths qui ont été développées par des physiciens au XXe siècle dans le contexte de la physique statistique et qui se reposent en fait sur la mécanique quantique aussi.

Certaines méthodes d'inférence probabiliste aussi se reposent sur des méthodes mathématiques très similaires à ce qu'on appelle les intégrales de chemin. Ils ont été développés par Richard Feynman après la seconde guerre mondiale.

Donc des méthodes de base. Apprenez des méthodes de base dont la durée de vie, la date d'opération est après la fin de votre carrière. D'accord ?

Et pas des technologies dont la durée de vie va être 5 ans et de toute façon va être de plus en plus courte parce que le progrès s'accélère. Apprenez à apprendre. Bonjour.

J'ai deux questions pour vous qui font écho en particulier à la précédente leçon inaugurale qu'on a eue il y a une semaine de cela,  de M.

Speaker 3:
Olivier Amant.

Speaker 1:
La première, c'est comment vous positionnez vis-à-vis du parallèle IA et crise climatique ? En particulier,  est-ce que vous pensez que l'IA peut nous aider à résoudre la crise climatique,

 en particulier en regard à la consommation énergétique mondiale qui ne cesse d'augmenter,  due à l'IA notamment ? Et ma deuxième question porte sur le paradigme robustesse et performance.

Vous avez énormément mentionné le fait qu'on essaie d'améliorer en continu les performances et l'efficacité des algorithmes,  notamment avec le GEPA. Est-ce que vous pensez que c'est un paradigme,  enfin,

 un concept plutôt qui est durable dans le temps ou ça risque plutôt de nous tendre vers une dépendance à ces technologies et faire face à des crises,  notamment par exemple avec Microsoft récemment,  mondiales,

 qui risquent de nous rendre plus vulnérables ? Merci. Ok, il y a 4 questions, au moins. Alors la dépendance par rapport à la technologie,  on est dépendant de la technologie,  c'est juste une autre étape dans cette dépendance,  mais bon,

 c'est déjà le cas,  on est complètement dépendant de la technologie. Donc je ne vois pas ça comme forcément un problème qualitativement différent. Ensuite, les problèmes énergétiques. Il y a plusieurs avis sur la question. La proportion de...

Parmi toute l'énergie consommée dans le monde,  la proportion qui est à l'heure actuelle consommée par les data centers est relativement faible. C'est de l'ordre de... L'ordre de 2 ou 3%. Alors ça va aller en croissant,

 parce qu'il y a un effort de construction de data center qui est absolument gigantesque,  à cause du fait qu'il faut faire tourner des systèmes d'IA. Ce n'est pas vraiment l'entraînement, c'est plutôt l'inférence.

C'est-à-dire qu'une fois que les systèmes d'IA sont entraînés,  pour répondre aux questions de tous les utilisateurs assez rapidement,  surtout dans un futur où tout le monde peut entraîner des lunettes intelligentes ou des choses comme ça,

 il faut beaucoup d'infrastructures. Donc c'est ça en fait que construisent Hyperscaler et tout ça, c'est des infrastructures.

Ça consomme beaucoup d'énergie et cette énergie n'est pas forcément disponible aux endroits où ces entreprises veulent construire ces data centers. Donc ce qu'elles font pour l'instant,

 c'est qu'elles mettent à côté de leurs data centers des turbines à gaz,  ce qui n'est pas vraiment bon pour les émissions. Mais beaucoup d'entre elles, en fait, investissent massivement dans le nucléaire. Et en fait,

 ça donne une nouvelle vie au nucléaire,  qui avait été plus ou moins abandonné,  certainement,  aux Etats-Unis,  en Allemagne,  et on n'est pas passé loin de l'abandonner en France.

Et les gens maintenant se disent, en fait, c'est le meilleur moyen de produire l'énergie dont on va avoir besoin. C'est basse émission, etc. Donc il y a un futur, probablement, assez brillant pour le nucléaire.

Peut-être pas la sorte de nucléaire à laquelle on est habitué en France. Les technologies EPR et tout ça qu'on a développées,  c'est peut-être plutôt des réacteurs de plus petite taille,  ce genre de choses. Et puis énergie renouvelable.

Mais le problème des énergies renouvelables, c'est qu'il faut trouver un moyen de stockage d'énergie à grande échelle. Parce que quand il n'y a pas de soleil ni de vent, il faut quand même produire l'énergie.

Donc pour ça, il faut pouvoir stocker l'énergie. On peut le faire avec des batteries, mais c'est assez limité. Donc les technologies, mais là c'est plutôt Jérôme qui spécialise les batteries, c'est pas moi.

En tout cas dans le temps, je ne sais pas si tu es toujours branché sur les batteries. Le moyen le plus efficace de stocker l'énergie, c'est sous forme d'hydrogène. Utiliser l'électricité pour séparer l'hydrogène de l'oxygène.

C'est un domaine dans lequel l'IA peut avoir un rôle. On n'a pas de méthode pour séparer efficacement l'hydrogène de l'oxygène qui puisse passer à l'échelle.

On peut le faire de manière efficace en utilisant des catalyseurs du genre de platine, mais c'est trop cher. J'ai des collègues, toute une équipe à Meta, qui s'appelle le groupe de chimie, dirigé par un certain Laris Zipnik.

Ils ont un projet ouvert en collaboration avec les universités,  peut-être certains d'entre vous veulent y collaborer,  qui s'appelle Open Catalyst Project,  c'est opencatalystproject.org je crois,

 dans lequel ils ont une grande base de données produite par simulation numérique Ce qu'on appelle DFT,  c'est simuler la chimie,  l'absorption de molécules d'eau sur des substrats divers et variés obtenus par simulation.

On peut utiliser ça comme donnée d'entraînement pour entraîner un réseau de neurones à prédire quelles vont être les propriétés de...

Speaker 2:
...

Speaker 1:
de catalyses d'un matériau ou d'un composé particulier.

Les promesses de l'IA dans la science des matériaux et la chimie sont énormes et c'est un domaine très prometteur et je pense que c'est un domaine qui devrait intéresser beaucoup de gens ici. Et sur la robustesse versus la performance ?

Speaker 2:
Ah oui !

Speaker 1:
Alors,  il y a une chose intéressante vis-à-vis des réseaux neurones,  c'est que justement,  les réseaux neurones sont plus ou moins,  par construction,  robustes. Si vous prenez un réseau neurone,  vous l'entraînez,

 et puis vous enlevez certains des paramètres,  vous trucidez certaines des unités qui sont dedans,  il marche à peu près pareil. Il se dégrade, mais il se dégrade progressivement.

Ce n'est pas très intéressant cette propriété pour l'instant parce qu'on n'a pas de système hardware. On simule ces systèmes sur des ordinateurs pas vraiment classiques, c'est des GPU, c'est très paralysé.

Mais pour que cette robustesse ait un intérêt,  il faudrait des implantations de ces réseaux neurones qui soient plus un peu comme le cerveau,  c'est-à-dire avec un neurone physique par neurone dans le.

Speaker 2:
Dans la zone ronde.

Speaker 1:
Et ça, ça n'existe pas encore. On n'a pas la technologie pour ça. Mais ces systèmes sont robustes en général.

Speaker 2:
Peut-être une dernière question.

Speaker 3:
Bonjour. Merci beaucoup pour la présentation très intéressante. J'avais une question. Je voulais savoir ce que vous pensiez de la dépendance de l'Europe par rapport à la technologie américaine. Le fait que l'année dernière,

 il y a eu deux prix Nobel de physique et de chimie par des équipes de Google. Je sais que les Français sont très présents sur la scène de l'IA,  notamment à travers l'équipe de Meta à Paris,  Mistral,  etc.

Mais malgré tout, on doit reconnaître qu'on est extrêmement dépendants dans un contexte mondial compliqué. Est-ce que vous pensez que l'Europe devrait jouer une carte ? Est-ce que les nouvelles générations devraient faire des startups ?

Qu'est-ce que vous pensez de l'avenir pour l'Europe, justement ?

Speaker 1:
Alors oui, question très importante. Alors d'abord,  il faut se dire que les prix Nobel de chimie dont vous parlez,  Demis Hassabis,  John Jumper et David Baker. David Baker est américain et les deux autres sont anglais.

Ils sont basés à Londres. Ils ne sont pas américains. Ils travaillent pour une entreprise américaine mais ils sont basés à Londres. Le modèle open source,

 le LLM open source produit par ou la famille de LLM open source produit par Meta est le résultat d'un projet de recherche à faire Paris par une douzaine de personnes. Presque tous français. Donc c'était l'ABA1 qui a été produit fin 2022,

 qui a été,  disons,  rendu disponible début 2023.  Et puis ensuite il y a eu l'AMA2,  etc. Et puis bon,  ensuite il y a eu une grosse organisation qui s'est branchée dessus,  avec des gens un peu partout en Europe,  aux États-Unis,  etc.

Mais l'origine, c'est un petit groupe de recherche d'une douzaine de personnes à Paris, presque tous français. Deux de ces personnes ont cofondé Mistral. Quelque chose que je voudrais vous dire aussi,  c'est qu'à Meta,  à Paris,

 dans le Labo de recherche de Paris,  FAIR,  qui est l'Organisation de recherche fondamentale,  a à peu près 500 à 600 personnes. Il y a plus de 100 personnes à Paris,  plutôt dans les 140.  Sur ces 140,

 il y en a 40 qui sont des étudiants doctorants en résidence. Et on en sort une douzaine par an. D'accord et en fait on va signer un accord justement qui permettra de faire ça un petit peu plus systématiquement avec le NPC.

Donc on n'a pas de complexe à avoir en Europe,  on a les talents et c'est ça en fait qui est le plus difficile à construire si on ne l'a pas,  c'est les talents. Maintenant ce qu'il faut c'est donner à ces talents les moyens de s'épanouir.

Et c'est là que l'Europe fait des progrès, mais n'est pas idéale. La grosse différence, c'est qu'aux États-Unis, par exemple, il y a un accès relativement facile au capital.

C'est-à-dire, si on veut monter une start-up et lever 500 millions, 1 milliard, ça se fait. En Europe, c'est plus difficile. Mais ça commence à changer. Donc je pense que le futur est en fait assez brillant. Et ce qu'il faut se dire aussi,

 c'est que ce que je disais au départ de la conférence,  c'est que On a assisté à quelques révolutions de l'IA ces dernières années. La dernière étant LLM IA Générative. Ce n'est pas la dernière. Comme j'en ai parlé,

 il y en aura une autre qui va arriver dans les 3 à 5 ans qui viennent,  juste au moment où vous allez finir. Un bon moment pour démarrer un doctorat. Et je pense que l'Europe a un rôle très important à jouer dans cette prochaine révolution.

Unknown Speaker:
Merci, Yann. Je propose qu'on applaudisse.

