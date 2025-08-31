from django import forms
from .models import Atividade

class AdicionarAtividade(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['descricao', 'categoria', 'data_vencimento']  
        widgets = {
            'data_vencimento': forms.DateInput(attrs={'type': 'date'}),
        }

class EditarAtividade(forms.Form):
    opcoes_categoria = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('precisa ser feita', 'Precisa ser feita'),
    )

    Atividade = forms.CharField(max_length=400)
    categoria = forms.ChoiceField(choices=opcoes_categoria)