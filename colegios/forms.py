from django import forms
from colegios.models import Colegios

class ColegioForm(forms.ModelForm):
    class Meta:
        model = Colegios
        fields = ('rbd','nombre','regione','provincia','comuna','nroalumnos',
		'corporacion','web')
	
    def __init__(self,*args,**kwargs):
    	super(ColegioForm,self).__init__(*args,
    		**kwargs)
    	self.fields["nroalumnos"].required = True

