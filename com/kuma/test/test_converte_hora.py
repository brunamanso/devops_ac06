import pylint

from com.kuma.converte_hora import converte_hora


def test_converte_hora_none():
	assert converte_hora(24, 70) is None, "should be none"


def test_converte_hora_zero():
	assert converte_hora(0, 22) == '12:22 AM', "should be 12"


def test_converte_hora_12():
	assert converte_hora(10, 30) == "10:30 AM", "should be 10:30 AM"


def test_converte_hora_24():
	assert converte_hora(13, 13) == "01:13 PM", "should be 12"
