def test_fizzBuzz():
    assert fizzBuzz(1) == "1"
    assert fizzBuzz(3) == "Fizz"
    assert fizzBuzz(5) == "Buzz"
    assert fizzBuzz(15) == "FizzBuzz"
    assert fizzBuzz(7) == "7"
    assert fizzBuzz(30) == "FizzBuzz"

if __name__ == "__main__":
    test_fizzBuzz()
    print("Tous les tests sont réussis !")