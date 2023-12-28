import pytest
from . import note


def test_natural_notes_produce_correct_numbers():
    assert note.to_number("C") == 0
    assert note.to_number("D") == 2
    assert note.to_number("E") == 4
    assert note.to_number("F") == 5
    assert note.to_number("G") == 7
    assert note.to_number("A") == 9
    assert note.to_number("B") == 11


def test_sharp_notes_produce_correct_numbers():
    assert note.to_number("C#") == 1
    assert note.to_number("D#") == 3
    assert note.to_number("E#") == 5
    assert note.to_number("F#") == 6
    assert note.to_number("G#") == 8
    assert note.to_number("A#") == 10
    assert note.to_number("B#") == 0


def test_double_sharp_notes_produce_correct_numbers():
    assert note.to_number("C##") == 2
    assert note.to_number("D##") == 4
    assert note.to_number("E##") == 6
    assert note.to_number("F##") == 7
    assert note.to_number("G##") == 9
    assert note.to_number("A##") == 11
    assert note.to_number("B##") == 1


def test_flat_notes_produce_correct_numbers():
    assert note.to_number("Cb") == 11
    assert note.to_number("Db") == 1
    assert note.to_number("Eb") == 3
    assert note.to_number("Fb") == 4
    assert note.to_number("Gb") == 6
    assert note.to_number("Ab") == 8
    assert note.to_number("Bb") == 10


def test_double_flat_notes_produce_correct_numbers():
    assert note.to_number("Cbb") == 10
    assert note.to_number("Dbb") == 0
    assert note.to_number("Ebb") == 2
    assert note.to_number("Fbb") == 3
    assert note.to_number("Gbb") == 5
    assert note.to_number("Abb") == 7
    assert note.to_number("Bbb") == 9


def test_lowercase_notes_should_raise_exception():
    with pytest.raises(Exception):
        note.to_number("a")


def test_invalid_notes_should_raise_exception():
    with pytest.raises(ValueError):
        note.to_number("H")

    with pytest.raises(ValueError):
        note.to_number("I")

    with pytest.raises(ValueError):
        note.to_number("J")


def test_uppercase_accidentals_should_raise_exception():
    with pytest.raises(ValueError):
        note.to_number("CBB")

    with pytest.raises(ValueError):
        note.to_number("CB")


def test_invalid_accidentals_should_raise_exception():
    with pytest.raises(ValueError):
        note.to_number("Cbbb")

    with pytest.raises(ValueError):
        note.to_number("C###")

    with pytest.raises(ValueError):
        note.to_number("C+")

    with pytest.raises(ValueError):
        note.to_number("C-")
