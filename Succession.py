from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
import sys

def long(ch):
    """Calcule la longueur d'une chaîne de caractères."""
    compteur = 0
    for _ in ch:
        compteur += 1
    return compteur

def verif_saisie(ch):
    """Vérifie si la chaîne est un entier positif."""
    n_ch = long(ch)
    return n_ch > 0 and ch.isdecimal()

def trier_chiffres(ch):
    """Trie les chiffres d'une chaîne de caractères dans l'ordre croissant.

    Implémentation par tri à bulles manuel sur la chaîne (les chaînes étant
    immutables en Python, on les reconstruit par tranches lors d'une permutation).
    Aucun appel à sort() ni à join() — non listés dans le programme officiel.
    """
    n = long(ch)
    echange = True
    while (echange == True) and (n != 1):
        echange = False
        for i in range(n - 1):
            if ch[i] > ch[i + 1]:
                # Permutation par reconstruction (la chaîne est immutable)
                ch = ch[:i] + ch[i + 1] + ch[i] + ch[i + 2:]
                echange = True
        n = n - 1
    return ch

def Verifier(m, n):
    """Vérifie si M et N forment une succession parfaite."""
    # Concaténation et tri des chiffres
    ch_concat = str(m) + str(n)
    ch_trie = trier_chiffres(ch_concat)

    # Suppression des doublons pour vérifier la succession
    ch_unique = ""
    n_ch_trie = long(ch_trie)
    if n_ch_trie > 0:
        ch_unique = ch_trie[0]
        for i in range(1, n_ch_trie):
            if ch_trie[i] != ch_trie[i-1]:
                ch_unique += ch_trie[i]

    # Vérification de la succession parfaite (avec drapeau, sans break)
    est_parfaite = True
    n_ch_unique = long(ch_unique)
    if n_ch_unique <= 1:
        est_parfaite = True
    else:
        i = 0
        while (i < n_ch_unique - 1) and est_parfaite:
            if int(ch_unique[i+1]) - int(ch_unique[i]) != 1:
                est_parfaite = False
            i = i + 1

    # Formatage du message de résultat
    res = f"{m} et {n}"
    if est_parfaite:
        res += f" forment une succession parfaite ({ch_unique})"
    else:
        res += f" ne forment pas une succession parfaite ({ch_trie})"
    return res

def Play():
    """Module principal exécuté au clic du bouton Vérifier."""
    chm = w.m.text()
    chn = w.n.text()

    if not verif_saisie(chm) or not verif_saisie(chn):
        Msg = 'Veuillez introduire 2 entiers positifs'
    else:
        m = int(chm)
        n = int(chn)
        Msg = Verifier(m, n)

    w.res.setText(Msg)

def Reset():
    """Efface les champs de saisie et le résultat."""
    w.m.clear()
    w.n.clear()
    w.res.clear()

# --- Programme Principal ---
app = QApplication(sys.argv)
w = loadUi("InterfaceSuccession.ui")
w.show()
# Connexion des signaux aux slots
w.verif.clicked.connect(Play)
sys.exit(app.exec_())