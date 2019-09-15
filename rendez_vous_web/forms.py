from django import forms

CHOIX_DU_ROLE = [
    ('enseignant', 'Enseignant'),
    ('élève', 'Élève'),
]

class FormulaireDeConnexionUtilisateur(forms.Form):
    email = forms.EmailField(widget=forms.TextInput, label="Email")
    mot_de_passe = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")

class FormulaireDeCreationUtilisateur(forms.Form):
    nom = forms.CharField(widget=forms.TextInput, label='Nom', max_length=100)
    prenom = forms.CharField(widget=forms.TextInput, label='Prénom', max_length=100)
    mot_de_passe = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
    email = forms.EmailField(widget=forms.TextInput, label="Email")
    telephone = forms.CharField(widget=forms.TextInput, label="Téléphone")
    role = forms.ChoiceField(widget=forms.Select, choices=CHOIX_DU_ROLE)