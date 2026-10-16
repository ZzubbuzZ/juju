# Réglages de la charge et du shunt

Réglages de la batterie de servitude LiFePO4 (Humsienk 12 V 200 Ah Plus), du chargeur de quai Blue Smart IP67 12/17 et du SmartShunt. Décidés par les études [E](../etudes/E-batterie/README.md) (E-H1, E-H5) et [D](../etudes/D-shunt/README.md) (D-H1). Tous se règlent dans l'application VictronConnect.

**Rédigé le 16/10, avant la mise en service.** Les valeurs viennent de la fiche Humsienk (relevée le 05/10 dans [E-H1](../etudes/E-batterie/H1-lifepo4/proposition.md)) et des notices Victron. Le profil du chargeur a été saisi le 16/10 avec les valeurs ci-dessous (Q69). Les seuils du BMS restent à lire dans son application Bluetooth (Q68).

## Ce qu'il faut savoir avant de régler

- **La batterie demande** une charge à 14,4 V ± 0,2 V d'après la fiche en ligne, 14,6 V ± 0,2 V d'après la notice papier (Q68, 16/10), sous 40 A au plus, entre 0 et 55 °C. 14,4 V est dans les deux plages. Ni la fiche ni la notice ne donnent de floating ou de seuils du BMS : à lire dans l'application Bluetooth (Q68).
- **Le Blue Smart ne reçoit pas la tension du shunt.** Le réseau VE.Smart n'est pas pris en charge par les Blue Smart IP65 et IP67 (liste de compatibilité de Victron). Le chargeur règle donc la tension à ses bornes, et la batterie, au bout des 1,40 m de câble fourni (Q64, 16/10), voit environ 0,27 V de moins à 17 A ([dimensionnement](../commun/dimensionnement.md#chute-de-tension-du-chargeur-de-quai-1610)). Cette chute diminue avec le courant : environ 0,06 V à 4 A.
- **L'Orion XS, lui, est compatible VE.Smart.** Ses câbles sont courts : la compensation est un plus, pas une nécessité.
- **Le shunt se recale à 100 %** quand trois conditions durent ensemble : tension au-dessus de la « tension chargée », courant de charge sous le « courant de queue », pendant la « durée de détection ». Si le chargeur termine sa charge avant, le shunt ne se recale pas, et son état de charge dérive d'une charge à l'autre. **Le courant de queue du shunt doit donc être plus élevé que le courant auquel le chargeur arrête l'absorption.**

## Blue Smart IP67 12/17 : profil « HumsienkLiFePO4 »

