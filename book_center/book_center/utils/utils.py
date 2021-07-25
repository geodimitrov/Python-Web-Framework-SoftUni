from django import forms


#bot catcher
def bot_catcher(obj):
    bot_catcher = obj.cleaned_data['bot_catcher']

    if bot_catcher:
        raise forms.ValidationError('Bot detected')
    return bot_catcher


