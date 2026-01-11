def loading_bar(num: int) -> str:
    if num == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loaded_percents = num // 10
    not_loaded_percents = 10 - loaded_percents
    return f"{num}% [{'%' * loaded_percents}{'.' * not_loaded_percents}]\nStill loading..."

number = int(input())
print(loading_bar(number))