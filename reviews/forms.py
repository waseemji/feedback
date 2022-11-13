from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label = "Your Name",max_length=100, error_messages={
#         "required":"Your name cannot be empty",
#         "max_length":"Bteer use your pet name"
#     })
#     review_text = forms.CharField(label="Your FeedBack", widget=forms.Textarea, max_length=250)
#     rating = forms.IntegerField(label="your Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = ['user_name','review_text','rating']
        fields = '__all__' #To include all fields in database
        # exclude = ['owner_comment']

        # We lose our labels when use direct from models
        labels = {
            "user_name":"Your name",
            "review_text" : "Your Feedback",
            "rating":"Your Rating"
        }

        error_messages = {
            "user_name": {
                "required" : "Your name cannot be empty",
                "max_length" : "Bteer use your pet name"
            }
        }