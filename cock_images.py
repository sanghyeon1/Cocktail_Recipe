import pathlib


def cocktail_image():
    # 이미지의 저장경로를 불러옴.
    image_path = str(pathlib.Path(__file__).parent.absolute())
    print(image_path)
    slash = "/"
    for i in range(len(image_path)):
        if image_path[i] == "\\":
            image_path = image_path.replace("\\", "/", 10)
        else:
            pass

    transparent = ['transparent', image_path + '/images/transparent_image.png']
    print(transparent)
    kir = ['kir', image_path + '/images/kir.png']
    negroni = ['negroni', image_path + '/images/negroni.png']
    old_fashioned = ['old_fashioned', image_path + '/images/old_fashioned.png']
    rusty_nail = ['rusty_nail', image_path + '/images/rusty_nail.png']
    black_russian = ['black_russian', image_path + '/images/black_russian.png']
    moscow_mule = ['moscow_mule', image_path + '/images/moscow_mule.png']
    bloody_mary = ['bloody_mary', image_path + '/images/bloody_mary.png']
    seabreeze = ['seabreeze', image_path + '/images/seabreeze.png']
    cuba_libre = ['cuba_libre',image_path + '/images/cuba_libre.png']
    long_island_ice_tea = ['long_island_ice_tea', image_path + '/images/long_island_iced_tea.png']
    harvey_wallbanger = ['harvey_wallbanger', image_path + '/images/harvey_wallbanger.png']
    tequila_sunrise = ['tequila_sunrise', image_path + '/images/tequila_sunrise.png']
    mai_tai = ['mai_tai', image_path + '/images/mai_tai.png']
    blue_hawaiian = ['blue_hawaiian', image_path + '/images/blue_hawaiian.png']
    pina_colada = ['pina_colada', image_path + '/images/pina_colada.png']
    b_52 = ['b_52', image_path + '/images/b_52.png']
    pousse_cafe = ['pousse_cafe', image_path + '/images/pousse_cafe.png']
    manhattan = ['manhattan', image_path + '/images/manhattan.png']

    all_images = [transparent, kir, negroni, old_fashioned, rusty_nail, black_russian, moscow_mule, bloody_mary, seabreeze, cuba_libre,
                    long_island_ice_tea, harvey_wallbanger, tequila_sunrise, mai_tai, blue_hawaiian, pina_colada, b_52,
                    pousse_cafe, manhattan]

    return all_images
