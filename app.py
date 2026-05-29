def calculate_project_price(hours, hourly_rate, complexity="medium"):
    """Рассчитывает стоимость проекта в зависимости от сложности."""
    base_price = hours * hourly_rate
    
    if complexity == "high":
        coefficient = 1.3  # +30% за сложность
    elif complexity == "low":
        coefficient = 0.9  # -10% скидка
    else:
        coefficient = 1.0
        
    final_price = base_price * coefficient
    return round(final_price, 2)

if __name__ == "__main__":
    print("--- Калькулятор стоимости проекта ---")
    h = float(input("Введите количество часов: "))
    rate = float(input("Введите ставку в час ($): "))
    comp = input("Сложность (low, medium, high): ").strip().lower()
    
    total = calculate_project_price(h, rate, comp)
    print(f"\nИтоговая стоимость проекта: ${total}")
    print("Stariy put")