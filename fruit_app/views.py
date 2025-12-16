from django.http import JsonResponse

# Create your views here.

def send_fruits(request):
    fruits = [
        {
            'name': 'Apfel',
            'gewicht': 150,
            'farbe': 'Rot'
        },
        {
            'name': 'Banane',
            'gewicht': 120,
            'farbe': 'Gelb'
        },
        {
            'name': 'Orange',
            'gewicht': 200,
            'farbe': 'Orange'
        },
        {
            'name': 'Erdbeere',
            'gewicht': 20,
            'farbe': 'Rot'
        },
        {
            'name': 'Traube',
            'gewicht': 5,
            'farbe': 'Lila'
        }
    ]
    
    return JsonResponse({'fruits': fruits})