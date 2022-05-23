from django import forms

from exam.web.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')
        widgets = {
                'username': forms.TextInput(
                        attrs = {
                                'placeholder': 'Username',
                        },
                ),
                'email': forms.TextInput(
                        attrs = {
                                'placeholder': 'Email',
                        },
                ),
                'age': forms.TextInput(
                        attrs = {
                                'placeholder': 'Age',
                        },
                ),
        }


class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image_url', 'price')
        widgets = {
                'name': forms.TextInput(
                        attrs = {
                                'placeholder': 'Album Name',
                        },
                ),
                'artist': forms.TextInput(
                        attrs = {
                                'placeholder': 'Artist',
                        },
                ),

                'description': forms.Textarea(
                        attrs = {
                                'placeholder': 'Description',
                        },
                ),

                'image_url': forms.TextInput(
                        attrs = {
                                'placeholder': 'Image URL',
                        },
                ),
                'price': forms.TextInput(
                        attrs = {
                                'placeholder': 'Price',
                        },
                ),

        }


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'price')


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit = True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'price')


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit = True):
        self.instance.delete()
        Album.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()
