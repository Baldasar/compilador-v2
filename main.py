import numpy as np
import os
import re

def dicionario():
    return {
        "write": 0,
        "while": 1,
        "until": 2,
        "to": 3,
        "then": 4,
        "string": 5,
        "repeat": 6,
        "real": 7,
        "read": 8,
        "program": 9,
        "procedure": 10,
        "or": 11,
        "of": 12,
        "literal": 13,
        "integer": 14,
        "if": 15,
        "identificador": 16,
        "î": 17,
        "for": 18,
        "end": 19,
        "else": 20,
        "do": 21,
        "declaravariaveis": 22,
        "const": 23,
        "char": 24,
        "chamaprocedure": 25,
        "begin": 26,
        "array": 27,
        "and": 28,
        ">=": 29,
        ">": 30,
        "=": 31,
        "<>": 32,
        "<=": 33,
        "<": 34,
        "+": 35,
        "numreal": 36,
        "numinteiro": 37,
        "nomestring": 38,
        "nomechar": 39,
        "]": 40,
        "[": 41,
        ";": 42,
        ":": 43,
        "/": 44,
        "..": 45,
        ".": 46,
        ",": 47,
        "*": 48,
        ")": 49,
        "(": 50,
        "$": 51,
        "-": 52,
    }

def busca_por_valor(valor):
    dicionario_invertido = {v: k for k, v in dicionario().items()}
    return dicionario_invertido.get(valor, None)

