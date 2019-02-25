from django.shortcuts import redirect


def index(request):
    '''
This function is the view for:
showing the complete mineral list

for project 8, this view redirects to the letter filter for "A"
    '''
    return redirect('minerals:filter', query="A")
