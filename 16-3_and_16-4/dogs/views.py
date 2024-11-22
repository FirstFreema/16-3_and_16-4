from django.shortcuts import render, get_object_or_404, redirect
from .models import Breed, Dog, Pet
from .forms import PetForm
from django.http import JsonResponse

# View для отображения списка пород
def breed_list(request):
    """
    Отображает список всех пород животных.

    :param request: объект HTTP-запроса
    :return: рендер страницы с списком пород
    """
    breeds = Breed.objects.all()
    return render(request, 'dogs/breed_list.html', {'breeds': breeds})


# View для отображения списка собак
def dog_list(request):
    """
    Отображает список всех собак.

    :param request: объект HTTP-запроса
    :return: рендер страницы с списком собак
    """
    dogs = Dog.objects.all()
    return render(request, 'dogs/dog_list.html', {'dogs': dogs})


# Create (создание нового питомца)
def create_pet(request):
    """
    Создает нового питомца.
    """
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read_pets')  # Перенаправление на список питомцев
    else:
        form = PetForm()
    return render(request, 'dogs/pet_form.html', {'form': form})


# Read (просмотр списка питомцев)
def read_pets(request):
    """
    Отображает список всех питомцев.
    """
    pets = Pet.objects.all()
    return render(request, 'dogs/pet_list.html', {'pets': pets})


# Update (обновление информации о питомце)
def update_pet(request, pk):
    """
    Обновляет информацию о питомце.
    """
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('read_pets')  # Перенаправление на список питомцев
    else:
        form = PetForm(instance=pet)
    return render(request, 'dogs/pet_form.html', {'form': form})


# Delete (удаление питомца)
def delete_pet(request, pk):
    """
    Удаляет питомца.
    """
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('read_pets')  # Перенаправление на список питомцев
    return render(request, 'dogs/pet_confirm_delete.html', {'pet': pet})


# List View (отображение всех питомцев в формате JSON)
def list_view(request):
    """
    Возвращает список всех питомцев в формате JSON.
    """
    pets = Pet.objects.values()  # Получаем все объекты Pet как словари
    return JsonResponse({'pets': list(pets)}, safe=False)
