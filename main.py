import Calculator

if __name__ == '__main__':
    calc = Calculator.Calculator()
    calc.add_car(
        Calculator.Car("Mini Cooper", 35000, 6,
                       1000, 2000)
    )
    calc.add_car(
        Calculator.ElectricCar("Mini Cooper S", 37000,
                               7, 1200)
    )
    calc.add_car(
        Calculator.Car("Mini Clabman", 40000, 8,
                       1000, 2000)
    )
    calc.add_car(
        Calculator.Car("Mini Contryman", 48000, 8,
                       1000, 2000)
    )
    calc.print_cars()

    calc.remove_car("Mini Contryman")

    calc.print_cars()

    calc_two = Calculator.Calculator()

    calc_two.add_car(
        Calculator.Car("Volvo XC 90", 60000, 10,
                       1000, 2000)
    )

    calc_two.add_car(
        Calculator.Car("Volvo XC 60", 55000, 10,
                       1000, 2000)
    )

    calc_two.print_cars()

    calc_two.remove_car("Volvo XC 90")

    calc_two.print_cars()