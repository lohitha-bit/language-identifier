from django.shortcuts import render
from langdetect import detect

def index(request):
    result = None
    if request.method == 'POST':
        text = request.POST['text']
        result = detect(text)
    language_name = get_language_name(result)
    return render(request, 'index.html', {'result': language_name})

def get_language_name(result):
    switcher = {
        'af': "Afrikaans",
        'ar': "Arabic",
        'bg': "Bulgarian",
        'bn': "Bengali",
        'ca': "Catalan",
        'cs': "Czech",
        'cy': "Welsh",
        'da': "Danish",
        'de': "German",
        'el': "Greek",
        'en': "English",
        'es': "Spanish",
        'et': "Estonian",
        'fa': "Persian",
        'fi': "Finnish",
        'fr': "French",
        'ga': "Irish",
        'gl': "Galician",
        'gu': "Gujarati",
        'he': "Hebrew",
        'hi': "Hindi",
        'hr': "Croatian",
        'hu': "Hungarian",
        'id': "Indonesian",
        'is': "Icelandic",
        'it': "Italian",
        'ja': "Japanese",
        'jv': "Javanese",
        'kn': "Kannada",
        'ko': "Korean",
        'lt': "Lithuanian",
        'lv': "Latvian",
        'mk': "Macedonian",
        'ml': "Malayalam",
        'mr': "Marathi",
        'ne': "Nepali",
        'nl': "Dutch",
        'no': "Norwegian",
        'pa': "Punjabi",
        'pl': "Polish",
        'pt': "Portuguese",
        'ro': "Romanian",
        'ru': "Russian",
        'sk': "Slovak",
        'sl': "Slovenian",
        'so': "Somali",
        'sq': "Albanian",
        'sv': "Swedish",
        'sw': "Swahili",
        'ta': "Tamil",
        'te': "Telugu",
        'th': "Thai",
        'tl': "Tagalog",
        'tr': "Turkish",
        'uk': "Ukrainian"
    }
    return switcher.get(result, None)
