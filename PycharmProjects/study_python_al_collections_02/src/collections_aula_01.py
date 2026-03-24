usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(len(assistiram))
print(*assistiram, sep='  ')

print(set(assistiram))

assistiram = set(usuarios_data_science) | set(usuarios_machine_learning)
print(assistiram)

assistiram = set(usuarios_data_science) & set(usuarios_machine_learning)
print(assistiram)

assistiram = set(usuarios_data_science) - set(usuarios_machine_learning)
print(assistiram)

assistiram = set(usuarios_data_science) ^ set(usuarios_machine_learning)
print(assistiram)