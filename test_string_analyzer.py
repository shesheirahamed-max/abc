from string_analyzer import analyze_digits_and_case

def test_standard_string():
    # Hello 2026 -> Uppercase 'H' (1), Digits 2+0+2+6 = 10
    result = analyze_digits_and_case("Hello 2026")
    assert result == (1, 10)

def test_no_matches_and_empty():
    assert analyze_digits_and_case("") == (0, 0)
    assert analyze_digits_and_case("python") == (0, 0)

def test_symbols_and_spaces():
    # #1 CAT & 9 DOGS -> Uppercase C, A, T, D, O, G, S (7), Digits 1+9 = 10
    result = analyze_digits_and_case(" #1 CAT & 9 DOGS ")
    assert result == (7, 10)