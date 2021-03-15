def notas(* n, sit=False):
    """
    -> Função para analizae notas e situação de vários alunos.
    :param n: uma ou mais notas dos alunos.
    :param sit: opcional, indica se deve ou não mostrar a situação.
    :return: dicionário com várias informações sobre a turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] > 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r
resp = notas(5.5, 5, 10, 8.5, sit=True)
print(resp)
help(notas)
