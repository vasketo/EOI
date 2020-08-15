# -*- encoding: utf-8 -*-

# Find techniques of some specific tactic.

from pyattck import Attck

attack = Attck()

for tactic in attack.enterprise.tactics:

    if tactic.name == "Initial Access":
        print("==============================================")
        print(tactic.name)
        print("==============================================")
        
        for technique in tactic.techniques:
            print(technique.name)

