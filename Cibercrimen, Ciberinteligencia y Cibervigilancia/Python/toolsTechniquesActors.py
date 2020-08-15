# -*- encoding: utf-8 -*-

# Find techniques and actors related to an specific tool.

from pyattck import Attck

attack = Attck()

# accessing tools
for tool in attack.enterprise.tools:

    if tool.name == "Cobalt Strike":
        print("==============================================")
        print(f"Tool: {tool.name} ")
        print("==============================================")
        for id, technique in enumerate(tool.techniques):
            print(f"Technique {id+1}: {technique.name}")
        print("==============================================")
        for id, actor in enumerate(tool.actors):
            print(f"Actor {id+1}: {actor.name}")

