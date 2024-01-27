import random

def print_result(user_choice, ai_choice):
    if user_choice == ai_choice:
        return "Empate! Tentar novamente."
    elif (user_choice == "pedra" and ai_choice == "tesoura") or (user_choice == "papel" and ai_choice == "pedra") or (user_choice == "tesoura" and ai_choice == "papel"):
        return "Você venceu!"
    else:
        return "A IA venceu!"

def game():
    choices = ["pedra", "papel", "tesoura"]
    while True:
        user_choice = input("Escolha entre pedra, papel ou tesoura: ").lower()
        while user_choice not in choices:
            user_choice = input("Escolha inválida. Escolha entre pedra, papel ou tesoura: ").lower()
        ai_choice = random.choice(choices)
        print("Você escolheu:", user_choice)
        print("A IA escolheu:", ai_choice)
        result = print_result(user_choice, ai_choice)
        print(result)
        if "Tentar novamente." not in result:
            break

game()