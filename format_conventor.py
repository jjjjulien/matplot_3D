while True:

    str = input("原字符串：")

    output = str.replace('{m_dX=', '')
    output = output.replace(' m_dY=', ', ')
    output = output.replace(' m_dZ=', ', ')
    output = output.replace(' }', '')
    print(output)