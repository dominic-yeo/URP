from app import greet


def test_greet_prints_name(capsys):
    greet("Ada")
    captured = capsys.readouterr()
    assert "Ada" in captured.out


