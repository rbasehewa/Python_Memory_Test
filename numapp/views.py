from django.http import JsonResponse

def find_odd_and_even_numbers(numbers):
    odd_numbers = []
    even_numbers = []
    
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return {
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "odd_count": len(odd_numbers),
        "even_count": len(even_numbers),
    }


def odd_even_view(request):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = find_odd_and_even_numbers(numbers)
    return JsonResponse(result)
