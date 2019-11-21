Mbaïressem Gondjé Hypolite 18A920Fs

#Class compte_Gré_a_Gré
    #constructeur
Def_init_(self,Mr=0.0,solde=0.0):
Self._mt=mt
Self._solde=solde
    #Methode d'affichage du solde d'abord avant de commencer
Def._str_(self):
Return "solde  disponible {0}".format(self.solde)
    #Methode d'affichage du solde qui sera
Utiliser après avoir fait un versement ou un retrait
Def infoSolde()
 Print("virement de {0} FCFA effectué
!". format (mt))
Self.infoSolde()
     #Methode versement
Def versement (self.mt):
Self._solde+=Mr
Print("versement de {0}FCFA effectué
!. format (mt))
Self.infoSolde()
     #Methode retrait
Def retrait (self.mt)
  If(mt>solde):
Print("solde insuffisant")
 Else
Self._solde-=mt
Print("le montant débité est de {0}FCFA."format (mt)
