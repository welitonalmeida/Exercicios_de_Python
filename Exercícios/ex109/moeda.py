def aumentar(preço=0, taxa=0, formato=False):
    """
    :param preço: Preço a ser informado pelo usuário.
    :param taxa: Valor do desconto ou acréscimo.
    :param formato: False por padrão para manter sem formatação de moeda. True para formatar os valores de saída no padrão moeda.
    :return: Returna os valores da opção selecionada com a devida formatação.
    """
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    """
    :param preço: Preço a ser informado pelo usuário.
    :param taxa: Valor do desconto ou acréscimo.
    :param formato: False por padrão para manter sem formatação de moeda. True para formatar os valores de saída no padrão moeda.
    :return: Returna os valores da opção selecionada com a devida formatação.
    """
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    """
    :param preço: Preço a ser informado pelo usuário.
    :param formato: False por padrão para manter sem formatação de moeda. True para formatar os valores de saída no padrão moeda.
    :return: Returna os valores da opção selecionada com a devida formatação.
    """
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    """
    :param preço: Preço a ser informado pelo usuário.
    :param formato: False por padrão para manter sem formatação de moeda. True para formatar os valores de saída no padrão moeda.
    :return: Returna os valores da opção selecionada com a devida formatação.
    """
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    """
    :param preço: Preço a ser informado pelo usuário.
    :param formato: False por padrão para manter sem formatação de moeda. True para formatar os valores de saída no padrão moeda.
    :return: Returna os valores da opção selecionada com a devida formatação.
    """
    return f'{moeda}{preço:.2f}'.replace('.', ',')
