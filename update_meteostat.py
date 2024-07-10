import pandas as pd

file_path = '/Users/haddock_ana/Ironhack/final_project/Data/wine_analysis/Data/nulls_coordenadas.csv'

# Cargar el archivo CSV original
nulls_coords_df = pd.read_csv(file_path)


coordinates = {
    "Champagne Premier Cru": (49.0833, 3.8650),
    "Amarone della Valpolicella Classico": (45.5333, 10.9000),
    "Távora-Varosa": (41.0087, -7.7781),
    "Fino Sherry": (36.6844, -6.1266),
    "Oloroso Sherry": (36.6844, -6.1266),
    "Amontillado Sherry": (36.6844, -6.1266),
    "Romania Viniculture": (45.9432, 24.9668),
    "Beaujolais-Villages": (46.1407, 4.7217),
    "Saint-Émilion Grand Cru": (44.8915, -0.1557),
    "Côtes Catalanes": (42.6980, 2.8930),
    "Côtes du Roussillon Villages": (42.6980, 2.8930),
    "Pouilly-Fumé": (47.2850, 2.9200),
    "Côtes de Thongue": (43.5050, 3.2800),
    "Côtes-du-Rhône-Villages 'Plan de Dieu'": (44.1821, 4.9027),
    "Chablis 1er Cru 'Fourchaume'": (47.8500, 3.8000),
    "Mercurey 1er Cru 'Clos des Myglands'": (46.8561, 4.7489),
    "Chablis 1er Cru 'Côte de Lechet'": (47.8500, 3.8000),
    "Chablis 1er Cru 'Beauroy'": (47.8500, 3.8000),
    "Chablis 1er Cru 'Mont de Milieu'": (47.8500, 3.8000),
    "Pommard 1er Cru 'Clos des Epeneaux'": (47.0026, 4.7839),
    "Volnay 1er Cru 'Champans'": (47.0033, 4.7783),
    "Côtes de Thau": (43.4075, 3.6660),
    "Puligny-Montrachet 1er Cru 'Clos de la Mouchère'": (46.9522, 4.7528),
    "Côte de Beaune Villages": (47.0033, 4.7833),
    "Alsace Grand Cru 'Rosacker'": (48.1860, 7.3386),
    "Chablis 1er Cru 'Montmains'": (47.8500, 3.8000),
    "Nuits-Saint-Georges 1er Cru 'Aux Perdrix'": (47.1320, 4.9441),
    "Grands-Échezeaux Grand Cru": (47.1667, 4.9667),
    "Rully 1er Cru 'Cloux'": (46.8508, 4.7547),
    "Chablis Grand Cru 'Preuses'": (47.8500, 3.8000),
    "Aloxe-Corton 1er Cru 'Les Chaillots'": (47.0650, 4.8364),
    "Comté Tolosan": (44.8924, 1.2186),
    "Collines Rhodaniennes": (45.4243, 4.3302),
    "Côte de Nuits Villages": (47.1770, 4.9517),
    "Saint-Aubin 1er Cru 'Les Frionnes'": (46.9472, 4.7028),
    "Alsace Grand Cru 'Hengst'": (48.0500, 7.2333),
    "Sable de Camargue": (43.5392, 4.1367),
    "Chablis 1er Cru 'Vaillons'": (47.8500, 3.8000),
    "Chablis Grand Cru 'Bougros'": (47.8500, 3.8000),
    "Volnay 1er Cru 'Clos des Chênes'": (47.0000, 4.7800),
    "Chablis Grand Cru 'Blanchot'": (47.8500, 3.8000),
    "Givry 1er Cru 'Servoisine'": (46.8506, 4.7347),
    "Chassagne-Montrachet 1er Cru 'La Boudriotte'": (46.9272, 4.7389),
    "Gevrey-Chambertin 1er Cru 'Les Cazetiers'": (47.2303, 4.9611),
    "Clairette de Languedoc": (43.5149, 3.5374),
    "Chablis 1er Cru 'Côte de Jouan'": (47.8500, 3.8000),
    "Muscadet-Côtes de Grandlieu": (47.1715, -1.6032),
    "Gevrey-Chambertin 1er Cru 'Clos des Varoilles'": (47.2303, 4.9611),
    "Chambolle-Musigny 1er Cru 'Les Amoureuses'": (47.1853, 4.9511),
    "Grignan-les-Adhémar": (44.4417, 4.8453),
    "Beaujolais Supérieur": (46.1407, 4.7217),
    "Bordeaux Moelleux": (44.8378, -0.5792),
    "Alsace Grand Cru 'Sommerberg'": (48.1347, 7.2971),
    "Chassagne-Montrachet 1er Cru 'Les Grandes Ruchottes'": (46.9264, 4.7480),
    "Givry 1er Cru 'Cellier aux Moines'": (46.8506, 4.7347),
    "Savigny-lès-Beaune 1er Cru 'La Dominode'": (47.0687, 4.8334),
    "Côtes-du-Rhône-Villages 'Signargues'": (44.1041, 4.6920),
    "Vosne-Romanée 1er Cru 'Les Suchots'": (47.1739, 4.9508),
    "Santenay 1er Cru 'La Maladière'": (46.9258, 4.7186),
    "Montagny Premier Cru": (46.8243, 4.7097),
    "Volnay 1er Cru 'Les Caillerets'": (47.0033, 4.7783),
    "Volnay 1er Cru 'Clos des 60 Ouvrées'": (47.0033, 4.7783),
    "Corton Grand Cru 'Clos des Meix'": (47.0667, 4.8333),
    "Chablis Premier Cru": (47.8500, 3.8000),
    "Chambolle-Musigny 1er Cru 'Les Borniques'": (47.1853, 4.9511),
    "Puligny-Montrachet 1er Cru 'Les Combettes'": (46.9531, 4.7533),
    "Givry 1er Cru 'Clos Charle'": (46.8506, 4.7347),
    "Saint-Aubin 1er Cru 'Les Murgers des Dents de Chien'": (46.9472, 4.7028),
    "Saint-Aubin 1er Cru 'La Chatenière'": (46.9472, 4.7028),
    "Montagny 1er Cru 'Les Coeres'": (46.8243, 4.7097),
    "Chambolle-Musigny 1er Cru 'Les Sentiers'": (47.1853, 4.9511),
    "Charmes-Chambertin Grand Cru": (47.2333, 4.9528),
    "Beaune 1er Cru 'Les Teurons'": (47.0231, 4.8353),
    "Saint-Aubin 1er Cru 'Derrière chez Edouard'": (46.9472, 4.7028),
    "Givry 1er Cru 'Clos Marole'": (46.8506, 4.7347),
    "Terre Siciliane": (37.6000, 14.0154),
    "Aloxe-Corton 1er Cru 'Les Fournières'": (47.0650, 4.8364),
    "Puligny-Montrachet 1er Cru 'Les Folatières'": (46.9528, 4.7539),
    "Nuits-Saint-Georges 1er Cru 'Aux Chaignots'": (47.1320, 4.9441),
    "Chassagne-Montrachet 1er Cru 'La Maltroie'": (46.9264, 4.7480),
    "Mazis-Chambertin Grand Cru": (47.2333, 4.9528),
    "Gevrey-Chambertin 1er Cru 'Combe au Moine'": (47.2303, 4.9611),
    "Puligny-Montrachet 1er Cru 'Les Referts'": (46.9531, 4.7533),
    "Volnay 1er Cru 'En Chevret'": (47.0033, 4.7783),
    "Bordeaux Clairet": (44.8378, -0.5792),
    "Chassagne-Montrachet 1er Cru 'Les Chenevottes'": (46.9264, 4.7480),
    "Beaune 1er Cru 'Les Vignes Franches'": (47.0231, 4.8353),
    "Morey-Saint-Denis 1er Cru 'Les Ruchots'": (47.2036, 4.9606),
    "Chablis 1er Cru 'Vau Ligneau'": (47.8500, 3.8000),
    "Gevrey-Chambertin 1er Cru 'Aux Combottes'": (47.2303, 4.9611),
    "Chablis 1er Cru 'Vaulorent'": (47.8500, 3.8000),
    "Barbera d'Asti": (44.8976, 8.2030),
    "Gevrey-Chambertin 1er Cru 'Poissenot'": (47.2303, 4.9611),
    "Mercurey 1er Cru 'Clos des grands Voyens'": (46.8561, 4.7489),
    "Savigny-lès-Beaune 1er Cru 'Les Lavières'": (47.0687, 4.8334),
    "Alsace Grand Cru 'Furstentum'": (48.1456, 7.3000),
    "Alsace Grand Cru 'Mandelberg'": (48.1450, 7.3200),
    "Volnay 1er Cru 'Santenots'": (47.0033, 4.7783),
    "Puligny-Montrachet 1er Cru 'Le Cailleret'": (46.9531, 4.7533),
    "Nuits-Saint-Georges 1er Cru 'Les Damodes'": (47.1320, 4.9441),
    "Nuits-Saint-Georges 1er Cru 'Aux Murgers'": (47.1320, 4.9441),
    "Meursault 1er Cru 'Les Bouchères'": (46.9733, 4.7683),
    "Côtes-du-Rhône-Villages 'Massif d'Uchaux'": (44.2200, 4.8769),
    "Nuits-Saint-Georges 1er Cru 'Aux Vignerondes'": (47.1320, 4.9441),
    "Savigny-lès-Beaune 1er Cru 'Aux Guettes'": (47.0687, 4.8334),
    "Savigny-lès-Beaune 1er Cru 'Aux Serpentières'": (47.0687, 4.8334),
    "Chassagne-Montrachet 1er Cru 'Cailleret'": (46.9264, 4.7480),
    "Volnay 1er Cru 'Taille Pieds'": (47.0033, 4.7783),
    "Chablis Grand Cru 'Grenouilles'": (47.8500, 3.8000),
    "Savigny-lès-Beaune 1er Cru 'Aux Clous'": (47.0687, 4.8334),
    "Griotte-Chambertin Grand Cru": (47.2333, 4.9528),
    "Mercurey 1er Cru 'Sazenay'": (46.8561, 4.7489),
    "Chassagne-Montrachet 1er Cru 'Les Baudines'": (46.9264, 4.7480),
    "Vosne-Romanée 1er Cru 'Malconsorts'": (47.1739, 4.9508),
    "Volnay 1er Cru 'Clos de la Cave des Ducs'": (47.0033, 4.7783),
    "Alsace Grand Cru 'Pfersigberg'": (48.0500, 7.3000),
    "Chassagne-Montrachet 1er Cru 'Les Fairendes'": (46.9264, 4.7480),
    "Givry 1er Cru 'Les grands Pretans'": (46.8506, 4.7347),
    "Mercurey 1er Cru 'La Bondue'": (46.8561, 4.7489),
    "Nuits-Saint-Georges 1er Cru 'Les Hauts Pruliers'": (47.1320, 4.9441),
    "Vosne-Romanée 1er Cru 'Au Cros Parantoux'": (47.1739, 4.9508),
    "Morey-Saint-Denis 1er Cru 'Les Charrières'": (47.2036, 4.9606),
    "Morey-Saint-Denis 1er Cru 'Les Chaffots'": (47.2036, 4.9606),
     "Chassagne-Montrachet 1er Cru 'Les Petits Clos'": (46.9264, 4.7480),
    "Aloxe-Corton 1er Cru 'Clos du Chapître'": (47.0650, 4.8364),
    "Morey-Saint-Denis 1er Cru 'Clos Sorbe'": (47.2036, 4.9606),
    "Mercurey 1er Cru 'Le Clos L’Evêque'": (46.8561, 4.7489),
    "Bourgogne Côtes d’Auxerre": (47.8000, 3.5667),
    "Pommard 1er Cru 'Les Poutures'": (47.0000, 4.7833),
    "Chassagne-Montrachet 1er Cru 'Les Embazées'": (46.9264, 4.7480),
    "Alsace Grand Cru 'Sonnenglanz'": (48.1617, 7.3033),
    "Alsace Grand Cru 'Steingrubler'": (48.0170, 7.2900),
    "Santenay 1er Cru 'Clos Faubard'": (46.9258, 4.7186),
    "Beaune 1er Cru 'Les Chouacheux'": (47.0231, 4.8353),
    "Givry Premier Cru": (46.8506, 4.7347),
    "Pommard 1er Cru 'Les Grands Epenots'": (47.0000, 4.7833),
    "Gevrey-Chambertin 1er Cru 'Issarts'": (47.2303, 4.9611),
    "Pernand-Vergelesses 1er Cru 'Ile des Vergelesses'": (47.0667, 4.8375),
    "Morey-Saint-Denis 1er Cru 'La Riotte'": (47.2036, 4.9606),
    "Gevrey-Chambertin 1er Cru 'Cherbaudes'": (47.2303, 4.9611),
    "Alsace Grand Cru 'Marckrain'": (48.1617, 7.3033),
    "Corton Grand Cru 'Hautes Mourottes'": (47.0667, 4.8333),
    "Pacherenc du Vic-Bilh": (43.5180, -0.0590),
    "Vosne-Romanée 1er Cru 'Les Rouges'": (47.1739, 4.9508),
    "Chassagne-Montrachet 1er Cru 'La Romanée'": (46.9264, 4.7480),
    "Rosé des Riceys": (48.0958, 4.3603),
    "Gevrey-Chambertin 1er Cru 'La Romanée'": (47.2303, 4.9611),
    "Alsace Grand Cru 'Kaefferkopf'": (48.0861, 7.2892),
    "Alsace Grand Cru 'Wiebelsberg'": (48.4017, 7.4122),
    "Pommard 1er Cru 'Les Boucherottes'": (47.0000, 4.7833),
    "Alsace Grand Cru 'Vorbourg'": (47.5750, 7.3508),
    "Bourgogne Mousseux": (47.0500, 4.6167),
    "Saint-Aubin 1er Cru 'Sur le Sentier du Clou'": (46.9472, 4.7028),
    "Gevrey-Chambertin 1er Cru 'Clos Prieur'": (47.2303, 4.9611),
    "Rully 1er Cru 'Margotés'": (46.8508, 4.7547),
    "Chassagne-Montrachet 1er Cru 'Blanchot Dessus'": (46.9264, 4.7480),
    "Bourgogne Montrecul": (47.0000, 4.6167),
    "Vosne-Romanée 1er Cru 'Aux Brulées'": (47.1739, 4.9508),
    "Pernand-Vergelesses 1er Cru 'Sous Frétille'": (47.0667, 4.8375),
    "Volnay 1er Cru 'Fremiets'": (47.0033, 4.7783),
    "Coteaux du Vendômois": (47.7936, 1.0628),
    "Alsace Grand Cru 'Frankstein'": (48.3831, 7.4208),
    "Nuits-Saint-Georges 1er Cru 'Aux Boudots'": (47.1320, 4.9441),
    "Pernand-Vergelesses 1er Cru 'Clos Berthet'": (47.0667, 4.8375),
    "Chassagne-Montrachet 1er Cru 'Abbaye de Morgeot'": (46.9264, 4.7480),
    "Chambolle-Musigny 1er Cru 'Les Feusselottes'": (47.1853, 4.9511),
    "Savigny-lès-Beaune 1er Cru 'Les Haut Jarrons'": (47.0687, 4.8334),
    "Mercurey 1er Cru 'Les Crêts'": (46.8561, 4.7489),
    "Nuits-Saint-Georges 1er Cru 'Les Chaboeufs'": (47.1320, 4.9441),
    "Savigny-lès-Beaune 1er Cru 'Les Peuillets'": (47.0687, 4.8334),
    "Alsace Grand Cru 'Goldert'": (48.0861, 7.2892),
    "Chassagne-Montrachet 1er Cru 'Les Murées'": (46.9264, 4.7480),
    "Pommard 1er Cru 'Les Pézerolles'": (47.0000, 4.7833),
    "Nuits-Saint-Georges 1er Cru 'La Richemone'": (47.1320, 4.9441),
    "Pernand-Vergelesses 1er Cru 'Les Fichots'": (47.0667, 4.8375),
    "Nuits-Saint-Georges 1er Cru 'Les Didiers'": (47.1320, 4.9441),
    "Saint-Aubin 1er Cru 'Les Champlots'": (46.9472, 4.7028),
    "Pommard 1er Cru 'Les Arvelets'": (47.0000, 4.7833),
    "Pommard 1er Cru 'Les Chaponnières'": (47.0000, 4.7833),
    "Savigny-lès-Beaune 1er Cru 'Les Vergelesses'": (47.0687, 4.8334),
    "Beaune 1er Cru 'Les Bressandes'": (47.0231, 4.8353),
    "Nuits-Saint-Georges 1er Cru 'Les Vallerots'": (47.1320, 4.9441),
    "Savigny-lès-Beaune 1er Cru 'Les Talmettes'": (47.0687, 4.8334),
    "Chassagne-Montrachet 1er Cru 'Tête du Clos'": (46.9264, 4.7480),
    "Volnay 1er Cru 'Les Brouillards'": (47.0033, 4.7783),
    "Pommard 1er Cru 'Les Epenots'": (47.0000, 4.7833),
    "Vosne-Romanée 1er Cru 'En Orveaux'": (47.1739, 4.9508),
    "Pommard 1er Cru 'Les Fremiers'": (47.0000, 4.7833),
    "Pommard 1er Cru 'Les Combes Dessus'": (47.0000, 4.7833),
    "Givry 1er Cru 'Petit Marole'": (46.8506, 4.7347),
    "Beaune 1er Cru 'Les Aigrots'": (47.0231, 4.8353),
    "Chambolle-Musigny 1er Cru 'Les Gruenchers'": (47.1853, 4.9511),
    "Montagny 1er Cru 'Les Gouresses'": (46.8243, 4.7097),
    "Pommard 1er Cru 'Clos de la Commaraine'": (47.0000, 4.7833),
    "Chambolle-Musigny 1er Cru 'Aux Beaux Bruns'": (47.1853, 4.9511),
    "Gevrey-Chambertin 1er Cru 'La Bossière'": (47.2303, 4.9611),
    "Nuits-Saint-Georges 1er Cru 'Aux Bousselots'": (47.1320, 4.9441),
    "Nuits-Saint-Georges 1er Cru 'Les Vaucrains'": (47.1320, 4.9441),
    "Savigny-lès-Beaune 1er Cru 'Redrescul'": (47.0687, 4.8334),
    "Chambolle-Musigny 1er Cru 'La Combe d’Orveau'": (47.1853, 4.9511),
    "Valpolicella Ripasso": (45.5333, 10.9000),
    "Alsace Grand Cru 'Ollwiller'": (47.7758, 7.1375),
    "Saint-Aubin 1er Cru 'Sous Roche Dumay'": (46.9472, 4.7028),
    "Montagny 1er Cru 'Les Bonneveaux'": (46.8243, 4.7097),
    "Beaune 1er Cru 'Les Sizies'": (47.0231, 4.8353),
    "Vosne-Romanée 1er Cru 'Les Gaudichots'": (47.1739, 4.9508),
    "Maranges 1er Cru 'Le Clos des Loyères'": (46.8997, 4.6822),
    "Gevrey-Chambertin 1er Cru 'Au Closeau'": (47.2303, 4.9611),
    "Savigny-lès-Beaune 1er Cru 'Aux Gravains'": (47.0687, 4.8334),
    "Rully Premier Cru": (46.8508, 4.7547),
    "Pommard 1er Cru 'Les Charmots'": (47.0000, 4.7833),
    "Santenay 1er Cru 'La Comme'": (46.9258, 4.7186),
    "Rully 1er Cru 'Raclot'": (46.8508, 4.7547),
    "Montagny 1er Cru 'Vigne du Soleil'": (46.8243, 4.7097),
    "Alsace Grand Cru 'Zotzenberg'": (48.3600, 7.4142),
    "Volnay 1er Cru 'Clos du Verseuil'": (47.0033, 4.7783),
    "Morey-Saint-Denis 1er Cru 'Les Chenevery'": (47.2036, 4.9606),
    "Volnay 1er Cru 'Robardelle'": (47.0033, 4.7783),
    "Nuits-Saint-Georges 1er Cru 'Les Poulettes'": (47.1320, 4.9441),
    "Meursault 1er Cru 'Porusot'": (46.9733, 4.7683),
    "Alsace Grand Cru 'Mambourg'": (48.1456, 7.3000),
    "Montagny 1er Cru 'Les Vignes Derrière'": (46.8243, 4.7097),
    "Alsace Grand Cru 'Zinnkoepfle'": (47.5750, 7.3508),
    "Vougeot 1er Cru 'Les Crâs'": (47.1881, 4.9547),
    "Montagny 1er Cru 'Les Bouchots'": (46.8243, 4.7097),
    "Alsace Grand Cru 'Steinert'": (48.0842, 7.3078),
    "Pommard 1er Cru 'Les Petits Epenots'": (47.0000, 4.7833),
    "Alsace Grand Cru 'Hatschbourg'": (48.0247, 7.3156),
    "Coteaux-d'Ensérune": (43.3588, 3.2158),
    "Pommard 1er Cru 'En Largillière'": (47.0000, 4.7833),
    "Coteaux Champenois": (49.0675, 3.9583),
    "Nuits-Saint-Georges 1er Cru 'Les Cailles'": (47.1320, 4.9441),
    "Aloxe-Corton 1er Cru 'Les Valozières'": (47.0650, 4.8364),
    "Pommard 1er Cru 'La Platière'": (47.0000, 4.7833),
    "Pernand-Vergelesses 1er Cru 'Vergelesses'": (47.0667, 4.8375),
    "Alsace Grand Cru 'Froehn'": (48.0822, 7.3242),
    "Morey-Saint-Denis 1er Cru 'Les Sorbes'": (47.2036, 4.9606),
    "Mercurey 1er Cru 'Clos Voyens'": (46.8561, 4.7489),
    "Gevrey-Chambertin 1er Cru 'Champonnet'": (47.2303, 4.9611),
    "Rully 1er Cru 'Chapitre'": (46.8508, 4.7547),
    "Savigny-lès-Beaune 1er Cru 'Les Narbantons'": (47.0687, 4.8334),
    "Rully 1er Cru 'Vauvry'": (46.8508, 4.7547),
    "Chambolle-Musigny 1er Cru 'Les Fuées'": (47.1853, 4.9511),
    "Mercurey 1er Cru 'Clos des Barraults'": (46.8561, 4.7489),
    "Pommard 1er Cru 'Les Saussilles'": (47.0000, 4.7833),
    "Comtés Rhodaniens": (46.1740, 4.8251),
    "Gevrey-Chambertin 1er Cru 'Les Goulots'": (47.2303, 4.9611),
    "Alsace Grand Cru 'Kanzlerberg'": (48.1433, 7.2747),
    "Montagny 1er Cru 'Les Burnins'": (46.8243, 4.7097),
    "Montagny 1er Cru 'Les Resses'": (46.8243, 4.7097),
    "Roussette du Bugey": (45.8733, 5.3877),
    "Beaune 1er Cru 'Champs Pimont'": (47.0231, 4.8353),
    "Vins des Allobroges": (45.8733, 6.2236),
    "Coteaux des Baronnies": (44.3726, 5.2271),
    "Montagny 1er Cru 'Montorge'": (46.8243, 4.7097),
    "Gevrey-Chambertin 1er Cru 'Craipillot'": (47.2303, 4.9611),
    "Montagny 1er Cru 'Les Chaniots'": (46.8243, 4.7097),
    "Volnay 1er Cru 'Le Ronceret'": (47.0033, 4.7783),
    "Savigny-lès-Beaune 1er Cru 'Les Rouvrettes'": (47.0687, 4.8334),
    "Bienvenues-Bâtard-Montrachet Grand Cru": (46.9264, 4.7480),
    "Chassagne-Montrachet 1er Cru 'En Cailleret'": (46.9264, 4.7480),
    "Beaune 1er Cru 'Blanches Fleurs'": (47.0231, 4.8353),
    "Alsace Grand Cru 'Moenchberg'": (48.3722, 7.4689),
    "Montagny 1er Cru 'L'epaule'": (46.8243, 4.7097),
    "Bourgogne Passe-tout-grains": (47.0514, 4.3839),
    "Auxey-Duresses 1er Cru 'Les Duresses'": (46.9750, 4.7469),
    "Montagny 1er Cru 'Les Platieres'": (46.8243, 4.7097),
    "Pernand-Vergelesses 1er Cru 'En Caradeux'": (47.0667, 4.8375),
    "Chablis 1er Cru 'Les Beauregards'": (47.8500, 3.8000),
    "Meursault 1er Cru 'Les Caillerets'": (46.9733, 4.7683),
    "Saint-Aubin 1er Cru 'Pitangeret'": (46.9472, 4.7028),
    "Srednja I Juzna Dalmacija": (43.1614, 17.0655),
    "Bolgheri Sassicaia": (43.2569, 10.6231),
    "Chianti Rùfina": (43.8415, 11.4677),
    "Amarone della Valpolicella": (45.5833, 10.8667),
    "Valpolicella Classico": (45.5333, 10.9000),
    "Irpinia Campi Taurasini": (40.9312, 14.9820),
    "Soave Classico": (45.4333, 11.2500),
    "Valpolicella Ripasso Classico": (45.5333, 10.9000),
    "Aglianico del Vulture": (40.9333, 15.6167),
    "Amarone della Valpolicella Valpantena": (45.5333, 10.9000),
    "Carignano del Sulcis": (39.1833, 8.5833),
    "Teroldego Rotaliano": (46.2167, 11.1000),
    "Moscato d'Asti": (44.7353, 8.2744),
    "Bardolino Classico": (45.5500, 10.7167),
    "Rosso Conero Riserva": (43.5000, 13.5833),
    "Dolcetto d'Alba": (44.7000, 8.0333),
    "Trebbiano d'Abruzzo": (42.3500, 14.1667),
    "Vigneti delle Dolomiti": (46.0667, 11.1500),
    "Montepulciano d'Abruzzo Colline Teramane": (42.7500, 13.8333),
    "Falerno del Massico": (41.2061, 13.9514),
    "Verdicchio di Matelica Riserva": (43.2500, 13.0167),
    "Coste della Sesia": (45.6333, 8.1500),
    "Falanghina del Beneventano": (41.1333, 14.7833),
    "Recioto della Valpolicella Classico": (45.5833, 10.8667),
    "Brachetto d'Acqui": (44.6750, 8.4689),
    "Vermentino di Gallura": (40.8872, 9.4033),
    "Oltrepò Pavese": (45.0100, 9.1856),
    "Falanghina del Sannio": (41.1667, 14.7833),
    "Sforzato della Valtellina": (46.1500, 9.8833),
    "Verdicchio dei Castelli di Jesi Riserva": (43.5333, 13.0500),
    "Vin Santo del Chianti Classico": (43.5000, 11.3167),
    "Primitivo di Manduria Dolce Naturale": (40.3991, 17.6377),
    "Recioto della Valpolicella": (45.5833, 10.8667),
    "Montello e Colli Asolani": (45.8333, 11.9667),
    "Corti Benedettine del Padovano": (45.4167, 11.8833),
    "Cerasuolo d'Abruzzo": (42.3500, 14.1667),
    "Colli Tortonesi": (44.8908, 8.8663),
    "Terre del Volturno": (41.0667, 14.2000),
    "Colli del Limbara": (40.9031, 9.1458),
    "Colline Teatine": (42.3500, 14.4167),
    "Colline Pescaresi": (42.4608, 14.2142),
    "Atesino delle Venezie": (45.7000, 11.5000),
    "Trevenezie": (45.5000, 12.1000),
    "Valpolicella Valpantena": (45.5500, 11.0167),
    "Bonarda dell'Oltrepo Pavese": (45.1833, 9.3333),
    "Dolcetto d'Asti": (44.8953, 8.2042),
    "Grignolino del Monferrato Casalese": (45.0600, 8.4267),
    "Grignolino d'Asti": (44.8667, 8.2067),
    "Ansonica Costa dell'Argentario": (42.4542, 11.2092),
    "Vin Santo del Chianti": (43.5000, 11.3167),
    "Recioto di Soave Classico": (45.4500, 11.2500),
    "Buttafuoco dell'Oltrepo Pavese": (45.0167, 9.3167),
    "Gutturnio": (44.9333, 9.7167),
    "Colli Orientali del Friuli Picolit": (46.0833, 13.3833),
    "Dolcetto d'Acqui": (44.6769, 8.4742),
    "Colline Novaresi": (45.4667, 8.6333),
    "Colli Euganei Fior d'Arancio": (45.3000, 11.7000),
    "Colli Aprutini": (42.3500, 13.5000),
    "Terre degli Osci": (41.8000, 14.6667),
    "Falerio Pecorino": (43.0333, 13.4833),
    "Colli Trevigiani": (45.6667, 12.1667),
    "Curtefranca": (45.6053, 10.0269),
    "Colli Bolognesi Classico Pignoletto": (44.4667, 11.2667),
    "Candia dei Colli Apuani": (44.0833, 10.0667),
    "Oltrepo Pavese Metodo Classico": (45.0100, 9.1856),
    "Valli Ossolane": (46.1333, 8.3000),
    "Moldova Viniculture": (47.4116, 28.3699),
    "Dominio de Valdepusa": (39.8047, -4.1822),
    "Getariako Txakolina": (43.2767, -2.1967),
    "Pedro Ximénez Sherry (PX)": (37.1765, -6.0522),
    "Pago Florentino": (39.3903, -3.1381),
    "Valles de Sadacia": (42.3333, -2.3333),
    "Granada Sur-Oeste": (37.1882, -3.6067),
    "Cream Sherry": (36.7783, -6.3533),
    "Palo Cortado Sherry": (36.6836, -6.1261),
    "Dalmatian Coast": (43.1728, 17.6258),
    "Breedekloof": (-33.6820, 19.2032),
    "Voor Paardeberg": (-33.5333, 18.9333),
    "Southern Fieurieu": (-35.4667, 138.6000),
    "Savigny-lès-Beaune 1er Cru 'Les Marconnets'": (47.0687, 4.8334),
    "Twenty Mile Bench": (43.1643, -79.2856),
    "Short Hills Bench": (43.1090, -79.2462),
    "Zenatta": (40.7619, 14.2506),
    "Pangeon": (41.0667, 24.3667),
    "Amyndeon": (40.6833, 21.6333),
    "Slopes of Meliton": (40.0889, 23.7589),
    "Wiener Gemischter Satz": (48.2000, 16.3500),
    "Dealurile Olteniei": (44.3333, 23.8167),
    "Les Coteaux de l’Atlas": (31.6315, -8.0083),
    "Bündner Herrschaft": (46.9833, 9.5333),
    "Upper Thrace": (42.5000, 25.0000),
    "Neusiedlersee-Hügelland": (47.8333, 16.7167),
    "Povardarie": (41.6667, 21.9333),
    "Commandaria": (34.7720, 32.4252),
    "Južnoslovenská": (47.9333, 18.1667),
    "Slopes of Paiko": (40.8500, 22.2833),
    "Heuvellandse Wijn": (50.8212, 5.8888),
    "Subotica-Horgos": (46.1000, 19.6667),
    "Slopes of Egialia": (38.1667, 22.2333),
    "Trakiiska Nizina": (42.1833, 25.3333),
    "Cotes de l'Orbe": (46.6667, 6.5167),
    "Shamakha": (40.6347, 48.6403),
    "Magnissia": (39.3795, 22.9270),
    "Haspengouwse Wijn": (50.7667, 5.1667),
    "Westschweiz": (46.8182, 8.2275)
}



# Añadir las coordenadas al DataFrame
for region, (lat, lon) in coordinates.items():
    nulls_coords_df.loc[nulls_coords_df['RegionName'] == region, 'Latitude'] = lat
    nulls_coords_df.loc[nulls_coords_df['RegionName'] == region, 'Longitude'] = lon

updated_file_path = '/mnt/data/nulls_coordenadas_updated.csv'
nulls_coords_df.to_csv(updated_file_path, index=False)

updated_file_path