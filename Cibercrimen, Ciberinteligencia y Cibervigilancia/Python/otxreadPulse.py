# -*- encoding: utf-8 -*-

# Get all the indicators associated with a pulse

from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes

otx = OTXv2("")

indicators = otx.get_pulse_indicators("5ef84d895d118c6dedb442c0")
for indicator in indicators:
    print (indicator["type"], indicator["indicator"].replace("htt","hxx"))


