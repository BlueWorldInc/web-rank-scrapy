# Web Rank Scrapy

## Description:
<br>
Un application de scrapping, de transformation et de visualisation de données. L'application à pour but de télécharger les données du classement battle dev de 2021 sous format HTML. Ensuite de transformer ces données pour les mettres dans une base de données. Puis utilisé cette base pour visualiser les données dans un format graphique qui soit parlant.
<br>
<br>

## Etapes:
<br>

**Le projet sera divisé en trois partie:**

**La première partie** aura pour objectif de télécharger les données du site web sous format HTML. Pour cela je vais utiliser un outil qui va me permettre d'une part de télécharger la page sous format html (probablement curl) mais également un autre outil qui va me permettre de naviguer sur la page pour pouvoir passer à la page suivante (selenium). En effet il n'y a pas moyen de naviguer juste avec l'url sur la page, la page étant construit de manière dynamique.

**La seconde partie** aura pour objectif de transformer les pages htmls brut pour les intégrer dans une base de données. Pour faire cela j'ai besoin d'extraire les données des pages html sous format csv. Je vais utiliser pour cela (beautifull soup). Pour la partie intégration des données je vais utiliser panda.

**La troisième partie** consistera à utiliser la base de donnée pour visualiser les données. Pour cela je vais utiliser matplotlib pour réaliser les graphiques. Je vais crée une section, en amont, détaillant les graphiques que je voudrais voir pour pouvoir les réalisés par la suite.
<br>
<br>

## Graphiques souhaité:
<br>

Je pense qu'il y a plusieurs graphiques qui serait intéressant de voir.

* Le premier est le graphique présentant le nombre d'utilisateur par language, pour voir ceux qui sont les plus populaires.
* Le second graphique qui permettra de voir la distribution de ceux qui sont dans le top 100, dans le top 1000.
* Le troisième graphique qui permettra de voir la moyen des exos complétés par languages.
* Le quatrième graphique identique mais pour les personnes ayant au moins réalisés les 2 premiers exercice (qui était classé comme facile).
* Le cinquième la distribution de chaque language dans chaque catégorie (un % de la representation du language sur le % de representation moyenne pour les 10% les meilleurs, pour les 10% les plus mauvais, etc...).