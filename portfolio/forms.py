from django import forms


class ContactForm(forms.Form):
    """Formulario de contacto"""

    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 bg-gray-800/50 border border-gray-700 rounded-lg focus:outline-none focus:border-blue-500 transition-colors text-white placeholder-gray-400',
            'placeholder': 'Tu nombre'
        })
    )

    correo = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-3 bg-gray-800/50 border border-gray-700 rounded-lg focus:outline-none focus:border-blue-500 transition-colors text-white placeholder-gray-400',
            'placeholder': 'tu@email.com'
        })
    )

    asunto = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 bg-gray-800/50 border border-gray-700 rounded-lg focus:outline-none focus:border-blue-500 transition-colors text-white placeholder-gray-400',
            'placeholder': 'Asunto del mensaje'
        })
    )

    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full px-4 py-3 bg-gray-800/50 border border-gray-700 rounded-lg focus:outline-none focus:border-blue-500 transition-colors text-white placeholder-gray-400',
            'placeholder': 'Escribe tu mensaje aquí...',
            'rows': 6
        })
    )
