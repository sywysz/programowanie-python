zmienna = 2.0

if isinstance(zmienna, int) or isinstance(zmienna, float):
    print('Zmienna jest liczbą')
    if isinstance(zmienna, int) or zmienna.is_integer() :
        print('Zmienna jest liczbą całkowitą')
    else:
        print('Zmienna jest liczbą zmiennoprzecinkową')
else:
    print('Zmienna jest ciągiem znaków')
