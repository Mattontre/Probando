from django.shortcuts import render

def certificado_view(request):
	return render(request, "appcertificado/certificado.html")