def getProducoes():
    producoes = [[9, 16, 42, 54, 46, -1, -1, -1, -1, -1, -1, -1, -1, -1]]                                   
    producoes = np.append(producoes, [[55, 56, 57, 58, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[23, 16, 31, 59, 42, 60, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[16, 31, 59, 42, 60, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[22, 61, 43, 59, 42, 62, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[16, 63, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[47, 16, 63, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[61, 43, 59, 42, 62, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[27, 41, 37, 45, 37, 40, 12, 64, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[14, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[24, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)     
    producoes = np.append(producoes, [[7, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)     
    producoes = np.append(producoes, [[14, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[24, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)     
    producoes = np.append(producoes, [[7, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)     
    producoes = np.append(producoes, [[10, 16, 65, 57, 58, 42, 55, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[50, 61, 43, 59, 42, 62, 49, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[26, 66, 42, 67, 19, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[66, 42, 67, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[15, 41, 68, 40, 4, 26, 66, 19, 69, -1, -1, -1, -1, -1]], axis=0)     
    producoes = np.append(producoes, [[1, 41, 68, 40, 21, 26, 66, 19, -1, -1, -1, -1, -1, -1]], axis=0)     
    producoes = np.append(producoes, [[6, 66, 2, 41, 68, 40, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)      
    producoes = np.append(producoes, [[8, 50, 70, 49, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)     
    producoes = np.append(producoes, [[25, 16, 72, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[0, 50, 73, 74, 49, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)     
    producoes = np.append(producoes, [[18, 41, 16, 31, 68, 40, 3, 41, 68, 40, 21, 26, 66, 19]], axis=0)     
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[50, 61, 49, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[13, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[68, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[47, 73, 74, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[75, 76, 77, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[78, 79, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[37, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[16, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[38, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[39, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[36, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[50, 68, 49, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[31, 80, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[34, 80, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[30, 80, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[29, 80, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[33, 80, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[32, 80, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[35, 75, 76, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[52, 75, 76, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[75, 76, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[35, 75, 76, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[52, 75, 76, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[11, 75, 76, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[48, 78, 79, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[44, 78, 79, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[28, 78, 79, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[20, 26, 66, 19, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[16, 71, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[47, 16, 71, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    producoes = np.append(producoes, [[17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], axis=0)    
    
    return producoes

def getTabParsing():
    tabela = np.zeros((82, 82), dtype=int)
    
    tabela[53][9] = 1    
    
    tabela[54][10] = 2   
    tabela[54][23] = 2   
    tabela[54][22] = 2   
    tabela[54][26] = 2   
    
    tabela[55][10] = 23  
    tabela[55][23] = 3   
    tabela[55][22] = 7   
    tabela[55][26] = 27  
    
    tabela[56][23] = 3   
    tabela[56][22] = 4   
    tabela[56][26] = 4   
    tabela[56][42] = 4   
    
    tabela[57][22] = 7   
    tabela[57][26] = 8   
    tabela[57][42] = 8   
    
    tabela[58][26] = 27  
    
    tabela[59][14] = 19  
    tabela[59][24] = 20  
    tabela[59][5] = 21   
    tabela[59][7] = 22   
    tabela[59][27] = 14  
    
    tabela[60][16] = 5   
    tabela[60][22] = 6   
    tabela[60][26] = 6   
    
    tabela[61][16] = 9   
    
    tabela[62][16] = 12  
    tabela[62][26] = 13  
    tabela[62][42] = 13  
    tabela[62][49] = 13  
    
    tabela[63][43] = 11  
    tabela[63][49] = 11  
    tabela[63][47] = 10   
    
    tabela[64][14] = 15  
    tabela[64][24] = 16  
    tabela[64][5] = 17   
    tabela[64][7] = 18   
    
    tabela[65][50] = 25  
    tabela[65][22] = 26  
    tabela[65][26] = 26  
    
    tabela[66][15] = 30  
    tabela[66][1] = 31   
    tabela[66][6] = 32   
    tabela[66][8] = 33   
    tabela[66][25] = 34  
    tabela[66][0] = 35   
    tabela[66][18] = 36  
    tabela[66][2] = 37  
    tabela[66][19] = 37  
    tabela[66][42] = 37  
   
    tabela[67][15] = 28  
    tabela[67][1] = 28   
    tabela[67][6] = 28   
    tabela[67][8] = 28   
    tabela[67][25] = 28  
    tabela[67][0] = 28   
    tabela[67][18] = 28  
    tabela[67][42] = 28  
    tabela[67][19] = 29  
    
    tabela[68][16] = 44  
    tabela[68][36] = 44  
    tabela[68][37] = 44  
    tabela[68][38] = 44  
    tabela[68][39] = 44  
    tabela[68][50] = 44  
    
    tabela[69][20] = 70  
    tabela[69][42] = 70  
    
    tabela[70][16] = 72  
    
    tabela[71][47] = 73  
    tabela[71][49] = 74  
    
    tabela[72][50] = 38  
    tabela[72][42] = 39  
    
    tabela[73][13] = 40  
    tabela[73][11] = 41  
    tabela[73][28] = 41  
    tabela[73][29] = 41  
    tabela[73][30] = 41  
    tabela[73][31] = 41  
    tabela[73][32] = 41  
    tabela[73][33] = 41  
    tabela[73][34] = 41  
    tabela[73][35] = 41  
    tabela[73][35] = 41  
    tabela[73][36] = 41  
    tabela[73][37] = 41  
    tabela[73][38] = 41  
    tabela[73][39] = 41  
    tabela[73][44] = 41  
    tabela[73][48] = 41  
    tabela[73][16] = 41  
    tabela[73][50] = 41  
    tabela[73][52] = 41  
    
    tabela[74][47] = 42  
    tabela[74][49] = 43  

    tabela[75][16] = 45  
    tabela[75][36] = 45  
    tabela[75][37] = 45  
    tabela[75][38] = 45  
    tabela[75][39] = 45  
    tabela[75][50] = 45  

    tabela[78][37] = 46  
    tabela[78][16] = 47  
    tabela[78][38] = 48  
    tabela[78][39] = 49  
    tabela[78][36] = 50  
    tabela[78][50] = 51  
    
    tabela[77][31] = 52  
    tabela[77][34] = 53  
    tabela[77][30] = 54  
    tabela[77][29] = 55  
    tabela[77][33] = 56  
    tabela[77][32] = 57  
    tabela[77][4] = 58  
    tabela[77][21] = 58  
    tabela[77][2] = 58  
    tabela[77][3] = 58  
    tabela[77][47] = 58  
    tabela[77][49] = 58  
    tabela[77][40] = 58  
    tabela[77][41] = 58  
    
    tabela[76][35] = 59  
    tabela[76][52] = 60  
    tabela[76][37] = 61  
    tabela[76][16] = 61  
    tabela[76][38] = 61  
    tabela[76][39] = 61  
    tabela[76][36] = 61  
    tabela[76][50] = 61  

    tabela[76][35] = 62  
    tabela[76][52] = 63  
    tabela[76][11] = 64  
    tabela[76][4] = 65  
    tabela[76][21] = 65  
    tabela[76][2] = 65  
    tabela[76][3] = 65  
    tabela[76][47] = 65  
    tabela[76][49] = 65  
    tabela[76][40] = 65  
    tabela[76][41] = 65  
    tabela[76][29] = 69  
    tabela[76][30] = 69  
    tabela[76][31] = 69  
    tabela[76][32] = 69  
    tabela[76][33] = 69  
    tabela[76][34] = 69  
    tabela[76][35] = 69  

    tabela[79][48] = 66  
    tabela[79][44] = 67  
    tabela[79][28] = 68  
    tabela[79][16] = 69  
    tabela[79][29] = 69  
    tabela[79][30] = 69  
    tabela[79][31] = 69  
    tabela[79][32] = 69  
    tabela[79][33] = 69  
    tabela[79][34] = 69  
    tabela[79][35] = 69  
    tabela[79][36] = 69  
    tabela[79][37] = 69  
    tabela[79][38] = 69  
    tabela[79][39] = 69  
    tabela[79][50] = 69  
    tabela[79][4] = 69  
    tabela[79][21] = 69  
    tabela[79][2] = 69  
    tabela[79][3] = 69  
    tabela[79][47] = 69  
    tabela[79][49] = 69  
    tabela[79][40] = 69  
    tabela[79][41] = 69  
    
    tabela[80][35] = 59  
    tabela[80][52] = 60  
    tabela[80][16] = 61  
    tabela[80][37] = 61  
    tabela[80][36] = 61  
    tabela[80][38] = 61  
    tabela[80][39] = 61  
    tabela[80][50] = 61  

    return tabela

def lexico(palavra):
    tokens = []
    lexemas = []
    lines = []
    espacos = [' ', '\n', '\t', '\r']
    comparativos = ['>=', '>', '=', '<>', '<=', '<', '+']
    simbolos = [']', '[', ';', ':', '/', '..', '.', ',', '*', ')', '(', '', '-']
    reservados = ['write', 'while', 'until', 'to', 'then', 'string', 'repeat', 'real', 'read', 'program',
                'procedure', 'or', 'of', '', 'integer', 'if', '', 'î', 'for', 'end', 'else', 'do', 'declaravariaveis',
                'const', 'char', 'chamaprocedure', 'begin', 'array', 'and']

    lexema = ''
    catchError = ''
    currentLine = 1
    lineComment = False
    blockComment = False
    literalLimiter = False
    charLimiter = False
    strLimiter = False
    numLimiter = False

    for i in range(len(palavra)):
        if lineComment or blockComment:
            if lineComment and palavra[i] == '\n':
                lineComment = False
                currentLine += 1
            elif blockComment and palavra[i:i+2] == '*/':
                blockComment = False
                i += 1
            continue

        if palavra[i:i+2] == '//':
            lineComment = True
            i += 1

        elif palavra[i:i+2] == '/*':
            blockComment = True
            i += 1

        elif palavra[i] == '\n':
            currentLine += 1
            lineComment = False

        elif palavra[i] == '_':
            if literalLimiter:
                tokens.append(13)
                lines.append(currentLine)
                lexemas.append(lexema)
                strLimiter = False
                charLimiter = False
                literalLimiter = False
                lexema = ''
            else: 
                literalLimiter = True

        elif palavra[i] == '"':
            if strLimiter:
                if len(lexema) > 21:
                    catchError = f'Erro: String não pode ter mais de 20 caracteres. Linha: {currentLine}'
                    break
                tokens.append(38)
                lines.append(currentLine)
                lexemas.append(lexema)
                strLimiter = False
                charLimiter = False
                literalLimiter = False
                lexema = ''
            else:
                strLimiter = True

        elif palavra[i] == "'":
            if charLimiter:
                if len(lexema) > 2:
                    catchError = f'Erro: Char não pode ter mais de um caractere. Linha: {currentLine}'
                    break
                else:
                    tokens.append(39)
                    lines.append(currentLine)
                    lexemas.append(lexema)
                    strLimiter = False
                    charLimiter = False
                    literalLimiter = False
                    lexema = ''
            else:
                charLimiter = True

        elif palavra[i].isdigit():
            lexema = lexema + palavra[i]
            numLimiter = True

        elif palavra[i] == '.' and numLimiter:
            lexema = lexema + palavra[i]

        elif numLimiter:
            parts = lexema.split('.')
            if len(parts[0]) > 5:
                catchError = f'Erro: Número real não pode conter mais de 5 dígitos antes do divisor. Linha: {currentLine}'
                break
            elif len(parts) > 1 and len(parts[1]) > 2:
                catchError = f'Erro: Número real não pode conter mais de 2 dígitos após do divisor. Linha: {currentLine}'
                break
            else:
                tokens.append(36 if '.' in lexema else 37)
                lines.append(currentLine)
                lexemas.append(lexema)
                lexema = ''
                numLimiter = False

        elif palavra[i].isalpha():
            lexema = lexema + palavra[i]
            if charLimiter or strLimiter or literalLimiter:
                continue
            elif lexema in reservados and (palavra[i+1] in espacos or palavra[i+1] in simbolos):
                tokens.append(reservados.index(lexema))
                lines.append(currentLine)
                lexemas.append(lexema)
                lexema = ''

            elif len(lexema) > 20:
                catchError = f'Erro: Identificador não pode ter mais de 20 caracteres. Linha: {currentLine}'
                break

            elif palavra[i+1] in espacos or palavra[i+1] in simbolos:
                tokens.append(16)
                lines.append(currentLine)
                lexemas.append(lexema)
                lexema = ''

        elif palavra[i] in simbolos:
            if lexema:
                if charLimiter or strLimiter or literalLimiter:
                    lexema = lexema + palavra[i]
                    continue
                elif lexema in reservados:
                    tokens.append(reservados.index(lexema))
                else:
                    tokens.append(16)
                lines.append(currentLine)
                lexemas.append(lexema)
                lexema = ''
            
            if i + 1 < len(palavra) and palavra[i] == '.' and palavra[i+1] == '.':
                tokens.append(45)
                lines.append(currentLine)
                lexemas.append(palavra[i] + palavra[i+1])
                lexema = ''
                continue
            elif i + 1 < len(palavra) and palavra[i] == '.' and palavra[i+1] != '.':
                continue
            else:
                tokens.append(simbolos.index(palavra[i]) + 40)
                lines.append(currentLine)
                lexemas.append(palavra[i])
                lexema = ''
        
        elif palavra[i] in comparativos:

            if lexema:
                if charLimiter or strLimiter or literalLimiter:
                    lexema = lexema + palavra[i]
                    continue
                elif lexema in reservados:
                    tokens.append(reservados.index(lexema))
                else:
                    tokens.append(16)
                lines.append(currentLine)
                lexemas.append(lexema)
                lexema = ''

            if (palavra[i] == '>' and palavra[i+1] == '='):
                tokens.append(29)
                lines.append(currentLine)
                lexemas.append(palavra[i] + palavra[i+1])
                lexema = ''
            elif (palavra[i] == '<' and palavra[i+1] == '>'):
                tokens.append(32)
                lines.append(currentLine)
                lexemas.append(palavra[i] + palavra[i+1])
                lexema = ''
            elif (palavra[i] == '<' and palavra[i+1] == '='):
                tokens.append(33)
                lines.append(currentLine)
                lexemas.append(palavra[i] + palavra[i+1])
                lexema = ''
            else:
                tokens.append(comparativos.index(palavra[i]) + 29)
                lines.append(currentLine)
                lexemas.append(palavra[i])
                lexema = ''

        elif palavra[i] in espacos:
            if lexema:
                if charLimiter or strLimiter or literalLimiter:
                    lexema = lexema + palavra[i]
                    continue
                elif lexema in reservados:
                    tokens.append(reservados.index(lexema))
                else:
                    tokens.append(16)
                lines.append(currentLine)
                lexemas.append(lexema)
                lexema = ''

    for i in range(0,len(tokens)):
        print('Token: '+str(tokens[i]) + ' - Lexema: '+str(lexemas[i]) + ' - Linha: ' +str(lines[i]))

    if (catchError != ''):
        print(catchError)

    tokens = np.array(tokens)
    
    return { 'tokens': tokens, 'lexemas': lexemas, 'lines': lines }

class Semantico:
    def __init__(self, arrayTokens, arrayLexemas):
        self.tabela_simbolos = {
            "nome": [],
            "categoria": [],
            "tipo": [],
        }
        self.arrayTokens = arrayTokens
        self.arrayLexemas = arrayLexemas

    def executaAcaoSemantica(self, token, linha, proximoToken, lexema, posicaoToken):
        if proximoToken == 43 or proximoToken == 47:
            if token != "literal":
                self.insereTabelaSimbolos(lexema, "variavel", linha, posicaoToken)

        if proximoToken == 16:
            if token == "procedure":
                self.insereTabelaSimbolos(self.arrayLexemas[posicaoToken + 1], "procedure", linha, posicaoToken)
        
        if token == "const":
            self.insereTabelaSimbolos(lexema, "const", linha, posicaoToken)

    def insereTabelaSimbolos(self, nome, categoria, linha, posicaoToken):
        self.verificaDuplicidadeVariaveis(nome, linha)
        
        tipo = self.buscaTipo(posicaoToken, categoria)
    
        self.tabela_simbolos.get("nome").append(nome)
        self.tabela_simbolos.get("categoria").append(categoria)
        self.tabela_simbolos.get("tipo").append(tipo)

    def buscaTipo(self, posicaoToken, categoria):
        tipo = None
        tipos = ["string", "integer", "real", "char"]

        if categoria == "variavel":
            for i in range(posicaoToken, len(self.arrayTokens) - 1):
                proximoToken = self.arrayTokens[i + 1]

                if self.arrayTokens[i] == ":" and proximoToken in tipos:
                    tipo = proximoToken
                    break
        if categoria == "procedure":
            tipo = "procedure"
        if categoria == "const":
            tipo = "const"
        return tipo

    def printaTabelaSimbolos(self):
        nomes = self.tabela_simbolos.get("nome")
        categorias = self.tabela_simbolos.get("categoria")
        tipos = self.tabela_simbolos.get("tipo")

        print()
        print(f"{'Nome':<20}{'Categoria':<20}{'Tipo':<20}")
        print("=" * 50)
        for nome, categoria, tipo in zip(nomes, categorias, tipos):
            print(f"{nome:<20} {categoria:<20} {tipo:<20}")

    ##### ERROS SEMANTICOS #####

    def verificaDuplicidadeVariaveis(self, nome, linha):
        if nome in self.tabela_simbolos.get("nome"):
            print(f"Erro semantico: Variavel '{nome}' ja declarada na linha {linha}")
            raise Exception("Erro semantico")
    def verificiarVariavelNaoDeclarada(self, nome, linha):
        if nome not in self.tabela_simbolos.get("nome"):
            print(f"Erro semantico: Variavel '{nome}' nao declarada na linha {linha}")
            raise Exception("Erro semantico")
    def verificaDivisaoPorzero(self, valor, linha):
        if valor == 0:
            print(f"Erro semantico: Divisao por zero na linha {linha}")
            raise Exception("Erro semantico")

def sintatico(obt):
    token_array = obt['tokens']
    tokens = np.array(token_array)

    lexema_array = obt['lexemas']
    lexemas = np.array(lexema_array)

    lines_array = obt['lines']
    lines = np.array(lines_array)

    elemento_analisado = 0

    producoes = getProducoes()
    tabParsing = getTabParsing()

    pilha = [51]
    pilha = np.hstack([producoes[0][:], pilha])

    print("Tokens iniciais:", tokens)
    print("Pilha inicial:", pilha)

    token_text = [busca_por_valor(token) for token in tokens]

    x = pilha[0]
    a = tokens[0]

    sem = Semantico(token_text, lexemas)

    print("Analisando sintaticamente...")
    print(tokens)
    print(lexemas)

    while x != 51:
        print("Pilha:", pilha)
        print("Elemento a ser analisado:", a)

        if x == 17 or x == -1:
            pilha = np.delete(pilha, [0])
            x = pilha[0]
        else:
            if x <= 52:
                if x == a:  
                    pilha = np.delete(pilha, [0])
                    tokens = np.delete(tokens, [0])

                    token = token_text[elemento_analisado] if len(token_text) > 0 else ""
                    linha = lines[elemento_analisado] if len(lines) > 0 else ""
                    proximoToken = tokens[0] if len(tokens) > 0 else ""
                    lexema = lexemas[elemento_analisado] if len(lexemas) > 0 else ""

                    sem.executaAcaoSemantica(token, linha, proximoToken, lexema, elemento_analisado)

                    elemento_analisado += 1

                    if tokens.size != 0:
                        a = tokens[0]
                    else:
                        a = 51
                    if pilha.size != 0:
                        x = pilha[0]
                    else:
                        x = 51
                else:
                    print('Erro: Token inesperado', a)
                    break
            else: 
                if tabParsing[x][a] != 0:
                    producao = producoes[tabParsing[x][a] - 1]
                    pilha = np.delete(pilha, [0])
                    pilha = np.hstack([producao[producao != -1], pilha])
                    x = pilha[0]
                else:
                    print('Erro: Nenhuma produção encontrada para', x, 'e', a)
                    break

    if x == 51 and a == 51:
        print("Análise sintática concluída com sucesso.")
        sem.printaTabelaSimbolos() 
    else:
        print("Falha na análise sintática.")

try:
    with open('./exemplos/03.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()

    tokens = lexico(conteudo)

    sintatico(tokens)


except FileNotFoundError:
    print("O arquivo não foi encontrado.")