from django import forms
from posts.models import Hashtag
HASHTAG_CHOICES = (
    (hashtag.id, hashtag.title) for hashtag in Hashtag.objects.all()
)



class PostCreateForm(forms.Form):
    title = forms.CharField(max_length=10)
    text = forms.CharField(widget=forms.Textarea)
    likes = forms.IntegerField()
    hashtag = forms.ChoiceField(choices=HASHTAG_CHOICES)



class CommentCreateForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Введите комментарий')






