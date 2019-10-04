import pytest
from com.bbjp.converte_hora import converteHora

def test_converte_hora_none():
	assert converteHora(24,70) == None, "should be none"

def test_converte_hora_zero():
	assert converteHora(0,22) == '12:22 AM', "should be 12"

def test_converte_hora_12():
	assert converteHora(10,30) == "10:30 AM", "should be 10:30 AM"

def test_converte_hora_24():
	assert converteHora(13,13) == "01:13 PM", "should be 12"