Réglages → Préréglage batterie → « User defined » (défini par l'utilisateur), puis paramètres avancés. Profil créé par l'utilisateur le 16/10 avec ces valeurs (Q69).

| Paramètre | Valeur saisie | Pourquoi |
|---|---|---|
| Absorption | **14,4 V** | Dans la plage de la fiche en ligne comme dans celle de la notice papier (le mode Li-ion de Victron est à 14,2 V). À 17 A, la batterie ne voit qu'environ 14,1 V ; elle ne voit 14,4 V qu'en fin de charge, quand le courant a baissé. Ne pas monter plus haut : à faible courant la batterie reçoit vraiment la tension réglée, et une cellule déséquilibrée ferait couper le BMS. Si l'application du BMS donne une coupure en charge sous 14,6 V, revenir à 14,2 V (Q68). |
| Durée d'absorption | **Fixe, 2 h** au plus | Le mode adaptatif calcule la durée d'après la durée de la charge principale, une logique prévue pour le plomb. |
| Courant de fin d'absorption | **2 %, 4 A** (si le réglage est proposé) | La batterie est pleine dès que le courant tombe sous ce seuil. Il doit rester sous le courant de queue du shunt (8 A, voir plus bas). |
| Floating | **13,5 V** | Valeur de Victron pour le lithium : la batterie reste pleine sans être poussée. |
| Stockage | **13,5 V** ; passer à **13,3 V** pour de longues semaines au quai | Plus bas, la batterie reste un peu sous 100 %, ce qui ralentit son vieillissement. |
| Absorption répétée | **Désactivée** | Utile au plomb seulement. |
| Reconditionnement | **Désactivé** | **Impératif** : la surtension d'égalisation ferait couper le BMS et abîmerait les cellules. |
| Compensation de température | **Désactivée (0 mV/°C)** | Prévue pour le plomb (−16 mV/°C par défaut). Ne s'applique pas au lithium. |
| Courant maximal | **17 A** (mode normal) | Bien sous les 40 A recommandés. Le mode « faible courant » donne 6 A. |
| Charge par temps froid | sans réglage | L'IP67 n'a pas de sonde. Le BMS coupe la charge sous 0 °C, ce qui suffit en Méditerranée (Q47). |

**Contrôle à la mise en service** : en fin de charge, comparer la tension affichée par le chargeur et celle du shunt, au même moment. L'écart doit suivre la chute calculée (environ 0,016 V par ampère).

## Orion XS 12/12-50 A

Même tension d'absorption que le Blue Smart, **14,4 V**, et mêmes floating et compensation (13,5 V, désactivée). La batterie est ainsi chargée de la même façon au moteur et au quai. Ajouter l'Orion XS au réseau VE.Smart du shunt (tension de la batterie).

## SmartShunt 500 A

Réglages → Batterie, puis Alarmes et Divers. Les valeurs d'usine conviennent en LiFePO4, sauf le courant de queue, l'exposant de Peukert et le rendement de charge (notice Victron). La tension chargée et les alarmes sont adaptées à Juju.

### Batterie

| Paramètre | Usine | Valeur pour Juju | Pourquoi |
|---|---|---|---|
| Capacité de la batterie | 200 Ah | **200 Ah** | Capacité nominale de la Humsienk. |
| Tension chargée | 13,2 V | **14,0 V** | Victron conseille 0,2 à 0,3 V sous le floating, soit 13,2 V ici. Mais une LiFePO4 en charge dépasse 13,3 V bien avant d'être pleine, et le shunt se recalerait à 100 % sur une charge lente, au moteur ou plus tard au soleil. 14,0 V n'est atteint qu'en absorption : avec le Blue Smart, la batterie voit environ 14,3 V quand le courant tombe à 8 A. |
| Courant de queue | 4 % | **4 %, 8 A** | Garder la valeur d'usine. Elle reste au-dessus des 4 A où le chargeur arrête l'absorption : le shunt a le temps de se recaler avant que la tension retombe au floating. |
| Durée de détection de la charge | 3 min | **3 min** | Valeur d'usine. |
| Exposant de Peukert | 1,25 | **1,05** | Valeur de Victron pour le lithium. |
| Rendement de charge | 95 % | **99 %** | Une LiFePO4 restitue presque tout ce qu'elle reçoit. Avec 95 %, le shunt sous-estimerait la charge. |
| Seuil de courant | 0,10 A | **0,10 A** | Valeur d'usine. Les courants plus faibles sont ignorés, pour ne pas accumuler l'erreur de zéro. Une fuite qui compte (étude D, point 3) est bien au-dessus. |
| Durée de moyenne du temps restant | 3 min | **3 min** | Valeur d'usine. |
| Seuil de décharge | 50 % | **20 %** | Le temps restant est calculé jusqu'à ce seuil. 50 % est prévu pour le plomb. |
| Démarrage synchronisé | | **Oui** | Après une coupure de l'alimentation du shunt, il reprend son dernier état de charge. |

### Alarmes

| Alarme | Déclenchement | Fin | Pourquoi |
|---|---|---|---|
| État de charge bas | **20 %** | **30 %** | Laisse le temps de démarrer le moteur ou de délester avant la coupure du BMS (étude D, point 2). |
| Tension basse | **12,4 V** | **12,8 V** | Filet de sécurité si l'état de charge a dérivé : une LiFePO4 sous 12,4 V est presque vide. |
| Tension haute | **14,6 V** | **14,4 V** | Signale un chargeur mal réglé (mode plomb, reconditionnement, Dolphin rebranché par erreur) avant que le BMS ne coupe. |
| Entrée auxiliaire | **Batterie de démarrage** | | Tension de la batterie moteur (étude D, point 4). |
| Tension basse de la batterie de démarrage | **12,0 V** | **12,4 V** | Batterie au plomb à moitié vide, ou alternateur qui ne charge plus. |

Les seuils de tension sont à revoir avec la notice de la batterie (Q68).

### Mise en service

1. **Étalonnage du zéro**, avant la première utilisation. Aucun courant ne doit traverser le shunt : chargeurs débranchés, Orion XS arrêté, coupe-circuits de la servitude et des négatifs ouverts. Vérifier que le shunt lit 0,00 A environ, puis « Étalonner » (« Calibrate ») dans VictronConnect.
2. **Première charge complète au quai.** Si le shunt ne s'est pas recalé seul à la fin, le recaler avec « Synchroniser ».
3. **Pendant les premières semaines**, comparer l'état de charge du shunt et celui du BMS (application Humsienk), et vérifier que le shunt se recale à 100 % à chaque fin de charge au quai.

### Recalage dans la durée

Le shunt compte les ampères-heures. Sans recalage, sa petite erreur s'accumule d'un jour à l'autre. Au quai, chaque fin de charge le recale. En croisière au mouillage, ne compter sur lui qu'après une charge complète : au moins une fois par semaine ou toutes les deux semaines, au quai ou en longue route au moteur.

## Quelle source croire : le shunt ou le BMS ?

| Pour savoir… | Lire | Pourquoi |
|---|---|---|
| L'énergie qui reste (état de charge, Ah consommés, temps restant) | **le SmartShunt** | Il mesure les faibles courants au centième d'ampère, compte toutes les charges et toutes les consommations de la servitude, et se recale à chaque fin de charge. Les BMS de ce prix mesurent mal les petits courants. |
| La consommation d'un circuit, une fuite, l'historique | **le SmartShunt** | Seul à garder un historique exploitable (étude D, points 3 et 5). |
| La batterie moteur | **le SmartShunt** | Entrée auxiliaire. Le BMS ne la voit pas. |
| L'état des cellules : tension de chacune, écart entre elles, température, nombre de cycles | **le BMS** | Le shunt ne voit que la batterie entière. |
| Pourquoi la servitude est coupée : surcharge, décharge, surintensité, température | **le BMS** | C'est lui qui coupe ; le shunt ne fait que constater que la tension a disparu. |

**Règle pratique** : l'état de charge se lit sur le shunt. Si les deux lectures s'écartent nettement près du vide, se fier à la plus basse : c'est le BMS qui coupe, quoi qu'en dise le shunt. Un écart qui grandit de semaine en semaine signale un shunt mal recalé (voir plus haut) ou des cellules déséquilibrées (à lire dans l'application du BMS).

## Sources

- Blue Smart IP67 : [notice, caractéristiques techniques](https://www.victronenergy.com/media/pg/Blue_Smart_IP67_Charger_120V_manual/en/technical-specifications---bsc---psc.html) (mode Li-ion : 14,2 V, pas de floating, stockage 13,5 V ; compensation −16 mV/°C ; 6 A en faible courant), [configuration avancée](https://www.victronenergy.com/media/pg/Blue_Smart_IP67_Charger_230V_manual/en/advanced-configuration---bsc---psc.html), [fiche technique](https://www.victronenergy.com/upload/documents/Datasheet-Blue-Smart-IP67-Charger-230VAC-EN.pdf) (câbles rouge et noir de 1,5 m, fusible contre l'inversion de polarité). Pages ouvertes le 16/10.
- VE.Smart : [liste de compatibilité de Victron](https://www.victronenergy.com/media/pg/VE.Smart_Networking/en/ve-smart-networking-product-compatibility.html) (Orion XS compatible, Blue Smart IP65 et IP67 « pas encore »), [forum Victron](https://community.victronenergy.com/t/firmware-blue-smart-ip67-charger-and-ve-smart-networking/32098) (firmware v3.65, mai 2026). Pages ouvertes le 16/10.
- SmartShunt : [notice, réglages](https://www.victronenergy.com/media/pg/SmartShunt/en/all-features-and-settings.html) (valeurs d'usine, Peukert 1,05 pour le lithium, tension chargée, étalonnage du zéro). Page ouverte le 16/10.
