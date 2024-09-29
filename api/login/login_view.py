from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from api.models import Usuario

class LoginView(APIView):
    # Variable donde se almacena el nombre del template a usar en la vista GET
    template_view = 'view.html'
    
    def post(self, request):
        # Obtener el nombre de usuario y la contraseña del request
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Aquí se busca el usuario en la base de datos
        try:
            usuario = Usuario.objects.get(nombre_completo=username)  # Asumiendo que el username es el correo
        except Usuario.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # Verificar la contraseña (este es solo un ejemplo, deberías usar un método seguro)
        if usuario and usuario.nombre_completo == username:  # Asegúrate de que el modelo Usuario tenga un campo contraseña
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        # Renderizar el template para la vista GET
        return render(request, self.template_view)
