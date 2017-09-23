class RotorsConfig:

    key_binder_R = [2, 1, 5, 6, 3, 4, 21, 14, 15, 20, 22, 26, 17, 8, 9, 19, 13, 23, 16, 10, 7, 11, 18, 25, 24, 12]
    key_binder_M = [8, 5, 13, 7, 2, 21, 4, 1, 20, 22, 26, 17, 3, 19, 24, 18, 12, 16, 14, 9, 6, 10, 25, 15, 23, 11]
    key_binder_L = [5, 13, 24, 17, 1, 11, 15, 20, 22, 26, 6, 23, 2, 18, 7, 21, 4, 14, 25, 8, 16, 9, 12, 3, 19, 10]
    key_binder_U = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    rotor_R = {k:v for k, v in zip([i for i in range(1, 27)], key_binder_R)}
    rotor_M = {k:v for k, v in zip([i for i in range(1, 27)], key_binder_M)}
    rotor_L = {k:v for k, v in zip([i for i in range(1, 27)], key_binder_L)}
    rotor_U = {k:v for k, v in zip([i for i in range(1, 27)], key_binder_U)}



class CipheringSteps:

    def step_R(value, R):

        if value <= (26 - (R - 1)):
            value = value + (R - 1)
        else:
            value = value - (26 - (R - 1))
        for key in RotorsConfig.rotor_R:
            if value == key:
                value = RotorsConfig.rotor_R[key]
                break
        if value > (R - 1):
            value = value - (R - 1)
        else:
            value = value + (26 - (R - 1))
        return value


    def step_M(value, M):

        if value <= (26 - (M - 1)):
            value = value + (M - 1)
        else:
            value = value - (26 - (M - 1))
        for key in RotorsConfig.rotor_M:
            if value == key:
                value = RotorsConfig.rotor_M[key]
                break
        if value > (M - 1):
            value = value - (M - 1)
        else:
            value = value + (26 - (M - 1))
        return value


    def step_L(value, L):

        if value <= (26 - (L - 1)):
            value = value + (L - 1)
        else:
            value = value - (26 - (L - 1))
        for key in RotorsConfig.rotor_L:
            if value == key:
                value = RotorsConfig.rotor_L[key]
                break
        if value > (L - 1):
            value = value - (L - 1)
        else:
            value = value + (26 - (L - 1))
        return value


    def step_U(value):

        for key in RotorsConfig.rotor_U:
            if value == key:
                value = RotorsConfig.rotor_U[key]
                break
        return value



class Ciphering:

    def ciphering(value, R, M, L):

        value = CipheringSteps.step_R(value, R)
        value = CipheringSteps.step_M(value, M)
        value = CipheringSteps.step_L(value, L)
        value = CipheringSteps.step_U(value)
        value = CipheringSteps.step_L(value, L)
        value = CipheringSteps.step_M(value, M)
        value = CipheringSteps.step_R(value, R)
        return value


    def rotors_turning(R, M, L):

        if R < 26:
            R = R + 1
        elif M < 26:
            R = 1
            M = M + 1
        elif L < 26:
            R = 1
            M = 1
            L = L + 1
        else:
            R = 1
            M = 1
            L = 1
        return R, M, L



class Mechanics:

    @classmethod
    def rotors_start(cls, R, M, L):
        cls.R, cls.M, cls.L = R, M, L

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encode = {k:v for k, v in zip(alphabet, [i for i in range(1, 27)])}
    decode = {k:v for k, v in zip([i for i in range(1, 27)], alphabet)}

    def letter_encoding(R, M, L):

        for key in Mechanics.encode:
            if R == key:
                R = Mechanics.encode[key]
        for key in Mechanics.encode:
            if M == key:
                M = Mechanics.encode[key]
        for key in Mechanics.encode:
            if L == key:
                L = Mechanics.encode[key]
        return R, M, L


    def letter_decoding(R, M, L):

        for key in Mechanics.decode:
            if R == key:
                R = Mechanics.decode[key]
        for key in Mechanics.decode:
            if M == key:
                M = Mechanics.decode[key]
        for key in Mechanics.decode:
            if L == key:
                L = Mechanics.decode[key]
        return R, M, L


    def ciphering(letter):

        for key in Mechanics.encode:
            if letter == key:
                value = Mechanics.encode[key]
                break
        value = Ciphering.ciphering(value, Mechanics.R, Mechanics.M, Mechanics.L)
        Mechanics.R, Mechanics.M, Mechanics.L = Ciphering.rotors_turning(Mechanics.R, Mechanics.M, Mechanics.L)
        for key in Mechanics.decode:
            if value == key:
                letter = Mechanics.decode[key]
                break
        return letter



class Main:

    def ciphering(input_text):

        output_text = ""
        for letter in input_text:
            try:
                letter = letter.upper()
                letter = Mechanics.ciphering(letter)
            except:
                pass
            output_text = output_text + letter
        return output_text


    def set_rotors_positions():

        try:
            start = input("SET: ")
            start = start.upper()
            start_L = start[0]
            start_M = start[1]
            start_R = start[2]
            start_R, start_M, start_L = Mechanics.letter_encoding(start_R, start_M, start_L)
            Mechanics.rotors_start(int(start_R), int(start_M), int(start_L))
        except:
            print ("ERROR")


    def show_rotors_positions():

        current_L, current_M, current_R = Mechanics.letter_decoding(Mechanics.L, Mechanics.M, Mechanics.R)
        print ("POS: " + current_L + current_M + current_R)


    print ("""
        ????????   ??    ??   ????????    ???????   ??    ??    ??????
        ??         ???   ??      ??      ???        ???  ???   ??    ??
        ?????      ?? ?? ??      ??      ??  ????   ?? ?? ??   ????????
        ??         ??   ???      ??      ???   ??   ??    ??   ??    ??
        ????????   ??    ??   ????????    ???????   ??    ??   ??    ??
    """)
    set_rotors_positions()
    while True:
        try:
            input_text = input("?: ")
            if input_text == "?EXIT":
                break
            elif input_text == "?SET":
                set_rotors_positions()
                continue
            elif input_text == "?POS":
                show_rotors_positions()
                continue
            else:
                output_text = ciphering(input_text)
                print ("!: " + output_text)
        except:
            print ("ERROR")



#ENIGMA
#rotors: 3
#reflector: yes
#plugboard: no
#created by Artem Matveev
